from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

import os
import pickle
from time import sleep

CONTACT_FILE_PATH = 'contacts.pkl'
WHATSAPP_CONTACT_LINK = 'https://wa.me/'
INITIATE_CHAT_BUTTON_XPATH = '//*[@id="action-button"]'
ACCESS_WHATSAPP_WEB_BUTTON_XPATH = '//*[@id="fallback_block"]/div/div/h4[2]/a'
QR_CODE_WHATSAPP_XPATH = '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]'
TYPE_BAR_XPATH = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div/p'
SEND_MESSAGE_BUTTON_XPATH = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button'

navigator : webdriver.Chrome = ''
contact_list : list = list()

#gerenciamento de arquivos

def read_file() -> list:

    with open(CONTACT_FILE_PATH, 'rb') as file:
        file_data = pickle.load(file)

    file.close()

    return file_data
    

def write_file():
    with open(CONTACT_FILE_PATH, 'wb') as file:
        pickle.dump(file)
    
    file.close()

def check_if_contact_file_exists():
    return os.path.isfile(CONTACT_FILE_PATH)


def create_contact_file():
    with open(CONTACT_FILE_PATH, w) as file:
        file.write("")
        
    file.close()


#gerenciamento do whatsapp
def initiate_navigator_driver() -> webdriver.Chrome:

    chromeOptions = Options()
    chromeOptions.add_experimental_option("detach", True)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chromeOptions)

    return driver


def send_messages_to(number : str, messages : list):

    navigator.get(WHATSAPP_CONTACT_LINK + number)
    navigator.find_element(By.XPATH, INITIATE_CHAT_BUTTON_XPATH).click()
 
    WebDriverWait(navigator, 300).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ACCESS_WHATSAPP_WEB_BUTTON_XPATH))
    )

    navigator.find_element(By.XPATH, ACCESS_WHATSAPP_WEB_BUTTON_XPATH).click()

    sleep(10)

    WebDriverWait(navigator, 300).until(
        expected_conditions.invisibility_of_element_located((By.XPATH, QR_CODE_WHATSAPP_XPATH))
    )

    #Manda as mensagens para o contato
    for message in messages:
        type_message(message)
        sleep(7)



def type_message(message : str):

    WebDriverWait(navigator, 300).until(
        expected_conditions.visibility_of_element_located((By.XPATH, TYPE_BAR_XPATH))
    )

    navigator.find_element(By.XPATH, TYPE_BAR_XPATH).send_keys(message)
    navigator.find_element(By.XPATH, SEND_MESSAGE_BUTTON_XPATH).click()