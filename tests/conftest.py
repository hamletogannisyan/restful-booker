from faker import Faker
import pytest
fake=Faker()
import random
import requests
URL='https://restful-booker.herokuapp.com'

# creates body for booking with random data
@pytest.fixture()
def create_body_for_booking(firstname=fake.first_name(),
                   lastname=fake.last_name(),
                   totalprice=random.randint(0, 10000),
                   depositpaid=random.choices([True, False]),
                   checkin=str(fake.date()),
                   checkout=str(fake.date()),
                   additionalneeds=None):
    body = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {"checkin": checkin, "checkout": checkout},
        "additionalneeds": additionalneeds
    }
    return body