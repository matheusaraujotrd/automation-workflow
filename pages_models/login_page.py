from playwright.async_api import expect
from load_environment_variables import login_url, home_url

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = login_url
        
        # Locators
        self.email_input = page.get_by_placeholder("seu@email.com")
        self.password_input = page.get_by_placeholder("••••••••")
        self.login_button = page.get_by_text("Entrar")
        self.create_account_link = page.get_by_text("Criar conta")
        
        # Error messages
        self.invalid_email_error = page.get_by_text("Por favor, insira um email válido")
        self.short_password_error = page.get_by_text("O campo password deve ter pelo menos 6 caracteres")
        self.invalid_credentials_error = page.get_by_text("Credenciais inválidas. Por favor, tente novamente.")
    
    async def navigate(self):
        await self.page.goto(self.url)
    
    async def login(self, email: str, password: str):
        await self.email_input.fill(email)
        await self.password_input.fill(password)
        await self.login_button.click()
    
    async def verify_invalid_email_error(self):
        await expect(self.invalid_email_error).to_be_visible()
    
    async def verify_short_password_error(self):
        await expect(self.short_password_error).to_be_visible()
    
    async def verify_invalid_credentials_error(self):
        await expect(self.invalid_credentials_error).to_be_visible()

    async def exiting_login_page(self):
        await expect(self.page).not_to_have_url(self.url)
    
    async def succesful_login(self):
        await expect(self.page).to_have_url(home_url)