from behave import given, then, when


@given('Open Amazon page')
def open_amazon_page(context):
    context.app.main_page.open_main_page()


@when('Search for "{item}" in the "{department}" department')
def search_in_department(context, item, department):
    context.app.search_bar.select_department(department)
    context.app.search_bar.search_for_product(item)


@then('Verify "{item}" is shown in the result page')
def verify_result(context, item):
    context.app.result_page.verify_result(item)


@given('Open "{item}" product page')
def open_product_page(context, item):
    context.app.product_page.open_product_page(item)


@when('Mouse cursor hovers over New Arrivals menu')
def hover_over_menu(context):
    context.app.product_page.hover_over_new_arrivals()


@then('Verify deals are shown')
def verify_deals(context):
    context.app.product_page.verify_deals()
