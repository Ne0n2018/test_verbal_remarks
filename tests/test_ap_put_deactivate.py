import requests

from utils.api_helpers import print_dict_pretty, save_response_to_json


def test_ap_put_register(base_url, auth):
    headers = {
        "Authorization": f"Bearer {auth}",
        "Content-Type": "application/json",
    }
    url = f"{base_url}/kps-kb-ap/api/kps-kb/ap/deactivate/verbalRemarks/309ca325-f867-49eb-9d07-3d6dd09d0428"
    response = requests.put(url, headers=headers, timeout=15, verify=False)
    assert response.status_code == 200,f'{response.status_code}\n{response.text}'
    data = response.json()
    print("\n" + "=" * 80)
    print("VERBAL REMARKS (устные замечания)")
    print("=" * 80)
    print_dict_pretty(data)
    print("=" * 80 + "\n")

    save_response_to_json(data, "verbal_remarks_put_deactivate", subdirectory="verbal")