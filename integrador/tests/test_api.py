import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    response = requests.get(f"{BASE_URL}/posts", timeout=10)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    primer_post = data[0]
    for campo in ("userId", "id", "title", "body"):
        assert campo in primer_post

def test_get_inexistente():
    response = requests.get(f"{BASE_URL}/post/999999", timeout=10)

    assert response.status_code == 404
    assert response.json() == {}

def test_create_post():
    payload = {
        "title": "Prueba automatizada con requests",
        "body": "Validando creacion y encadenamiento en Pytest",
        "userId": 1,
    }
    post_response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)

    assert post_response.status_code == 201
    creado = post_response.json()
    assert creado["title"] == payload["title"]
    assert creado["body"] == payload["body"]
    assert creado["userId"] == payload["userId"]
    assert "id" in creado

    # Encadenamiento: consulta un recurso existente para verificar flujo GET posterior
    get_response = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert get_response.status_code == 200
    assert "id" in get_response.json()

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code in (200, 204)