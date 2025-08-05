import pytest

from pages.item_page import ItemPage
from pages.login_page import LoginPage


promo_links = [
    'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear2019',
    'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
]

@pytest.mark.parametrize('item', promo_links)
def test_add_to_cart(browser, item):
    link = item
    page = ItemPage(browser, link)
    page.open()
    page.add_to_cart(is_promo=True)
    page.should_be_success_message()
    page.should_be_message_cart_total()
    page.should_be_correct_item_added()


links = [
    'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0',
    'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer1',
    'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer2',
    'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer3',
    'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer4',
    'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer5',
    'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer6',
    pytest.param('https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail),
    'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer8',
    'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer9'
]

@pytest.mark.parametrize('link', links)
def test_guest_can_add_item_to_basket(browser, link):
    link = link
    page = ItemPage(browser, link)
    page.open()
    page.add_to_cart(is_promo=True)
    page.should_be_message_cart_total()
    page.should_be_correct_item_added()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_item_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ItemPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ItemPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_item_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ItemPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_success_message_disappear()

def test_guest_should_see_login_link_on_item_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ItemPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ItemPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
