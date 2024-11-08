from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=4000)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	sl_1 = page.get_by_label("Example select")
	#select option name 2
	sl_1.select_option("2")
	#select option name 4
	sl_1.select_option("4")
	#multiple select
	sl_2 = page.get_by_label("Example multiple select")
	#select option name 3
	sl_2.select_option("3")
	#select mutiple options
	sl_2.select_option(["3", "4"])
	browser.close()