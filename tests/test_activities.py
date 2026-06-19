def test_get_activities_returns_expected_structure(client):
    # Arrange
    path = "/activities"

    # Act
    response = client.get(path)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_get_activities_includes_seed_participants(client):
    # Arrange
    path = "/activities"

    # Act
    response = client.get(path)

    # Assert
    participants = response.json()["Chess Club"]["participants"]
    assert "michael@mergington.edu" in participants
    assert "daniel@mergington.edu" in participants
