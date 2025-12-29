import requests
from pygments.lexers import data

from utils.api_helpers import print_dict_pretty, save_response_to_json


def test_ap_post(base_url,auth):
    headers = {
        'Authorization': f"Bearer {auth}",
        'Content-Type': 'application/json'
    }
    url = f"{base_url}/kps-kb-ap/api/kps-kb/ap"
    payload = {
    "verbalRemarkDate": "2025-12-24",
    "articleName": {
        "type": "articlesNorm",
        "id": "340fadcb-147a-45cb-857e-e83436da12c1"
    },
    "articleSign": {
        "type": "signsAp",
        "id": "708e1c72-6a39-4088-b440-fd4a83eff1b3"
    },
    "circOffence": {
        "type": "detCircOffence",
        "id": "4c64bd3f-4a5a-48fa-bbde-14f572b989bc"
    },
    "pto": {
        "type": "ptoBr",
        "id": "67315b2a-0c2e-4de5-bad3-f4c863df98a2"
    },
    "citizenship": {
        "id": "107ec56b-1137-449a-8208-8315cd2592a4",
        "dateFrom": "1998-07-16",
        "dateTo": "4712-12-31",
        "createdAt": "2025-09-30T15:22:41.648479",
        "createdBy": "eeaa0824-753d-4d94-9226-1f8a772c0723",
        "createdByFio": "AUTO",
        "updatedAt": "2025-09-30T15:22:41.000003",
        "updatedBy": None,
        "updatedByFio": None,
        "code": 8,
        "name": "Республика Албания",
        "nameShort": "Албания",
        "nameEn": "ALBANIA                                 ",
        "code2": "AL",
        "code3": "ALB"
    },
    "customs": {
        "id": "7ced546d-f94e-4b01-915b-77882675b2c6",
        "dateFrom": "1995-04-17",
        "dateTo": "4712-12-31",
        "createdAt": "2025-07-12T14:27:13.275985",
        "createdBy": "2c9a5081-7573-9b1d-0175-b6703fe70006",
        "createdByFio": "IBA",
        "updatedAt": "2025-07-12T14:27:13.275987",
        "updatedBy": "2c9a5081-7573-9b1d-0175-b6703fe70006",
        "updatedByFio": "IBA",
        "code": 1,
        "name": "ГОСУДАРСТВЕННЫЙ ТАМОЖЕННЫЙ КОМИТЕТ РБ",
        "phone": "",
        "address": "220007, Г. МИНСК, УЛИЦА МОГИЛЕВСКАЯ ДОМ 45, КОРПУС 1"
    },
    "lastName": "Иванов",
    "firstName": "Иван",
    "surname": "Иванович",
    "birthDate": "2009-12-11",
    "docNum": None,
    "docId": None,
    "departureCountry": {
        "id": "cbd72157-785f-4d53-8c39-cd6043e80a8e",
        "dateFrom": "1995-04-17",
        "dateTo": "4712-12-31",
        "createdAt": "2025-09-30T15:22:41.648479",
        "createdBy": "eeaa0824-753d-4d94-9226-1f8a772c0723",
        "createdByFio": "AUTO",
        "updatedAt": "2025-09-30T15:22:41.000006",
        "updatedBy": None,
        "updatedByFio": None,
        "code": 20,
        "name": "Княжество Андорра",
        "nameShort": "Андорра",
        "nameEn": "ANDORRA                                 ",
        "code2": "AD",
        "code3": "AND"
    },
    "destinationCountry": {
        "id": "ef1a5783-acad-4454-bc72-f073a00d7b03",
        "dateFrom": "1995-04-17",
        "dateTo": "4712-12-31",
        "createdAt": "2025-09-30T15:22:41.648479",
        "createdBy": "eeaa0824-753d-4d94-9226-1f8a772c0723",
        "createdByFio": "AUTO",
        "updatedAt": None,
        "updatedBy": None,
        "updatedByFio": None,
        "code": 112,
        "name": "Республика Беларусь",
        "nameShort": "Беларусь",
        "nameEn": "BELARUS",
        "code2": "BY",
        "code3": "BLR"
    },
    "objectDescription": {
        "id": "2d77ca00-df8d-4d2c-af3d-73f65744c932",
        "dateFrom": "2010-01-01",
        "dateTo": "2100-12-31",
        "createdAt": "2025-07-12T10:42:12.118387",
        "createdBy": "2c9a5081-7573-9b1d-0175-b6703fe70006",
        "createdByFio": "IBA",
        "updatedAt": "2025-07-12T10:42:12.118387",
        "updatedBy": "2c9a5081-7573-9b1d-0175-b6703fe70006",
        "updatedByFio": "IBA",
        "code": 2,
        "name": "Психотропные вещества"
    },
    "objectDescriptionText": None,
    "amount": "1",
    "measureUnit": {
        "type": "itemsUnits",
        "id": "ff7e2951-1f3b-4ce6-9725-9c5a420f46c2"
    },
    "unitCost": "12",
    "movementDirection": {
        "type": "dirMov",
        "id": "19cd3563-7f7c-4e29-9896-66ccc0e678fc"
    },
    "docType": {
        "type": "docId",
        "id": "ee3471d1-b130-401a-868d-7f7ecfbeb0ef"
    },
    "type": "verbalRemarks",
    "customsRef": {
        "type": "tamBr",
        "id": "7ced546d-f94e-4b01-915b-77882675b2c6"
    },
    "citizenshipRef": {
        "type": "countries",
        "id": "107ec56b-1137-449a-8208-8315cd2592a4"
    },
    "departureCountryRef": {
        "type": "countries",
        "id": "cbd72157-785f-4d53-8c39-cd6043e80a8e"
    },
    "destinationCountryRef": {
        "type": "countries",
        "id": "ef1a5783-acad-4454-bc72-f073a00d7b03"
    },
    "objectDescriptionRef": {
        "type": "detItems",
        "id": "2d77ca00-df8d-4d2c-af3d-73f65744c932"
    }
}
    response = requests.post(url, json=payload, headers=headers, verify=False)
    assert response.status_code == 200,f'{response.status_code}\n{response.text}'
    data = response.json()
    print("\n" + "=" * 80)
    print("VERBAL REMARKS (устные замечания)")
    print("=" * 80)
    print_dict_pretty(data)
    print("=" * 80 + "\n")

    save_response_to_json(data, "verbal_remarks_post", subdirectory="verbal")