import time

from behave import given,when,then

from pages.Dashboard_page import DashboardPage
from pages.Manage_MarketTerminal import ManageMarketTerminal
from pages.common_action import CommonActions


@when('User click the "Manage Market" button')
def step_impl(context):
    context.manage_market_terminal=ManageMarketTerminal(context)
    context.manage_market_terminal.click_on_manage_market()

@then('User should be taken to the Market management page')
def step_impl(context):
    context.common_actions.has_loader_disappeared()
    assert context.manage_market_terminal.is_user_on_market_terminal_management_page()

@then('the user should see the following sections')
def step_impl(context):
    context.manage_market_terminal=ManageMarketTerminal(context)

    List_of_columns_to_check= ["Market Name","Country","State","Name","Zip Code"]
    List_of_columns_present_on_page= context.manage_market_terminal.get_list_of_column_names()
    for entry in List_of_columns_to_check:
        assert entry in List_of_columns_present_on_page, f'{entry} column is not present on the page'

    List_of_buttons_to_check=["Add Market","Remove Market","Upload CSV","Clear","Active Markets","InActive Markets"]
    List_of_buttons_present_on_page = context.manage_market_terminal.get_list_of_button_names()
    for entry in List_of_buttons_to_check:
        assert entry in List_of_buttons_present_on_page, f'{entry} column is not present on the page'

@when('the user clicks on "Add Market" button')
def step_impl(context):
    context.common_actions=CommonActions(context)
    context.manage_market_terminal=ManageMarketTerminal(context)

    context.manage_market_terminal.click_add_Market()
    context.common_actions.has_loader_disappeared()

@then('the user should see a popup with the following fields')
def step_impl(context):
    List_of_labels_to_check_on_add_market_popup = ["Country","State","Name","Zip Code"]
    List_of_labels_present_on_add_market_popup = context.manage_market_terminal.get_list_of_labels_on_add_market_popup()
    for entry in List_of_labels_to_check_on_add_market_popup:
        assert entry in List_of_labels_present_on_add_market_popup, f'{entry} column is not present on the page'

    print("all labels are present on the add market popup")

@when('the user fill all the required fields')
def step_impl(context):
    context.manage_market_terminal= ManageMarketTerminal(context)
    Country=context.manage_market_terminal.select_country_from_dropdown()
    time.sleep(2)
    State = context.manage_market_terminal.select_state_from_dropdown()
    Market_name = context.manage_market_terminal.fill_market_name_field()
    Zip_code = context.manage_market_terminal.fill_zip_code_field(Country)

    context.Market_data_while_creation={"Country":Country, "State":State, "Name": Market_name, "Zip Code":Zip_code}
    context.manage_market_terminal.created_market_data(context.Market_data_while_creation)
    context.manage_market_terminal.get_created_market_data()

@then('User see a popup with message "Market created"')
def step_impl(context):
    assert context.manage_market_terminal.verify_Market_created_message()

@then("the new Market should be added to the list of active Markets")
def step_impl(context):
    context.manage_market_terminal.fill_created_market_details_in_search_box(context.Market_data_while_creation)

    context.common_actions =CommonActions(context)
    context.common_actions.has_loader_disappeared()
    time.sleep(3)

    assert context.manage_market_terminal.verify_market_in_market_list(context.Market_data_while_creation)

@given('the user is on the "Create Quote/Quote Detail Page"')
def step_impl(context):
    context.common_actions=CommonActions(context)
    context.common_actions.move_to_dashboard_page()
    context.common_actions.has_loader_disappeared()


@then('the user should see the created market listed in the dropdown')
def step_impl(context):
    context.dashboard_page = DashboardPage(context)
    context.manage_market_terminal=ManageMarketTerminal(context)
    market_data=context.manage_market_terminal.get_created_market_data()
    assert context.dashboard_page.verify_market_in_market_dropdown_list(market_data)
#
# @when('the user clicks on the "+" icon next to a market')
# def step_impl(context):
#     pass
#
#
# @then('the user clicks "Submit"')
# def step_impl(context):
#     pass
#
#
# @then('the terminal should be created successfully')
# def step_impl(context):
#     pass
#
#
# @when('the user selects the market under which the terminal is created')
# def step_impl(context):
#     pass
#
#
# @when('clicks on the "Terminal" dropdown')
# def step_impl(context):
#     pass
#
#
# @then('the user should see the created terminal listed in the dropdown')
# def step_impl(context):
#     pass
