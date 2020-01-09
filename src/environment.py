import os

from behave_django.testcase import BehaviorDrivenTestCase
from django.conf import settings
from django.core.management import call_command
from django.test import TransactionTestCase
from pyvirtualdisplay import Display
from splinter import Browser
from wagtail.core.models import Site, Page


def setup_test_environment(context, scenario, visible=0, use_xvfb=True):
    """
    Method used to setup the BDD test environment
     - Sets up virtual display
     - Sets up webdriver instance
     - Sets window size
     - Flushes cookies
     - Enables debug (Allows for more verbose error screens)
     - Sets scenario
     - Truncates database tables

    Options:
     - visible (0 or 1) - Toggle Xephyr to view the Xvfb instance for limited debugging. 0: Off, 1: On.
     - use_xvfb (True/False) - Toggle Xvfb to run the tests on your desktop for in-depth debugging.
    """

    driver = os.environ.get('WEBDRIVER_TYPE', None)
    if use_xvfb:
        context.display = Display(visible=visible, size=(1920, 1080))
        context.display.start()

    context.browser = Browser('chrome')

    context.browser.driver.set_window_size(1920, 1080)
    # Flushes all cookies.
    context.browser.cookies.delete()
    # Re-enables yellow screens on failure. (Normally disabled by
    # LiveServerTestCase)
    settings.DEBUG = True


def save_failure_screenshot(context, step):
    if step.status == "failed":
        file_path = '%s_%s_error.png' % (context.scenario, step.name)
        context.browser.driver.save_screenshot(file_path)


def flush_context(context, scenario):
    context.browser.quit()  # Close the browser to get a fresh one for each test
    context.browser = None  # Flush browser from context
    if hasattr(context, 'display'):
        context.display.stop()  # Closes the virtual display (if it exists)


def load_wagtail_base_data():
    if Site.objects.filter(is_default_site=True).count() < 1:
        root = Page.objects.create(
            title='Root',
            path='0001',
            depth=1,
        )

        root_page = root.add_child(instance=Page(
            title='Home',
            path='00010001',
            depth=2,
        ))

        Site.objects.create(
            hostname='localhost',
            port=80,
            is_default_site=True,
            root_page=root_page,
        )
