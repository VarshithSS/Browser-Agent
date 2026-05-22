from playwright.async_api import async_playwright


class BrowserTools:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    async def start(self):

        self.playwright = await async_playwright().start()

        self.browser = await self.playwright.chromium.launch(
            headless=False
        )

        self.page = await self.browser.new_page()

    async def open_url(self, url: str):

        await self.page.goto(url)

        return f"Opened {url}"

    async def google_search(self, query: str):

        await self.page.goto("https://www.google.com")

        await self.page.fill("textarea", query)

        await self.page.press("textarea", "Enter")

        return f"Searched Google for: {query}"