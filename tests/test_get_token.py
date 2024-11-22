import pytest
from helpers.api_client import APIClient
from helpers.schemas import GET_TOKEN_SCHEMA
from jsonschema import validate

class TestGetToken:
    def test_get_token_success(self):
        client = APIClient()
        response = client.get_token("admin", "password123")
        
        assert response.status_code == 200

        response_data = response.json()
        validate(instance=response_data, schema=GET_TOKEN_SCHEMA)