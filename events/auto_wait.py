from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	browser = playwright.chromium.launch(headless=False, slow_mo=1000)
	page = browser.new_page()
	page.goto("https://bootswatch.com/default/")
	#select a link to click that is hidden.The page will wait for a certain amount of time for link to be visible.
	#if link that we are selecting is not visible, then page will timeout
	#auto_wait waits till page and DOM elements are loaded and also visible before performing actions like click
	link = page.get_by_role("link", name="Cerulean")
	#normal click with wait of 30000ms
	#link.click()
	#custom timeout of 2000ms
	link.click(timeout=2000)
	browser.close()


