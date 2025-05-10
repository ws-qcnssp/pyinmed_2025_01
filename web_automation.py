from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, Playwright, Browser, BrowserContext

def start_pw(pw: Playwright, headless=False):
    browser = pw.chromium.launch(
        headless=headless
    )
    context = browser.new_context()
    return browser, context

def stop_pw(browser: Browser, context: BrowserContext):
    context.stop()
    browser.stop()