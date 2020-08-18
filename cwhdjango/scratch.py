from selenium import webdriver
import os
import time

def main():
    driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

    # name = input("Enter the name of the user you want to send message : ")
    # msg = input("Enter the message you want to send : ")
    # count = int(input("Enter the count of message to sent : "))

    name = "Best Friend"
    msg = "Hello"
    count = 1

    driver.get("https://web.whatsapp.com/")

    input("Enter any key after Scanning the qr code...")

    user = driver.find_element_by_xpath(f'//span[@title = "{name}"]').click()

    #message = driver.find_element_by_class_name("_2FbwG")

    driver.find_element_by_class_name("_1JNuk").click()


    # for i in range(count):
    #     message.send_keys(msg)
    #     driver.find_element_by_class_name('_1U1xa').click()

    # for i in range(count):
    #     message.send_keys("Hello")
    #     # The classname of send button may vary.
    #     button = driver.find_element_by_class_name('_3M-N-')
    #     button.click()

    print("Complete...")


main()



