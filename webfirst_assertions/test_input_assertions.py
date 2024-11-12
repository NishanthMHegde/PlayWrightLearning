import pytest
from playwright.sync_api import expect,Page

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'



def test_get_started_link(page: Page):
	page.goto("https://playwright.dev/python/")
	search_box = page.get_by_placeholder("Search docs")
	expect(search_box).not_to_be_visible()

	search_btn = page.get_by_role("button", name="Search")
	search_btn.click()
	expect(search_box).to_be_visible()
	expect(search_box).to_be_editable()
	expect(search_box).to_be_empty()
	query="assertions"
	search_box.fill(query)
	expect(search_box).to_have_value(query)




