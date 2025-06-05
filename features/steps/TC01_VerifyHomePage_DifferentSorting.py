from behave import given,when,then
from pages.HomePage import HomePage
from pages.common_action import CommonActions

@given('the user is on the Draydex Homepage page')
def step_impl(context):
    context.home_page=HomePage(context)
    context.common_actions=CommonActions(context)

    context.home_page.open_homepage()
    context.common_actions.has_loader_disappeared()

@when('the user clicks on Carrier Company Name title to sort in ascending order')
def step_impl(context):
    context.home_page.click_on_carrier_company_name_sort()

    context.common_actions.has_loader_disappeared()

@then('the user should see Carrier Company Names in ascending order')
def step_impl(context):
    assert context.home_page.are_carrier_company_names_in_ascending()


@when('the user clicks on Carrier Company Name title again to sort in descending order')
def step_impl(context):
    context.home_page.click_on_carrier_company_name_sort()
    context.common_actions.has_loader_disappeared()

@when('the user should see Carrier Company Names in descending order')
def step_impl(context):
    assert context.home_page.are_carrier_company_names_in_descending()
    
#----------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------#

@when('the user clicks on Location title to sort in ascending order')
def step_impl(context):
    context.home_page.click_on_location_sort()
    context.common_actions.has_loader_disappeared()

@then('the user should see Locations in ascending order')
def step_impl(context):
    assert context.home_page.are_locations_in_ascending()


@when('the user clicks on Location title again to sort in descending order')
def step_impl(context):
    context.home_page.click_on_location_sort()
    context.common_actions.has_loader_disappeared()


@when('the user should see Locations in descending order')
def step_impl(context):
    assert context.home_page.are_locations_in_descending()

#----------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------#

@when('the user clicks on Phone title to sort in ascending order')
def step_impl(context):
    context.home_page.click_on_phone_sort()
    context.common_actions.has_loader_disappeared()


@then('the user should see Phone numbers in ascending order')
def step_impl(context):
    assert context.home_page.are_phone_numbers_in_ascending()


@when('the user clicks on Phone title again to sort in descending order')
def step_impl(context):
    context.home_page.click_on_phone_sort()
    context.common_actions.has_loader_disappeared()


@when('the user should see Phone numbers in descending order')
def step_impl(context):
    assert context.home_page.are_phone_numbers_in_descending()

#----------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------#

@when('the user clicks on Service State title to sort in ascending order')
def step_impl(context):
    context.home_page.click_on_service_state_sort()
    context.common_actions.has_loader_disappeared()

@when('If user see multiple service state he picks the lower most among them in ascending order')
def step_impl(context):
    context.List_of_states_in_ascending=context.home_page.pick_service_state_from_row_for_ascending()

@then('the user verifies Service State are in ascending order')
def step_impl(context):
    assert context.List_of_states_in_ascending == sorted(context.List_of_states_in_ascending)


@when('the user clicks on Service State title again to sort in descending order')
def step_impl(context):
    context.home_page.click_on_service_state_sort()
    context.common_actions.has_loader_disappeared()

@when('If user see multiple service state he picks the top most among them in descending order')
def step_impl(context):
    context.List_of_states_in_descending=context.home_page.pick_service_state_from_row_for_descending()

@then('the user verifies Service State are in descending order')
def step_impl(context):
    assert context.List_of_states_in_descending == sorted(context.List_of_states_in_descending, reverse=True)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------#

@when('the user clicks on Market title to sort in ascending order')
def step_impl(context):
    context.home_page.click_on_market_sort()
    context.common_actions.has_loader_disappeared()

@when('If user see multiple Market he picks the lower most among them in ascending order')
def step_impl(context):
    context.List_of_markets_in_ascending=context.home_page.pick_market_from_row_for_ascending()

@then('the user verifies Market are in ascending order')
def step_impl(context):
    assert context.List_of_markets_in_ascending == sorted(context.List_of_markets_in_ascending)


@when('the user clicks on Market title again to sort in descending order')
def step_impl(context):
    context.home_page.click_on_market_sort()
    context.common_actions.has_loader_disappeared()

@when('If user see multiple Market he picks the top most among them in descending order')
def step_impl(context):
    context.List_of_markets_in_descending=context.home_page.pick_market_from_row_for_descending()

@then('the user verifies Market are in descending order')
def step_impl(context):
    assert context.List_of_markets_in_descending == sorted(context.List_of_markets_in_descending, reverse=True)