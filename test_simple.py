from playwright.sync_api import Page, expect
from load_environment_variables import user, password, login_url, home_url

def check_account_creation_page(page: Page):
    page.goto(login_url)
    response = page.request.get()
    page.get_by_text("Criar conta").click()
    expect(page).not_to_have_url(login_url)
    expect(page).to_be_ok()

def test_invalid_email_login(page: Page):
    page.goto(login_url)
    page.get_by_placeholder("seu@email.com").fill("email@a")
    page.get_by_placeholder("••••••••").fill(password)
    page.get_by_text("Entrar").click()
    expect(page.get_by_text("Por favor, insira um email válido")).to_have_text("Por favor, insira um email válido")

def test_short_password_login(page: Page):
    page.goto(login_url)
    page.get_by_placeholder("seu@email.com").fill(user)
    page.get_by_placeholder("••••••••").fill("123")
    page.get_by_text("Entrar").click()
    expect(page.get_by_text("O campo password deve ter pelo menos 6 caracteres")).to_have_text("O campo password deve ter pelo menos 6 caracteres")

def test_sucessful_login(page: Page):
    page.goto(login_url)
    page.get_by_placeholder("seu@email.com").fill(user)
    page.get_by_placeholder("••••••••").fill(password)
    page.get_by_text("Entrar").click()
    expect(page).not_to_have_url(login_url)
    expect(page).to_have_url(home_url)