import pytest
from playwright.sync_api import sync_playwright
from session import PlaywrightSession

@pytest.fixture(scope="session")
def pw_session():
    session = PlaywrightSession()
    yield session
    session.close()

@pytest.fixture(scope="function")
def setup_teardown(pw_session):
     # If this is the first test, start the session
    if pw_session.page is None:
        page = pw_session.start()
    else:
        # Otherwise, reset to home page before test
        pw_session.reset_to_home()
        page = pw_session.page
    
    # Run the test
    yield page
    


