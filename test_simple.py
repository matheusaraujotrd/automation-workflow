from playwright.sync_api import Page, expect
from pages_models.login_page import LoginPage
from load_environment_variables import user, password, home_url

#def check_account_creation_page(page: Page):


def test_invalid_email_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("teste@em", "123456")
    expect(page.get_by_text("Por favor, insira um email válido")).to_be_visible()

def test_short_password_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("teste@email.com", "123")
    expect(page.get_by_text("O campo password deve ter pelo menos 6 caracteres")).to_be_visible()


def test_sucessful_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(user, password)
    expect(page).not_to_have_url(login_page.url)
    expect(page).to_have_url(home_url)