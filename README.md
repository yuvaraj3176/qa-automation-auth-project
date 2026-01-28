# QA Automation – Authentication Module (Selenium + Pytest)

## 📌 Project Overview
This project is a **QA Automation framework** developed to automate the testing of a web application’s **Authentication module** using **Selenium WebDriver and Pytest**.

It covers:
- Login functionality
- Forgot Password workflow
- Data-driven testing using CSV
- Screenshot capture on test failure
- Logging and HTML reporting

This project simulates **real-world enterprise QA automation practices** and is suitable for **HCL / MNC QA Automation roles**.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Automation Tool:** Selenium WebDriver
- **Test Framework:** Pytest
- **Browser:** Google Chrome
- **Data Source:** CSV
- **Reporting:** Pytest HTML Report
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

qa_automation_auth_project/
│
├── pages/
│ ├── base_page.py
│ ├── login_page.py
│ └── forgot_password_page.py
│
├── tests/
│ ├── test_login.py
│ └── test_forgot_password.py
│
├── testdata/
│ └── login_data.csv
│
├── local_app/
│ └── login.html
│
├── logs/
│ └── execution.log
│
├── reports/
│ ├── test_report.html
│ └── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


---

## 🔑 Features Implemented

- ✅ Automated Login with valid & invalid credentials
- ✅ Forgot Password workflow automation
- ✅ Page Object Model (POM)
- ✅ Data-Driven Testing using CSV
- ✅ Explicit waits for synchronization
- ✅ Screenshot capture on test failure
- ✅ Logging for execution tracking
- ✅ HTML test execution report
- ✅ Smoke & Regression test markers
- ✅ Localhost login page testing

---

## 🌐 Local Login Application (Test Environment)

A simple **local login page** is created using HTML & JavaScript and hosted on **localhost**.

### ▶ Start Local Server
bash
cd local_app
python -m http.server 8000
🌍 Open Login Page
http://localhost:8000/login.html
📊 Test Data (CSV)
testdata/login_data.csv

username,password,expected
yuvaraj,12345,success
yuvaraj,wrongpass,Invalid username or password
wronguser,12345,Invalid username or password
▶️ How to Run Tests
🔹 Run All Tests
pytest
🔹 Run Smoke Tests
pytest -m smoke
🔹 Run Regression Tests
pytest -m regression
📸 Screenshots on Failure
<img width="1920" height="1080" alt="Screenshot 2026-01-22 121310" src="https://github.com/user-attachments/assets/f0be9414-6c63-40ee-879f-5850343cdf81" />
<img width="1920" height="1080" alt="Screenshot 2026-01-22 121325" src="https://github.com/user-attachments/assets/09d06daf-9b29-415d-8a05-ec8179d075ca" />
<img width="1920" height="1080" alt="Screenshot 2026-01-22 121347" src="https://github.com/user-attachments/assets/8d7a8e38-6615-4a25-878a-ea5d2b10088e" />

Screenshots are automatically captured only on test failure

Stored in:

reports/screenshots/
📑 HTML Report
After execution, open:

reports/test_report.html
🧠 Key QA Concepts Demonstrated
Manual testing before automation

Data-driven testing

Assertion-based validation

Failure debugging using screenshots

Enterprise-level test organization

Test categorization (Smoke & Regression)







