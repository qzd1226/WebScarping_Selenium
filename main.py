import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import io
import re
import csv
import random
import time


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
    page_end = min('10',page_end)
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
    # free label:
    freelabel = ""
    try:
        freelabel = driver.find_element(By.CLASS_NAME,"free-label").text
        print(freelabel)
    except:
        print("can't find free label")
    # pdf link:
    pdflink = ""
    #freelabel = "stop"
    if(freelabel == "Free PMC article"):
        try:
            original_window = driver.current_window_handle
            curherf = driver.find_element(By.CLASS_NAME,"pmc").get_attribute('href')
            # 在新的标签页打开链接
            driver.execute_script(f'window.open("{curherf}", "_blank");')
            # 切换到新的标签页
            driver.switch_to.window(driver.window_handles[-1])
            rand = random.randint(0, 5)
            time.sleep(rand)
            # 单独处理
            try:
                pdflink = driver.find_element(By.CLASS_NAME,"int-view").get_attribute("href")
                print(pdflink)
            except:
                pass
            # 关闭当前标签页
            driver.close()
            # 切回到之前的标签页
            driver.switch_to.window(original_window)
        except:
            pass

    print(abstract)
    print(type(abstract))
    return [query,title, authors, abstract, pdflink]


def write_data_to_file(query, data_list, filename):
    fields = ['KeyWord','Title','Authors','Abstract','Link']
    query = query
    filename = 'table/' + filename
    data_list = data_list
    with open(filename,'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(data_list)


# ______________MAIN______________
if __name__ == "__main__":
    import os
    import time
    dependentAll = ['lifespan','all-cause mortality','Disease','weight BMI','Biological systems',
                 'cardiovasular heart','digestive','endocrine','sensory system','immune and hematology',
                 'lymphatic','muscular system','skeletal system bones','nervous system brain','reproductive system',
                 'respiratory system lungs','integumentary system skin','urinary system','Performance','Physical',
                 'mental','stress','happiness','depression','genomic instabilitry','telomere attrition','epigenetic alteration',
                 'loss of proteostasis','deregulated nutrient sensing','mitochondrial dysfunction','cellular senescence',
                 'stem cell exhaustion','altered intercellular communication']
    independentAll = ['fasting','intermittent fasting','meat','fish','vegetable','fruit','legumes','grains',
                   'fats','saturated','refined sugars','dairy','nuts','Mediterranean','Vegetarian',
                   'Plant-based','Gluten fee','Vegan','Keto','Dairy Free','Low Fat','Okinawan',
                   'Alternate Healthy Eating Index','general exercise','aerobic cardio exercise',
                   'muscle strengthening','resistance training','stretching','bone strengthening',
                   'Sleep Amount','Sleep quality','Stress Reduction relaxation','Stress meditation',
                   'mindfulness','tai chi','breathing','Stress distraction','Stress Induction sauna bathing',
                   'Stress Induction cold','Stress Induction heat','Calcium','Dietary Fiber','Fat','Saturated fat',
                   'Protein','Magnesium','Manganese','Phosphorus','Potassium','Vitamin A','Vitamin C','Vitamin D',
                   'Vitamin K','Biotin','Chloride','Chromium','Copper','Folate Folic Acid','Molybdenum','Niacin (B3)',
                   'Pantothenic Acid','Riboflavin (B2)','Selenium','Sodium','Thiamin (B1)','Total carbohydrate',
                   'Added sugars','Choline','Vitamin B6','Vitamin B12','Vitamin E','Zinc','Cholesterol','Iodine',
                   'Iron','Nickel','Ashwagandha','Turmeric','Garlic','Matcha green tea','fish oil omega 3','plant sterols',
                   'NMN','NR','Calcium AKG','Alpha lipoic acid','fisetin','quercetin','PQQ','collagen peptides',
                   'hyalauronic acid','chlorella','spirulina','resveratrol','CoQ10','probioltics','melatonin','Acetyl-L-carnitine',
                   'olive oil','lutein','milk thistle','spermidine','creatine','trimethyl glycine']
    independent = ['meat']
    dependent = ['Biological systems',
                 'cardiovasular heart','digestive','endocrine','sensory system','immune and hematology',
                 'lymphatic','muscular system','skeletal system bones','nervous system brain','reproductive system',
                 'respiratory system lungs','integumentary system skin','urinary system','Performance','Physical',
                 'mental','stress','happiness','depression','genomic instabilitry','telomere attrition','epigenetic alteration',
                 'loss of proteostasis','deregulated nutrient sensing','mitochondrial dysfunction','cellular senescence',
                 'stem cell exhaustion','altered intercellular communication']
    for inde in independent:
        for dep in dependent:
            query = inde + ' ' + dep
            print("Connecting to Pubmed")
            driver = webdriver.Chrome("/Users/williamlast/PycharmProjects/WebScarping_Pubmed/chromedriver")
            driver.get("https://pubmed.ncbi.nlm.nih.gov/")
            print("Starting Query:")
            print(query)
            # insert search quary below
            enter_query(query)
            # retrieve href and title from all results
            href_list = []
            href_list = get_href()
            # extract title, author and abstract for each result.
            full_data_list = []
            print("Extracting abstracts!, this might take a while.")
            num = 1
            for url in href_list:
                goto_page(url)
                full_data_list.append(extract_data())
            driver.close()
            filename = query + ".csv"
            print("Writing To file: {}".format(filename))
            write_data_to_file(query, full_data_list, filename)

    print("process complete, press any key to close window")
    input()





