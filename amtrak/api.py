from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from amtrak.validators.utils import validate_passenger_counts
from amtrak.validators import Station, Traveler, Travelers, PromoCode, CouponCode
from amtrak.enums import AgeGroup, Discount

from pydantic import ValidationError, conint
from typing import Optional
from datetime import date
from time import sleep

DEPARTING_STATION_SELECTOR = "input.mat-input-element[data-placeholder='From']"
RETURNING_STATION_SELECTOR = "input.mat-input-element[data-placeholder='To']"

ACCEPT_COOKIES_BUTTON_SELECTOR = "button#onetrust-accept-btn-handler"

DEPARTING_DATE_SELECTOR = "input[amt-auto-test-id='fare-finder-depart-date-oneway']"

DONE_BUTTON_SELECTOR = "button[aria-label='Done']"

TRAVELERS_MENU_DROPDOWN_SELECTOR = "button[amt-auto-test-id='traveler-dropdown-button']"
TRAVELERS_MENU_DONE_BUTTON_SELECTOR = "button[amt-auto-test-id='traveler-component-discount-done-button']"

INCREMENT_ADULTS_SELECTOR = "button.increment[amt-auto-test-id='traveler-component-adult-incr-button']"
DECREMENT_ADULTS_SELECTOR = "button.decrement[amt-auto-test-id='traveler-component-adult-dcr-button']"

INCREMENT_SENIOR_SELECTOR = "button.increment[amt-auto-test-id='traveler-component-senior-incr-button']"
DECREMENT_SENIOR_SELECTOR = "button.decrement[amt-auto-test-id='traveler-component-senior-dcr-button']"

INCREMENT_YOUTH_SELECTOR = "button.increment[amt-auto-test-id='traveler-component-youth-incr-button']"
DECREMENT_YOUTH_SELECTOR = "button.decrement[amt-auto-test-id='traveler-component-youth-dcr-button']"

INCREMENT_CHILD_SELECTOR = "button.increment[amt-auto-test-id='traveler-component-child-incr-button']"
DECREMENT_CHILD_SELECTOR = "button.decrement[amt-auto-test-id='traveler-component-child-dcr-button']"

INCREMENT_INFANT_SELECTOR = "button.increment[amt-auto-test-id='traveler-component-infants-incr-button']"
DECREMENT_INFANT_SELECTOR = "button.decrement[amt-auto-test-id='traveler-component-infants-dcr-button']"

