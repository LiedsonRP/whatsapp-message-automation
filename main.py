from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pickle

CONTACT_FILE_NAME = 'contacts.pkl'


contact_list = list()

#gerenciamento de arquivos

def read_file() -> list:

    with open(CONTACT_FILE_NAME, 'rb') as file:
        file_data = pickle.load(file)

    file.close()

    return file_data
    

def write_file():
    with open(CONTACT_FILE_NAME, 'wb') as file:
        pickle.dump(file)
    
    file.close()


#gerenciamento do whatsapp
def initiate_navigator() -> webdriver:

    chromeOptions = Options()
    chromeOptions.add_experimental_option("detach", True)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chromeOptions)

    return driver

def enter_in_contact_with(number):
    pass


#Código principal
read_file()