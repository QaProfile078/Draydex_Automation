from behave import given,when,then

@when(u'User click on the "Block/Ban Carrier" button')
def step_impl(context):
    pass


@then(u'a warning popup should be displayed with message')
def step_impl(context):
    pass


@then(u'the popup should display "Submit" and "Cancel" buttons')
def step_impl(context):
    pass


@when(u'User click on the "Submit" button')
def step_impl(context):
    pass


@then(u'the carrier should be blocked')
def step_impl(context):
    pass


@then(u'a message "Carrier Blocked. Carrier is now unable to view/quote your rate request." should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a message "Carrier Blocked. Carrier is now unable to view/quote your rate request." should be displayed')


@when(u'User block a carrier from the details page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User block a carrier from the details page')


@then(u'the blocked carrier should have a PINK background on the "Carrier Listing Page"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the blocked carrier should have a PINK background on the "Carrier Listing Page"')


@given(u'a carrier is already blocked and has a PINK background')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a carrier is already blocked and has a PINK background')


@when(u'User click on that blocked carrier')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User click on that blocked carrier')


@when(u'User click on the "Unblock/UnBan Carrier" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User click on the "Unblock/UnBan Carrier" button')


@then(u'a confirmation popup should appear with the message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a confirmation popup should appear with the message')


@then(u'the carrier should be unblocked')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the carrier should be unblocked')


@then(u'a message "Carrier unblock successfully." should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a message "Carrier unblock successfully." should be displayed')
