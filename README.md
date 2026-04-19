# Login Test Automation Framework

This project demonstrates a basic end-to-end QA automation workflow using Azure Test Plans, Selenium, Python, Pytest, and GitHub.

## Project Overview
The goal of this project was to test and automate the login functionality of the sample website below:

https://the-internet.herokuapp.com/login

## Scope
The following login scenarios were covered:
- Valid login
- Invalid login

## Tools & Technologies
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML Report
- Azure DevOps Test Plans
- GitHub
- VS Code

## Framework Design
This project uses:
- Page Object Model (POM)
- Pytest fixtures
- WebDriver Manager

## Project Structure
```text
selenium-azure-qa-framework/
│
├── tests/
│   └── test_login.py
├── pages/
│   └── login_page.py
├── reports/
├── screenshots/
├── requirements.txt
├── README.md
└── .gitignore

## Azure Pipeline
Azure Pipeline YAML has been configured for automated execution of the Selenium Pytest suite. Pipeline execution is set up to:
- install dependencies
- run tests
- publish JUnit test results
- publish HTML reports

Note: Pipeline run depends on hosted agent parallelism being enabled in the Azure DevOps organization.