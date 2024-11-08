import pytest
from playwright.sync_api import Page

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'

@pytest.fixture()
def playwright_page(page:Page):
	page.goto("https://playwright.dev/python/")
	return page
	


def test_get_started_link(playwright_page: Page):
	link = playwright_page.get_by_role('link', name="Get started")
	link.screenshot(path='get_started.png') #PNG to have transparent background
	assert DOC_URL == playwright_page.url

def test_page_screenshot(playwright_page: Page):
	playwright_page.screenshot(path="python_playwright.jpg")