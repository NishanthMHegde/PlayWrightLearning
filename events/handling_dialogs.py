from playwright.sync_api import sync_playwright

def on_alert(alert):
	print("Alert received")
	#you can only accept alerts
	alert.accept()

def on_dialog(dialog):
	print("Dialog received")
	#accept the dialogue by clicking okay
	dialog.accept()
	#dismiss the dialogue by clicking cancel
	# dialog.dismiss()

def on_prompt(prompt):
	print("Prompt received")
	#accept the prompt by entering something
	prompt.accept("I accept prompt")
	#dismiss the prompt by clicking cancel
	# prompt.dismiss()

with sync_playwright() as playwright:
	browser = playwright.chromium.launch(headless=False, slow_mo=2000)
	page = browser.new_page()
	page.on("alert", on_alert)
	# page.on("dialog", on_dialog)
	page.on("dialog", on_prompt)
	page.goto("https://testpages.eviltester.com/styled/alerts/alert-test.html")
	# btn = page.get_by_role("button", name="Show alert box")
	# btn.click()
	# btn = page.get_by_role("button", name="Show confirm box")
	# btn.click()
	btn = page.get_by_role("button", name="Show prompt box")
	btn.click()
	page.remove_listener("alert", on_alert)
	# page.remove_listener("dialog", on_dialog)
	page.remove_listener("dialog", on_prompt)
	
	browser.close()


