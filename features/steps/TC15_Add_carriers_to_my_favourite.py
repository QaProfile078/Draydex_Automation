import time
from behave import when,then
from pages.CarriersPage import CarriersPage


@when('User click on "+ Add to Carriers"')
def step_impl(context):
    context.carriers_page= CarriersPage(context)
    context.carriers_page.click_on_add_to_carrier()

@then('User should see a confirmation popup with buttons "Confirm" and "Close"')
def step_impl(context):
    buttons_to_check= ["Confirm","Close"]
    button_in_popup= context.carriers_page.buttons_present_in_modal_popup()
    for entry in buttons_to_check:
        assert entry in button_in_popup, f'{entry} button is not in confirmation pop-up'

@when('User click on "Confirm"')
def step_impl(context):
    context.carriers_page = CarriersPage(context)
    context.carriers_page.click_on_confirm()

@then('User should see a message "Added to carriers successfully"')
def step_impl(context):
    message = "Added to carriers successfully"
    assert message in context.carriers_page.popup_message_after_adding_to_favourite(), f'{message} message did not appear'

@when('User click on the "Back" button to return to the "Carriers Listing Page"')
def step_impl(context):
    context.carriers_page = CarriersPage(context)
    context.carriers_page.click_on_back_button()

@when('User click on "My Carrier"')
def step_impl(context):
    time.sleep(5)
    context.carriers_page.click_on_my_carrier()

@then('User should see the favorite carriers with a BLUE background')
def step_impl(context):
    assert context.carriers_page.check_carrier_in_blue_background() , f'Carrier added to favourite is not in My carriers List'
    time.sleep(10)


@when('User select one or more carriers using the checkboxes')
def step_impl(context):
    pass


@then('the "Update Carrier List" button should be enabled')
def step_impl(context):
    pass


@when('User click on "Update Carrier List"')
def step_impl(context):
    pass


@then('User should see a message "My Carrier list updated successfully"')
def step_impl(context):
    pass


@then('the selected carriers should appear under "My Carrier"')
def step_impl(context):
    pass


@when('User remove a carrier from the detail page by clicking "+ Remove as My Carrier" Or User deselect carriers in the listing page and click "Update Carrier List"')
def step_impl(context):
    pass


@then('the carrier should be removed from "My Carrier"')
def step_impl(context):
    pass
