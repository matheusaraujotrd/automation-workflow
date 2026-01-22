from playwright.async_api import expect
from load_environment_variables import login_url, home_url, create_account_url, forgot_password_url, service_terms_url, privacy_policy_url

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = login_url
        
        # Locators
        self.email_input = page.get_by_placeholder("seu@email.com")
        self.password_input = page.get_by_placeholder("••••••••")
        self.login_button = page.get_by_text("Entrar", exact=True)
        self.create_account_button = page.get_by_text("Criar conta")
        self.service_terms_link = page.get_by_text("Termos de Serviço")
        self.forgot_password_link = page.get_by_text("Esqueceu a senha?")
        self.privacy_policy_link = page.get_by_text("Política de Privacidade")
        
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
    
    async def click_create_account(self):
        await self.create_account_button.click()

    async def click_service_terms(self):
        await self.service_terms_link.click()

    async def click_forgot_password(self):
        await self.forgot_password_link.click()

    async def click_privacy_policy(self):
        await self.privacy_policy_link.click() 
    
    async def verify_invalid_email_error(self):
        await expect(self.invalid_email_error).to_be_visible()
    
    async def verify_short_password_error(self):
        await expect(self.short_password_error).to_be_visible()
    
    async def verify_invalid_credentials_error(self):
        await expect(self.invalid_credentials_error).to_be_visible()
    
    async def succesful_login(self):
        await expect(self.page).to_have_url(home_url)
    
    async def verify_broken_links(self):
        await self.click_service_terms()
        await expect(self.page).to_have_url(service_terms_url)
        await self.page.go_back()
        await self.click_forgot_password()
        await expect(self.page).to_have_url(forgot_password_url)
        await self.page.go_back()
        await self.click_privacy_policy()
        await expect(self.page).to_have_url(privacy_policy_url)
        await self.page.go_back()

    async def verify_create_account_navigation(self):
        await self.click_create_account()
        await expect(self.page).to_have_url(create_account_url)