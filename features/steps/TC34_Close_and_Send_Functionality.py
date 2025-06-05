import random
import time

from behave import when,then

from pages.CarriersPage import CarriersPage
from pages.Dashboard_page import DashboardPage
from pages.QuoteDetails import CreatedQuoteDetails
from pages.common_action import CommonActions


@then('User should see List of favorite carriers')
def step_impl(context):
    context.carriers_page = CarriersPage(context)
    context.common_actions= CommonActions(context)

    context.common_actions.has_loader_disappeared()
    assert context.carriers_page.is_favourite_carrier_present()

@then('User will fetch data of favorite of carriers')
def step_impl(context):
    global List_of_favorite_carrier_data
    List_of_favorite_carrier_data = context.carriers_page.fetch_carriers_data()


@when('User select the Market same as that of favourite carrier')
def step_impl(context):
    context.createdQuotedetails = CreatedQuoteDetails(context)
    Quote_details_while_creation = context.createdQuotedetails.get_stored_Quote_details()

    market_list = [sublist[4] for sublist in List_of_favorite_carrier_data]
    print(market_list)
    valid_markets = [markets for markets in market_list if markets != 'N/A']
    if valid_markets:
        market = random.choice(valid_markets)
        print(market)
    else:
        market = market_list[0]

    Quote_details_while_creation['Market'] = market
    context.dashboard_page.select_specific_market_from_dropdown(market)
    context.createdQuotedetails.store_quote_details(Quote_details_while_creation)
    context.createdQuotedetails.get_stored_Quote_details()

@then('User should see that the favorite carrier has received the "Carrier Mail" under the "Send to Carrier" section')
def step_impl(context):
    time.sleep(10)
    pass