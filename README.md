# GuildEd_DogShelter
Guild Home Exercise

This application was coded in Python 3.8.2.
Automated unit tests require pytest to be installed:
==> pip3 install pytest

this application can be cloned by running the following comand:

==> git clone https://github.com/Steve20181010/GuildEd_DogShelter.git

To execute application "calc_dogdood_supply.py":

==> python calc_dogdood_supply.py

To execute unit tests (from cloned directory):
==> pytest
 
About the app:
The following application parameters have been configured:

    PRM_SMLL_DOGS_LBS = 10
    PRM_MED_DOGS_LBS = 20
    PRM_LRG_DOGS_LBS = 30
    PRM_AMT_MULTIPLIER = .2
    ALLOWED_DOGS = 30

By running the app, user will be prompted to required data to calculate dog food order amount.

Unit Tests are in two categories:
1. Data Entry Validation (frontend)
2. Calculate dogfood to order (backend testing)

Data entry validation tests:
    # Test Max Dogs equal max 30
    # Test Max Dogs greater than 30
    # Test Dog numbers cannot be negative numbers
    # Test Max Dogs equal 0
    # Test Max Dogs way large
    # Test Invalid Smll Dogs entry (entered string)
    # Test Invalid Med Dogs entry (entered string)
    # Test Invalid Big Dogs entry (entered string)

Calculate dog food order amount tests:
    # Test order quantity equal 363.6
    # Test order quantity equal 1059.6
    # Test leftover quantity is negative and calc'ed equal to -20.4
    # Test order quantity equal 630.0
