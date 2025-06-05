import time
from token import MINUS

from behave import given, when,then
from pages.RunAnalysis import RunAnalysis
from pages.RateQuotes_page import RateQuotePage
from pages.common_action import  CommonActions
from pages.FallbackTable_page import FallbackTable

@when('the user fills select market input filed')
def step_impl(context):

    context.runanalysis_page= RunAnalysis(context)
    global market
    market=context.runanalysis_page.fill_market_field()
    print("Market filled in Select market field: ",market)

@when('the user fills origin/destination field')
def step_impl(context):
    global origin_destination
    origin_destination=context.runanalysis_page.fill_address_field()
    print("Address filled in Origin destination field: ",origin_destination)

@when('the user clicks on Run Analysis button')
def step_impl(context):
    context.runanalysis_page.click_on_runAnalysis_button()

    context.common_actions=CommonActions(context)
    context.common_actions.has_loader_disappeared()

@then('the user should see the data according to filter applied')
def step_impl(context):
    context.common_actions.are_all_markets_selected_one(market)

    global Min_Roundtrip, Max_Roundtrip
    Min_Roundtrip=context.runanalysis_page.get_value_in_min_roundtrip()
    print("MinimumRoundtrip value from the table: ",Min_Roundtrip)
    Max_Roundtrip=context.runanalysis_page.get_value_in_max_roundtrip()
    print("Maximum Roundtrip value from the table: ",Max_Roundtrip)

    context.common_actions.are_all_roundtrips_between_min_and_max(Min_Roundtrip,Max_Roundtrip)

@then('user will fetch multiplier from fallback back table')
def step_impl(context):
    context.fallback_table= FallbackTable(context)
    context.fallback_table.open_fallback_table_page()

    time.sleep(5)
    global Avg_Roundtrip
    Avg_Roundtrip= (Min_Roundtrip+Max_Roundtrip)/2
    print("Round trip miles for which we need $/mile rate from fallback table: ",Avg_Roundtrip)

    global Multiplier
    Multiplier= context.fallback_table.fetch_dollar_per_mile_for_roundtrip_miles(Avg_Roundtrip)
    print("$/mile rate for that Round trip Miles: ", Multiplier)

@when('the user will move back to Rate Quotes Page')
def step_impl(context):
    context.rate_quote_page = RateQuotePage(context)
    context.rate_quote_page.move_to_rate_quotes_page()

    context.common_actions = CommonActions(context)
    context.common_actions.has_loader_disappeared()

@then('the user will verify calculations under "Avg. Spot Carrier Rate w/Fuel"')
def step_impl(context):
    calculated_Avg_Spot_Carrier_Rate_Fuel= Avg_Roundtrip * Multiplier
    print("calculated Avg Spot Carrier Rate Fuel: ",calculated_Avg_Spot_Carrier_Rate_Fuel)

    assert context.runanalysis_page.get_Avg_Spot_Carrier_Rate_Fuel() == calculated_Avg_Spot_Carrier_Rate_Fuel