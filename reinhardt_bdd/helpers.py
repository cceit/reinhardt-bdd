
def fill_and_submit_form(browser, fields, submit_button_name='submit'):
    """
    Fills a dictionary of form fields on a page and clicks the submit button

    :param browser: browser object
    :param fields: iterable of fields
    :param string submit_button_name: optional button name field in case
     there's multiple buttons on the page
    """
    fill_form(browser, fields)
    click_element_by_name(browser, submit_button_name)


def fill_form(browser, fields):
    """
    Fills a dictionary of form fields on a page

    :param browser: browser object
    :param fields: iterable of fields
    """
    for field in fields:
        function = field['function']
        name = field['name']
        if 'value' in field:
            value = field['value']
            getattr(browser, function)(name, value)
        else:
            getattr(browser, function)(name)


def click_element_by_name(browser, name, index=0):
    """
    Clicks an element in the DOM by the element name

    :param browser: browser object
    :param string name: name of element
    :param integer index: index of the element in the DOM
    """
    browser.find_by_name(name)[index].click()
