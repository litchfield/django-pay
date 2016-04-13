from setuptools import setup, find_packages
import os

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

VERSION = '0.1'


setup(
    name='django-pay',
    version=VERSION,
    description="Braintree/Stripe for Django",
    long_description="PCI DSS compliant integration of modern payment gateways for Django including subscriptions, recurring payments, refunds and more",
    keywords="braintree, stripe, django, payment gateway, subscriptions, recurring payments",
    author="Simon Litchfield",
    author_email="simon@litchfield.digital",
    url="http://github.com/litchfield/django-pay",
    license="MIT License",
    platforms=["any"],
    packages=['pay'],
    #data_files=[(template_dir, templates)],
    install_requires=[
        'django>=1.7',
        'braintree>=3.25.0',
        'stripe>=1.32.2',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
