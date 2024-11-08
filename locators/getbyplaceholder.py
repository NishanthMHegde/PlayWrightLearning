from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=4000)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	#Get the doc role by its link so we can click it
	#placeholder tag in the HTML inspect are called placeholder roles
	placeholder_link = page.get_by_placeholder('Password')
	print(placeholder_link)
	#click it
	placeholder_link.highlight()

	browser.close()