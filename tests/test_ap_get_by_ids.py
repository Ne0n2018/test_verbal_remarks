import requests

from utils.api_helpers import print_dict_pretty, save_response_to_json


def test_ap_get_by_ids(base_url, auth):
    headers = {
        "Authorization": f"Bearer {auth}",
        "Accept": "application/json"
    }
    url = f'{base_url}/kps-kb-ap/api/kps-kb/ap/verbalRemarks/find-by-ids?ids=dc759a6b-c8d3-450a-aa6d-41970893050b&ids=70561eae-7b9b-49da-97cc-a20926e79814'
    response = requests.get(url, headers=headers, verify=False)
    assert response.status_code == 200, f'ошибка {response.status_code}\n{response.text}'
    data = response.json()
    print("\n" + "=" * 80)
    print("VERBAL REMARKS (устные замечания)")
    print("=" * 80)
    print_dict_pretty(data)
    print("=" * 80 + "\n")

    save_response_to_json(data, "verbal_remarks_get_by_ids", subdirectory="verbal")