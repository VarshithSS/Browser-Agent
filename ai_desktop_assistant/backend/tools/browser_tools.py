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

        search_url = (
            f"https://www.google.com/search?q={query}"
        )

        await self.page.goto(search_url)

        return f"Searched Google for {query}"

    async def get_page_title(self):

        return await self.page.title()



    async def get_page_text(self):

        body = await self.page.locator("body").inner_text()

        return body[:5000]