import pytest
from page.common_page import CommonPage
from page.login_page import LoginPage
from page.home_page import HomePage
from page.pix_page import PixPage

@pytest.fixture
def page(page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://leogcarvalho.github.io/simulabank/login.html")
    return page

@pytest.fixture
def common_page(page):
        return CommonPage(page)

@pytest.fixture
def login_page(page):
        return LoginPage(page)

@pytest.fixture
def home_page(page):
        return HomePage(page)

@pytest.fixture
def pix_page(page):
        return PixPage(page)