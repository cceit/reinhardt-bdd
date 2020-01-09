from setuptools import setup

setup(
    name="reinhardt-bdd",
    version="0.1",
    author_email='devhelp@cce.ou.edu',
    description='A collection of helpers for implementing BDD in Django',
    author='University of Oklahoma - College of Continuing Education - IT',
    license='BSD',
    install_requires=[
        "django>=2.0",
        "behave-django>=1.3.0",
        "PyVirtualDisplay>=0.2.5",
        "splinter>=0.13.0",
    ],
    classifiers=[
        'Development Status :: 0.1',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    url='https://github.com/cceit/reinhardt-bdd',
    packages=['reinhardt_bdd'],
    include_package_data=True,
    package_data={
        'reinhardt_bdd': [
            '*.py',
            'management/commands/*.py',
        ],
    },
    zip_safe=False,
)
