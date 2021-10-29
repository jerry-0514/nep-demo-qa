# nep-demo-qa

## Overview

This project repo contains the automated test solution for the book store application 
of Demo QA (https://demoqa.com/login). The project is using behave as base framework and python as programming language for steps implementation. 


## Tools Used

This project was developed using the following tools:
- Behave (2.6) as base framework
- Python (3.8) as programming language for steps implementation.
- Selenium webdriver (4.0) to interact with the browser  
- Tested using Chrome browser version 95.0.4638.54
- Tested using selenium chromedriver version 95 (webdriver/chromedriver_win32.zip)
- Code is written using pycharm professional (2020.3.4) as IDE
- Python libraries which the user can install using pip. Please see Test Execution Section


## Folder Structure

- /features/*.feature - feature files where scenarios are written. Since we are using behave, tests are written in Gherkin format (given, when, then)
- /features/steps - python implementation of the test steps
- /features/environment.py - contains test hooks for test setup and teardown
- /data - contains the datasource (books.json) used by the script to check the completeness of the book records and config for logging (logging.ini)
- /pages - classes to handle the pages of the app. This contains the locators for each element and methods to interact with them
- /webdriver - contains selenium webdriver used for this test
- /requirement.txt - file which contains the python dependencies for this project

## Out of Scope

- Captcha - The application under test contains captcha. The script can't handle it. 
  So as a workaround, I added a prompt to ask the user to perform the captcha manually. 
  After doing the captcha, the user can accept the alert message so that the script can resume the test. 
  I added a tag for test scenarios with captcha (@with_manual_intervention). User can exclude them if they wish to do so.
- Alerts - For some reason, the tools which I am currently using are not able to interact with the alerts used by the application. 
  I was not able to perform validation for the alerts, and I'm just simulating the ENTER key to accept the prompt. 

## Test Execution

Install the dependencies from requirements.txt

`pip install -r requirements.txt`

To run the test using behave, execute this in your terminal

`behave <path of feature file>`

To exclude tests with captcha, add tag argument to skip them

`behave <path of feature file> --tags=-with_manual_intervention`

## Test Artifacts

Test results can be found at /results folder. 
I also have a video recording for the test execution which can be downloaded from this drive: https://drive.google.com/drive/folders/1vpcUaEEriwVmTF4Wavj3ISIjnNfGnu-o?usp=sharing 