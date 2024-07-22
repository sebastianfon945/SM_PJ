from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def setup_driver():
    """Configura el controlador de Chrome."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver


def search_author(driver, query):
    """Realiza la búsqueda por autor."""
    driver.get("https://openlibrary.org/")

    wait = WebDriverWait(driver, 10)
    search_box = driver.find_element(By.NAME, "q")

    author_option = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[aria-label="Search by"] [value="author"]')))
    author_option.click()

    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


def navigate_to_books_section(driver):
    """Navega a la sección de Libros."""
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.search-results-stats'))
        )

    books_link = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a[data-ol-link-track="SearchNav|SearchBooks"]')))
    books_link.click()


def sort_by_rating(driver):
    """Ordena los resultados por Mejor valorados."""
    wait = WebDriverWait(driver, 10)

    rating_link = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a[data-ol-link-track="SearchSort|Rating"]')))
    rating_link.click()


def get_top_results(driver, num_results=3):
    """Obtiene los primeros resultados de búsqueda."""
    wait = WebDriverWait(driver, 10)

    time.sleep(3)

    results = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".booktitle"))
        )

    top_results = [result.text for result in results[:num_results]]
    return top_results


def main():
    driver = setup_driver()
    try:
        search_author(driver, "Julio Verne")
        navigate_to_books_section(driver)
        sort_by_rating(driver)
        top_results = get_top_results(driver, num_results=3)
        for result in top_results:
            print(result)
        time.sleep(5)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
