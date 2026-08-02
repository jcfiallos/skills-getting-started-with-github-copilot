from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    activities[activity_name]["participants"] = [
        participant
        for participant in activities[activity_name]["participants"]
        if participant != email
    ]

    post_response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    assert post_response.status_code == 200

    delete_response = client.delete(
        f"/activities/{activity_name}/unregister?email={email}"
    )

    assert delete_response.status_code == 200
    assert email not in activities[activity_name]["participants"]
