from playwright.sync_api import sync_playwright
from cred import *

with sync_playwright() as playwright:
	browser = playwright.chromium.launch(headless=False, slow_mo=1000)
	context = browser.new_context()
	page = context.new_page()
	page.goto("https://accounts.google.com")

	email = page.get_by_label("Email or phone")
	email.fill(EMAIL)
	btn = page.get_by_role("button", name="Next")
	btn.click()
	password = page.get_by_label("Enter your password")
	password.fill(PASSWORD)

	btn = page.get_by_role("button", name="Next")
	btn.click()
	page.pause()
	#save the context for future use
	context.storage_state(path='playwright/.auth/user_info.json')

	context.close()