from datetime import date
from dateutil.relativedelta import relativedelta
import logging
import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os.path
import json
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import email
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta, date
import pytz
import time
import requests
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pynput.keyboard import Key, Controller
import random
import string
import allure

x_path_calender = '/html/body/div[1]/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div[1]/div[3]/div/div'
x_path_calender_top = '/html/body/div[1]/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div[1]/div[3]/div/div/div/div[1]/form/div/div[1]/div/span[1]/input'
x_path_calender_top2 = '/html/body/div[1]/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div/div/div[1]/div[2]/div/div/div[4]/div/div/div/div[1]/form/div/div[1]/div/span[2]/input'
x_path_apply_button = '/html/body/div[1]/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div[1]/div[3]/div/div/div/div[1]/form/button'
x_path_top_call = '/html/body/div[1]/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div/div/div[3]/div[2]/div/div/div/div/div[1]/table/tbody/tr[1]/td[11]/div[1]/div[1]/a/button'
x_path_LoginButton = '/html/body/div[1]/div[2]/div/div/div/div/div/div/div[1]/form/div[4]/button'
x_path_view_feedback_button = "//a[normalize-space()='View Feedback in detail']"
x_path_send_to_agent_checkbox_scorecard_form = '/html/body/div[3]/div/div[1]/div/div/div[2]/div/div/form/div[3]/label/input'
x_path_submit_button_scorecard_form = '/html/body/div[3]/div/div[1]/div/div/div[2]/div/div/form/div[6]/button[2]'
x_path_agent_name_mcsTop = '/html/body/div[1]/div[2]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/p/span[2]'

@pytest.fixture(scope="class")
def setup_class(request):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Open Chrome in maximized mode
    chrome_options.add_argument("--disable-infobars")  # Disable info bars
    chrome_options.add_argument("--disable-extensions")  # Disable extensions

    # Provide the path to chromedriver (you can modify it to the location where your chromedriver is located)
    chrome_driver_path = r"C:\Users\Laudiuu\chromedriver-win64\chromedriver.exe"  # Update this with your chromedriver path
    service = Service(chrome_driver_path)

    # Initialize the Chrome WebDriver with options and service
    driver = webdriver.Chrome(service=service, options=chrome_options)

    request.cls.driver = driver  # Assign driver to the class instance
    yield
    driver.quit()


