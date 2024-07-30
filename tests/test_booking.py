import requests
from faker import Faker
import pytest
URL='https://restful-booker.herokuapp.com'
fake=Faker()
import datetime
import random
import json
from datetime import datetime

def response_to_dict(resp:bytes):
    data_str = resp.content.decode('utf-8')
    data_dict = json.loads(data_str)
    return data_dict

class TestBooking:
    def test_getbookingids(self, firstname=fake.first_name(), lastname=fake.last_name()):
        body = {"firstname": firstname, "lastname": lastname, "checkin": '2002-01-01'}
        response = requests.get(url=f'{URL}/booking', json=body)
        assert response.status_code == 200

    def test_get_booking(self,create_body_for_booking):
        body = create_body_for_booking
        response_create = requests.post(url=f'{URL}/booking', json=body)
        assert response_create.status_code == 200
        response_create=response_to_dict(response_create)
        id=response_create["bookingid"]
        response_get = requests.get(url=f"{URL}/booking/{id}")
        assert response_get.status_code == 200
        response_get=response_to_dict(response_get)
        assert(response_create["booking"] == response_get)

    def test_create_booking(self,create_body_for_booking):
        body = create_body_for_booking
        response_create = requests.post(url=f'{URL}/booking', json=body)
        assert response_create.status_code == 200

    @pytest.mark.skip(reason="status code is 500")
    @pytest.mark.parametrize("field", ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"])
    def test_create_booking_with_empty_fields(self,create_body_for_booking, field):
        body = create_body_for_booking
        body[field]=None
        print(body)
        response_create = requests.post(url=f'{URL}/booking', json=body)
        assert response_create.status_code == 400

    def test_create_booking_with_empty_additionalneeds(self,create_body_for_booking):
        body = create_body_for_booking
        body["additionalneeds"]=None
        print(body)
        response_create = requests.post(url=f'{URL}/booking', json=body)
        assert response_create.status_code == 200

    @pytest.mark.parametrize("id", [0, -1])
    def test_get_booking_with_negative_id(self,id):
        response_get = requests.get(url=f"{URL}/booking/{id}")
        assert response_get.status_code == 404


