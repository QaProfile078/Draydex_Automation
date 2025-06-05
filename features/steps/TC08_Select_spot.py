import time

from behave import given,when,then

from pages.AddRate import AddRate
from pages.QuoteDetails import CreatedQuoteDetails
from pages.Switched_window import SwitchedWindow
from pages.common_action import CommonActions
from pages.Rate_to_Client import RateToClient

#---------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------#


import re
def extract_postal_code(address):
    # Regular expression for global postal code formats
    pattern = r'\b\d{5}(?:-\d{4})?\b|\b\d{6}\b|[A-Z]\d[A-Z] \d[A-Z]\d|[A-Z]\d{1,2} [A-Z]{2}|\d{4,10}'

    # Search for postal code in the address
    match = re.search(pattern, address, re.IGNORECASE)

    if match:
        return match.group()
    else:
        return "No postal code found."


def search_and_click_quote(context, Quote_ID):

    context.common_actions.goto_quote_placeholder().click()
    for digit in Quote_ID:
        context.common_actions.goto_quote_placeholder().send_keys(digit)
        context.common_actions.has_loader_disappeared()

    if context.common_actions.is_quote_present_in_table(Quote_ID) == True:
        if context.common_actions.check_selected_quote_is_rated():
            context.common_actions.click_on_quote_id(Quote_ID)
            return True  # Rated Quote found and clicked
        else:
            return False # Found Quote is not Rated
    else:
        return False  # Quote not found In the table

#---------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------#

@when('User open the "Select Spot" popup')
def step_impl(context):
    context.common_actions= CommonActions(context)
    context.rate_to_client= RateToClient(context)

    # Keep trying until quote is found
    while True:
        global Quote_ID
        # Quote_ID = context.common_actions.get_random_quote_to_search()      # Get a random Quote_ID
        # Quote_ID= "7335"                                                    # hardcoded Quote id (used for explicit action

        if context.quote_id is not None:
            Quote_ID = context.quote_id
        else:
            Quote_ID = context.common_actions.get_stored_quote()            # Get Quote just created(used while parallel execution)


        if search_and_click_quote(context, Quote_ID):                       # Attempt to search and click a rated quote
            break                                                           # Exit the loop when rated quote is found and clicked
        else:                                                               # If rated quote is not found, clear and retry
            context.common_actions.click_on_clear_button()
            context.common_actions.has_loader_disappeared()

    context.common_actions.has_loader_disappeared()
    context.rate_to_client.open_rate_to_quote()
    context.common_actions.has_loader_disappeared()

@when('User click on "Select Spot"')
def step_impl(context):
    context.common_actions= CommonActions(context)
    context.add_rate = AddRate(context)
    context.rate_to_client= RateToClient(context)

    context.common_actions.has_loader_disappeared()
    context.rate_to_client.open_rate_to_quote()
    context.common_actions.has_loader_disappeared()

@then('User should see the label "ESTIMATED TOTAL:" at the bottom of the Carrier Charge column')
def step_impl(context):
    assert context.rate_to_client.is_estimated_total_label_present()

@then('User should see the label "GROSS MARGIN:" at the bottom of the Carrier Charge column')
def step_impl(context):
    assert context.rate_to_client.is_gross_margin_label_present()

@then('User will verify the "Estimated Total" field is non-editable')
def step_impl(context):
    context.rate_to_client= RateToClient(context)
    assert context.rate_to_client.is_estimated_total_field_disabled()

@then('User will verify the "Gross Margin" field is non-editable')
def step_impl(context):
    assert context.rate_to_client.is_gross_margin_field_disabled()

@when('User check the "Your Charge" and "Carrier Charges" column')
def step_impl(context):
    context.rate_to_client= RateToClient(context)
    global Carrier_Charges, Your_charges
    Carrier_Charges=context.rate_to_client.get_carrier_charges_for_charge_types()
    Your_charges=context.rate_to_client.get_your_charges_for_charge_types()

@then('User view the sum of "Your Charge" in "Estimated Total"')
def step_impl(context):
    your_charges_calculated_total = context.rate_to_client.estimated_total_calculation(Your_charges)
    global value_in_Estimated_total
    value_in_Estimated_total = context.rate_to_client.value_present_in_esimated_total()

    print(your_charges_calculated_total == value_in_Estimated_total)

@then('User should see the difference between sum of "Your Charge" and sum of "Carrier Charge" in "Gross Margin"')
def step_impl(context):
    context.rate_to_client= RateToClient(context)

    global value_in_Gross_margin, calculated_Gross_margin
    calculated_Gross_margin = context.rate_to_client.Gross_margin_calculation(Carrier_Charges,value_in_Estimated_total)
    value_in_Gross_margin = context.rate_to_client.value_present_in_Gross_Margin()
    print(calculated_Gross_margin == value_in_Gross_margin)

