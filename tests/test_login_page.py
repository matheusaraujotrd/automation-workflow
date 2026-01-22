import pytest
from pages_models.login_page import LoginPage
from load_environment_variables import user, password

# 8 test cases for the login page; latest average runtime 17.8s.

@pytest.mark.asyncio
async def test_invalid_email_login(async_page_two_browsers):
    login_page = LoginPage(async_page_two_browsers)
    await login_page.navigate()
    await login_page.login("teste@em", "123456")
    await login_page.verify_invalid_email_error()

@pytest.mark.asyncio
async def test_short_password_login(async_page_two_browsers):
    login_page = LoginPage(async_page_two_browsers)
    await login_page.navigate()
    await login_page.login("teste@email.com", "123")
    await login_page.verify_short_password_error()


@pytest.mark.asyncio
async def test_sucessful_login(async_page_two_browsers):
    login_page = LoginPage(async_page_two_browsers)
    await login_page.navigate()
    await login_page.login(user, password)
    await login_page.succesful_login()

@pytest.mark.asyncio
async def test_check_secondary_links(async_page_chromium):
    login_page = LoginPage(async_page_chromium)
    await login_page.navigate()
    await login_page.verify_broken_links()

@pytest.mark.asyncio
async def test_create_account_navigation(async_page_chromium):
    login_page = LoginPage(async_page_chromium)
    await login_page.navigate()
    await login_page.verify_create_account_navigation()