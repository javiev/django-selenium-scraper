import python_setup
from datetime import datetime

from django.db import transaction
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from newScrap.models import ScrapedData


@transaction.atomic
def scraper_base():
    """
    This function scrapes headlines from a specific Chilean newspaper website.
    It saves the scraped data into the database if the headline does not already exist.
    """
    # Get the current date and time
    current_datetime = datetime.now()

    # Set up the Selenium driver options
    options = Options()
    options.add_argument("-headless")

    print('1 - Initializing driver')
    driver = webdriver.Firefox(options=options)
    website = '#'  # The URL of the website to scrape

    print('2 - Loading website')
    driver.get(website)

    print('3 - Finding headline')
    # Locate the main headline element using XPATH
    titular_element = driver.find_element(By.XPATH, '#')
    headline_text = titular_element.text
    headline_href = titular_element.get_attribute('href')

    print('4 - Finding other headlines')
    # Locate other headline elements using CLASS_NAME
    titulares = driver.find_elements(By.CLASS_NAME, '#')

    # Create a list of headlines with their text and links
    lista_titulares = [
        {'text': titular.text, 'link': titular.find_element(By.TAG_NAME, 'a').get_attribute('href')}
        for titular in titulares
    ]

    # Check if the main headline already exists in the database
    if not ScrapedData.objects.filter(headline=headline_text).exists():
        # The headline does not exist, prepare the data to be saved
        data_to_save = [
                           ScrapedData(
                               datetime=current_datetime,
                               website=website,
                               headline=headline_text,
                               link=headline_href
                           )
                       ] + [
                           ScrapedData(
                               datetime=current_datetime,
                               website=website,
                               headline=titular['text'],
                               link=titular['link']
                           ) for titular in lista_titulares
                       ]

        # Save the data to the database
        ScrapedData.objects.bulk_create(data_to_save)

        print('5 - Data saved to the database')
    else:
        print('5 - No new data has been saved')

    driver.quit()
    print('6 - Driver quit')


# Call the function containing the script
if __name__ == "__main__":
    scraper_base()
