"""Write a Python script that extracts all email addresses from a given text using regular expressions.
HINT
The expression is as follows
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
Example Input:

pythonCopyEdittext = "Contact us at support@example.com or sales@example.org for assistance."
Expected Output:

cssCopyEdit['support@example.com', 'sales@example.org']"""
import re

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

pythonCopyEdittext = "Contact us at support@example.com or sales@example.org for assistance."

emails = re.findall(email_pattern, pythonCopyEdittext)

print(emails)


