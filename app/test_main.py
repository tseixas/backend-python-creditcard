from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_create_card():
    data = {
        "exp_date": "2023-10-12",
        "holder": "holder",
        "number": "4539578763621486",
        "cvv": 123
    }

    response = client.post(
        "/api/v1/credit-card/",
        json=data
    )

    assert response.status_code == 200


def test_create_card_invalid_exp_date():
    data = {
        "exp_date": "2023-10-01",
        "holder": "holder",
        "number": "4539578763621486",
        "cvv": 123
    }

    response = client.post(
        "/api/v1/credit-card/",
        json=data
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid Expiration date"
    }


def test_create_card_invalid_holder():
    data = {
        "exp_date": "2023-10-12",
        "holder": "a",
        "number": "4539578763621486",
        "cvv": 123
    }

    response = client.post(
        "/api/v1/credit-card/",
        json=data
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid Holder"
    }


def test_create_card_invalid_number():
    data = {
        "exp_date": "2023-10-12",
        "holder": "holder",
        "number": "123",
        "cvv": 123
    }

    response = client.post(
        "/api/v1/credit-card/",
        json=data
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid Card"
    }


def test_create_card_invalid_cvv_max():
    data = {
        "exp_date": "2023-10-12",
        "holder": "holder",
        "number": "4539578763621486",
        "cvv": 12345
    }

    response = client.post(
        "/api/v1/credit-card/",
        json=data
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid CVV"
    }

def test_create_card_invalid_cvv_min():
    data = {
        "exp_date": "2023-10-12",
        "holder": "holder",
        "number": "4539578763621486",
        "cvv": 12
    }

    response = client.post(
        "/api/v1/credit-card/",
        json=data
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid CVV"
    }


def test_card_valid():
    response = client.get("/api/v1/credit-card/1")

    assert response.status_code == 200


def test_card_invalid():
    response = client.get("/api/v1/credit-card/999")

    assert response.status_code == 404


def test_cards():
    response = client.get("/api/v1/credit-card/")

    assert response.status_code == 200
