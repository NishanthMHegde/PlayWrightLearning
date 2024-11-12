import pytest
from playwright.sync_api import expect,Page

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'



def test_get_started_link(page: Page):
	page.goto("https://playwright.dev/python/")
	link = page.get_by_role('link', name="Get started")
	link.click()
	expect(page).to_have_url(DOC_URL)

def test_get_title(page: Page):
	page.goto("https://playwright.dev/python/")
	expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright Python")

