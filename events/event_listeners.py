from playwright.sync_api import sync_playwright


def page_loaded(page):
	print("Page %s has been loaded" % (page))

def request_created(request):
	print("Request %s was made" % request)

def file_handler(file_handler):
	file_handler.set_files("file.txt")

with sync_playwright() as playwright:
	browser = playwright.chromium.launch(headless=False, slow_mo=1000)
	page = browser.new_page()
	#create an event listener that activates once the page is loaded
	# page.on('load', page_loaded)
	# page.goto("https://bootswatch.com/default/")
	# #remove the listener once done
	# page.remove_listener('load', page_loaded)

	#create an event listener that activates once requests are fired
	# page.on('request', request_created)
	# page.goto("https://bootswatch.com/default/")
	# #remove the listener once done
	# page.remove_listener('request', request_created)

	#create an event listener that activates once file uploader is used
	page.on('filehandler', file_handler)
	page.goto("https://bootswatch.com/default/")
	f_h = page.get_by_label("Default file input example")
	f_h.click()
	#remove the listener once done
	page.remove_listener('filehandler', file_handler)
	browser.close()


