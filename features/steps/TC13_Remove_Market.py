import time

from behave import when,then

from pages.Dashboard_page import DashboardPage
from pages.Manage_MarketTerminal import ManageMarketTerminal
from pages.common_action import CommonActions

selected_Market_Data= None


@when('User search for Market from active Market tabel to Remove')
def step_impl(context):
    context.manage_market=ManageMarketTerminal(context)
    market_data=context.manage_market.get_created_market_data()
    # market_data={'Country': 'USA', 'State': 'TENNESSEE', 'Name': 'TestMarket36', 'Zip Code': '99302'}

    context.manage_market.fill_market_details_in_search_box(market_data)
    time.sleep(10)
    selected_Market_Data = context.manage_market.select_market_to_remove(market_data)
    print("selected Market_ data: ",selected_Market_Data)


@then('User should see Remove Market button is enabled')
def step_impl(context):
    assert context.manage_market.Is_RemoveMarket_button_disabled() == False , "Remove Market Button is not enabled"

@when('User clicks "Remove Market" button')
def step_impl(context):
    context.manage_market.click_on_Remove_Market()

@then('User should see a Market Removal confirmation Popup with close and confirm buttons')
def step_impl(context):
    assert context.manage_market.has_confirm_Market_Removal_popup_aapeared(), "Market Removal confirmation popup did not appear as expected."
    assert context.manage_market.Is_close_and_confirm_button_present()

@when('User click on "Cancel" to cancel Market Removal')
def step_impl(context):
    context.manage_market.click_on_cancel_confirmation()

@then('User should see selected Market still in list of active Markets')
def step_impl(context):
    market_data=context.manage_market.get_created_market_data()
    # market_data={'Country': 'USA', 'State': 'TENNESSEE', 'Name': 'TestMarket36', 'Zip Code': '99302'}

    context.manage_market.fill_market_details_in_search_box(market_data)
    time.sleep(10)
    assert context.manage_market.verify_market_in_market_list(market_data)

@then('User will click on clear to reset Market table')
def step_impl(context):
    context.manage_market.click_on_clear_button()
    context.common_actions= CommonActions(context)
    context.common_actions.has_loader_disappeared()

@when('User click on "Confirm" to confirm Market Removal')
def step_impl(context):
    context.manage_market.click_on_confirm_confirmation()

@then('User should see "Market(s) move to inactive" popup message')
def step_impl(context):
    context.manage_market.verify_market_moved_to_inactive_popup()

@then('User should see selected Market not in list of active Markets')
def step_impl(context):
    market_data = context.manage_market.get_created_market_data()
    # market_data={'Country': 'USA', 'State': 'TENNESSEE', 'Name': 'TestMarket36', 'Zip Code': '99302'}

    context.manage_market.fill_market_details_in_search_box(market_data)
    time.sleep(10)
    assert "No record found" in context.manage_market.verify_market_in_market_list(market_data), "The market deleted is still in active Markets list"

@when('User click on InActive Market button')
def step_impl(context):
    context.manage_market=ManageMarketTerminal(context)
    context.manage_market.click_on_InActive_Market()

    context.common_actions = CommonActions(context)
    context.common_actions.has_loader_disappeared()

@then('the Market removed should be added to the InActive Market table')
def step_impl(context):
    market_data = context.manage_market.get_created_market_data()
    # market_data={'Country': 'USA', 'State': 'TENNESSEE', 'Name': 'TestMarket36', 'Zip Code': '99302'}

    context.manage_market.fill_market_details_in_search_box(market_data)
    time.sleep(10)
    assert context.manage_market.verify_market_in_market_list(market_data) , "The Market deleted is not moved to inActive Markets list "

@then('the user should not see the created market listed in the dropdown')
def step_impl(context):
    context.dashboard_page = DashboardPage(context)
    context.manage_market_terminal=ManageMarketTerminal(context)
    market_data=context.manage_market_terminal.get_created_market_data()
    # market_data={'Country': 'USA', 'State': 'TENNESSEE', 'Name': 'TestMarket36', 'Zip Code': '99302'}

    assert context.dashboard_page.verify_market_in_market_dropdown_list(market_data) == False