from tools.browser_tools import BrowserTools


browser = BrowserTools()


async def initialize_browser():
    await browser.start()


async def run_agent(user_input: str):

    user_input = user_input.lower()

    if "linkedin" in user_input:
        return await browser.open_url("https://linkedin.com")

    elif "youtube" in user_input:
        return await browser.open_url("https://youtube.com")

    elif "google" in user_input:

        query = user_input.replace("google", "")

        return await browser.google_search(query)

    return "I don't understand yet."