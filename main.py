from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import telebot
import os
from load_dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))


def main(teacher, search):
    print("Starting...")
    options = webdriver.EdgeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Edge(options=options)

    driver.get("https://edugate.jadara.edu.jo/student")

    username = driver.find_element(By.ID, "lognForm:j_idt14")
    username.send_keys(os.getenv("USERNAME_"))

    password = driver.find_element(By.ID, "lognForm:j_idt18")
    password.send_keys(os.getenv("PASSWORD_"))

    password.send_keys(Keys.ENTER)
    time.sleep(0.5)

    driver.get("https://edugate.jadara.edu.jo/student/onlineRegistration")
    time.sleep(0.5)
    driver.find_element(By.ID, "contents:j_idt121").click()
    time.sleep(4)

    elements = []
    driver.execute_script(
        'let s=document.getElementsByName("contents:coursesTable_rppDD")[0];let o = document.createElement("option");o.value=1000;o.text="1000";s.add(o);'
    )

    s = driver.find_element(By.NAME, "contents:coursesTable_rppDD")
    s.click()
    s.send_keys(1000)
    s.send_keys(Keys.ENTER)
    time.sleep(0.5)

    elements += (
        driver.find_element(By.ID, "contents:coursesTable")
        .find_element(By.ID, "contents:coursesTable_data")
        .find_elements(By.TAG_NAME, "tr")
    )

    result = []

    for element in elements:
        if search in element.text:
            result.append(element)

    result[-1].find_elements(By.TAG_NAME, "td")[-1].click()
    time.sleep(1)
    try:
        driver.find_element(By.ID, "contents:j_idt175").click()
    except:
        pass
    time.sleep(1)
    clases = driver.find_element(By.ID, "contents:sectionsTable_data").find_elements(
        By.TAG_NAME, "tr"
    )
    final = ""
    for clase in clases:
        text = int(clase.text[:2])
        if text == teacher:
            final = clase.find_elements(By.TAG_NAME, "td")[-1].text
            break
    driver.quit()
    print("Done")
    return final
