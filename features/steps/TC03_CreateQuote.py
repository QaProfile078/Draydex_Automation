import time
from behave import given,when,then

from pages.RateQuotes_page import RateQuotePage
from pages.login_page import LoginPage
from pages.Dashboard_page import DashboardPage
from pages.common_action import CommonActions
from pages.QuoteDetails import CreatedQuoteDetails



@given('the user is on the dashboard page')
def step_impl(context):
    context.login_page = LoginPage(context)
    context.dashboard_page= DashboardPage(context)
    context.common_actions= CommonActions(context)

    context.login_page.open(context)

    if (context.email_id and context.password):
        context.login_page.login(context.email_id, context.password)
    else:
        context.login_page.login('admin@gofmi.com', 'password')
        # context.login_page.login('admin@gofmi.com', 'Password@1234')


    # context.login_page.login(context.email_id, context.password)
    context.login_page.submit_login()

    context.common_actions.has_loader_disappeared()
    assert context.dashboard_page.is_dashboard_displayed_in_title()
    
@given('the user move to the rate quotes page')
def step_impl(context):
    context.login_page = LoginPage(context)
    context.dashboard_page = DashboardPage(context)
    context.common_actions = CommonActions(context)
    context.rateQuotes_page = RateQuotePage(context)

    context.login_page.open(context)
    # context.login_page.login('admin@gofmi.com', 'password')
    context.login_page.login(context.email_id, context.password)
    context.login_page.submit_login()
    context.common_actions.has_loader_disappeared()
    context.rateQuotes_page.move_to_rate_quotes_page()
    assert context.rateQuotes_page.is_rateQuotes_displayed_in_title()

@when('user move to the rate quotes page')
def step_impl(context):
    context.rateQuotes_page = RateQuotePage(context)
    context.rateQuotes_page.move_to_rate_quotes_page()
    assert context.rateQuotes_page.is_rateQuotes_displayed_in_title()


@when('the user misses to fill required field for quote creation')
def step_impl(context):
    pass

@when('the user click Create Quote button')
def step_impl(context):
    context.dashboard_page.click_on_create_quote()

@then('the user should see "value is required" in error message under')
def step_impl(context):
    assert context.dashboard_page.check_invalid_feedback_message() , "Value Required is not present under Required fields"

@then('the user will be on dashboard page.')
def step_impl(context):
    assert context.dashboard_page.is_dashboard_displayed_in_title(), "User is not on Dashboard"

@when('the user fill all required details for quote creation')
def step_impl(context):
    context.common_actions=CommonActions(context)
    context.dashboard_page = DashboardPage(context)
    Quote_details_while_creation={}
    Quote_details_while_creation['origin_destination']= context.dashboard_page.fill_origin_destination_field()
    Quote_details_while_creation['special_services']= context.dashboard_page.fill_special_services_field()
    Quote_details_while_creation['Weight_unit']= context.dashboard_page.select_weight_unit_from_dropdown()
    Quote_details_while_creation['Equipment']= context.dashboard_page.select_equipment_from_dropdown()
    Quote_details_while_creation['Terminal']= context.dashboard_page.select_terminal_from_dropdown()
    Quote_details_while_creation['Market']= context.dashboard_page.select_market_from_dropdown()
    Quote_details_while_creation['Size']= context.dashboard_page.select_size_from_dropdown()
    Quote_details_while_creation['Type']= context.dashboard_page.select_type_from_dropdown()
    Quote_details_while_creation['Quantity']= context.dashboard_page.fill_quantity_field()
    Quote_details_while_creation['Weight']= context.dashboard_page.fill_weight_field()

    context.createdQuotedetails=CreatedQuoteDetails(context)
    context.createdQuotedetails.store_quote_details(Quote_details_while_creation)
    context.createdQuotedetails.get_stored_Quote_details()

@then('the user should see "New Quote Created!" message popup with a quote number')
def step_impl(context):
    global quote_id
    quote_id = context.dashboard_page.fetch_quote_id_created()
    context.common_actions.stored_quote_id(quote_id)
    context.common_actions.get_stored_quote()

    print("New Quote is created with Quote ID : ",quote_id)
    assert context.dashboard_page.check_quote_created_message() , "New Quote Created! message is not Present in popup" 

@then('User will verify "View Quote" and "Close & Send" on the newly created Quote pop-up')
def step_impl(context):
    context.dashboard_page=DashboardPage(context)
    assert context.dashboard_page.check_view_quote_present_in_pop_up(), "View Quote Button is not Present"
    assert context.dashboard_page.check_Close_and_Send_present_in_pop_up(), "Close and Send Button is not Present"

@then('the user click "close and send" the message')
def step_impl(context):
    context.dashboard_page=DashboardPage(context)
    context.dashboard_page.click_on_close_and_send()
