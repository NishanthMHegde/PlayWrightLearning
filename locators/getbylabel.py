from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=4000)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	#Get the doc role by its link so we can click it
	#label tag in the HTML inspect are called label roles
	label_link = page.get_by_label('Email address')
	print(label_link)
	#click it
	label_link.highlight()

	browser.close()