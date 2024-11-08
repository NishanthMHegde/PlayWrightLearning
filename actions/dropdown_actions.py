from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=4000)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	drop_dwn = page.locator("div.bs-component a.dropdown-toggle").locator("nth=0")
	drop_dwn.click()
	#select one of the options that then appear
	sel = page.locator("div.bs-component a:text('Another action')")
	browser.close()