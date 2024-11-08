from playwright.sync_api import sync_playwright
from cred import *

with sync_playwright() as playwright:
	browser = playwright.chromium.launch(headless=False, slow_mo=1000)
	#use storage state that has been saved
	context = browser.new_context(storage_state="playwright/.auth/user_info.json")
	page = context.new_page()
	page.goto("https://accounts.google.com")
	context.close()