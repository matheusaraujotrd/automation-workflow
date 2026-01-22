# Test Automation Workflow

## Overview
End-to-end test automation for a login page based on bug reports from beta testing.

For detailed (and a bit less technical) project information, see [My Portfolio](https://suehtam.notion.site/Portfolio-178b439588e0472fa8fd64f92c68cbff?pvs=74).

## Key Features
- **8 test cases** covering validation, authentication, and navigation
- **Cross-browser testing** on Chromium and Firefox
- **Fast execution**: Average runtime of 17.8 seconds
- **Page Object Model (POM)** for maintainable test structure
- **Async/await** with Playwright and pytest-asyncio
- **Secure credential management** using environment variables

## Project Scope
Right now, this automation only covers the **login page** of the web app, checking for things such as correct error display and valid login. I might add tests to other pages later, as life allows.

### Project Structure
```
automation-workflow/
├── tests/
│   └── test_login_page.py         # Login page test suite
|   └── conftest.py                # used to configure fixtures
├── pages_models/
│   └── login_page.py              # Page Object Model implementation
├── load_environment_variables.py  # Environment variables management
└── README.md                      # Documentation
```

### Result screenshot

![img](https://github.com/matheusaraujotrd/automation-workflow/blob/main/Results_img.png?raw=true)

## Test Cases Explained
- **test_invalid_email_login**: Originally, the app would not display the correct error message after inputting an e-mail with the "@" character, but invalid (such as "email@a"), displaying an API response instead (which, not only confusing, might also be a security issue). This test case exists to check for the correct error message.
- **test_short_password_login**: Originally, the app would not display the correct error message during a short password scenario, displaying an API response instead (which, not only confusing, might also be a security issue). This test case exists to check for the correct error message.
- **test_successful_login**: Basic test to check if the login is being made successfully.
- **test_check_secondary_link**: Basic link integrity test to check if policy and privacy terms are not broken. This is the only test with multiple assertions to test async behavior in this situation.
- **test_create_account_navigation**: Basic link integrity test to check if the create account button in the login page is working properly.

## Notes
- Browser testing limited to Chromium and Firefox to avoid rate limiting
- Credentials anonymized for portfolio use

## Next Steps
- Will possibly try some parameterizing to reduce the number of individual tests, making the test cycle even shorter.