@pytest.mark.usefixtures("setup_class")
class TestLoginNologin():
    def test_mcs_through_feedback_form_shared_mail(self):

        driver = self.driver
        self.driver.get("https://staging-secure.enthu.ai/login")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'email_address').send_keys('aditya+staging3@enthu.ai')
        self.driver.find_element(By.ID, 'password').send_keys('12345678')
        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_LoginButton)))
        print("login button found")
        login_button.click()
        time.sleep(3)
        self.driver.get("https://staging-secure.enthu.ai/analyse/call/")
        time.sleep(2)
        calender = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, 'calendarButton')))
        calender.click()
        current_date = date.today()
        today_date = current_date.strftime("%b %d, %Y")
        two_months_ago = current_date - relativedelta(months=2)
        two_months_ago_date = two_months_ago.strftime("%b %d, %Y")
        calender_top_element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Early']")))
        calender_top_element.click()
        for i in range(6):
            calender_top_element.send_keys(Keys.BACKSPACE)
        for i in range(6):
            calender_top_element.send_keys(Keys.DELETE)
        calender_top_element.send_keys(two_months_ago_date)
        time.sleep(1)
        calender_top_element2 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_calender_top2)))
        calender_top_element2.click()
        for i in range(6):
            calender_top_element2.send_keys(Keys.BACKSPACE)
        for i in range(6):
            calender_top_element2.send_keys(Keys.DELETE)
        calender_top_element2.send_keys(today_date)
        calender_apply_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, 'applyDateFilter')))
        calender_apply_button.click()
        time.sleep(3)
        top_call_reviewed_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_top_call)))
        top_call_reviewed_button.click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        top_feedback_button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'feedbackFormBadge-0')))
        offset = top_feedback_button.location_once_scrolled_into_view['y']
        driver.execute_script("window.scrollTo(0, arguments[0]);", offset)
        time.sleep(3)
        top_feedback_button.click()
        time.sleep(2)
        mark_all_yes_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, 'markAllYes')))
        mark_all_yes_button.click()
        time.sleep(2)
        collapse_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, 'toggleSectionExpandButton')))
        driver.execute_script("arguments[0].scrollIntoView(true);", collapse_button)
        collapse_button.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        send_to_agent_checkbox = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'emailToAgent')))
        send_to_agent_checkbox.click()
        time.sleep(1)
        submit_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, 'submitFeedbackForm')))
        submit_button.click()
        time.sleep(5)
        # Now checking the email

        SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

        # Load credentials from the JSON file
        credentials_path = os.path.join(os.path.dirname(__file__), 'client_secret.json')
        creds = None

        # The token.json stores the user's access and refresh tokens
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        # If there are no (valid) credentials available, let the user log in
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        # Connect to the Gmail API
        service = build('gmail', 'v1', credentials=creds)

        # Define a query to search for the email
        subject_to_search = 'You have received a feedback on your call'
        query = f'is:unread subject:"{subject_to_search}"'
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q=query).execute()

        messages = results.get('messages', [])

        if not messages:
            print('No unread messages found.')
        else:
            # Get the latest message
            message = service.users().messages().get(userId='me', id=messages[0]['id']).execute()

            # Extract email details
            msg_id = message['id']
            msg_snippet = message['snippet']
            msg_payload = message['payload']
            headers = msg_payload.get('headers', [])

            # Find the subject and from headers
            subject = None
            sender = None

            for header in headers:
                if header['name'] == 'Subject':
                    subject = header['value']
                if header['name'] == 'From':
                    sender = header['value']

            print(f'From: {sender}')
            print(f'Subject: {subject}')
            print(f'Snippet: {msg_snippet}')

            # Generate the Gmail URL for the email
            email_url = f"https://mail.google.com/mail/u/1/?ogbl#inbox/{msg_id}"

            # Print the URL (optional)
            print(f'Email URL: {email_url}')

            # Open the email in the default web browser
            self.driver.get("https://accounts.google.com/signin/v2/identifier")
            email_space = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'identifierId')))
            email_space.send_keys('aditya@enthu.ai')
            email_space.send_keys(Keys.ENTER)
            time.sleep(3)
            password_space = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.NAME, 'Passwd')))
            password_space.send_keys('aditya@2672002')
            password_space.send_keys(Keys.ENTER)
            time.sleep(2)
            self.driver.get(email_url)
            time.sleep(2)

            view_feedback_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_view_feedback_button)))
            print("Button Details======== ", view_feedback_button)
            offset = view_feedback_button.location_once_scrolled_into_view['y']
            driver.execute_script("window.scrollTo(0, arguments[0]);", offset)
            view_feedback_button.click()
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[-1])
            url_main_call_screen = driver.current_url
            print("URL FIRST PART(feedback agent share)======== ", url_main_call_screen)
            assert 'preview/comment' not in url_main_call_screen, "Error: The URL contains the word preview/comment"
            time.sleep(4)

    # def test_mcs_through_scorecard_share_mail(self):
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     self.driver.execute_script("window.scrollTo(0, 0);")
    #     time.sleep(1)
    #     top_call_reviewed_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_top_call)))
    #     top_call_reviewed_button.click()
    #     time.sleep(3)
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     share_scorecard_button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'shareFeedback_0')))
    #     share_scorecard_button.click()
    #     send_to_agent_checkbox_scorecard_form = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, x_path_send_to_agent_checkbox_scorecard_form)))
    #     send_to_agent_checkbox_scorecard_form.click()
    #     submit_scorecard_form = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_submit_button_scorecard_form)))
    #     submit_scorecard_form.click()
    #     time.sleep(2)
    #
    #     # Now checking the email
    #     SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    #
    #     # Load credentials from the JSON file
    #     credentials_path = os.path.join(os.path.dirname(__file__), 'client_secret.json')
    #     creds = None
    #
    #     # The token.json stores the user's access and refresh tokens
    #     if os.path.exists('token.json'):
    #         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    #
    #     # If there are no (valid) credentials available, let the user log in
    #     if not creds or not creds.valid:
    #         if creds and creds.expired and creds.refresh_token:
    #             creds.refresh(Request())
    #         else:
    #             flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
    #             creds = flow.run_local_server(port=0)
    #         # Save the credentials for the next run
    #         with open('token.json', 'w') as token:
    #             token.write(creds.to_json())
    #
    #     # Connect to the Gmail API
    #     service = build('gmail', 'v1', credentials=creds)
    #
    #     # Define a query to search for the email
    #     subject_to_search = 'You have received a feedback on your call'
    #     query = f'is:unread subject:"{subject_to_search}"'
    #     results = service.users().messages().list(userId='me', labelIds=['INBOX'], q=query).execute()
    #
    #     messages = results.get('messages', [])
    #
    #     if not messages:
    #         print('No unread messages found.')
    #     else:
    #         # Get the latest message
    #         message = service.users().messages().get(userId='me', id=messages[0]['id']).execute()
    #
    #         # Extract email details
    #         msg_id = message['id']
    #         msg_snippet = message['snippet']
    #         msg_payload = message['payload']
    #         headers = msg_payload.get('headers', [])
    #
    #         # Find the subject and from headers
    #         subject = None
    #         sender = None
    #
    #         for header in headers:
    #             if header['name'] == 'Subject':
    #                 subject = header['value']
    #             if header['name'] == 'From':
    #                 sender = header['value']
    #
    #         print(f'From: {sender}')
    #         print(f'Subject: {subject}')
    #         print(f'Snippet: {msg_snippet}')
    #
    #         # Generate the Gmail URL for the email
    #         email_url = f"https://mail.google.com/mail/u/1/?ogbl#inbox/{msg_id}"
    #
    #         # Print the URL (optional)
    #         print(f'Email URL: {email_url}')
    #
    #         self.driver.switch_to.window(self.driver.window_handles[-1])
    #         # Open the email in the default web browser
    #         self.driver.get("https://accounts.google.com/signin/v2/identifier")
    #         time.sleep(2)
    #         self.driver.get(email_url)
    #         time.sleep(2)
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         view_feedback_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_view_feedback_button)))
    #         print("Button Details======== ", view_feedback_button)
    #         offset = view_feedback_button.location_once_scrolled_into_view['y']
    #         self.driver.execute_script("window.scrollTo(0, arguments[0]);", offset)
    #         view_feedback_button.click()
    #         time.sleep(3)
    #         self.driver.switch_to.window(self.driver.window_handles[-1])
    #         url_main_call_screen = self.driver.current_url
    #         print("URL SECOND PART(scorecard agent share) ==", url_main_call_screen)
    #         assert 'preview/comment' not in url_main_call_screen, "Error: The URL contains the word preview/comment"
    #
    # def test_mcs_through_scorecard_share_custom(self):
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     self.driver.execute_script("window.scrollTo(0, 0);")
    #     time.sleep(1)
    #     top_call_reviewed_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_top_call)))
    #     top_call_reviewed_button.click()
    #     time.sleep(3)
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     agent_name_mcsTop = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, x_path_agent_name_mcsTop)))
    #     agent_name_mcsTop_text = agent_name_mcsTop.text
    #     share_scorecard_button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'shareFeedback_0')))
    #     share_scorecard_button.click()
    #     custom_email_box = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'inputTags')))
    #     custom_email_box.click()
    #     custom_email_box.send_keys('aditya@enthu.ai')
    #     custom_email_box.send_keys(Keys.ENTER)
    #     submit_scorecard_form = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_submit_button_scorecard_form)))
    #     submit_scorecard_form.click()
    #     time.sleep(2)
    #
    #     # Now checking the email
    #     SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    #
    #     # Load credentials from the JSON file
    #     credentials_path = os.path.join(os.path.dirname(__file__), 'client_secret.json')
    #     creds = None
    #
    #     # The token.json stores the user's access and refresh tokens
    #     if os.path.exists('token.json'):
    #         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    #
    #     # If there are no (valid) credentials available, let the user log in
    #     if not creds or not creds.valid:
    #         if creds and creds.expired and creds.refresh_token:
    #             creds.refresh(Request())
    #         else:
    #             flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
    #             creds = flow.run_local_server(port=0)
    #         # Save the credentials for the next run
    #         with open('token.json', 'w') as token:
    #             token.write(creds.to_json())
    #
    #     # Connect to the Gmail API
    #     service = build('gmail', 'v1', credentials=creds)
    #
    #     # Define a query to search for the email
    #     subject_to_search = f'You have received a feedback on "{agent_name_mcsTop_text}" call'
    #     query = f'is:unread subject:"{subject_to_search}"'
    #     results = service.users().messages().list(userId='me', labelIds=['INBOX'], q=query).execute()
    #
    #     messages = results.get('messages', [])
    #
    #     if not messages:
    #         print('No unread messages found.')
    #     else:
    #         # Get the latest message
    #         message = service.users().messages().get(userId='me', id=messages[0]['id']).execute()
    #
    #         # Extract email details
    #         msg_id = message['id']
    #         msg_snippet = message['snippet']
    #         msg_payload = message['payload']
    #         headers = msg_payload.get('headers', [])
    #
    #         # Find the subject and from headers
    #         subject = None
    #         sender = None
    #
    #         for header in headers:
    #             if header['name'] == 'Subject':
    #                 subject = header['value']
    #             if header['name'] == 'From':
    #                 sender = header['value']
    #
    #         print(f'From: {sender}')
    #         print(f'Subject: {subject}')
    #         print(f'Snippet: {msg_snippet}')
    #
    #         # Generate the Gmail URL for the email
    #         email_url = f"https://mail.google.com/mail/u/1/?ogbl#inbox/{msg_id}"
    #
    #         # Print the URL (optional)
    #         print(f'Email URL: {email_url}')
    #
    #         self.driver.switch_to.window(self.driver.window_handles[-1])
    #         # Open the email in the default web browser
    #         self.driver.get("https://accounts.google.com/signin/v2/identifier")
    #         time.sleep(2)
    #         self.driver.get(email_url)
    #         time.sleep(2)
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         view_feedback_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_path_view_feedback_button)))
    #         print("Button Details======== ", view_feedback_button)
    #         offset = view_feedback_button.location_once_scrolled_into_view['y']
    #         self.driver.execute_script("window.scrollTo(0, arguments[0]);", offset)
    #         view_feedback_button.click()
    #         time.sleep(3)
    #         self.driver.switch_to.window(self.driver.window_handles[-1])
    #         url_main_call_screen = self.driver.current_url
    #         print("URL THIRD PART(custom) ==", url_main_call_screen)
    #         assert 'preview/comment' in url_main_call_screen, "Error: The URL does not contains the word preview/comment"