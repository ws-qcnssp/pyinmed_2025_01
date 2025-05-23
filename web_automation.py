from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, Playwright, Browser, BrowserContext
import os
import re

# pw = sync_playwright().start()
# browser = pw.chromium.launch(headless=False)
# page = browser.new_page()

URL = 'http://the-internet.herokuapp.com/'

def start_pw(pw: Playwright, headless=False, ignore_errors = False):
    if ignore_errors:
        context = pw.chromium.launch_persistent_context(
            user_data_dir='',
            headless=headless,
            ignore_https_errors = ignore_errors
        )
        browser = None
    else:
        browser = pw.chromium.launch(
            headless=headless,
            slow_mo=1000
        )
        context = browser.new_context()
    return browser, context

def stop_pw(browser: Browser, context: BrowserContext):
    if browser:
        browser.close()
    context.close()

def test_logowania(page: Page):
    page.goto(URL)
    page.locator('a[href*=login]').click()
    page.locator('input[id=username]').fill('tomsmith')
    page.locator('input[id=password]').fill('SuperSecretPassword!')
    page.locator('button[type=submit]').click()
    info_el = page.locator('div[id=flash]')
    if 'You logged into a secure area!' in info_el.inner_text():
        print('login test - OK')
    page.locator('a[href*=logout]').click()
    if 'You logged out of the secure area!' in info_el.inner_text():
        print('logout test - OK')

def test_pobierania(page: Page):
    nazwa_pliku = 'test.txt'
    if os.path.exists(nazwa_pliku):
        os.remove(nazwa_pliku)
    page.goto(URL + 'download')
    with page.expect_download() as download_info:
        page.locator('a[href*=txt]').first.click()
        plik = download_info.value
        plik.save_as(nazwa_pliku)
    if os.path.exists(nazwa_pliku):
        print('test pobierania - OK')
    else:
        print('test pobierania - ERROR')


def test_pobierania_wielu(page: Page):
    nazwa_pliku = 'test_{}.txt'
    page.goto(URL + 'download')
    linki = page.locator('a[href*=txt]')
    cnt = linki.count()
    for index, link in enumerate(linki.all()):
        with page.expect_download() as download_info:
            link.click()
            plik = download_info.value
            plik.save_as(nazwa_pliku.format(index))
    pobrane_cnt = len([nazwa for nazwa in os.listdir() if re.match(r'test_[0-9]+.txt', nazwa)])
    print(f'oczekiwano: {cnt}, pobrano: {pobrane_cnt}')

def main():
    with sync_playwright() as pw:
        browser, context = start_pw(pw)
        page = context.new_page()
        # test_logowania(page)
        # test_pobierania(page)
        test_pobierania_wielu(page)
        stop_pw(browser, context)


if __name__ == '__main__':
    main()