import requests
from utils.api_helpers import print_dict_pretty, save_response_to_json


def test_ap_get_all(base_url, auth):
    headers = {
        "Authorization": f"Bearer {auth}",
        "Accept": "application/json"
    }

    url = f"{base_url}kps-kb-ap/api/kps-kb/ap"
    params = {
        "type": "verbalRemarks",
        "page": 0,
        "size": 10,
        "sort": "createdAt,desc"
    }

    response = requests.get(url, headers=headers, params=params, timeout=15, verify=False)

    assert response.status_code == 200, f"Ошибка {response.status_code}: {response.text[:500]}"

    data = response.json()

    print("\n" + "="*80)
    print("VERBAL REMARKS (устные замечания)")
    print("="*80)
    print_dict_pretty(data)
    print("="*80 + "\n")

    save_response_to_json(data, "verbal_remarks_get_all", subdirectory="verbal")

    assert "content" in data
    assert isinstance(data["content"], list)