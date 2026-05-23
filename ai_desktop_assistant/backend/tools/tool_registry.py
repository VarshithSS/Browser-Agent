from tools.browser_tools import BrowserTools

browser = BrowserTools()

TOOLS = {

    "open_url": {
        "func": browser.open_url,
        "description": "Open a website URL"
    },

    "google_search": {
        "func": browser.google_search,
        "description": "Search Google"
    },

    "get_page_title": {
        "func": browser.get_page_title,
        "description": "Get current webpage title"
    },

    "get_page_text": {
        "func": browser.get_page_text,
        "description": "Extract webpage text"
    }
}