from playwright.sync_api import sync_playwright
from web_automation import start_pw, stop_pw

def main():
    with sync_playwright() as pw:
        browser, context = start_pw(pw)
        page = context.new_page()
        stop_pw(browser, context)