import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import io
import re
import csv


def goto_page(url):
    """Navigates to given url, url must be string"""
    driver.get(url)


def enter_query(query):
    """Enters the wanted query into the pubmed search bar and presses RETURN"""
    #text_bar = driver.find_element(By.NAME, 'p')
    text_bar = driver.find_element(By.NAME, 'term')  # Find the search box
    text_bar.send_keys(query + Keys.RETURN)

def get_href():
    """Ïterates through all results, adding href and title to list. Returns that list."""
    href_list = []
    try:
        total_pages = driver.find_element(By.CLASS_NAME,"search-results-chunk").get_attribute('data-pages-amount')
        page_end = total_pages
        page_end = re.sub("\D", "", page_end)
        print(page_end)
    except:
        page_end = 1

    for i in range(int(page_end)):
        # for i in range(1):
        print("Collecting data: page {} of {}".format(i + 1, page_end))
        for title in driver.find_elements(By.CLASS_NAME,"docsum-content"):
            href = title.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
            href_list.append(href)
        try:
            driver.find_element_by_class_name("next").click()
        except:
            pass
    return (href_list)


def extract_data():
    """Gets title, authors and abstract from individual result pages"""
    title = driver.find_element(By.XPATH,"//meta[@property = 'og:title']").get_attribute("content")
    authors = driver.find_element(By.XPATH,"//meta[@name = 'keywords']").get_attribute("content")
    #citation = driver.find_element_by_class_name("cit").text
    #abstract_block = driver.find_element_by_class_name("abstract")
    #paragraphs = abstract_block.find_elements_by_css_selector("p")
    #abstract = driver.find_element(By.XPATH,"//meta[@property = 'og:description']").get_attribute("content")
    try:
        abstract = driver.find_element(By.ID,"abstract").find_element(By.TAG_NAME,"p").text
    except:
        print("can't find abstract")
        abstract = "can't find abstract"
    print(abstract)
    print(type(abstract))
    # for paragraph in paragraphs:
    #     abstract += paragraph.text
    #  print(title, authors,abstract)
    return [title, authors, abstract]


def write_data_to_file(query, data_list, filename):
    fields = ['Title','Authors','Abstract']

    query = query
    filename = filename
    data_list = data_list
    with open(filename,'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(data_list)


# ______________MAIN______________
if __name__ == "__main__":
    import os
    import time

    driver = webdriver.Chrome("/Users/williamlast/PycharmProjects/WebScarping_Pubmed/chromedriver")

    # always first go to pubmed page
    print("Connecting to Pubmed")
    driver.get("https://pubmed.ncbi.nlm.nih.gov/")
    print("Starting Query")

    # insert search quary below
    query = 'red meat covid'
    enter_query(query)
    # retrieve href and title from all results
    href_list = get_href()

    # extract title, author and abstract for each result.
    full_data_list = []
    print("Extracting abstracts!, this might take a while.")
    for url in href_list:
        goto_page(url)
        full_data_list.append(extract_data())
    driver.close()

    filename = "Result" + ".csv"
    print("Writing To file: {}".format(filename))
    write_data_to_file(query, full_data_list, filename)

    print("process complete, press any key to close window")
    input()





