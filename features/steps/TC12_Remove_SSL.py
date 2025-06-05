import time

from behave import when,then
from pages.ManageSSL import ManageSSL
from pages.common_action import CommonActions

selected_SSL_Data= None

@then('User verifies different elements present on this page')
def step_impl(context):
    context.manage_ssl=ManageSSL(context)
    Button_blocks=context.manage_ssl.get_list_of_button_blocks()

    assert 'Active SSL' in Button_blocks , 'Active SSL Button is not Present on Manage SSL page'
    assert 'InActive SSL' in Button_blocks, 'InActive SSL Button is not Present on Manage SSL page'
    assert 'Add SSL' in Button_blocks,   'Add SSL Button is not Present on Manage SSL page'
    assert 'Remove SSL' in Button_blocks, 'Remove SSL Button is not Present on Manage SSL page'
    assert 'Upload CSV' in Button_blocks, 'Upload SSL Button is not Present on Manage SSL page'
    assert 'Clear' in Button_blocks, 'Clear Button is not Present on Manage SSL page'

    assert context.manage_ssl.Is_RemoveSSL_button_disabled() , "Remove SSL button is enabled"

@when('User select first SSL from active SSL tabel')
def step_impl(context):
    context.manage_ssl=ManageSSL(context)
    global selected_SSL_Data
    selected_SSL_Data=context.manage_ssl.select_first_ssl_to_remove()
    print(selected_SSL_Data)

@then('User should see Remove SSl button is enabled')
def step_impl(context):
    assert context.manage_ssl.Is_RemoveSSL_button_disabled() == False , "Remove SSL Button is not enabled"

@when('User clicks "Remove SSl" button')
def step_impl(context):
    context.manage_ssl.click_on_Remove_SSL()
    # context.common_actions= CommonActions(context)
    # context.common_actions.has_loader_disappeared()

@then('User should see a SSL Removal confirmation Popup with close and confirm buttons')
def step_impl(context):
    assert context.manage_ssl.has_confirm_SSL_Removal_popup_aapeared(), "SSL Removal confirmation popup did not appear as expected."
    assert context.manage_ssl.Is_close_and_confirm_button_present()

@when('User click on "Cancel" to cancel SSL Removal')
def step_impl(context):
    context.manage_ssl.click_on_cancel_confirmation()

@then('User should see selected SSL still in list of active SSLs')
def step_impl(context):
    Data_of_all_active_ssl = context.manage_ssl.SSL_data_in_active_SSl_table()
    print(selected_SSL_Data)
    assert selected_SSL_Data in Data_of_all_active_ssl

@then('User will click on clear to reset table')
def step_impl(context):
    context.manage_ssl.click_on_clear_button()
    context.common_actions= CommonActions(context)
    context.common_actions.has_loader_disappeared()

@when('User click on "Confirm" to confirm SSL Removal')
def step_impl(context):
    context.manage_ssl.click_on_confirm_confirmation()

@then('User should see "SSL(s) move to inactive" popup')
def step_impl(context):
    context.manage_ssl.verify_ssl_moved_to_inactive_popup()

@then('User should see selected SSL not in list of active SSLs')
def step_impl(context):
    Data_of_all_active_ssl = context.manage_ssl.SSL_data_in_active_SSl_table()
    print(selected_SSL_Data)
    assert selected_SSL_Data not in Data_of_all_active_ssl , "Removed SSl is still in Active SSL Table"

@when('User click on InActive SSL button')
def step_impl(context):
    context.manage_ssl=ManageSSL(context)
    context.manage_ssl.click_on_InActive_SSl()
    context.common_actions = CommonActions(context)
    context.common_actions.has_loader_disappeared()

@then('the SSL removed should be added to the InActive SSL table')
def step_impl(context):
    Data_of_all_InActive_ssl = context.manage_ssl.SSL_data_in_InActive_SSl_table()
    assert selected_SSL_Data in Data_of_all_InActive_ssl , "Removed SSL not Present in InActive SSL Table"