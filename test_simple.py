from playwright.sync_api import Page, expect
from load_environment_variables import user, password

def test_invalid_email_login(page: Page):
    page.goto("https://www.airfinance.com.br/login")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("seu@email.com").fill("email@a")
    page.get_by_placeholder("••••••••").fill(password)
    page.get_by_text("Entrar").click()
    expect(page.get_by_text("Por favor, insira um email válido"), "Por favor, insira um email válido").to_be_visible()

def test_short_password_login(page: Page):
    page.goto("https://www.airfinance.com.br/login")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("seu@email.com").fill(user)
    page.get_by_placeholder("••••••••").fill("123")
    page.get_by_text("Entrar").click()
    expect(page.get_by_text("O campo password deve ter pelo menos 6 caracteres"), "O campo password deve ter pelo menos 6 caracteres").to_be_visible()

def test_sucessful_login(page: Page):
    page.goto("https://www.airfinance.com.br/login")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("seu@email.com").fill(user)
    page.get_by_placeholder("••••••••").fill(password)
    page.get_by_text("Entrar").click()