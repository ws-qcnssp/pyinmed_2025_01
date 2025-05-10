from playwright.sync_api import sync_playwright, Page
from web_automation import start_pw, stop_pw
# import exception_handling.exception_handling.concat_1 as cc

import easygui as eg
from time import sleep

T3DB_URL = 'https://www.t3db.ca/'

def check_chemical(page: Page, chemical: str):
    page.goto(T3DB_URL + 'text_query')
    page.locator('main input[id=query]').fill(chemical)
    page.locator('main button[type=submit]').click()
    sleep(30)

def main():
    chemical = eg.enterbox('Please provide chemical name or CAS number')
    if not chemical:
        eg.msgbox('No chemical provided!')
        return
    with sync_playwright() as pw:
        browser, context = start_pw(pw, ignore_errors=True)
        page = context.new_page()

        stop_pw(browser, context)

if __name__ == '__main__':
    main()