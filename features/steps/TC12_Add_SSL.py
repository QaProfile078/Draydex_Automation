import time

from behave import given,when,then

from pages.ManageSSL import ManageSSL
from pages.common_action import CommonActions


@then('User should see a "Settings" tab and move to it')
def step_impl(context):
    context.manage_ssl=ManageSSL(context)
    context.manage_ssl.check_and_move_to_manage_settings()

@then('the user should see the following options in settings tab')
def step_impl(context):
    context.common_actions = CommonActions(context)
    assert context.common_actions.is_manage_ssl_present_in_settings()
    assert context.common_actions.is_fallback_table_present_in_settings()
    assert context.common_actions.is_manage_market_present_in_settings()
    assert context.common_actions.is_manage_terminal_present_in_settings()


@when('User click the "Manage SSL" button')
def step_impl(context):
    context.manage_ssl.click_on_manage_ssl()

@then('User should be taken to the SSL management page')
def step_impl(context):
    context.common_actions.has_loader_disappeared()
    assert context.manage_ssl.is_user_on_ssl_management_page()

@given('User is on the SSL management page')
def step_impl(context):
    context.manage_ssl=ManageSSL(context)
    context.manage_ssl.open_SSL_management_page()

@when('User click the "Add SSL" button')
def step_impl(context):
    context.manage_ssl=ManageSSL(context)
    context.manage_ssl.click_add_ssl()

@then('User should see a popup with the following fields')
def step_impl(context):
    assert context.manage_ssl.check_ssl_name_field() , "SSL Name field is not displayed"
    assert context.manage_ssl.check_scac_code_field() , "SCAC Code field is not displayed"
    assert context.manage_ssl.check_abbreviated_name_field() , "Abbreviated Name field is not displayed"

    print("all fileds are checked and present on the page")

@then('there should be a "Save" and "Cancel" button')
def step_impl(context):
    context.manage_ssl=ManageSSL(context)
    assert context.manage_ssl.check_cancel_button_field, "Cancel button is not displayed"
    assert context.manage_ssl.check_save_button_field, "Save button is not displayed"

@when('User leave one or more fields empty')
def step_impl(context):
    pass

@when('click the "Save" button')
def step_impl(context):
    context.manage_ssl=ManageSSL(context)
    context.manage_ssl.click_on_save_button()

@then('User should see a error message with "is required" in it')
def step_impl(context):
    error_messages=context.manage_ssl.error_message_list_while_creating_ssl()
    print(error_messages)
    for entry in error_messages:
        assert "is required" in entry

@when('User fill in all fields (SSL Name, SCAC Code, Abbreviated Name)')
def step_impl(context):
    context.manage_ssl=ManageSSL(context)
    context.ssl_name=context.manage_ssl.fill_ssl_name_field()
    context.scac_code=context.manage_ssl.fill_scac_code_field()
    context.abbreviated_name=context.manage_ssl.fill_abbreviated_name_field()
    context.SSL_data_while_creation={"SSL name":context.ssl_name,"SCAC Code": context.scac_code,"Abbreviated Name": context.abbreviated_name}

    print(context.SSL_data_while_creation)

@then('User see a popup with message "SSL created"')
def step_impl(context):
    assert context.manage_ssl.verify_SSl_created_message()

@then('the new SSL should be added to the list of active SSLs')
def step_impl(context):
    Data_of_all_active_ssl=context.manage_ssl.SSL_data_in_active_SSl_table()
    assert context.SSL_data_while_creation in Data_of_all_active_ssl, "Newly Created SSL is not in Active SSl list"

@when('User click the "Cancel" button')
def step_impl(context):
    context.manage_ssl = ManageSSL(context)
    context.manage_ssl.click_on_cancel_button()
