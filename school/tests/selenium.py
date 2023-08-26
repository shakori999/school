import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options 


@pytest.fixture(scope="module")
def firefox_broswer_instance(request):
    '''
    provide a selenium webdirve instance
    '''

    options = Options()
    options.headless = False
    
    browser = webdriver.Firefox()
    yield browser
    browser.close()

