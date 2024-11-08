from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=4000)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	i_field = page.locator("input#exampleInputEmail1")
	i_field.highlight()
	#fill field with a value
	i_field.fill("me@sample.com")
	#clear it
	i_field.clear()
	#type the characters one by one
	i_field.type("me@sample.com", delay=200)
	#clear it
	i_field.clear()
	i_field.fill("me@sample.com")
	#get the value present in the field
	i_val = i_field.input_value()
	
	browser.close()