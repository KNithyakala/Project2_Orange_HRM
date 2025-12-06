**HR Management Web Application – Orange HRM**

**Title**

Automated Testing of the Web Application https://opensource-demo.orangehrmlive.com

**Test Objective**

The objective of this project is to automate the testing of the web application https://opensource-demo.orangehrmlive.com by simulating user actions and validating core functionalities. The goal is to ensure key modules like login, menu accessibility, user management, and logout are functioning as intended.

**Test Scenario**

Test Case 1 - Validate login functionality using multiple sets of credentials. 

Test Case 2 - Verify that the home URL is accessible.

Test Case 3 - Validate presence of login fields.

Test Case 4 - Verify visibility and clickability of main menu items after login.

Test Case 5- Create a new user and validate login.

Test Case 6- Validate presence of the newly created user in the admin user list.

Test Case 7- Verify "Forgot Password" link functionality. 

Test Case 8- Validate the presence of menu items under “My Info”.

Test Case 9- Assign leave to an employee and verify assignment.

Test Case 10 -Initiate a claim request and verify claim history.

**Project Overview**

This project is a test automation suite for an HR Management, developed using Data-driven approach, POM with Selenium. 
The main objective is to automate functional testing for various critical flows in an HR Management Application, 
such as adding new user, login, accessibility of menu items like Admin, Dashboard, Leave, MyInfo, Claims & etc, assigning leave and claim request flow and Logout. 
By using Data-driven approach, POM with Selenium, the test suite validates that application operates as intended and provides seamless experience for users.

**Table of Contents**
•	Features
•	Tech Stack
•	Setup and Installation
•	Running Tests
•	Project Structure

**Features**

•	Automation POM Framework: Base Page (reusable actions), Login Page, Admin Page, Leave Page, Myinfo Page, Dashboard Page and Claim Page are automated and reusable design. Locators are kept in separate file so that it will easy to maintain.

•	Data-driven approach: Test data is maintained in separate files(Excel, python). So it can be maintain easily. Used Excel based data driven approach to validate 
login functionality using multiple sets of credentials.

•	Cross Browser Validation: It supports Chrome, Firefox, Edge and Safari

•	Config driven Approach: Used 'config.ini' for browser settings and Credentials.

•	Logging and Reporting Support: We can get test result in HTML format and test logs file is also generated. 

To get allure report, use below commands

pytest --alluredir=allure-results

allure serve allure-results

allure generate allure-results -o allure-report --clean

**Tech Stack**

•	Programming Language: Python

•	Test Framework: pytest 

•	Automation Tool: Selenium Web Driver

•	Reporting: pytest-html, pytest—alluredir, test_log, 

•	Browser Compatibility: Chrome, Firefox, Edge and Safari

•	CI/CD Integration: GitHub Actions

**Setup and Installation**

To set up and run this project locally, follow these steps:

**Clone the Repository: **

**1.	Clone the Repository**

  	 git clone https://github.com/username/Project2_Orange_HRM.git cd Project2_Orange_HRM
  
**2. Create a Virtual Environment (optional but recommended) **

   python3 -m venv env source env/bin/activate # Linux/Mac env\Scripts\activate # Windows
   
**3. Install Dependencies: **
   
   pip install -r requirements.txt
   
**4. Set Up Environment Variables: **
    
    Create a .env file in the root directory to store sensitive information such as login credentials and URLs. Example:
    BASE_URL=https://example.com
    USER_EMAIL=test@example.com
    USER_PASSWORD=yourpassword


**Running Tests**

To execute tests, use the following commands:

1.	Run All Tests:

pytest

2.	Generate HTML Report:

pytest --html=report.html

3.	Run Tests by Marker (e.g., only "login" tests):

pytest -m login

4.	Headless Browser Execution:

You can set up tests to run in headless mode by configuring the config.ini file or directly in your test script.

**Project Structure**  



