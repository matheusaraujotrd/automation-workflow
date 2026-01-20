from load_environment_variables import login_url

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
    
    def navigate(self):
        self.page.goto(self.url)
    
    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()