from time import sleep

from .base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):
    def add_to_cart(self, is_promo=False):
        add_item_button = self.browser.find_element(*ItemPageLocators.ADD_ITEM_BUTTON)
        add_item_button.click()
        if is_promo:
            self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        assert self.is_element_present(*ItemPageLocators.SUCCESS_MESSAGE), 'Alert about added item is not present after adding item'

    def should_be_message_cart_total(self):
        assert self.is_element_present(*ItemPageLocators.CART_SUM), "There's no "
        

    def should_be_correct_item_added(self):
        item_name = self.browser.find_element(*ItemPageLocators.ITEM_NAME).text
        added_item_alert = self.browser.find_element(*ItemPageLocators.SUCCESS_MESSAGE).text
        assert item_name == added_item_alert, f"Added item's name '{item_name}' is not equal the name from the addition alert: '{added_item_alert}'"

    def should_be_correct_cart_price(self):
        item_price = self.browser.find_element(*ItemPageLocators.ITEM_PRICE).text
        cart_price = self.browser.find_element(*ItemPageLocators.CART_SUM).text
        assert item_price == cart_price, "Total cart price didn't change"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ItemPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ItemPageLocators.SUCCESS_MESSAGE), "Success message did not disappear"
