Selenium Login Validation Script

This project demonstrates how to automate login validation using Selenium in Python. It checks multiple sets of credentials against the [OrangeHRM demo login page](https://opensource-demo.orangehrmlive.com/) and reports which logins passed or failed.

📌 Features

- Automates login testing with Selenium WebDriver
- Validates multiple username/password combinations
- Uses functions for cleaner and reusable code (`login()`, `logout()`)
- Prints summary of passed and failed attempts
- Demonstrates usage of XPath, CSS selectors, and implicit waits
- Opens and closes the browser programmatically

🕹 How It Works

The script:
1. Launches a Chrome browser using Selenium
2. Loops through a list of credential pairs
3. Inputs each username and password on the login form
4. Checks if login was successful by verifying the URL
5. Logs out if login is successful, or goes back to login page if not
6. Displays a summary of passed and failed logins

🖥️ Technologies Used

- Python
- Selenium webdriver
- ChromeDriver

