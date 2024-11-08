import pytest
from playwright.sync_api import Page, BrowserContext

#command to run this
#pytest --headed --browser firefox test_app.py

DOC_URL = 'https://playwright.dev/python/docs/intro'

@pytest.fixture(autouse=True)
def context_tracer(context:BrowserContext):
	context.tracing.start(
		name="playwright",
		screenshots = True,
		snapshots=True,
		sources=True
		)
	yield #makes it wait for test to finish
	context.tracing.stop(path="trace.zip")


def test_get_started_link(page: Page):
	page.goto("https://playwright.dev/python/")
	link = page.get_by_role('link', name="Get started")
	link.click()
	assert DOC_URL == page.url

