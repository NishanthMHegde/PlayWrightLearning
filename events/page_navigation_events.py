from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
	browser = playwright.chromium.launch(headless=False, slow_mo=1000)
	page = browser.new_page()
	#measure time taken to load the page for different events
	#load full page
	# start_time = perf_counter()
	# page.goto("https://bootswatch.com/default/", wait_until="load")
	# end_time = perf_counter()
	# time_taken = end_time - start_time
	# print("Time taken to load page fully is %2s" % (time_taken))

	#load only document
	# start_time = perf_counter()
	# page.goto("https://bootswatch.com/default/", wait_until="domcontentloaded")
	# end_time = perf_counter()
	# time_taken = end_time - start_time
	# print("Time taken to load document DOM fully is %2s" % (time_taken))

	#just wait for initial commit
	# start_time = perf_counter()
	# page.goto("https://bootswatch.com/default/", wait_until="commit")
	# end_time = perf_counter()
	# time_taken = end_time - start_time
	# print("Time taken to commit is %2s" % (time_taken))

	#wait for comlete network activities to be over
	start_time = perf_counter()
	page.goto("https://bootswatch.com/default/", wait_until="networkidle")
	end_time = perf_counter()
	time_taken = end_time - start_time
	print("Time taken to network idle is %2s" % (time_taken))

	browser.close()