@when('User change one or more charges in the "Your Charge" column')
def step_impl(context):
    context.rate_to_client= RateToClient(context)
    global updated_Your_charges
    updated_Your_charges = context.rate_to_client.get_updated_your_charges_for_charge_types()

@then('User should see the "Estimated Total" column update automatically')
def step_impl(context):
    global updated_value_in_Estimated_total
    updated_value_in_Estimated_total = context.rate_to_client.value_present_in_esimated_total()
    assert updated_value_in_Estimated_total != value_in_Estimated_total

@then('User should see the "ESTIMATED TOTAL" recalculate based on the new charges')
def step_impl(context):

    updated_your_charges_calculated_total = context.rate_to_client.estimated_total_calculation(updated_Your_charges)
    updated_value_in_Estimated_total = context.rate_to_client.value_present_in_esimated_total()

    print(updated_your_charges_calculated_total == updated_value_in_Estimated_total)
    assert updated_your_charges_calculated_total == updated_value_in_Estimated_total, f'Estimated total is not updated or it is calculated wrong'


@then('User should see "GROSS MARGIN" update dynamically')
def step_impl(context):
    global updated_value_in_gross_margin
    updated_value_in_gross_margin = context.rate_to_client.value_present_in_Gross_Margin()
    assert updated_value_in_gross_margin != value_in_Gross_margin

@then('User should see the "GROSS MARGIN" recalculate based on the new charges')
def step_impl(context):
    updated_calculated_Gross_margin = context.rate_to_client.Gross_margin_calculation(Carrier_Charges,updated_value_in_Estimated_total)
    # updated_value_in_Gross_margin = context.rate_to_client.value_present_in_Gross_Margin()
    print(updated_calculated_Gross_margin == updated_value_in_gross_margin)
    assert updated_calculated_Gross_margin == updated_value_in_gross_margin, f'Gross Margin is not updated or it is calculated wrong'

@when('User verifies Email field present at the bottom of popup')
def step_impl(context):
    context.common_actions= CommonActions(context)
    context.rate_to_client= RateToClient(context)
    assert context.rate_to_client.Is_email_field_present()

@then('User will enter an email id into the field')
def step_impl(context):
    global entered_email
    entered_email= context.rate_to_client.enter_email_in_email_field()

@when('User will submit the updated values')
def step_impl(context):
    context.rate_to_client.click_on_submit_button()
    context.common_actions.has_loader_disappeared()

@then('User will see "Quote Rated successfully" message')
def step_impl(context):
        assert "rated successfully" in context.rate_to_client.Quote_rated_popup_message(), "Rated successfully message did not appear"


@then('User will see an entry with updated values having green background')
def step_impl(context):
    context.add_rate= AddRate(context)
    assert context.add_rate.is_rates_table_present(), "Rates table is not present"
    time.sleep(10)
    assert context.add_rate.is_first_row_a_success_class() , "Rates does not have success class or Quote has not been rated"

## Data of the sent rate marked with green background
    Carriers_name_of_sent_rate = context.add_rate.get_carrier_names_from_rates_table()[0]
    Linehauls_of_sent_rate = context.add_rate.get_linehauls_from_rates_table()[0]
    FSC_of_sent_rate = context.add_rate.get_FSC_from_rates_table()[0]
    Chassis_of_sent_rate = context.add_rate.get_Chassis_from_rates_table()[0]


## Data we used while sending rate
    Linehaul= float(updated_Your_charges['Linehaul($)'])
    FSC = float(updated_Your_charges['Linehaul($)'])* float(updated_Your_charges['FSC (%)'])/100
    Chassis = float(updated_Your_charges['Chassis ($/day)'])* updated_Your_charges['min_chassis_days']

    print("Linehaul",Linehaul,"FSC",FSC, "Chassis",Chassis)

    assert Linehaul == Linehauls_of_sent_rate, f"Linehaul in sent rate:{Linehauls_of_sent_rate} is not same as used while sending it ie {Linehaul}"
    assert FSC== FSC_of_sent_rate, f"FSC in sent rate:{FSC_of_sent_rate} is not same as used while sending it ie{FSC}"
    assert  Chassis == Chassis_of_sent_rate, f"Linehaul in sent rate:{Chassis_of_sent_rate} is not same as used while sending it ie{Chassis}"

@when('User will switch to another window')
def step_impl(context):
    context.switched_window= SwitchedWindow(context)
    context.switched_window.open_a_new_tab()
    context.switched_window.switch_to_yopmail()

@when('User open email id entered during Mark-up')
def step_impl(context):
    # context.switched_window.open_the_mailbox(entered_email)
    context.switched_window.open_the_mailbox("draydextesting@yopmail.com")
    assert context.switched_window.is_on_inbox_page()

