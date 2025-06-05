import time

from behave import given,when,then

from pages.QuoteDetails import CreatedQuoteDetails
from pages.common_action import CommonActions


@when('the user will check for "ACTIVE/RECENT SPOT QUOTES" table')
def step_impl(context):
    context.common_actions=CommonActions(context)
    try:
        context.common_actions.has_loader_disappeared()
        context.common_actions.is_data_table_present_on_page()
    except:
        context.common_actions.is_data_table_present_on_page()

@when('user searches for quote in the table')
def step_impl(context):
    context.common_actions=CommonActions(context)
    context.common_actions.goto_quote_placeholder().click()
    if  context.quote_id is not None:
        quote_id= context.quote_id
    else:
        quote_id=context.common_actions.get_stored_quote()

    print("Quote :-------", quote_id)
    for digit in quote_id:
        context.common_actions.goto_quote_placeholder().send_keys(digit)
        context.common_actions.has_loader_disappeared()

@when('user should see the quote in the table on current page')
def step_impl(context):

    if  context.quote_id is not None:
        quote_id= context.quote_id
    else:
        quote_id=context.common_actions.get_stored_quote()
    assert context.common_actions.is_quote_present_in_table(quote_id)

@then('the user will click on quote id')
def step_impl(context):
    if context.quote_id is not None:
        quote_id= context.quote_id
    else:
        quote_id=context.common_actions.get_stored_quote()
    context.common_actions.click_on_quote_id(quote_id)

@then('the following buttons should be displayed')
def step_impl(context):
    buttons_to_verify=["SEND TO CARRIERS","ADD RATE","UPDATE CHANGES","VOID QUOTE"]
    context.common_actions.has_loader_disappeared()
    time.sleep(2)
    List_of_buttons_on_Quote_details_page= context.common_actions.get_List_of_buttons_on_Quote_details_page()

    for entry in buttons_to_verify:
        assert entry in List_of_buttons_on_Quote_details_page, f'{entry} button is not present on the Quote Details page'


@then('the user will verify all the details of the quote')
def step_impl(context):
    context.createdQuotedetails = CreatedQuoteDetails(context)
    quote_details_after_creation=context.createdQuotedetails.data_in_quote_details_page()
    Stored_Quote_details= context.createdQuotedetails.get_stored_Quote_details()

    assert Stored_Quote_details['Market'] == quote_details_after_creation['Market'], "Market is not same as selected during Quote Creation"

    if Stored_Quote_details['Terminal'] == "Select Terminal":
        assert "select" in quote_details_after_creation['Terminal'].lower()
    else:
        assert Stored_Quote_details['Terminal'].lower() == quote_details_after_creation[
            'Terminal'].lower(), "Terminal is not same as selected during Quote Creation"

    assert Stored_Quote_details['origin_destination'] in quote_details_after_creation[
        'origin_destination'], "Origin_Destination is not same as selected during Quote Creation"
    assert Stored_Quote_details['special_services'] == quote_details_after_creation[
        'special_services'], "Special services is not same as selected during Quote Creation"
    assert Stored_Quote_details['Equipment'].lower() == quote_details_after_creation[
        'Equipment'].lower(), "Equipment is not same as selected during Quote Creation"
    assert str(Stored_Quote_details['Quantity']) == str(
        quote_details_after_creation['Quantity']), "Quantity is not same as selected during Quote Creation"
    assert Stored_Quote_details['Type'].lower() == quote_details_after_creation[
        'Type'].lower(), "Type is not same as selected during Quote Creation"

    assert str(Stored_Quote_details['Size']) == str(
        quote_details_after_creation['Size']), "Size is not same as selected during Quote Creation"

    if Stored_Quote_details['Weight_unit'] == 'KG':
        assert float(quote_details_after_creation['Weight']) == round(
            float(Stored_Quote_details['Weight']) * 2.20462, 2)
        assert quote_details_after_creation[
                   'Weight_unit'].lower() == 'lbs', "Weight unit is not in LBS or No weight unit is selected "

    else:
        assert str(Stored_Quote_details['Weight']) == str(quote_details_after_creation['Weight'])
        assert Stored_Quote_details['Weight_unit'].lower() == quote_details_after_creation[
            'Weight_unit'].lower(), "Weight unit is not in LBS or No weight unit is selected "

    # assert Stored_Quote_details['Market'] == context.createdQuotedetails.fetch_selected_market(), "Market is not same as selected during Quote Creation"
    #
    # if Stored_Quote_details['Terminal'] == "Select Terminal":
    #     assert context.createdQuotedetails.fetch_selected_terminal()== "Select"
    # else:
    #     assert Stored_Quote_details['Terminal'].lower() == context.createdQuotedetails.fetch_selected_terminal().lower(), "Terminal is not same as selected during Quote Creation"
    #
    # assert Stored_Quote_details['Origin_destination'] in context.createdQuotedetails.fetch_selected_origin_destination(), "Origin_Destination is not same as selected during Quote Creation"
    # assert Stored_Quote_details['Special_services'] == context.createdQuotedetails.fetch_selected_special_services(), "Special services is not same as selected during Quote Creation"
    # assert Stored_Quote_details['Equipment'].lower() == context.createdQuotedetails.fetch_selected_equipment().lower(), "Equipment is not same as selected during Quote Creation"
    # assert str(Stored_Quote_details['Quantity']) == str(context.createdQuotedetails.fetch_filled_quantity()) , "Quantity is not same as selected during Quote Creation"
    # assert Stored_Quote_details['Type'].lower() == context.createdQuotedetails.fetch_selected_type().lower() , "Type is not same as selected during Quote Creation"
    # assert str(Stored_Quote_details['Size']) == str(context.createdQuotedetails.fetch_selected_size()), "Size is not same as selected during Quote Creation"
    #
    # if Stored_Quote_details['Weight_unit'] == 'KG':
    #     assert float(context.createdQuotedetails.fetch_filled_weight()) == round(float(Stored_Quote_details['Weight']) * 2.20462, 2)
    #     assert context.createdQuotedetails.fetch_selected_weight_unit().lower() == 'lbs', "Weight unit is not in LBS or No weight unit is selected "
    #
    # else:
    #     assert str(Stored_Quote_details['Weight']) == str(context.createdQuotedetails.fetch_filled_weight())
    #     assert Stored_Quote_details['Weight_unit'].lower() == context.createdQuotedetails.fetch_selected_weight_unit().lower(), "Weight unit is not in LBS or No weight unit is selected "

#
# @then('User click on Close button.')
# def step_impl(context):
#     context.common_actions=CommonActions(context)
#     context.common_actions.has_loader_disappeared()
#     context.createdQuotedetails.click_on_close_button()

@then('the user should see "No record found." message in "ACTIVE/RECENT SPOT QUOTES" table')
def step_impl(context):
    try:
        quote_id = context.quote_id
    except:
        quote_id = context.common_actions.get_stored_quote()
    assert "No record found" in context.common_actions.is_quote_present_in_table(quote_id)



