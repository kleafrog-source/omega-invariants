from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_operators_endpoint_returns_registry() -> None:
    response = client.get("/operators")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload["operators"]) == 7


def test_analyze_endpoint_returns_omega_result() -> None:
    response = client.post(
        "/analyze",
        json={
            "text": (
                "Запуск начинается с импульса. "
                "Потом система стабилизируется. "
                "Затем начинается рост. "
                "Далее происходит переключение. "
                "После этого структуры объединяются. "
                "Затем активность снижается. "
                "В финале результат фокусируется."
            ),
            "domain": "text",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert "result" in payload
    assert len(payload["result"]["sequence"]) == 7


def test_export_json_endpoint_returns_attachment() -> None:
    response = client.post(
        "/export/json",
        json={"text": "The system starts. Then it becomes stable. Then it shifts. It switches mode. It merges layers. It relaxes. It reaches final focus.", "domain": "text"},
    )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert "attachment; filename=\"omega-analysis.json\"" == response.headers["content-disposition"]


def test_export_html_endpoint_returns_attachment() -> None:
    response = client.post(
        "/export/html",
        json={"text": "The system starts. Then it becomes stable. Then it shifts. It switches mode. It merges layers. It relaxes. It reaches final focus.", "domain": "text"},
    )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "attachment; filename=\"omega-analysis.html\"" == response.headers["content-disposition"]
