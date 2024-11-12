import pytest
from playwright.sync_api import expect,Page

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'



def test_contains_text(page: Page):
	page.goto("https://playwright.dev/python/")
	hdr = page.locator("h1.hero__title")
	expect(hdr).to_contain_text("modern web app")

def test_have_text(page: Page):
	page.goto("https://playwright.dev/python/")
	hdr = page.locator("a.getStarted_Sjon")
	expect(hdr).to_have_text("Get started")

def test_menu_have_text(page: Page):
	page.goto("https://playwright.dev/python/")
	hdr = page.locator("ul.dropdown__menu")
	expect(hdr).to_contain_text("Java")
	expect(hdr).to_contain_text("Python")
	expect(hdr).to_contain_text(".NET")

