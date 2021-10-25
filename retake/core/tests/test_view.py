from http import HTTPStatus

from django.urls import reverse

from retake.core.models import Part


def test_part_create_view(db, client):
    data = {
        "name": "Teste",
        "category": "ADVOGADO",
    }
    assert Part.objects.count() == 0

    response = client.post(reverse("core:create_part"), data=data)
    assert response.status_code == HTTPStatus.FOUND
    assert Part.objects.count() == 1

    response = client.get(reverse("core:list_part"))
    assert f"<td>{data['name']}</td>" in str(response.content)
    assert f"<td>{data['category']}</td>" in str(response.content)


def test_part_list_view(client, part):
    response = client.get(reverse("core:list_part"))
    assert response.status_code == HTTPStatus.OK
    assert f"<td>{part.name}</td>" in str(response.content)
    assert f"<td>{part.category}</td>" in str(response.content)
    assert "part/list.html" in response.template_name


def test_part_update_view(client, part):
    data = {
        "name": "Teste",
        "category": "ADVOGADO",
    }
    response = client.post(reverse("core:edit_part", kwargs={'uuid': part.uuid}), data=data)
    assert response.status_code == HTTPStatus.FOUND

    part.refresh_from_db()
    assert part.name == data['name']
    assert part.category == data['category']


def test_part_delete_view(client, part):
    assert Part.objects.count() == 1
    response = client.post(reverse("core:delete_part", kwargs={'uuid': part.uuid}))
    assert response.status_code == HTTPStatus.FOUND
    assert Part.objects.count() == 0


def test_process_create_view():
    pass


def test_process_list_view(client, process):
    response = client.get(reverse("core:list_process"))
    assert response.status_code == HTTPStatus.OK
    assert f"<td>{process.number}</td>" in str(response.content)
    assert f"<td>{process.class_name}</td>" in str(response.content)
    assert f"<td>{process.subject}</td>" in str(response.content)
    assert "process/list.html" in response.template_name


def test_process_update_view(client, part):
    pass


def test_process_delete_view(client, part):
    pass
