import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

class AvitoParse:
    def __init__(self, url: str, items: list = [], count_page: int = -1):
        self.url = url
        self.items = items
        self.count_page = count_page
        # count = -1 просматривает все страницы

    # методы приватны и не могут вызываться из вне
    def __setup(self):
        self.driver = uc.Chrome()

    # получает url
    def __get_url(self):
        self.driver.get(self.url)

    # нужен для парсинга всех страниц сайт, нажимает на нужную страницу(следующая)
    def __paginator_all(self):
        while self.driver.find_elements(By.CSS_SELECTOR, "[data-marker = 'pagination-button/nextPage']"):
            self.__parse_page()
            self.driver.find_element(By.CSS_SELECTOR, "[data-marker = 'pagination-button/nextPage']").click()
        self.__parse_page()

    # нужен для парсинга нескольких страниц сайта, нажимает на нужную страницу(следующая)
    def __paginator_any(self):
        while self.driver.find_elements(By.CSS_SELECTOR,
                                        "[data-marker = 'pagination-button/nextPage']") and self.count > 0:
            self.__parse_page()
            self.driver.find_element(By.CSS_SELECTOR, "[data-marker = 'pagination-button/nextPage']").click()
            self.count -= 1

    # парсит главную страницу
    def __parse_page(self):
        pages = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for page in pages:
            name = page.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            price = page.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute("content")
            specific_data = page.find_element(By.CSS_SELECTOR, "[data-marker='item-specific-params']").text
            address = page.find_element(By.CSS_SELECTOR, "[data-marker='item-address']").find_element(By.TAG_NAME,
                                                                                                      "span").text
            url_adress = page.find_element(By.CSS_SELECTOR, "[itemprop='url']").get_attribute("href")
            print(name)
            print(price)
            print(specific_data)
            print(address)
            print(url_adress)
            print()
            print()

    # самый главный метод из парсинга
    def parse(self):
        self.__setup()
        self.__get_url()
        if self.count_page == -1:
            self.__paginator_all()
        else:
            self.__paginator_any()

AvitoParse(url="https://www.avito.ru/rostov-na-donu/kvartiry/sdam/na_dlitelnyy_srok/2-komnatnye-ASgBAQICAkSSA8gQ8AeQUgFAzAgUkFk?cd=1&district=349&s=104").parse()

