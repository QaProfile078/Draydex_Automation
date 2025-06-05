import time

from behave import given,when,then
from pages.QuoteDetails import CreatedQuoteDetails

@when('User clicks on "Send to Carriers"')
def step_impl(context):
    context.quote_details_page= CreatedQuoteDetails(context)
    context.quote_details_page.click_on_Send_To_Carrier_button()

@then('the "E-mail Spot Quote Request to Your Carriers" pop-up should display')
def step_impl(context):
    assert context.quote_details_page.has_send_to_carrier_popup_appeared(), 'No Popup appeared with "E-mail Spot Quote Request to Your Carriers" header'

@then('the following columns should be displayed')
def step_impl(context):
    columns_to_display_send_to_carrier_popup=["Include","Sent?","Carrier Name","Phone#","Email","Other Email"]
    columns_present_on_send_to_carrier_popup= context.quote_details_page.get_send_to_carrier_popup_columns()

    for entry in columns_to_display_send_to_carrier_popup:
        assert entry in  columns_present_on_send_to_carrier_popup , f'{entry} column is not present on the send to carrier pop up'

@when('User enters a Carrier Name in the "Carrier Name" field and selects a carrier')
def step_impl(context):
    context.quote_details_page= CreatedQuoteDetails(context)
    if context.server == 'prod':
        context.carrier_name = context.quote_details_page.enter_carrier_name("Test Carrier2904")
    else:
        context.carrier_name=context.quote_details_page.enter_carrier_name("TestCarrier0402")

    print("Carrier Name: ",context.carrier_name)

@then('the system should automatically fetch the selected carrier\'s Phone# and Email')
def step_impl(context):

    context.phone_number=context.quote_details_page.get_filled_phone_number()
    print("Carrier Phone Number: ",context.phone_number)
    assert context.phone_number is not None
    context.email = context.quote_details_page.get_filled_email()
    print("Carrier email id:",context.email)
    assert context.email is not None


@then('User should be able to enter an email in the "Other Email" section')
def step_impl(context):

    other_email = context.quote_details_page.fill_other_email_field("testuser078@yopmail.com")


@then('User should be able to select multiple carriers using Add more button')
def step_impl(context):
    context.quote_details_page.click_on_add_more_button()


@then('User should be able to check the "Include" column to send an email to a particular carrier or select the "Select ALL" checkbox to send the email to all carriers')
def step_impl(context):
    pass


@then('User should be able to press the "Submit" button to send the email to a carrier')
def step_impl(context):
    pass


@when('User presses the "Submit" button')
def step_impl(context):
    pass


@when('User should see "Mail sent to carrier" popup message')
def step_impl(context):
    pass


@then('the "Sent?" status should be displayed as "Yes" for all the carriers to which mail has been sent')
def step_impl(context):
    pass

