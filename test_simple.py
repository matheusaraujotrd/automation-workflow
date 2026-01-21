import pytest
from pages_models.login_page import LoginPage
from load_environment_variables import user, password

@pytest.mark.asyncio
async def test_invalid_email_login(page):
    login_page = LoginPage(page)
    await login_page.navigate()
    await login_page.login("teste@em", "123456")
    await login_page.verify_invalid_email_error()


@pytest.mark.asyncio
async def test_short_password_login(page):
    login_page = LoginPage(page)
    await login_page.navigate()
    await login_page.login("teste@email.com", "123")
    await login_page.verify_short_password_error()


@pytest.mark.asyncio
async def test_sucessful_login(page):
    login_page = LoginPage(page)
    await login_page.navigate()
    await login_page.login(user, password)
    await login_page.exiting_login_page()
    await login_page.succesful_login()