from behave import given,when,then
from pages.common_action import CommonActions

@then('the user will click on "Void Quote" to delete the quote')
def step_impl(context):
    context.common_actions=CommonActions(context)
    context.common_actions.has_loader_disappeared()
    context.rateQuotes_page.click_on_void_quote_button()
    context.rateQuotes_page.click_on_confirm_button_to_proceed_deletion()


