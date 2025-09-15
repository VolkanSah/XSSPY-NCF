# XSSPY (NCF Version)
###### rebuilt 2019-2400 (v.2705.2024) | Datasheet last updated: Thu, 28 Aug 2025 07:33:16 +0000.
if forked, check orginalfor updates: [Source](https://github.com/VolkanSah/XSSPY-NCF/)

![XSS Py Rebuillt](xsspy-jpg.jpg)

> [!WARNING]
> This repository is intended for educational purposes and to help improve security. Use these tools and techniques responsibly and ethically. Always remember to follow the law and consider the impact of your actions.


I was inspired by the work of [faizann24](https://github.com/faizann24/XssPy) and use my script below with my own tools/scrappers. It appears that his account is no longer active, but Thanks bro for your smart idea.


## Introduction
XSSPY - NCF - Version is an advanced tool designed to help security researchers and ethical hackers identify potential Cross-Site Scripting (XSS) vulnerabilities in web applications. This updated version automates the process of testing for XSS vulnerabilities by analyzing web pages and submitting payloads to check for any possible security issues. With the ability to read payloads from an external file, it allows for a more flexible and comprehensive testing approach.

## Key Features
- **Automated XSS Testing**: Automatically scans web applications for XSS vulnerabilities with minimal user intervention.
- **Dynamic Payload Loading**: Load the latest XSS payloads from an external text file, making it easy to update and expand the list of payloads.
- **Comprehensive Scanning**: Perform in-depth scans of web applications, including form submissions and URL parameters.
- **Verbose Logging**: Enhanced logging capabilities to track the scanning process and results in detail.

## Installation
To install the necessary dependencies for XSSPY_2024, use the following commands:

```
pip install mechanize argparse logging
```

## Usage
To use XSSPY_2024, simply run the script with the target URL. Ensure you have your payloads file ready (e.g., `payloads.txt`).

### Basic Scan
```
python xsspy.py -u example.com
```

### Example: Comprehensive Scan with Verbose Output
```
python xsspy.py -u example.com -e -v
```

### Example: Using Custom Cookies
```
python xsspy.py -u example.com -c "cookie1=value1" "cookie2=value2"
```

## Advanced Features

### Loading Payloads from a File
You can load XSS payloads from an external file where each line contains a single payload. This allows for easy updating and testing with the latest payloads. Here is an example of how to read payloads from a file in the script:

```
def read_payloads_from_file(file_path):
    with open(file_path, 'r') as file:
        payloads = [line.strip() for line in file]
    return payloads

# Usage
payload_file_path = 'payloads.txt'
payloads = read_payloads_from_file(payload_file_path)
```

### Enhancing Logging
Modify the logging level to capture more detailed information during the scan by using the `-v` flag for verbose logging.

## Benefits
- **Time-Saving**: Automates the tedious process of manually testing for XSS vulnerabilities, allowing you to focus on other critical tasks.
- **Up-to-Date Testing**: Easily update your payloads with the latest techniques from trusted sources like the [PortSwigger XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet).
- **Comprehensive Coverage**: Capable of testing a wide range of payloads against multiple endpoints in a web application, increasing the chances of finding potential vulnerabilities.

## Example Scenario
Imagine you need to test a large web application for XSS vulnerabilities. Instead of manually injecting payloads into each form and URL parameter, you can use XSSPY_2024 to automate this process. Load the latest payloads from a trusted source, start the script, and let it run while you take a break. When you return, you will have a detailed log of potential XSS vulnerabilities found in the application.

## Changes from Original Code
This version of XSSPY_2024 has several improvements and updates compared to the original script by Faizan Ahmad:

1. **Python 3 Compatibility**:
   - Updated to work with Python 3, including changes from `httplib` to `http.client` and `urlparse` to `urllib.parse`.
   - `print` statements updated to `print()` function.

2. **Improved Payloads**:
   - Added more comprehensive and modern XSS payloads to increase the detection of XSS vulnerabilities.
   - Payloads can now be dynamically loaded from an external file, while the original inline payloads are still available but commented out.

3. **Error Handling and Logging**:
   - Enhanced error handling to ensure the script does not crash on encountering errors.
   - Improved logging with more detailed and clearer messages.

4. **Code Consistency and Readability**:
   - Improved the formatting and structure of the code for better readability and maintenance.
   - Used f-strings for more readable string formatting.

5. **HTTP/HTTPS Detection**:
   - Improved logic for detecting and handling HTTP/HTTPS compatibility.

6. **General Improvements**:
   - Included static methods in the `color` class.
   - Optimized the `testPayload` function.
7. **Compatibility**
   - works with PoisonIvory (Nemesis)

These changes aim to make the script more robust, user-friendly, and effective in detecting XSS vulnerabilities.

## Security Warning
> [!WARNING]
> **Important Note:** This information is provided for educational purposes and to help improve security. Use these tools and techniques responsibly and ethically. Unauthorized access to, or exploitation of, systems and data is illegal and unethical. Please be aware of the potential risks and consequences associated with using the knowledge and tools shared in this document. Ensure that you have proper authorization before attempting to test or exploit any systems.

### Thank you for your support!
- If you appreciate my work, please consider [becoming a 'Sponsor'](https://github.com/sponsors/volkansah), giving a :star: to my projects, or following me.

### Credits
- [VolkanSah on Github](https://github.com/volkansah)
- [Developer Site](https://volkansah.github.io)

### License
This project is licensed under the MIT - see the [LICENSE](LICENSE) file for details.

