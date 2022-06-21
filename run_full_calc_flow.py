from leumi.luemi import Luemi

with Luemi() as bot:
    bot.land_first_page()
    bot.click_calculator_btn()
    bot.click_work_acdnt_btn()
    bot.click_calc_acdnt()
    bot.fill_dates()
    bot.click_continue_btn()
    bot.drop_down_percent()