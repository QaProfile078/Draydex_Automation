import time
from pages.login_page import LoginPage
from pages.RateQuotes_page import RateQuotePage
from pages.common_action import CommonActions
from behave import given,when,then

@given('the user is on the Rate Quotes page')
def step_impl(context):
    context.login_page = LoginPage(context)
    context.rateQuotes_page= RateQuotePage(context)
    context.common_actions = CommonActions(context)
    context.login_page.open(context)
    context.login_page.login('admin@gofmi.com', 'password')
    context.login_page.submit_login()
    context.common_actions.has_loader_disappeared()

    context.rateQuotes_page.move_to_rate_quotes_page()
    assert context.rateQuotes_page.is_rateQuotes_displayed_in_title()

@when('the user verifies different fields of Rate Quotes page')
def step_impl(context):
    assert context.rateQuotes_page.is_carrier_rate_on_rateQuotes_page()
    assert context.rateQuotes_page.is_carrier_chasis_on_rateQuotes_page()
    assert context.rateQuotes_page.is_accessorial_fee_on_rateQuotes_page()
    assert context.common_actions.is_data_table_present_on_page()
    assert context.rateQuotes_page.is_differnt_sorts_present_on_rateQuotes_page()

# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------

@when('click on Quote sort button')
def step_impl(context):
    context.rateQuotes_page.click_on_Quote_to_sort()

@then('the user should see Quote ids in ascending order')
def step_impl(context):
    assert context.rateQuotes_page.is_quotes_in_ascending()
    print("Quotes are in ascending checked")


@then('the user click on Quote sort button again')
def step_def(context):
    context.rateQuotes_page.click_on_Quote_to_sort()

@then('the user should see Quote ids in descending order')
def step_def(context):
    assert context.rateQuotes_page.is_quotes_in_descending()
    print("Quotes are in descending checked")

# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------

@when('click on Market sort button')
def step_impl(context):
    context.rateQuotes_page.click_on_market_to_sort()

@then('the user should see Markets in ascending order')
def step_impl(context):
    assert context.rateQuotes_page.is_market_in_ascending()
    print("Markets are in ascending checked")


@then('the user click on Market sort button again')
def step_impl(context):
    context.rateQuotes_page.click_on_market_to_sort()


@then('the user should see Markets in descending order')
def step_impl(context):
    assert context.rateQuotes_page.is_market_in_descending()
    print("Markets are in descending checked")

# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------

@when('click on Origin/Destination sort button')
def step_impl(context):
    context.rateQuotes_page.click_on_origin_destination_to_sort()

@then('the user should see Origin/Destination in ascending order')
def step_impl(context):
    assert context.rateQuotes_page.is_origin_destination_in_ascending()
    print("origin/destination are in ascending checked")


@then('the user click on Origin/Destination sort button again')
def step_impl(context):
    context.rateQuotes_page.click_on_origin_destination_to_sort()

@then('the user should see Origin/Destination in descending order')
def step_impl(context):
    assert context.rateQuotes_page.is_origin_destination_in_descending()
    print("origin/destination are in descending checked")

# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------

@when('click on Roundtrip Miles sort button')
def step_impl(context):
    context.rateQuotes_page.click_on_roundtrip_to_sort()

@then('the user should see Roundtrip Miles in ascending order')
def step_impl(context):
    assert context.rateQuotes_page.is_roundtrip_in_ascending()
    print("roundtrip are in ascending checked")

@then('the user click on Roundtrip Miles sort button again')
def step_impl(context):
    context.rateQuotes_page.click_on_roundtrip_to_sort()

@then('the user should see Roundtrip Miles in descending order')
def step_impl(context):
    assert context.rateQuotes_page.is_roundtrip_in_descending()
    print("roundtrip are in descending checked")

# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------

@when('click on Estimated Total sort button')
def step_impl(context):
    context.rateQuotes_page.click_on_estimated_total_to_sort()

@then('the user should see Estimated Total in ascending order')
def step_impl(context):
    assert context.rateQuotes_page.is_estimated_total_in_ascending()
    print("Estimated_total are in ascending checked")

@then('the user click on Estimated Total sort button again')
def step_impl(context):
    context.rateQuotes_page.click_on_estimated_total_to_sort()

@then('the user should see Estimated Total in descending order')
def step_impl(context):
    assert context.rateQuotes_page.is_estimated_total_in_descending()
    print("estimated_total are in descending checked")