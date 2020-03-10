from selenium import webdriver
import pandas as pd
###from consts import HILL_LINK, GUARDIAN_LINK
from sentiment import sentiment_value
from jobs.cron import news_sentiment_data
import traceback


options = webdriver.ChromeOptions()
options.add_argument("--incognito")

#--------------------------------The Guardian Article ------------------------------
def guardian_article(link, publish_date, author, description):
    
    driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)  #Path of the crome driver, using headless.
    driver.get(link)

    try:
        #Headline for First Article
        title = driver.find_element_by_xpath("//h1[contains(@class, 'headline')]").text
        print(title + "\n")

        #Sub-heading of first article
        '''subheading = driver.find_element_by_xpath("//div[contains(@class, 'standfirst')]/p").text
        print(subheading+"\n")'''

        #Main content of the article
        numberOfParas = driver.find_elements_by_xpath("//div[contains(@class, 'article-body')]//following::p")
        numberOfParas = len(numberOfParas)
        para = ""  
        for i in range(numberOfParas):   
            para = para + " " + driver.find_element_by_xpath("(//div[contains(@class, 'article-body')]//following::p)[{}]".format(i+1)).text

        if para == '':
            para = description

        polarity, keyword_count = sentiment_value(title, para)

        news_sentiment_data("The Guardian", title, link, publish_date, author, polarity, keyword_count)


    except():
        print(str(traceback.format_exc()))

    driver.close()

#--------------------------------The Hill Article ------------------------------
def hill_article(link, publish_date, author, description):

    driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)  #Path of the crome driver, using headless.
    driver.get(link)
    
    try:
        #Headline for Second Article
        title = driver.find_element_by_xpath("//h1[@class='title']").text
        print(title + "\n")

        #Content of the second article
        numberOfParas = driver.find_elements_by_xpath("//div[@class='field-items']/div/p")
        numberOfParas = len(numberOfParas)
        para = ""  
        for i in range(numberOfParas):   
            para = para + " " + driver.find_element_by_xpath("(//div[@class='field-items']/div/p)[{}]".format(i+1)).text

        if para == '':
            para = description

        polarity, keyword_count = sentiment_value(title, para)

        news_sentiment_data("The Hill", title, link, publish_date, author, polarity, keyword_count)

    except:
        print(str(traceback.format_exc()))

    driver.close()