# reinhardt-bdd
BDD testing tools for Django 2.x

# Installation
Add 'behave_django' and 'reinhardt_bdd' to your INSTALLED_APPS setting.

    INSTALLED_APPS = [
        ...
        'behave_django',
        'reinhardt_bdd',
    ]

# Fixing flush command for Wagtail

There is a bug in wagtail that [breaks Django's flush command](https://github.com/wagtail/wagtail/issues/1824). Flush is usually run between each test so this bug breaks most test setups. To fix this add the following to your settings.txt. This will add allow_cascade option to the flush command in django.

    FIX_WAGTAIL_FLUSH = True
    
# Running tests

You can run all tests by using the behave command.

    python manage.py behave
    
You can run a single app's tests by specifying the app's features folder.

    python manage.py behave organization/features
    
You can also run a particular feature file by specifying it.

    python manage.py behave organization/features/organization.feature
