# Nebula Exploiter - Usage Guide

## Installation
To install and run Nebula Exploiter, follow these steps:

1. Open your Linux terminal.
2. Clone the repository:
```
git clone https://github.com/sudoxabit/nebula-strike.git
```
3. Navigate to the project directory:
```
cd nebula-strike
```
4. Install the required dependencies:
```
pip3 install -r requirements.txt
```
5. Run the tool:
```
python3 NebulaStrike.py
```

## Usage Instructions

### Option 1 (Under Development)
This feature is still in development and should be skipped.

### Option 2 - WordPress Login Checker
To use this feature, follow these steps:
1. Create a `.txt` file containing your target list in the following format:
```
https://www.example.com/wp-login.php#admin@pass
```
> **Note:** In this format, `admin` will be used as the username and `pass` as the password.

2. Run the tool and select Option 2. The tool will attempt to log in using the provided credentials.

### Option 3 - WordPress Registration Exploit
This feature checks if registration is enabled on WordPress sites and attempts to register a user using your chosen username and email.

1. Modify the code by replacing `nrnr551a@gmail.com` with your own email address for registration purposes.
2. Create a `.txt` file containing a list of WordPress site URLs in the following format:
```
https://www.example.com/
```
3. Run the tool and select Option 3 to begin checking the sites for registration vulnerabilities.

### Option 4 - SQL Injection (SQLi) Detector
This feature tests URLs with parameters for potential SQL injection vulnerabilities.

1. Create a `.txt` file containing target URLs with parameters in the following format:
```
https://www.example.com/page.php?id=12
```
2. Run the tool and select Option 4 to start testing.
3. If a URL is flagged as vulnerable, you can use `sqlmap` for further exploitation:
```
sqlmap -u "URL" --dbs --tables --columns --dump --batch
```

## Important Notes
- Ensure your target lists follow the correct format for each option to avoid errors.
- Use this tool responsibly and only for educational or authorized testing purposes.

Thank you for using Nebula Exploiter!

