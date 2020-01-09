import requests
from behave import when
from django.urls import NoReverseMatch, reverse


@when("I visit (.*)")
def visit_page(context, url_name):
    """Allows you to visit a page in the system. I visit (.*)


    :param object  context: behave's global object
    :param string url_name: url name to visit


    Usage:
        .. code-block:: python
            :linenos:

            Scenario Outline: Manage applications
                Given I am logged in as manager
                When I visit manage_application

    """
    b = context.browser

    try:
        url = context.get_url(reverse(url_name))
    except NoReverseMatch:
        try:
            url = context.get_url(reverse(url_name, kwargs={'pk': context.test_obj.pk}))
        except AttributeError:
            raise Exception("%s not found. Check the url config." % url_name)

    try:
        context.result = requests.get(url, cookies=b.cookies.all())
    except KeyError:
        pass
    b.visit(url)
