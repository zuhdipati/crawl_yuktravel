from .utils import auto_scroll
from playwright.sync_api import sync_playwright

def get_detail_join_trip(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        
        page.locator("h2.panel-title.sub_panel_title", has_text="INCLUSIONS").click()
        page.locator("h2.panel-title.sub_panel_title", has_text="EXCLUSIONS").click()
        page.locator("h2.panel-title.sub_panel_title", has_text="TERMS AND CONDITIONS").click()
        
        html = page.content()
        browser.close()

    return html


def get_list_join_trip(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        
        auto_scroll(page, scrolls=20, delay=500)
        
        html = page.content()
        browser.close()
        
    return html