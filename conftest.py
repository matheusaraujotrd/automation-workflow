import pytest_asyncio
from playwright.async_api import async_playwright


@pytest_asyncio.fixture(scope="function", params=["chromium", "firefox"])
async def async_page_two_browsers(request):
    async with async_playwright() as p:
        browser = await getattr(p, request.param).launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await context.close()
        await browser.close()

@pytest_asyncio.fixture(scope="function")
async def async_page_chromium():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await context.close()
        await browser.close()