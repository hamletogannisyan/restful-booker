# import requests
# from faker import Faker
# import pytest
# URL='https://restful-booker.herokuapp.com'
# fake=Faker()
# import datetime
# import random
# import json
# from datetime import datetime
# from test_booking import response_to_dict
#
# class TestDelete:
#     def test_delete(self, create_body_for_booking):
#         authbody = {"username": "admin", "password": "password123"}
#         response = requests.post(url=f'{URL}/auth', json=authbody)
#         assert response.status_code == 200 and "token" in response.text
#         print(response.text)
#         dictionary = json.loads(response.text)
#         print(dictionary)
#
#         body = create_body_for_booking
#         response_create = requests.post(url=f'{URL}/booking', json=body)
#         assert response_create.status_code == 200
#         response_create = response_to_dict(response_create)
#         id = response_create["bookingid"]
#
#         response_delete = requests.delete(url=f"{URL}/booking/{id}", headers={'Cookie': response.text})
#         print(response_delete.status_code)


