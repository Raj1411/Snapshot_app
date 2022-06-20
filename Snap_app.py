from matplotlib.pyplot import text
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from time import sleep
import streamlit as st



webdriveroptions = Options()
webdriveroptions.add_argument("--headless")
webdriveroptions.add_argument("--start-maximized")
# webdriveroptions.binary_location = 

st.title('Snapshot App')
link=st.text_input('Enter Web_Page link')

driver=webdriver.Firefox(executable_path="/home/appuser/.conda/bin/geckodriver",options=webdriveroptions)

if link=="":
    None
else:
    driver.get(link)
    # st.write(link)
    sleep(2)
    ele= driver.find_element_by_xpath('//*[@id="app"]')
    width=1920
    height=ele.size['height'] + 1000
    driver.set_window_size(width,height)
    sleep(2)
    driver.save_screenshot('nykaa.png')

    driver.close()