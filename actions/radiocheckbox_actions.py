from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=4000)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	chkbx_1 = page.get_by_role("checkbox", name="Default checkbox")
	#check it
	chkbx_1.check()
	#uncheck it
	chkbx_1.uncheck()
	#check if it is checked
	chkbx_1.is_checked()
	rb_1 = page.get_by_label("Option one is this and that—be sure to include why it's great")
	rb_1.highlight()
	#check it
	rb_1.check()
	rb_2 = page.get_by_label("Option two can be something else and selecting it will deselect option one")
	rb_2.check()
	#is checked
	rb_2.is_checked()
	browser.close()