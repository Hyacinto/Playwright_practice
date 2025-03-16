import pytest
from playwright.sync_api import sync_playwright

class PlaywrightSession:
    # A class to manage the Playwright session state
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
    
    def start(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.firefox.launch(headless=False)
        self.page = self.browser.new_page(ignore_https_errors=True)
        self.page.goto("https://www.uitestingplayground.com/")
        return self.page
    
    def reset_to_home(self):
        # Reset to the home page without creating a new page
        self.page.goto("https://www.uitestingplayground.com/")
    
    def close(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()