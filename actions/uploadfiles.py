from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	#launch the browser first
	browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=4000)
	#open new page in the browser
	page = browser.new_page(no_viewport=True)
	page.goto("https://bootswatch.com/default/")
	i_file = page.get_by_label("Default file input example")
	i_file.set_input_files("file.txt")
	#clear selection
	i_file.set_input_files([])
	#use with keyword to open a file upload listener to upload files
	with page.expect_file_chooser() as fc_choser:
		i_file.click()

	#now fc_choser gets value of file upload button click
	fc_value = fc_choser.value
	fc_value.set_files("file.txt")
