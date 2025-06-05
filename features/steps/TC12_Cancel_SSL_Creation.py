from behave import given,when,then
from pages.ManageSSL import ManageSSL

@then('the SSL should not be created and added to the list of active SSLs')
def step_impl(context):
    Data_of_all_active_ssl=context.manage_ssl.SSL_data_in_active_SSl_table()
    assert context.SSL_data_while_creation not in Data_of_all_active_ssl, "Newly Created SSL is in Active SSl list"

@when('click the "Cancel" button')
def step_impl(context):
    context.manage_ssl = ManageSSL(context)
    context.manage_ssl.click_on_cancel_button()