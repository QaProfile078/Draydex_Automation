import time

from behave import given,when,then

from pages.Forgot_password import ForgotPassword
from pages.Switched_window import SwitchedWindow
from pages.login_page import LoginPage

@when('the user clicks on the "Forgot Password?" link')
def step_impl(context):
    context.login_page=LoginPage(context)
    context.forgot_password=ForgotPassword(context)
    context.login_page.click_on_forgot_password()

@then('the "Forgot Password" page should be displayed with mandatory fields')
def step_impl(context):
    assert context.forgot_password.is_forgot_password_displayed_in_title()
    assert context.forgot_password.is_draydex_logo_present_on_page()
    assert context.forgot_password.is_forgot_password_heading_present_on_page()
    assert context.forgot_password.is_email_input_field_present_on_page()
    assert context.forgot_password.is_customer_and_carrier_radio_button_present_on_page()
    assert context.forgot_password.is_request_reset_link_button_present_on_page()
    assert context.forgot_password.is_back_to_login_button_present_on_page()

@when('enters a valid email address')
def step_impl(context):
    context.forgot_password.enter_a_valid_email("draydextesting@yopmail.com")

@when('User selects valid user type')
def step_impl(context):
    context.forgot_password.select_valid_usertype("carrier")

@when('clicks the "REQUEST RESET LINK" button')
def step_impl(context):
    context.forgot_password.click_on_request_reset_link_button()

@then('the user should see the message "If this email exists, you will receive a reset email."')
def step_impl(context):
    assert context.forgot_password.has_successful_message_popup_appeared()
    context.login_page=LoginPage(context)
    assert context.login_page.is_on_login_page()

@then('User should receive a "Forgot Password" email with a "Reset Password" button')
def step_impl(context):
    context.switched_window= SwitchedWindow(context)

@when('receives the "Forgot Password" email')
def step_impl(context):
    context.switched_window=SwitchedWindow(context)
    assert context.switched_window.is_forgot_password_heading_present_in_mail()

@when('clicks on the "Reset Password" link in the email')
def step_impl(context):
    assert context.switched_window.is_reset_password_button_present_in_mail()
    context.switched_window.click_on_reset_password()

@then('the user should see fields "Enter new Password","Confirm your Password" and "Enter Username"')
def step_impl(context):
    context.switched_window=SwitchedWindow(context)
    context.forgot_password=ForgotPassword(context)
    context.switched_window.switch_to_reset_password_window()
    assert context.forgot_password.is_reset_password_displayed_in_title()
    assert context.forgot_password.is_draydex_logo_present_on_page()
    assert context.forgot_password.is_reset_password_heading_present_on_page()
    assert context.forgot_password.is_new_password_field_present_on_page()
    assert context.forgot_password.is_confirm_password_field_present_on_page()
    assert context.forgot_password.is_username_input_field_present_on_page()
    assert context.forgot_password.is_update_password_button_present_on_page()
    assert context.forgot_password.is_back_to_login_button_present_on_page()

    context.forgot_password.enter_new_password()
    context.forgot_password.confirm_new_password()
    context.forgot_password.enter_valid_username("draydexcarrier")

@then('the user should be able to click the "Update Password" button')
def step_impl(context):
    assert context.forgot_password.is_update_password_button_clickable()
    context.forgot_password.click_on_update_password_button()

@then('the message "Your Password has been changed!" should be displayed')
def step_impl(context):
    assert "Your password has been changed!" in context.forgot_password.verify_password_changed_success_message()

@when ('the user enters the username and new password')
def step_impl(context):
    context.login_page= LoginPage(context)
    context.login_page.login('draydexcarrier', 'password')
