# import time
#
# from behave import given, when, then
# from pages.CustomerRegistration import CustomerRegistration
# @when('the user clicks on "Register Now" button')
# def step_impl(context):
#     context.customer_reg= CustomerRegistration(context)
#     context.customer_reg.click_on_register_now_button()
#
# @when('select "Customer" for registration')
# def step_impl(context):
#     context.customer_reg.click_on_customer_button()
#
# @then('the user is on Customer Registration Page')
# def step_impl(context):
#     assert context.customer_reg.is_customer_registration_displayed_in_title()
#
# @when('User clicks on "Register" button without filling details')
# def step_impl(context):
#     time.sleep(180)
#     assert context.customer_reg.verify_cloudfare_success_message()
#     context.customer_reg.click_on_register_button_to_submit()
#     time.sleep(10)
#
# @then('the user should see error messages under required field')
# def step_impl(context):
#     pass
