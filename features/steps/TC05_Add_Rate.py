import time

from behave import given,when,then

from pages.Rate_to_Client import RateToClient
from pages.common_action import CommonActions
from pages.AddRate import AddRate


# Added_Rates_data={"Carrier name": "","LineHaul":0,"FSC%":0,"Chasis_per_day":0,"min_chasis_day":0}
Added_Rates_data={}


def search_and_click_quote(context, Quote_ID):

    context.common_actions.goto_quote_placeholder().click()
    for digit in Quote_ID:
        context.common_actions.goto_quote_placeholder().send_keys(digit)
        context.common_actions.has_loader_disappeared()

    if context.common_actions.is_quote_present_in_table(Quote_ID) == True:
        context.common_actions.click_on_quote_id(Quote_ID)
        return True  # Rated Quote found and clicked
    else:
        return False  # Quote not found In the table

#----------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- Of No Use anymore-----------------------------------------------------------------------#

# @when('User open the "ADD Rate" popup')
# def step_impl(context):
#     context.common_actions= CommonActions(context)
#     context.rate_to_client= RateToClient(context)
#     context.add_rate= AddRate(context)
#
#     # Keep trying until quote is found
#     while True:
#         global Quote_ID
#         #Quote_ID = context.common_actions.get_random_quote_to_search()      # Get a random Quote_ID
#
#         if context.quote_id is not None:
#             Quote_ID = context.quote_id
#         else:
#             Quote_ID = context.common_actions.get_stored_quote()
#
#         # Quote_ID = context.common_actions.get_stored_quote()                 # Get Quote just created(used while parallel execution)
#         # Quote_ID="7335"                                                    # hardcoded Quote id (used for explicit action_
#         if search_and_click_quote(context, Quote_ID):
#             # Attempt to search and click a rated quote
#             break                                                            # Exit the loop when rated quote is found and clicked
#         else:                                                                # If rated quote is not found, clear and retry
#             context.common_actions.click_on_clear_button()
#             context.common_actions.has_loader_disappeared()
#
#     context.common_actions.has_loader_disappeared()
#     context.add_rate.click_on_Add_Rate()
#     context.common_actions.has_loader_disappeared()

#---------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------#

@when('User click on "Add Rate"')
def step_impl(context):
    context.common_actions= CommonActions(context)
    context.add_rate = AddRate(context)

    context.common_actions.has_loader_disappeared()
    context.add_rate.click_on_Add_Rate()
    context.common_actions.has_loader_disappeared()

@then('User should see the "Manually Add Carrier Spot Rate" popup with mandatory fields')
def step_impl(context):
    Mandatory_fields_on_popup=["Carrier Name / DOT#","Linehaul ($)","FSC (%)", "Chassis ($/day)","Min. Chassis Day","Add Accessorials","Carrier has Capacity?","Earliest Capacity?","Note","Submit","Cancel"]
    assert context.add_rate.Is_Manually_Add_Carrier_Spot_Rate_visible()

    Fields_present_on_popup= context.add_rate.list_of_fields_present_on_popup()
    for entry in Mandatory_fields_on_popup:
        assert entry in Fields_present_on_popup, f'{entry} is not present in the popup'

@when('user clicks on submit button without filling the required fields')
def step_impl(context):
    context.add_rate=AddRate(context)
    context.add_rate.click_on_submit_button()

@then('User should see errors under the Required fields')
def step_impl(context):
    assert context.add_rate.is_required_field_visible()


@when('User fill all the required field and click on submit')
def step_impl(context):
    context.add_rate=AddRate(context)
    context.common_actions= CommonActions(context)

    Added_Rates_data["Carrier name"]=context.add_rate.fill_Carrier_Name_field()

    context.common_actions.has_loader_disappeared()

    Added_Rates_data["LineHaul"]=context.add_rate.fill_linehauls_field()
    Added_Rates_data["FSC%"]=context.add_rate.fill_FSC_percent_field()
    Added_Rates_data["Chasis_per_day"]=context.add_rate.fill_Chassis_per_day_field()
    Added_Rates_data["min_chasis_day"]=context.add_rate.select_min_chassis_day()

    if context.add_rate.accessorials_are_present():
        accessorial_names= context.add_rate.get_accessorial_names()
        accessorial_values= context.add_rate.get_accessorial_values()
        for i in range(len(accessorial_names)):
            Added_Rates_data[accessorial_names[i]]=accessorial_values[i]


    context.add_rate.store_added_rates_data(Added_Rates_data)
    context.add_rate.get_stored_added_rates_data()

    context.add_rate.select_carrier_has_capacity()
    context.add_rate.click_on_submit_button()

@then('the user will see a message with "rate added successfully" in it')
def step_impl(context):
    assert "rate added successfully" in context.add_rate.verify_successful_rate_added_message(), "error in adding spot rate"


@then('Verify the Added rate is visible in Rate Quote Table list')
def step_impl(context):
    context.add_rate=AddRate(context)
    context.common_actions= CommonActions(context)
    context.common_actions.has_loader_disappeared()

    context.add_rate.get_stored_added_rates_data()

    assert context.add_rate.is_rates_table_present(), "Rates table is not present"

    Carriers_list_in_rates_table= context.add_rate.get_carrier_names_from_rates_table()
    Linehauls_list_in_rates_table = context.add_rate.get_linehauls_from_rates_table()
    FSC_list_in_rates_table = context.add_rate.get_FSC_from_rates_table()
    Chassis_list_in_rates_table = context.add_rate.get_Chassis_from_rates_table()


    assert Added_Rates_data["Carrier name"] in Carriers_list_in_rates_table, f'Added rate is with Carrier Name: {Added_Rates_data["Carrier name"]}, is not present in Rates Table'

    for i in range (len(Carriers_list_in_rates_table)):
        if Carriers_list_in_rates_table[i] == Added_Rates_data["Carrier name"]:
            try:
                assert Linehauls_list_in_rates_table[i] == Added_Rates_data["LineHaul"]
                assert FSC_list_in_rates_table[i] == (Added_Rates_data["LineHaul"] * Added_Rates_data["FSC%"]) / 100
                assert Chassis_list_in_rates_table[i] == Added_Rates_data["Chasis_per_day"] * Added_Rates_data["min_chasis_day"]
                print(f"Rate summary for carrier: {Added_Rates_data['Carrier name']} is present in Rate table at index {i+1}")

                context.add_rate.store_row_number_of_rate_added(i)

                break

            except AssertionError:
                print(f"Rate summary carrier: {Added_Rates_data['Carrier name']} is not same at index {i+1}, retrying...")



@then("User should see the following columns and buttons populated")
def step_impl(context):
    Expected_button_and_columns= ["Date","Provided By","Carrier","Rate Summary","Accessorials","Estimated Total","Capacity?","Notes","SELECT","DELETE"]
    Actual_columns_and_buttons_populated= context.add_rate.get_populated_columns_and_buttons()

    for entry in Expected_button_and_columns:
        assert entry in Actual_columns_and_buttons_populated, f'{entry} is not not present on rate quotes table'