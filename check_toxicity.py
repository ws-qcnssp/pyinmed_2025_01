from playwright.sync_api import sync_playwright
from web_automation import start_pw, stop_pw
# import exception_handling.exception_handling.concat_1 as cc

import easygui as eg


def main():
    chemical = eg.enterbox('Please provide chemical name or CAS number')
    if not chemical:
        eg.msgbox('No chemical provided!')
        return
    with sync_playwright() as pw:
        browser, context = start_pw(pw)
        page = context.new_page()

        stop_pw(browser, context)

if __name__ == '__main__':
    main()