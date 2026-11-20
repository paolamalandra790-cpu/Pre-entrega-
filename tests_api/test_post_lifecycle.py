import time
import pytest
import requests
from faker import Faker

fake = Faker()
BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.e2e
def test_post_lifecycle():
    inicio = time.time()

    # 1. POST
    payload = {
        "title": fake.sentence(),
        "body": fake.paragraph(),
        "userId": 1
    }
    r_post = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r_post.status_code == 201
    data_post = r_post.json()
    assert "id" in data_post
    assert isinstance(data_post["id"], int)
    post_id = data_post["id"]

    # 2. PATCH
    r_patch = requests.patch(
        f"{BASE_URL}/posts/{post_id}",
        json={"title": "Título actualizado por QA"}
    )
    assert r_patch.status_code == 200
    assert r_patch.json()["title"] == "Título actualizado por QA"

    # 3. DELETE
    r_delete = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert r_delete.status_code == 200

    # 4. Tiempo
    assert (time.time() - inicio) < 3
