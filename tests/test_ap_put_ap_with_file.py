

import requests

from utils.api_helpers import print_dict_pretty, save_response_to_json


def test_ap_put_ap_with_file(base_url, auth):
    headers = {
        'Authorization': f'Bearer {auth}',
        'Content-Type': 'application/json',
    }
    url = f'{base_url}/kps-kb-ap/api/kps-kb/ap'
    payload = {
            "type": "verbalRemarks",
            "id": "dc759a6b-c8d3-450a-aa6d-41970893050b",
            "createdAt": "2025-12-22T16:14:49.234479",
            "createdBy": "2c9a5081-7573-9b1d-0175-b6703fe70006",
            "createdByFio": "IBA",
            "updatedAt": "2025-12-22T16:15:50.471785",
            "updatedBy": "2c9a5081-7573-9b1d-0175-b6703fe70006",
            "updatedByFio": "IBA",
            "deleted": False,
            "isActive": True,
            "verbalRemarkDate": "2025-12-06",
            "articleName": {
                "type": "articlesNorm",
                "id": "2e460283-bc3f-4b26-8aae-5d2a0e6702e0"
            },
            "articleSign": {
                "type": "signsAp",
                "id": "797cbac1-672f-4c95-a07e-4d102cac15cf"
            },
            "circOffence": {
                "type": "detCircOffence",
                "id": "aade6f1c-1dc1-457e-bf19-7bb4d301247f"
            },
            "pto": {
                "type": "ptoBr",
                "id": "cb7ea372-53ca-430e-8609-138b5dadff22"
            },

            "customs": {
                "type": "tamBr",
                "id": "5f20945a-aa3a-48fb-a48a-d70d8d22d4ab",
                "code": 2,
                "name": "МИНСКАЯ ЦЕНТРАЛЬНАЯ ТАМОЖНЯ"
            },
            "objectDescriptionText": "второй трай",
            "fio": "Иванов Иван Иванович",
            "birthDate": "2009-12-24",
            "docType": {
                "type": "docId",
                "id": "ee3471d1-b130-401a-868d-7f7ecfbeb0ef"
            },
            "departureCountry": {
                "type": "countries",
                "id": "ef1a5783-acad-4454-bc72-f073a00d7b03",
                "code": 112,
                "name": "Республика Беларусь",
                "nameShort": "Беларусь"
            },
            "destinationCountry": {
                "type": "countries",
                "id": "107ec56b-1137-449a-8208-8315cd2592a4",
                "code": 8,
                "name": "Республика Албания",
                "nameShort": "Албания"
            },
            "objectDescription": {
                "type": "detItems",
                "id": "2d77ca00-df8d-4d2c-af3d-73f65744c932",
                "code": 2,
                "name": "Психотропные вещества"
            },
            "amount": 7878,
            "measureUnit": {
                "type": "itemsUnits",
                "id": "ff7e2951-1f3b-4ce6-9725-9c5a420f46c2"
            },
            "unitCost": 78778,
            "movementDirection": {
                "type": "dirMov",
                "id": "5cb90f35-ef3c-4fd5-af24-c39963bca3ba"
            },
            "customsRef": {
                "type": "tamBr",
                "id": "5f20945a-aa3a-48fb-a48a-d70d8d22d4ab"
            },
            "departureCountryRef": {
                "type": "countries",
                "id": "ef1a5783-acad-4454-bc72-f073a00d7b03"
            },
            "destinationCountryRef": {
                "type": "countries",
                "id": "107ec56b-1137-449a-8208-8315cd2592a4"
            },
            "objectDescriptionRef": {
                "type": "detItems",
                "id": "2d77ca00-df8d-4d2c-af3d-73f65744c932"
            }
    }



    response = requests.put(url, headers=headers, json=payload, timeout=15, verify=False)
    assert response.status_code == 200, f'ошибка {response.status_code}\n{response.text}'
    data = response.json()
    print("\n" + "=" * 80)
    print("VERBAL REMARKS (устные замечания)")
    print("=" * 80)
    print_dict_pretty(data)
    print("=" * 80 + "\n")

    save_response_to_json(data, "verbal_remarks_put_with_files", subdirectory="verbal")