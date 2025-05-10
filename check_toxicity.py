from playwright.sync_api import sync_playwright, Page, expect
from web_automation import start_pw, stop_pw
# import exception_handling.exception_handling.concat_1 as cc

import easygui as eg
from time import sleep

T3DB_URL = 'https://www.t3db.ca/'

def check_chemical(page: Page, chemical: str):
    page.goto(T3DB_URL + 'text_query')
    page.locator('main input[id=query]').fill(chemical)
    page.locator('main button[type=submit]').click()
    expect(page.locator('div[id=jumper] a[class=btn-jump], div[class=no-results], div[class=unearth-search-hit]').first).to_be_visible(timeout=60000)
    jump_buttons = page.locator('//div[@id="jumper"]//a[@class="btn-jump"]')
    no_results = page.locator('//div[@class="no-results"]')
    multiple_results = page.locator('//div[@class="unearth-search-hit"]')
    if jump_buttons.first.is_visible(timeout=100):
        print('chemical found in T3DB search')
    elif no_results.is_visible(timeout=100):
        eg.msgbox('No results found in T3DB search')
        return
    elif multiple_results.first.is_visible(timeout=100):
        first_5_results = multiple_results.all()[:5]
        chemicals = []
        for result in first_5_results:
            details_element = result.locator('div[class=result-info] a[class=show-loader]')
            link = details_element
            name = details_element.text_content()
            chemicals.append((name, link))
        names = [c[0] for c in chemicals]
        print(f'Multiple results found in T3DB search: {names}')
        choice = eg.choicebox('Multiple results found in T3DB search. Please select a chemical:', title='Check toxicity', choices=names)
        print(f'Choice: {choice}')
        if choice:
            choice_link = [c[1] for c in chemicals if c[0] == choice][0]
            choice_link.click()
            print('chemical found in T3DB search')
    else:
        eg.msgbox('Unexpected error occured in T3DB search')
        return
    props_rows = page.locator('.content-table tbody tr').all()
    props_to_fetch = ['Toxicity Values', 'Lethal Dose', 'Minimum Risk Level']
    props = {}
    for prop_row in props_rows:
        if prop_row.locator('th').count() > 0 and prop_row.locator('th').first.text_content() in props_to_fetch:
            props[prop_row.locator('th').first.text_content()] = prop_row.locator('td').first.text_content()
    output = '\n'.join([f'{k}:\n\n{v}\n\n' for k, v in props.items()])
    eg.msgbox(output, title=f'{chemical}: Toxicity properties from T3DB')

def main():
    chemical = eg.enterbox('Please provide chemical name or CAS number')
    if not chemical:
        eg.msgbox('No chemical provided!')
        return
    with sync_playwright() as pw:
        browser, context = start_pw(pw, ignore_errors=True)
        page = context.new_page()
        check_chemical(page, chemical)
        stop_pw(browser, context)

if __name__ == '__main__':
    main()