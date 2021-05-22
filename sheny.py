# This program has been created for Sheny to help her parents (Last update 2021-05-19)

# Import modules
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--user', help="Options are fari, shikoo or farishikoo", default='fari')
parser.add_argument('--jamatkhana', help="Options are hq, hq-overflow or both", default='hq')
parser.add_argument('--password', help="Add password")
args = parser.parse_args()

# Function to schedule seats if check availability is open
def schedule_seat(user, test):
    # Find and click on checkboxes
    time.sleep(2)
    
    checkboxes_enabled = 0
    # Checkbox for first person
    if web.find_elements_by_xpath('//*[@id="family-schedule-modal"]/div/div/div[2]/div/table/tbody/tr[1]/td[1]/input'):
        checkbox_1 = web.find_element_by_xpath('//*[@id="family-schedule-modal"]/div/div/div[2]/div/table/tbody/tr[1]/td[1]/input')
        if checkbox_1.is_enabled():
            checkboxes_enabled += 1
            if user=='fari' or user=='farishikoo':
                checkbox_1.click()
                print('Seat available for Fari!')

    # Checkbox for second person
    if web.find_elements_by_xpath('//*[@id="family-schedule-modal"]/div/div/div[2]/div/table/tbody/tr[2]/td[1]/input'):
        checkbox_2 = web.find_element_by_xpath('//*[@id="family-schedule-modal"]/div/div/div[2]/div/table/tbody/tr[2]/td[1]/input')
        if checkbox_2.is_enabled():
            checkboxes_enabled += 1
            if user=='shikoo' or user=='farishikoo':
                checkbox_2.click()
                print('Seat available for Shikoo!')

    if checkboxes_enabled>0:
        time.sleep(0.5)
        if web.find_elements_by_xpath('//*[@id="register-schedule-family"]'):
            schedule_now = web.find_element_by_xpath('//*[@id="register-schedule-family"]')
            if test=='yes':
                return 0
            else:
                schedule_now.click()
                time.sleep(2)
                if web.find_elements_by_xpath('/html/body/div[4]/div/div[3]/button[1]'):
                    are_you_sure = web.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[1]')
                    are_you_sure.click()
                    print('Successfully Scheduled!')
                    return 1
    else:
        print('Seat not available.')
        close_button = web.find_element_by_xpath('//*[@id="family-schedule-modal"]/div/div/div[3]/button[2]')
        close_button.click()
        time.sleep(5)
        web.find_element_by_class_name('refresh-item').click()
        return 0

def login_to_website():
    # Log-in credentials
    username = 'fskhoja'
    password = args.password

    username_textbox = web.find_element_by_xpath('/html/body/div[2]/div/div/form/div[1]/input')
    username_textbox.send_keys(username)

    password_textbox = web.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/input')
    password_textbox.send_keys(password)

    login_button = web.find_element_by_xpath('/html/body/div[2]/div/div/form/button')
    login_button.click()

if __name__ == '__main__':
    user = args.user
    jamatkhana = args.jamatkhana

    # Initialize Program
    print('Putting SHENY to work...')

    # Define web-driver and open webpage
    web = webdriver.Chrome()
    web.get('https://jamatkhana.theismailiusa.org/')

    # Wait for the webpage to load
    time.sleep(0.5)

    # Log in to the page
    login_to_website()

    # Click on Morning or Evening Availability
    tries = 0
    while tries<10000:
        # Click Check Availability
        time.sleep(2)
        check_availability = web.find_element_by_xpath('//*[@id="manual_event_list_btn"]')
        print('SHENY is now checking availability')
        check_availability.click()
        time.sleep(2)
        
        if web.find_elements_by_xpath('//*[@id="overflow_center_55"]/div[3]/div[2]/div[3]/button'):
            event2 = web.find_element_by_xpath('//*[@id="overflow_center_55"]/div[3]/div[2]/div[3]/button')
            event2.click()
            print('Check Availability Active!')
            # Schedule seat since availability is active
            scheduled=schedule_seat(user, 'no')
            if scheduled==1:
                break
                time.sleep(9999)
        elif web.find_elements_by_xpath('//*[@id="overflow_center_55"]/div[3]/div[1]/div[3]/button'):
            event1 = web.find_element_by_xpath('//*[@id="overflow_center_55"]/div[3]/div[1]/div[3]/button')
            event1.click()
            print('Check Availability Active!')
            # Schedule seat since availability is active
            scheduled=schedule_seat(user, 'no')
            if scheduled==1:
                break
                time.sleep(9999)
        elif web.find_elements_by_xpath('//*[@id="overflow_center_52"]/div[3]/div[2]/div[3]/button'):
            event1 = web.find_element_by_xpath('//*[@id="overflow_center_52"]/div[3]/div[1]/div[3]/button')
            event1.click()
            print('Check Availability Active!')
            # Schedule seat since availability is active
            scheduled=schedule_seat(user, 'no')
            if scheduled==1:
                break
                time.sleep(9999)
        elif web.find_elements_by_xpath('//*[@id="overflow_center_52"]/div[3]/div[1]/div[3]/button'):
            event1 = web.find_element_by_xpath('//*[@id="overflow_center_52"]/div[3]/div[1]/div[3]/button')
            event1.click()
            print('Check Availability Active!')
            # Schedule seat since availability is active
            scheduled=schedule_seat(user, 'no')
            if scheduled==1:
                break
                time.sleep(9999)
        else:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print('Try '+ str(tries) + ': No availability at ' + current_time)
            #web.find_element_by_class_name('refresh-item').click()
            time.sleep(1)
            web.refresh()
            time.sleep(2)
            tries += 1
            
    #web.close()