class API:
    endpoint = "https://www.amtrak.com"
    
    def __init__(self, headless: bool = True, timeout: float = 30):
        options = webdriver.ChromeOptions()
        
        if headless:
            options.add_argument("--headless=new")
            
        options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options = options)
        self.driver.implicitly_wait(timeout)
        
        self.timeout = timeout
        
    def search(self, query: Query):
        actions = ActionChains(self.driver)
        
        # Open the Amtrak homepage
        self.driver.get(self.endpoint)
        
        # Accept cookies
        wait = WebDriverWait(self.driver, timeout = self.timeout)
        accept_cookies_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ACCEPT_COOKIES_BUTTON_SELECTOR)))
        accept_cookies_button.click()
    
            # Open the travelers menu dropdown
        wait = WebDriverWait(self.driver, timeout = self.timeout)
        travelers_menu_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, TRAVELERS_MENU_DROPDOWN_SELECTOR)))
        travelers_menu_dropdown.click()
        
        print("Adults:", query.adults)
        print("Seniors:", query.seniors)
        print("Youth:", query.youth)
        print("Children:", query.children)
        print("Infants:", query.infants)
        
        # Set the number of adults
        if query.adults == 0:
            # Decrement the number of adults to 0
            wait = WebDriverWait(self.driver, timeout = self.timeout)
            decrement_adults_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, DECREMENT_ADULTS_SELECTOR)))
            decrement_adults_button.click()
        else:
            # Increment the number of adults
            wait = WebDriverWait(self.driver, timeout = self.timeout)
            increment_adults_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, INCREMENT_ADULTS_SELECTOR)))
            
            for clicks in range(query.adults - 1):
                increment_adults_button.click()
                sleep(0.3)
                continue
                while True:
                    increment_adults_button.click()
                    
                    try:
                        # Wait until the counter is updated
                        wait = WebDriverWait(self.driver, timeout = 3)
                        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, INCREMENT_ADULTS_SELECTOR).get_attribute("aria-label") == f"senior {clicks + 2}")
                        break
                    except:
                        print("HI")
                        print(EC.element_to_be_clickable((By.CSS_SELECTOR, INCREMENT_ADULTS_SELECTOR)).get_attribute("aria-label"))
                        continue
                    
        # Set the number of seniors
        for clicks in range(query.seniors):
            wait = WebDriverWait(self.driver, timeout = self.timeout)
            increment_senior_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, INCREMENT_SENIOR_SELECTOR)))
            increment_senior_button.click()
            
            while True:
                try:
                    # Wait until the counter is updated
                    wait = WebDriverWait(self.driver, timeout = 3)
                    wait.until(lambda _: increment_senior_button.get_attribute("aria-label") == f"senior {clicks + 1}")
                    break
                except:
                    print("HI")
                    continue

        # Set the number of youth
        for clicks in range(query.youth):
            wait = WebDriverWait(self.driver, timeout = self.timeout)
            increment_youth_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, INCREMENT_YOUTH_SELECTOR)))
            increment_youth_button.click()
            
            while True:
                try:
                    # Wait until the counter is updated
                    wait = WebDriverWait(self.driver, timeout = 3)
                    wait.until(lambda _: increment_youth_button.get_attribute("aria-label") == f"youth {clicks + 1}")
                    break
                except:
                    print("HI")
                    continue

        # Set the number of children
        for clicks in range(query.children):
            wait = WebDriverWait(self.driver, timeout = self.timeout)
            increment_child_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, INCREMENT_CHILD_SELECTOR)))
            increment_child_button.click()
            
            while True:
                try:
                    # Wait until the counter is updated
                    wait = WebDriverWait(self.driver, timeout = 3)
                    wait.until(lambda _: increment_child_button.get_attribute("aria-label") == f"children {clicks + 1}")
                    break
                except:
                    print("HI")
                    continue
                
        # Set the number of infants
        for clicks in range(query.infants):
            wait = WebDriverWait(self.driver, timeout = self.timeout)
            increment_infant_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, INCREMENT_INFANT_SELECTOR)))
            increment_infant_button.click()
            
            while True:
                try:
                    # Wait until the counter is updated
                    wait = WebDriverWait(self.driver, timeout = 3)
                    wait.until(lambda _: increment_infant_button.get_attribute("aria-label") == f"infant {clicks + 1}")
                    break
                except:
                    print("HI")
                    continue
        
        # Click the done button
        wait = WebDriverWait(self.driver, timeout = self.timeout)
        travelers_menu_done_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, TRAVELERS_MENU_DONE_BUTTON_SELECTOR)))
        travelers_menu_done_button.click()

        # Enter the departing station
        wait = WebDriverWait(self.driver, timeout = self.timeout)
        departing_station_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, DEPARTING_STATION_SELECTOR)))
        departing_station_field.send_keys(query.origin)
        
        # Wait for the departing station to be revealed
        wait = WebDriverWait(self.driver, timeout = self.timeout)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//div[contains(@class, 'station-plate-code')]/span[text()='{query.origin}']")))
        
        # Enter the returning station
        returning_station_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, RETURNING_STATION_SELECTOR)))
        returning_station_field.send_keys(query.destination)
        
        # Wait for the returning station to be revealed
        wait = WebDriverWait(self.driver, timeout = self.timeout)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//div[contains(@class, 'station-plate-code')]/span[text()='{query.destination}']")))
        
        if query.needs_assistance:
            # Click the assistance checkbox
            assistance_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[amt-auto-test-id='assistance-checkbox']")
            assistance_checkbox.click()
        
        # Get formatted dates (MM/DD/YYYY)
        depart_date = query.depart_date.strftime("%m/%d/%Y")
        print(depart_date)
        
        # Enter the departing date
        wait = WebDriverWait(self.driver, timeout = self.timeout)
        departing_date_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, DEPARTING_DATE_SELECTOR)))
        departing_date_field.click()
        departing_date_field.send_keys(depart_date)
        
        # Press tab to submit the departing date using actions
        actions.send_keys(Keys.TAB).perform()
        
        # Click the done button
        wait = WebDriverWait(self.driver, timeout = self.timeout)
        done_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, DONE_BUTTON_SELECTOR)))
        done_button.click()
    
        pass