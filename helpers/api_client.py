import requests

class APIClient:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def create_booking(self, payload):
        url = f"{self.BASE_URL}/booking"
        return requests.post(url, json=payload)

    def delete_booking(self, booking_id, token):
        url = f"{self.BASE_URL}/booking/{booking_id}"
        headers = {"Cookie": f"token={token}"}
        return requests.delete(url, headers=headers)

    def get_token(self, username, password):
        url = f"{self.BASE_URL}/auth"
        payload = {"username": username, "password": password}
        return requests.post(url, json=payload)