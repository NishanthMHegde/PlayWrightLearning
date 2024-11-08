from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=100)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	#get by css id name and highlight it
	btn_link = page.locator("div.bs-component ul.flex-column li.dropdown a.dropdown-toggle")
	btn_link.highlight()

	browser.close()