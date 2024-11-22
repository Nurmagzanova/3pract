import pytest
from helpers.api_client import APIClient
from helpers.schemas import CREATE_BOOKING_SCHEMA
from jsonschema import validate

class TestCreateBooking:
    def test_create_booking_success(self):
        client = APIClient()
        payload = {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": 123,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-11-01",
                "checkout": "2024-11-10"
            },
            "additionalneeds": "Breakfast"
        }
        response = client.create_booking(payload)
        assert response.status_code == 200

        validate(instance=response.json(), schema=CREATE_BOOKING_SCHEMA)

        booking_id = response.json()["bookingid"]

        token_response = client.get_token("admin", "password123")
        token = token_response.json()["token"]
        delete_response = client.delete_booking(booking_id, token)
        assert delete_response.status_code == 201