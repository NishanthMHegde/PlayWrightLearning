from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=100)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	#get by css classname and highlight it
	#button css element should have Large bu as substring
	btn_link = page.locator("button:text('Large bu')")
	#button css element should have Large button as exact string
	btn_link = page.locator("button:text-is('Large button')")
	#select 2nd button of the btn-primary classname
	btn_link = page.locator(":nth-match(button.btn-primary, 2)")
	btn_link = page.locator(":nth-match(button:text('Primary'), 4)")
	btn_link.highlight()

	browser.close()