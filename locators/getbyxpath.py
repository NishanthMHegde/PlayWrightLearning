from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=100)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	#get by css classname and highlight it
	ele_link = page.locator("//button[@class='btn-primary']")
	#locate only nth element
	ele_link = page.locator("//button[@class='btn-primary']").locator("nth=0")
	ele_link = page.locator("//input[@id='exampleInputEmail1']")
	#highlight its parent
	ele_link = page.locator("//input[@id='exampleInputEmail1']").locator("..")
	ele_link=page.locator("//h1[text() = 'Navbars']")
	#The above examples were all looking for exact matches. Let us explore locators with substring matches
	ele_link=page.locator("//h1[contains(text(), 'Nav')]")
	#chaining selectors
	ele_link = page.locator("//div[@class='bs-docs-section']").locator("//small[contains(text(),'faded')]")
	ele_link.highlight()

	browser.close()