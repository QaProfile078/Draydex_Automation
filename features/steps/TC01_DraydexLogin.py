from behave import given, when, then
from pages.login_page import LoginPage
from pages.Dashboard_page import DashboardPage
from pages.common_action import CommonActions

@given('the user is on the login page')
def step_impl(context):
    context.login_page = LoginPage(context)
    context.dashboard_page= DashboardPage(context)
    context.common_actions= CommonActions(context)
    context.login_page.open(context)

@when('the user enters a valid username and password')
def step_impl(context):
    if (context.email_id and context.password):
        context.login_page.login(context.email_id,context.password)
    else:
        context.login_page.login('admin@gofmi.com', 'password')

@when('the user enters an invalid username and a valid password')
def step_impl(context):
    context.login_page.login('admin@gmail.com', 'password')

@when('the user enters a valid username and an invalid password')
def step_impl(context):
    context.login_page.login('admin@gofmi.com', 'password123')

@when('the user leaves the username fields empty')
def step_impl(context):
    context.login_page.login('', 'password')

@when('the user leaves the password fields empty')
def step_impl(context):
    context.login_page.login('admin@gofmi.com', '')

@when('the user leaves the username and password fields empty')
def step_impl(context):
    context.login_page.login('', '')

@when('the user enters an invalid username or password')
def step_impl(context):
    context.login_page.login('invalidUser', 'invalidPassword')

@when('clicks the login button')
def step_impl(context):
    context.login_page.submit_login()

@then('the user should be redirected to the dashboard')
def step_impl(context):
    assert context.dashboard_page.is_dashboard_displayed_in_title()

@then('the user should see an error message indicating invalid credentials')
def step_impl(context):
    assert context.login_page.is_error_message_displayed()

@then('the user should remain on the login page')
def step_impl(context):
    assert context.login_page.is_on_login_page()

@then('the user should see an error message "The username field is required"')
def step_impl(context):
    assert context.login_page.is_username_required_displayed()

@then('the user should see an error message "The password field is required."')
def step_impl(context):
    assert context.login_page.is_password_required_displayed()