import pytest
from helpers.api_client import APIClient

class TestDeleteBooking:
    def test_delete_booking_success(self):
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
        create_response = client.create_booking(payload)
        booking_id = create_response.json()["bookingid"]

        token_response = client.get_token("admin", "password123")
        assert token_response.status_code == 200, f"Token generation failed: {token_response.text}"
        token = token_response.json()["token"]

        delete_response = client.delete_booking(booking_id, token)

        assert delete_response.status_code == 201