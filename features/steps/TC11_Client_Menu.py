# import time
#
# from behave import given,when,then
# from pages.ClientPage import ClientPage
# from pages.common_action import CommonActions
#
#
# @when('User click on the "Clients" option present on the left menu')
# def step_impl(context):
#     context.client_page = ClientPage(context)
#     context.common_actions = CommonActions(context)
#
#     context.client_page.move_to_client_page()
#     context.common_actions.has_loader_disappeared()
#     context.client_page.is_clients_displayed_in_title()
#
# @then('User should see the following buttons')
# def step_impl(context):
#     Expected_button_list = ["Add Client", "Cancellation Request", "Approval Request", "Edit View", "Clear"]
#     Buttons_present_on_clients_page = context.client_page.list_of_buttons_on_client_page()
#
#     for expected_button in Expected_button_list:
#         if not any(expected_button in actual_button for actual_button in Buttons_present_on_clients_page):
#             assert False, f'"{expected_button}" button is not present on clients page'
#
#
# @then('User should see the following column names')
# def step_impl(context):
#     List_of_Expected_column_names = ['Client Name', 'User Name', 'DOT Number', 'Status', 'MC Number',
#                                        'Email Address', 'Client Type','City','State','Subscriber Type',
#                                         'Number of Sub-Users', 'Active Users','Claim Status','Phone Number']
#     List_of_columns_on_Client_Page = context.client_page.list_of_column_names()
#     for entry in List_of_Expected_column_names:
#         assert entry in List_of_columns_on_Client_Page, f'"{entry}" column is not present on Clients Page'
#
#
# @then('User should see a list of all registered users including customers and carriers')
# def step_impl(context):
#     context.client_page = ClientPage(context)
#     List_of_clients = context.client_page.list_of_clients_present()
#     assert len(List_of_clients) > 1, "List of clients has not appeared"
#
# @when('User selects a client from the list')
# def step_impl(context):
#     context.clients_page = ClientPage(context)
#     selected_client_detail= context.clients_page.open_and_get_random_client_profile()
#     context.client_type= selected_client_detail["client type"]
#     print(context.client_type)
#
# @when('User selects a client of type "{client_type}" from the list, User should see the following options')
# def step_impl(context):
#     client_type = context.client_type.lower()
#
#     expected_options_by_type = {
#         "carrier": ["General Information","Billing Information Details","Subscription Details",
#             "Business Address","Carrier Details","Primary Business Contact","Associated Users"],
#         "customer": ["General Information","Billing Information Details","Subscription Details","Associated Users"]
#                                 }
#
#     assert client_type in expected_options_by_type, f'Unsupported client type: "{client_type}"'
#
#     expected_options = expected_options_by_type[client_type]
#     visible_options = context.clients_page.get_displayed_options_for_client(context.client_type)
#
#     for option in expected_options:
#         assert option in visible_options, f'"{option}" is not visible for {context.client_type} client type'


import time
from behave import given, when, then
from pages.ClientPage import ClientPage
from pages.common_action import CommonActions


@when('User click on the "Clients" option present on the left menu')
def step_impl(context):
    context.client_page = ClientPage(context)
    context.common_actions = CommonActions(context)

    context.client_page.move_to_client_page()
    context.common_actions.has_loader_disappeared()
    context.client_page.is_clients_displayed_in_title()


@then('User should see the following buttons')
def step_impl(context):
    expected_button_list = ["Add Client", "Cancellation Request", "Approval Request", "Edit View", "Clear"]
    buttons_present_on_clients_page = context.client_page.list_of_buttons_on_client_page()

    missing_buttons = []
    for expected_button in expected_button_list:
        if not any(expected_button in actual_button for actual_button in buttons_present_on_clients_page):
            missing_buttons.append(expected_button)

    assert not missing_buttons, f"Missing buttons: {', '.join(missing_buttons)}"


@then('User should see the following column names')
def step_impl(context):
    expected_column_names = ['Client Name', 'User Name', 'DOT Number', 'Status', 'MC Number',
                             'Email Address', 'Client Type', 'City', 'State', 'Subscriber Type',
                             'Number of Sub-Users', 'Active Users', 'Claim Status', 'Phone Number']
    columns_on_client_page = context.client_page.list_of_column_names()

    missing_columns = [entry for entry in expected_column_names if entry not in columns_on_client_page]
    assert not missing_columns, f"Missing columns: {', '.join(missing_columns)}"


@then('User should see a list of all registered users including customers and carriers')
def step_impl(context):
    context.client_page = ClientPage(context)
    list_of_clients = context.client_page.list_of_clients_present()
    assert len(list_of_clients) > 0, "No clients are listed."


@when('User selects a client from the list')
def step_impl(context):
    # Open a random client profile and get its details (client type, name, etc.)
    context.clients_page = ClientPage(context)
    selected_client_detail = context.clients_page.open_and_get_random_client_profile()
    context.client_type = selected_client_detail["client type"].lower()  # Capture the client type dynamically

    print(f"Selected client type: {context.client_type}")


@then('User should see appropriate options based on the client type')
def step_impl(context):
    expected_options_by_type = {
        "carrier": ['GENERAL INFORMATION', 'BILLING INFORMATION DETAILS', 'SUBSCRIPTION DETAILS', 'BUSINESS ADDRESS', 'CARRIER DETAILS', 'PRIMARY BUSINESS CONTACT', 'ASSOCIATED USERS'],
        "customer": ['GENERAL INFORMATION', 'BILLING INFORMATION DETAILS', 'SUBSCRIPTION DETAILS', 'ASSOCIATED USERS']
    }

    assert context.client_type in expected_options_by_type, f'Unsupported client type: "{context.client_type}"'
    expected_options = expected_options_by_type[context.client_type]
    visible_options = context.clients_page.get_displayed_options_for_client()
    for option in expected_options:
        assert option in visible_options, f'"{option}" is not visible for {context.client_type} client type'

@then("User should see Support options")
def step_impl(context):
    expected_support_options =["Send the Username to the user","Send the Password Reset LINK to the user"]
    visible_options = context.clients_page.get_support_options_for_client()
    for option in expected_support_options:
        assert option in visible_options, f'"{option}" support option is not visible for {context.client_type} client type'
        

@when('User update any available section')
def step_impl(context):
    pass

@when('User save the changes')
def step_impl(context):
    pass


@then('the updated information should be visible to the client in their "My Profile" section')
def step_impl(context):
    pass
