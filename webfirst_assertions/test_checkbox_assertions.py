import pytest
from playwright.sync_api import expect,Page

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'



def test_get_started_link(page: Page):
	page.goto("https://bootswatch.com/default/")
	def_checkbox = page.get_by_label("Default checkbox")
	checked_checkbox = page.get_by_label("Checked checkbox")

	expect(def_checkbox).not_to_be_checked()
	expect(checked_checkbox).to_be_checked()
	




