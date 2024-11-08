from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, slow_mo=2000)
	#open new page in the browser
	page = browser.new_page()
	page.goto("https://playwright.dev/python/")
	#Get the doc role by its link so we can click it
	#anchor tags in the HTML inspect are called link roles
	docs_link = page.get_by_role('link', name='Docs')
	print(docs_link)
	#click it
	docs_link.click()

	browser.close()