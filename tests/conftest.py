import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chr_opt
from selenium.webdriver.firefox.options import Options as ff_opt


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
        help="Choose browser: chrome or firefox. Default chrome"
    )
    parser.addoption(
        '--language', action='store', default='en',
        help='Choose language, default en: i.g. --language=ru'
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    if browser_name == 'chrome':
        chr_options = chr_opt()
        chr_options.add_experimental_option(
            'prefs', {'intl.accept_languages': language}
        )
        browser = webdriver.Chrome(options=chr_options)

    if browser_name == 'firefox':
        ff_options = ff_opt()
        ff_options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=ff_options)

    browser.implicitly_wait(10)
    yield browser
    browser.quit()
