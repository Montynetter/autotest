import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Chrome driver path
chrome_driver_path = 'E:\\chromedriver.exe'


@pytest.fixture
def driver():
    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')

    # Create Chrome driver
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    yield driver

    # Quit the driver
    driver.quit()


@pytest.fixture
def logger():
    return logging.getLogger('test_logger')


def test_smartphone_search(driver, logger):
    logger.info('Starting the test')

    # Open Yandex Market website
    driver.get('https://market.yandex.ru')
    logger.info('Opened Yandex Market website')

    # Click on "Catalog" link
    catalog_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'catalogPopupButton')))
    catalog_link.click()
    logger.info('Clicked on "Catalog" link')

    # Click on "Smartphones" link
    smartphones_link = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Смартфоны')]")))
    smartphones_link.click()
    logger.info('Clicked on "Smartphones" link')

    # Click on "All Filters" link
    all_filters_link = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-auto="allFiltersButton"]')))
    all_filters_link.click()
    logger.info('Clicked on "All Filters" link')

    # Set the price filter to 20000 RUB
    price_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-auto="range-filter-input-max"]')))
    price_input.clear()
    new_max_price = "20000"
    price_input.send_keys(new_max_price)
    logger.info('Set the price filter to 20000 RUB')

    # Select screen sizes
    screensize1 = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@value='3.5\"-4.9\"']")))
    screensize1.click()
    screensize2 = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@value='5.0\"-5.4\"']")))
    screensize2.click()
    screensize3 = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@value='5.5\"-5.9\"']")))
    screensize3.click()
    screensize4 = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@value='6.0\"-6.4\"']")))
    screensize4.click()
    screensize5 = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@value='6.5\" и больше']")))
    screensize5.click()
    logger.info('Selected screen sizes')

    # Select phone models
    model1 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='BQ']")))
    model1.click()
    model2 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='HONOR']")))
    model2.click()
    model3 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='HUAWEI']")))
    model3.click()
    model4 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='realme']")))
    model4.click()
    model5 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='vivo']")))
    model5.click()
    logger.info('Selected phone models')

    # Click on "Show" button
    show_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[data-autotest-id="result-filters-link"]')))
    show_button.click()
    logger.info('Clicked on "Show" button')

    # Count the number of smartphones on the page
    smartphones_count = len(driver.find_elements(By.XPATH, '//div[@class="n-snippet-cell2__title"]'))
    logger.info(f"Number of smartphones on the page: {smartphones_count}")

    # Get the name of the last smartphone
    last_smartphone_element = driver.find_elements(By.CSS_SELECTOR, '[data-index="9"]')
    last_smartphone_name = last_smartphone_element.text
    logger.info(f"Last smartphone name: {last_smartphone_name}")

    # Sort by discount
    sort_by_discount = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="по скидке"]')))
    sort_by_discount.click()
    logger.info('Sorted by discount')

    # Click on the name of the last smartphone
    driver.find_element(By.XPATH, f'//div[text()="{last_smartphone_name}"]').click()
    logger.info(f"Clicked on the name of the last smartphone: {last_smartphone_name}")

    # Get the rating of the selected smartphone
    rating_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="n-product-review-item__rate"]')))
    rating = rating_element.get_attribute("aria-label")
    logger.info(f"Rating of the selected smartphone: {rating}")

    logger.info('Test completed')


if __name__ == "__main__":
    pytest.main(['-s', '--log-cli-level=INFO'])