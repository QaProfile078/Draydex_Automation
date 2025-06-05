import time
from behave import when,then
from pages.Forgot_username import ForgotUsername

@when('the user clicks on "Forgot Username" button')
def step_impl(context):
    context.forgot_username= ForgotUsername(context)
    context.forgot_username.click_on_forgot_username()

@then('the user is on Forgot Username Page')
def step_impl(context):
    assert context.forgot_username.is_forgot_username_heading_on_the_page()

@when('User clicks on "Request To Get username" button')
def step_impl(context):
    context.forgot_username.click_on_get_username_button()
    time.sleep(2)

@then('the user should see error messages under required field')
def step_impl(context):
    error_messages=context.forgot_username.error_messages_present_under_required_field()
    assert 'Email is required' in error_messages
    assert 'Address is required' in error_messages
    assert 'Please select a user type' in error_messages

@when('User fills all required data fields')
def step_impl(context):
    context.forgot_username.fill_email_id_field_on_forgot_username_page()
    context.forgot_username.fill_dot_number_field_on_forgot_username_page()
    context.forgot_username.fill_company_address_field_on_forgot_username_page()
    context.forgot_username.select_customer_usertype()
    context.forgot_username.wait_for_dot_verification()
    time.sleep(10)

    #### NEED TO HANDLE VPN FOR DOT NUMBER ####