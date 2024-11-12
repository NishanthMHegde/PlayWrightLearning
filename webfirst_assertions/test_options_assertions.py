import pytest
from playwright.sync_api import expect,Page

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'



def test_select_option(page: Page):
	page.goto("https://bootswatch.com/default/")
	select_option = page.get_by_label("Example select")
	expect(select_option).to_have_value("1")

	select_option.select_option("2")
	expect(select_option).to_have_value("2")

def test_multiple_options(page: Page):
	page.goto("https://bootswatch.com/default/")
	select_option = page.get_by_label("Example multiple select")
	select_option.select_option("1")
	expect(select_option).to_have_value("1")
	select_option.select_option("2")
	expect(select_option).to_have_value("2")
	select_option.select_option(["3","4"])
	expect(select_option).to_have_values(["3","4"])
	




