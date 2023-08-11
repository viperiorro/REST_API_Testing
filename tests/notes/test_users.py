def test_login(notes_service, email, password):
    response = notes_service.post_users_login(email, password)
    assert response["data"]["token"] is not None


def test_login_invalid_email(notes_service, password):
    response = notes_service.post_users_login("invalid@email.com", password, expected_status_code=401)
    assert response["message"] == "Incorrect email address or password"


def test_profile_unauthenticated(notes_service):
    response = notes_service.get_users_profile(expected_status_code=401)
    assert response["message"] == "No authentication token specified in x-auth-token header"


def test_profile(authenticated_notes_service, email):
    response = authenticated_notes_service.get_users_profile()

    assert response["message"] == "Profile successful"
    assert response["data"]["email"] == email, "Email address is not correct"
