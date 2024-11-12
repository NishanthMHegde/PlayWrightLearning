import pytest
from playwright.sync_api import expect,Page

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'



def test_enabled_link(page: Page):
	page.goto("https://playwright.dev/python/")
	link = page.get_by_role('link', name="Get started")
	expect(link).to_be_enabled()

# def test_get_title(page: Page):
# 	page.goto("https://playwright.dev/python/")
# 	expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright Python")

def test_get_visible_link(page: Page):
	page.goto("https://playwright.dev/python/")
	link = page.get_by_role('link', name="Get started")
	expect(link).to_be_visible()

def test_get_hidden_link(page: Page):
	page.goto("https://playwright.dev/python/")
	link = page.get_by_role('link', name="Node.js")
	expect(link).to_be_hidden()