from behave import given, when, then

@given('the login page is available')
def step_login_page(context):
    print("Login page is available")

@when('the user enters valid credentials')
def step_enter_credentials(context):
    print("User entered valid credentials")

@then('the user should see a successful login message')
def step_login_success(context):
    print("Login successful")