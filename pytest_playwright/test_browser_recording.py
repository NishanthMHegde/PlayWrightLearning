import pytest
from playwright.sync_api import Browser

#command to run this
#pytest --headed --browser firefox test_app.py



def test_theme_change(browser:Browser):
	context = browser.new_context(record_video_dir = "video/")
	page = context.new_page()
	page.goto("https://playwright.dev/python/")
	btn = page.get_by_title("Switch between dark and light mode (currently dark mode)")
	btn.click()
	context.close()
	

# def test_link_visible(page: Page):
# 	link = page.get_by_role('link', name="Get started")
# 	assert link.is_visible