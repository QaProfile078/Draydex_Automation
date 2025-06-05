import time

from behave import when,then

from pages.Dashboard_page import DashboardPage
from pages.QuoteDetails import CreatedQuoteDetails
from pages.common_action import CommonActions


@when('User modify a value in the Quote Detail page')
def step_impl(context):
    context.dashboard_functions= DashboardPage(context)
    context.createdQuotedetails = CreatedQuoteDetails(context)

    modified_equipment=context.dashboard_functions.select_equipment_from_dropdown()

    while modified_equipment == context.createdQuotedetails.get_stored_Quote_details()['Equipment']:
        modified_equipment = context.dashboard_functions.select_equipment_from_dropdown()


@then('the "Update Changes" button should be enabled')
def step_impl(context):
    context.quote_details_page= CreatedQuoteDetails(context)
    assert context.quote_details_page.is_update_changes_button_enabled(), "Update Changes button is still disabled"

@then('User click on the "Update Changes" button')
def step_impl(context):
    context.quote_details_page= CreatedQuoteDetails(context)
    context.quote_details_page.click_on_update_changes()

@then('User should see a pop-up with message "You Have Updated the Details of This Quote!"')
def step_impl(context):
    context.common_actions= CommonActions(context)
    context.common_actions.has_loader_disappeared()
    assert context.quote_details_page.has_changes_updated_popup_appeared(), 'You Have Updated the Details of This Quote!" header did not appear'

    context.quote_details_page.click_on_close_changes_updated_popup()

    context.common_actions.has_loader_disappeared()

@when('User click on "View Log" button')
def step_impl(context):
    context.common_actions.has_loader_disappeared()
    context.quote_details_page.click_on_view_log_button()
    context.common_actions.has_loader_disappeared()

@then('User should see log of updated data in it')
def step_impl(context):
    assert context.quote_details_page.check_log_has_entry_of_updated_data(), "Log of Updated Data is not Present"
    context.quote_details_page.close_view_log_popup()

@then('Store the Quotes updated data')
def step_impl(context):
    context.createdQuotedetails = CreatedQuoteDetails(context)
    quote_details_after_update = context.createdQuotedetails.data_in_quote_details_page()
    context.createdQuotedetails.store_quote_details(quote_details_after_update)
    context.createdQuotedetails.get_stored_Quote_details()
