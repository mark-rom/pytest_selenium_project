from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators(BasePageLocators):
    ...

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,'#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ItemPageLocators():
    ADD_ITEM_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    '#messages > div:nth-child(1) > div > strong'
    ITEM_NAME = (By.CSS_SELECTOR, 'div > h1')
    
    CART_SUM = (By.CSS_SELECTOR, 'div.alertinner p strong')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    