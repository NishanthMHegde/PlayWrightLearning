from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=100)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://www.w3schools.com/html/html_images.asp")
	#Get the doc role by its link so we can click it
	#alt options for image tag in the HTML inspect
	alttext_link = page.get_by_alt_text('Girl in a jacket')
	print(alttext_link)
	#click it
	alttext_link.highlight()

	browser.close()