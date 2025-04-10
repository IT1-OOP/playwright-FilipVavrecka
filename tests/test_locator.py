import os
from playwright.sync_api import sync_playwright, expect
import urllib.parse

def test_page_elements():
    cesta = os.path.abspath(os.path.join(os.path.dirname(__file__), "../index.html"))
    cesta = urllib.parse.unquote(cesta)

    if not os.path.exists(cesta):
        raise FileNotFoundError(f"File not found: {cesta}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file:///{cesta}")
        h1_tag = page.locator('h1').first
        expect(h1_tag).to_be_visible()
        div_tag = page.locator('div').first
        expect(div_tag).to_be_visible()
        text_locator = page.locator('text="Test text"') 
        expect(text_locator).to_be_visible()
        w3schools_link = page.locator('a[href="https://www.w3schools.com"]')
        expect(w3schools_link).to_be_visible()
        w3schools_link.click()
        browser.close()