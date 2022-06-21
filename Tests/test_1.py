from leumi.constants import HOME_PAGE_TITLE, HURT_DATE, BRTH_DATE, WRONG_HURT_DATE, WRONG_BRTH_DATE
from leumi.luemi import Luemi

import pytest

#Ui Test Case
def test_m1():
    with Luemi() as bot:
        bot.land_first_page()
        bot.get_home_page_title()
        assert bot.title == HOME_PAGE_TITLE

#Negative Test Case
def test_m2():
    with Luemi() as bot:
        bot.land_calc_first_page()
        bot.fill_dates(WRONG_HURT_DATE, WRONG_BRTH_DATE)

# Positive Test Case
def test_m3():
    with Luemi() as bot:
        bot.land_calc_first_page()
        bot.fill_dates(HURT_DATE, BRTH_DATE)
