import time

from behave import given,then,when
from pages.common_action import CommonActions
from pages.RateQuotes_page import RateQuotePage
from pages.login_page import LoginPage

search_quote=''
Requestor=''
Origin_destination=''
Min_Roundtrip_Miles=''
Max_Roundtrip_Miles=''
Min_Estimated_Total=''
Max_Estimated_Total=''


@given('the user will go to the Rate Quotes page')
def step_impl(context):
    context.login_page = LoginPage(context)
    context.rateQuotes_page = RateQuotePage(context)
    context.commonActions= CommonActions(context)

    context.login_page.open(context)
    context.login_page.login('admin@gofmi.com', 'password')
    context.login_page.submit_login()
    context.commonActions.has_loader_disappeared()

    context.rateQuotes_page.move_to_rate_quotes_page()
    context.commonActions.has_loader_disappeared()
    assert context.rateQuotes_page.is_rateQuotes_displayed_in_title()

@when('the user verifies fields of Rate Quotes page')
def step_impl(context):
    assert context.rateQuotes_page.is_carrier_rate_on_rateQuotes_page()
    assert context.rateQuotes_page.is_carrier_chasis_on_rateQuotes_page()
    assert context.rateQuotes_page.is_accessorial_fee_on_rateQuotes_page()
    assert context.rateQuotes_page.is_differnt_sorts_present_on_rateQuotes_page()
    assert context.commonActions.is_data_table_present_on_page()

#--------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------#

@when('click on Quote id placeholder filter field')
def step_impl(context):
    global search_quote
    search_quote = context.commonActions.get_random_quote_to_search()
    context.commonActions.goto_quote_placeholder().click()

@when('the user enter a quote id')
def step_impl(context):
    for digit in search_quote:
        context.commonActions.goto_quote_placeholder().send_keys(digit)
        context.commonActions.has_loader_disappeared()


@then('the user should see only that specific Quote id in the table')
def step_impl(context):
    assert context.commonActions.is_quote_present_in_table(search_quote)


#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#

@when('click on Requested By placeholder filter field')
def step_impl(context):
    context.commonActions.goto_requested_by_placeholder().click()

@then('the user enter a Requestor name')
def step_impl(context):
    global Requestor
    Requestor = context.commonActions.get_random_requestor()
    context.commonActions.goto_requested_by_placeholder().send_keys(Requestor)
    context.commonActions.has_loader_disappeared()


@then('the user should see data related to that specific Requestor only in the table')
def step_impl(context):
    assert context.commonActions.are_all_requestor_selected_one(Requestor)

#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#

@when('click on Origin/Destination placeholder filter field')
def step_impl(context):
    global Origin_destination
    Origin_destination = context.commonActions.get_random_Origin_destination()
    context.commonActions.goto_origin_destination_placeholder().click()

@then('the user enter a Origin/Destination')
def step_impl(context):

    context.commonActions.goto_origin_destination_placeholder().send_keys(Origin_destination)
    context.commonActions.has_loader_disappeared()
    time.sleep(5)

@then('the user should see data related to entered Origin/Destination only in the table')
def step_impl(context):
    assert context.commonActions.are_all_Origin_destination_selected_one(Origin_destination)

#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#
@when('click on Minimum Roundtrip Miles placeholder filter field')
def step_impl(context):
    global Min_Roundtrip_Miles
    Min_Roundtrip_Miles = context.commonActions.get_random_min_roundtrip_miles()
    context.commonActions.goto_min_roundtrip_miles_placeholder().click()

@then('the user enter a Minimum Roundtrip Miles')
def step_impl(context):
    context.commonActions.goto_min_roundtrip_miles_placeholder().send_keys(Min_Roundtrip_Miles)

@when('click on Maximum Roundtrip Miles placeholder filter field')
def step_impl(context):
    global Max_Roundtrip_Miles
    Max_Roundtrip_Miles = context.commonActions.get_random_max_roundtrip_miles()
    context.commonActions.goto_max_roundtrip_miles_placeholder().click()

@then('the user enter a Maximum Roundtrip Miles')
def step_impl(context):
    context.commonActions.goto_max_roundtrip_miles_placeholder().send_keys(Max_Roundtrip_Miles)

@then('the user click on search button under Roundtrip miles')
def step_impl(context):
    context.commonActions.click_on_search_under_roundtrip()
    context.commonActions.has_loader_disappeared()

@then('the user should see data between Minimum Roundtrip Miles and Maiximum Roundtrip Miles only in the table')
def step_impl(context):
    assert context.commonActions.are_all_roundtrips_between_min_and_max(Min_Roundtrip_Miles, Max_Roundtrip_Miles)

#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#


@when('click on Minimum Estimated Total placeholder filter field')
def step_impl(context):
    global Min_Estimated_Total
    Min_Estimated_Total = context.commonActions.get_random_min_estimated_total()
    print(Min_Estimated_Total)
    context.commonActions.goto_min_estimated_total_placeholder().click()


@then('the user enter a Minimum Estimated Total')
def step_impl(context):
    context.commonActions.goto_min_estimated_total_placeholder().send_keys(Min_Estimated_Total)


@when('click on Maximum Estimated Total placeholder filter field')
def step_impl(context):
    global Max_Estimated_Total
    Max_Estimated_Total = context.commonActions.get_random_max_estimated_total()
    print(Max_Estimated_Total)
    context.commonActions.goto_max_estimated_total_placeholder().click()


@then('the user enter a Maximum Estimated Total')
def step_impl(context):
    context.commonActions.goto_max_estimated_total_placeholder().send_keys(Max_Estimated_Total)


@then('the user click on search button under Estimated Total')
def step_impl(context):
    context.commonActions.click_on_search_under_estimatedTotal()
    context.commonActions.has_loader_disappeared()


@then('the user should see data between Minimum Estimated Total and Maiximum Estimated Total only in the table')
def step_impl(context):
    context.commonActions.are_all_estimatedTotal_between_min_and_max(Min_Estimated_Total, Max_Estimated_Total)


#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#

@when('click on status select dropdown')
def step_impl(context):
    pass


@then('the user select a status from the dropdown')
def step_impl(context):
    pass


@then('the user shold see all the quotes in the table with same status')
def step_impl(context):
   pass


@when('click on Origin/Destination filter button')
def step_impl(context):
    pass


@then('the user click on Origin/Destination filter button again')
def step_impl(context):
    pass


@when('click on Roundtrip Miles filter button')
def step_impl(context):
    pass


@then('the user click on Roundtrip Miles filter button again')
def step_impl(context):
    pass


@when('click on Estimated Total filter button')
def step_impl(context):
    pass


@then('the user click on Estimated Total filter button again')
def step_impl(context):
    pass
