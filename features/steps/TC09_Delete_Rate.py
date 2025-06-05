import time

from behave import when,then

from pages.AddRate import AddRate
from pages.common_action import CommonActions


@when('User click the "Delete" button next to a rate')
def step_impl(context):
    context.delete_rate= AddRate(context)
    row_number= context.delete_rate.get_stored_row_number_of_rate_added()
    context.delete_rate.delete_added_rate_from_row(row_number)

@then('User should see a confirmation popup with message "Are you sure you want to delete this Rate?"')
def step_impl(context):

    message= "Are you sure you want to delete this Rate?"
    assert message in context.delete_rate.delete_rate_confirmation_popup_message(), f'{message} is not in confirmation popup message'


@then('User should see "Yes" and "No" buttons')
def step_impl(context):
    buttons_to_check= ["Yes","No"]
    button_in_popup= context.delete_rate.buttons_present_in_popup()
    for entry in buttons_to_check:
        assert entry in button_in_popup, f'{entry} button is not delete rate confirmation in pop-up'

@when('User confirm the rate deletion by clicking "Yes"')
def step_impl(context):
    context.delete_rate= AddRate(context)
    context.delete_rate.click_on_yes_to_delete_rate()

@then('User should see a message "Rate delete successfully"')
def step_impl(context):
    message= "Rate deleted successfully"
    assert message in context.delete_rate.popup_message_after_rate_deletion(), f'{message} message did not appear'

@then('the deleted rate should not appear in the quote')
def step_impl(context):

    context.delete_rate = AddRate(context)
    context.common_actions = CommonActions(context)
    context.common_actions.has_loader_disappeared()

    Added_Rates_data = context.delete_rate.get_stored_added_rates_data()

    if context.delete_rate.is_rates_table_present():
        Carrier_name_list_in_rates_table = context.delete_rate.get_carrier_names_from_rates_table()
        Linehauls_list_in_rates_table = context.delete_rate.get_linehauls_from_rates_table()
        FSC_list_in_rates_table = context.delete_rate.get_FSC_from_rates_table()
        Chassis_list_in_rates_table = context.delete_rate.get_Chassis_from_rates_table()

        for i in range(len(Carrier_name_list_in_rates_table)):
                if Carrier_name_list_in_rates_table[i] == Added_Rates_data["Carrier name"]:
                    try:
                        assert (
                                Linehauls_list_in_rates_table[i] != Added_Rates_data["LineHaul"]
                                or FSC_list_in_rates_table[i] != (Added_Rates_data["LineHaul"] * Added_Rates_data["FSC%"]) / 100
                                or Chassis_list_in_rates_table[i] != Added_Rates_data["Chasis_per_day"] * Added_Rates_data["min_chasis_day"] )

                        print(f'Added Rate summary for carrier: "{Added_Rates_data["Carrier name"]}" has been deleted from Rates table')

                    except AssertionError:
                        print(f"Added Rate summary for carrier: '{Added_Rates_data['Carrier name']}' is still present at index {i + 1}")

                else:
                    print(f'Added Rate summary for carrier: "{Added_Rates_data["Carrier name"]}" has been deleted from Rates table')

    else:
         print(f'Added Rate summary for carrier: "{Added_Rates_data["Carrier name"]}" has been deleted from Rates table')
    
    