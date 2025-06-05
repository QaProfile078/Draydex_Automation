from behave import when,then
from pages.CarriersPage import CarriersPage
from pages.common_action import CommonActions


@when('User click on the "Carriers" option from the left menu')
def step_impl(context):
    context.carriers_page= CarriersPage(context)
    context.common_actions=CommonActions(context)

    context.carriers_page.move_to_carriers_page()
    context.common_actions.has_loader_disappeared()
    context.carriers_page.is_carriers_displayed_in_title()


@then('User should see the "Find & Manage Carriers" heading')
def step_impl(context):
    assert context.carriers_page.is_carrier_table_present()
    assert "Find & Manage Carriers" in context.carriers_page.carrier_table_header()


@then('User should see a list of all carriers in the Draydex application')
def step_impl(context):
    List_of_carriers= context.carriers_page.list_of_carriers_present()
    assert len(List_of_carriers)>1 , "List of carriers has not appeared"

@then('User should see the following radio button options')
def step_impl(context):
    context.carriers_page= CarriersPage(context)
    List_of_Expected_radio_buttons=["20/40FT","53FT","HAZ","TRANSLOAD","CHASSIS","BONDED","PARKING"]
    List_of_radio_buttons_on_Carrier_Page= context.carriers_page.list_of_radio_buttons()
    for entry in List_of_Expected_radio_buttons:
        assert entry in List_of_radio_buttons_on_Carrier_Page, f'"{entry}" Radio button is not present on Carriers Page'


@then('User should see the following column headers')
def step_impl(context):
    List_of_Expected_column_headers= ['CARRIER COMPANY NAME', 'LOCATION', 'SERVICE STATE', 'MARKET', 'PORT/TERMINAL', 'PHONE', 'ENTITY TYPE']
    List_of_columns_on_Carrier_Page= context.carriers_page.list_of_column_headers()
    for entry in List_of_Expected_column_headers:
        assert entry in List_of_columns_on_Carrier_Page, f'"{entry}" column is not present on Carriers Page'


@then('User select a carrier from the list')
def step_impl(context):
    context.carriers_page= CarriersPage(context)
    context.common_actions= CommonActions(context)

    carrier_name= context.carriers_page.open_and_get_random_carrier_profile()
    context.carriers_page.store_selected_carrier_name(carrier_name)
    context.common_actions.has_loader_disappeared()

@then('User should see the following sections on the Carrier Details Page')
def step_impl(context):
    Expected_sections_on_carrier_details_page=['Carrier Company Name', 'MC', 'DOT', 'Carrier Bulletin', 'GENERAL INFORMATION', 'PRIMARY CONTACT INFORMATION', 'MARKETS & TERMINAL SERVICE AREA']
    Sections_on_carrier_details_page= context.carriers_page.list_of_different_sections_on_carrier_details_page()
    for entry in Expected_sections_on_carrier_details_page:
        assert entry in Sections_on_carrier_details_page, f'{entry} section is not present on Carrier Details Page'

@then('User should see a "+ Add to Carriers" button')
def step_impl(context):
    assert context.carriers_page.is_add_to_carrier_button_present(), '"Add to My Carrier" button is not present on carrier details page'

@then('User should see a "Block/Ban Carrier" button')
def step_impl(context):
    assert context.carriers_page.is_block_ban_carrier_button_present(), '"Block/Ban Carrier" button is not present on carrier details page'
