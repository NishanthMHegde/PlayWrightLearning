import pytest
from playwright.sync_api import Page

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'



def test_get_started_link(page: Page):
	page.goto("https://playwright.dev/python/")
	link = page.get_by_role('link', name="Get started")
	link.click()
	assert DOC_URL == page.url

def test_link_visible(page: Page):
	page.goto("https://playwright.dev/python/")
	link = page.get_by_role('link', name="Get started")
	assert link.is_visible