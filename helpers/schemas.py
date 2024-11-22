CREATE_BOOKING_SCHEMA = {
    "type": "object",
    "properties": {
        "bookingid": {"type": "integer"}
    },
    "required": ["bookingid"]
}

GET_TOKEN_SCHEMA = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}
