import pytest
from playwright.sync_api import Page

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'


#autouse means this fixture will automatically get called by every test function and its return value will get plugged into the page argument
#when scope is set to session, yield the page and once all functions are done using it, it can be closed 
@pytest.fixture(autouse=True, scope='function')
def playwright_page(page:Page):
	page.goto("https://playwright.dev/python/")
	yield page
	print("Closing the page")
	page.close()


def test_get_started_link(page: Page):
	link = page.get_by_role('link', name="Get started")
	link.click()
	assert DOC_URL == page.url

def test_link_visible(page: Page):
	link = page.get_by_role('link', name="Get started")
	assert link.is_visible