@then('User will see an email recieved from draydex')
def step_impl(context):
    context.switched_window.refresh_email_list()

@when('User checks if the email is received.')
def step_impl(context):
    assert context.switched_window.is_email_received() , "email not received or taking too long to appear"

@then('User should see Quote number and different informations')
def step_impl(context):
    context.common_actions= CommonActions(context)
    context.createdQuotedetails = CreatedQuoteDetails(context)

    # Quote_id_created = '7359'
    if context.quote_id is not None:
        Quote_id_created = context.quote_id
    else:
        Quote_id_created = context.common_actions.get_stored_quote()

    Quote_id_in_mail=context.switched_window.get_quote_number_from_mail()
    print(Quote_id_in_mail)

    assert Quote_id_created in Quote_id_in_mail
    context.info_in_mail = context.switched_window.get_all_info_related_to_quote()


@then('User Verifies all the infromations are correct')
def step_impl(context):
    Quote_details_while_creation= context.createdQuotedetails.get_stored_Quote_details()
    # print(updated_Your_charges)

    assert  Quote_details_while_creation['Type'].lower() == context.info_in_mail['Delivery Information']['Type'].lower() , "Type in mail is different from Type in Quote"

    if Quote_details_while_creation['Type'].upper() !='EXPORT':
        assert context.info_in_mail['Pickup Information']['Market'] == Quote_details_while_creation['Market'] , "Market in mail is different from Market in Quote"
        assert extract_postal_code(Quote_details_while_creation['origin_destination']) == extract_postal_code(
            context.info_in_mail['Delivery Information']['Address']), "Address is different from Address in Quote"
        if "N/A" in context.info_in_mail['Pickup Information']['Terminal']:
            assert 'select' in (Quote_details_while_creation['Terminal']).lower()
        else:
            assert context.info_in_mail['Pickup Information']['Terminal'] == 'Select Terminal' in Quote_details_while_creation['Terminal']

    else:
        assert context.info_in_mail['Delivery Information']['Market'] == Quote_details_while_creation['Market'], "Market in mail is different from Market in Quote"
        assert extract_postal_code(Quote_details_while_creation['origin_destination']) == extract_postal_code(
            context.info_in_mail['Pickup Information']['Address']), "Address is different from Address in Quote"
        if "N/A" in context.info_in_mail['Delivery Information']['Terminal']:
            assert 'select' in (Quote_details_while_creation['Terminal']).lower()
        else:
            assert context.info_in_mail['Delivery Information']['Terminal'] == 'Select Terminal' in Quote_details_while_creation['Terminal']

    assert context.info_in_mail['Delivery Information']['Size'] == Quote_details_while_creation['Size'], "Length in mail is different from Length in Quote"
    if Quote_details_while_creation['Weight_unit'] == "KG":
        assert float(context.info_in_mail['Delivery Information']['Weight']) == round(
            float(Quote_details_while_creation['Weight']) * 2.20462, 2) , "Weight is different from Weight in Quote"
    else:
        assert context.info_in_mail['Delivery Information']['Weight'] == Quote_details_while_creation['Weight'], "Weight is different from Weight in Quote"

    assert int(context.info_in_mail['Delivery Information']['Quantity']) == int(Quote_details_while_creation['Quantity']), "Quantity in mail is different from Quantity in Quote"

    assert float(context.info_in_mail['Rate Summary']['Linehaul'].replace("$","")) == round(float(updated_Your_charges['Linehaul($)']),2)
    assert context.info_in_mail['Rate Summary']['FSC%'] == updated_Your_charges['FSC (%)']

    Linehaul_FSC_total= float(updated_Your_charges['Linehaul($)']) * (100.00 + float(updated_Your_charges['FSC (%)'])) / 100
    assert float(context.info_in_mail['Rate Summary'][ 'Linehaul+FSC Total'].replace("$","")) == round(Linehaul_FSC_total,2)

    assert float(context.info_in_mail['Rate Summary']['Chassis/Day'].replace("$","")) == round(float(updated_Your_charges['Chassis ($/day)']),2)

    Applicable_Accessorials = {}
    for key in updated_Your_charges:
        if key not in ['Linehaul($)', 'FSC (%)', 'Chassis ($/day)', 'min_chassis_days']:
            if ":" in key:
                new_key = key.replace(":", "")
            else:
                new_key=key
            Applicable_Accessorials[new_key] = f'${float(updated_Your_charges[key]):.2f}'
    Applicable_Accessorials['Estimated Total'] = f'${float(updated_value_in_Estimated_total):.2f}'

    assert Applicable_Accessorials == context.info_in_mail['Applicable Accessorials']
