from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

