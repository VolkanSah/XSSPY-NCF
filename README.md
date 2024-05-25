# XSSPY_2024
###### Rebuilded 2023/24 (Version 4)
> [!WARNING]
>  Please note that this repository is for educational purposes and to help improve security. Use these tools and techniques responsibly and ethically. Always remember to follow the law and consider the impact of your actions-


I was inspired by the work of [faizann24](https://github.com/faizann24/XssPy) and use my script below with my own tools/scrappers. It appears that his account is no longer active, but Thanks bro for your smart idea.

```
____  ___              __________        
\   \/  /  ______ _____\______   \___.__.
 \     /  /  ___//  ___/|     ___<   |  |
 /     \  \___ \ \___ \ |    |    \___  |
/___/\  \/____  >____  >|____|    / ____|
      \/     \/     \/           \/     
XssPy 2024 - Finding XSS made much easier
Copyright S.Volkan Sah & Faizan Ahmad till yet :D
```

I won't provide a complete walkthrough to prevent misuse of this information by malicious individuals. Instead, I encourage ethical hackers to learn how to integrate this script with their existing Python tools to enhance their security testing capabilities.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Advanced Features](#advanced-features)
5. [Changes from Original Code](#changes-from-original-code)
6. [Security Warning](#security-warning)

## Introduction
XssPy is a tool designed to help security researchers and ethical hackers identify potential Cross-Site Scripting (XSS) vulnerabilities in web applications. It automates the process of testing for XSS vulnerabilities by analyzing web pages and submitting payloads to check for any possible security issues.

## Installation
To install the necessary dependencies for XssPy, use the following commands:

```shell
pip install mechanize argparse logging
```

## Usage
To use XssPy, simply run the script with the target URL:

```shell
python xsspy.py -u http://example.com
```

### Example: Comprehensive Scan with Verbose Output
```shell
python xsspy.py -u http://example.com -e -v
```

### Example: Using Custom Cookies
```shell
python xsspy.py -u http://example.com -c "cookie1=value1" "cookie2=value2"
```

## Advanced Features
### Adding New Payloads
You can extend the script by adding new payloads to the `payloads` list to test for more XSS vulnerabilities.

### Enhancing Logging
Modify the logging level to capture more detailed information during the scan.

## Changes from Original Code
This version of XssPy has several improvements and updates compared to the original script by Faizan Ahmad:

1. **Python 3 Compatibility**:
   - Updated to work with Python 3, including changes from `httplib` to `http.client` and `urlparse` to `urllib.parse`.
   - `print` statements updated to `print()` function.

2. **Improved Payloads**:
   - Added more comprehensive and modern XSS payloads to increase the detection of XSS vulnerabilities.

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

These changes aim to make the script more robust, user-friendly, and effective in detecting XSS vulnerabilities.

> [!WARNING]
> **Important Note:** This information is provided for educational purposes and to help improve security. Use these tools and techniques responsibly and ethically. Unauthorized access to, or exploitation of, systems and data is illegal and unethical. Please be aware of the potential risks and consequences associated with using the knowledge and tools shared in this document. Ensure that you have proper authorization before attempting to test or exploit any systems.


### Thank you for your support!
- If you appreciate my work, please consider [becoming a 'Sponsor'](https://github.com/sponsors/volkansah), giving a :star: to my projects, or following me. 
### Credits
- [VolkanSah on Github](https://github.com/volkansah)
- [Developer Site](https://volkansah.github.io)

### License
This project is licensed under the MIT - see the [LICENSE](LICENSE) file for details.
