import os
from logging import getLogger

import pytest

from rest.countries_rest import CountriesRest
from rest.notes_rest import NotesRest

logger = getLogger(__name__)


@pytest.fixture(scope="session")
def email():
    return os.getenv("EMAIL")


@pytest.fixture(scope="session")
def password():
    return os.getenv("PASSWORD")


@pytest.fixture
def notes_service():
    return NotesRest()


@pytest.fixture
def authenticated_notes_service(notes_service, email, password):
    notes_service.post_users_login(email, password)
    return notes_service


@pytest.fixture
def prepared_note(authenticated_notes_service) -> dict:
    logger.info("Preparing note for tests")
    response = authenticated_notes_service.post_notes(
        title="Test Title",
        description="Test Description",
        category="Home",
        expected_status_code=200
    )
    logger.info(f"Note prepared: {response['data']}")
    return response["data"]


@pytest.fixture
def countries_service():
    return CountriesRest()