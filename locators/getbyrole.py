from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, slow_mo=5000)
	#open new page in the browser
	page = browser.new_page()
	page.goto("https://bootswatch.com/default/")
	#Get the doc role by its link so we can click it
	#checbox in the HTML inspect are called checkbox roles and they can be checked
	chkbox_link = page.get_by_role('checkbox', name='Default checkbox')
	print(chkbox_link)
	#click it
	chkbox_link.highlight()
	chkbox_link.check()
	#radiobuttons in the HTML inspect are called radio roles and they can be checked
	radio_link = page.get_by_role('radio', name="Option two can be something else and selecting it will deselect option one")
	radio_link.check()
	print(radio_link)
	browser.close()