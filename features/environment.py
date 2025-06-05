from drivers.webdriver import create_webdriver

def before_all(context):
    context.driver = create_webdriver()
    context.email_id = context.config.userdata.get("EMAIL_ID")
    context.password = context.config.userdata.get("PASSWORD")
    context.quote_id = context.config.userdata.get("QUOTE_ID")
    context.server = context.config.userdata.get("SERVER")


def after_all(context):
    context.driver.quit()



