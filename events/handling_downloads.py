from playwright.sync_api import sync_playwright

def on_download(download):
	print("Download received")
	download.save_as('phone.jpg')

with sync_playwright() as playwright:
	browser = playwright.chromium.launch(headless=False, slow_mo=1000)
	page = browser.new_page()
	page.on('download', on_download)
	page.goto("https://unsplash.com/photos/a-person-is-holding-a-micro-device-in-their-hand-XmKxbgRc-bs")
	btn = page.get_by_role("link", name="Download free")
	with page.expect_download() as download_info:
		btn.click()
	page.remove_listener('download', on_download)
	browser.close()


