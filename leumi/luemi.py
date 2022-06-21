from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import


import os
import leumi.constants as const

class Luemi(webdriver.Chrome):

    # Locators
    HURT_DATE = (By.ID, "ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_DynDatePicker_PguiaDate_Date")
    BRTH_DATE = (By.ID, "ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_DynDatePicker_BirthDate_Date")
    CONTINUE_BTN = (By.ID, "ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_StartNavigationTemplateContainerID_StartNextButton")
    CALC_BTN = (By.ID, "ctl00_PlaceHolderMain_ToolBarControl_Repeater1_ctl01_a")
    CALC_BTN = (By.ID, "ctl00_PlaceHolderMain_ToolBarControl_Repeater1_ctl01_a")
    WORK_ACDNT_BTN = (By.LINK_TEXT, "נפגעי עבודה")

    def __init__(self, driver_path=r"/usr/local/bin", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Luemi, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def land_calc_first_page(self):
        self.get(const.CACL_URL)

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self, 10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def do_click(self, by_locator):
        WebDriverWait(self, 20).until(expected_conditions.visibility_of_element_located(by_locator)).click()

    def get_home_page_title(self):
        self.land_first_page()
        return self.title

    def click_calculator_btn(self):
        self.do_click(self.CALC_BTN)

    def click_work_acdnt_btn(self):
        # self.do_click(self.CALC_BTN)
        hrt_btn = self.find_element(By.LINK_TEXT, "נפגעי עבודה")
        self.implicitly_wait(15)
        hrt_btn.click()

    def click_calc_acdnt(self):
        self.implicitly_wait(10)
        link = self.find_element(By.LINK_TEXT, "חישוב גמלת נכות מעבודה")
        WebDriverWait(self, 10).until(expected_conditions.visibility_of_element_located(link))
        link.click()

    def drop_down_percent(self):
        percent = self.find_element(By.ID, "ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_Percent")
        percent.send_keys("50")
        drop_down_element = self.find_element(By.ID, "ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_ddl_Type")
        drp = Select(drop_down_element)
        drp.select_by_value("1")

    def click_save_btn(self):
        self.find_element(By.CSS_SELECTOR, "span[שמירת ליקוי]")

    def fill_dates(self, hurt_date, brth_date):
        self.do_send_keys(self.HURT_DATE, hurt_date)
        self.do_send_keys(self.BRTH_DATE, brth_date)
        self.do_click(self.CONTINUE_BTN)