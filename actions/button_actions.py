from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=4000)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	btn1 = page.locator("div.btn-group-vertical").locator("button.btn-primary").locator("nth=0")
	btn1.click()
	#left click
	btn1.click(button='left')
	#right click
	btn1.click(button='right')
	#double click
	btn1.dblclick(delay=200)
	#hover over the button
	btn1.hover()

	browser.close()