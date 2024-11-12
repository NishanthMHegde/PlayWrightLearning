import pytest
from playwright.sync_api import expect,Page

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'



def test_have_class(page: Page):
	page.goto("https://playwright.dev/python/")
	docs = page.get_by_role("link", name="Docs")

	
	expect(docs).to_have_class("navbar__item navbar__link")

def test_have_atrribute(page: Page):
	page.goto("https://playwright.dev/python/")
	docs = page.get_by_role("link", name="Docs")

	
	expect(docs).to_have_attribute("href", "/python/docs/intro")





