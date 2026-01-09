# Password-Strength-Checker-Python-
This project is a Python-based Password Strength Checker that evaluates the strength of a user’s password based on length and character composition. The program analyses the password and categorises it as Weak, Moderate, or Strong using clearly defined security rules.
This project demonstrates input validation, string processing, and algorithmic decision-making in Python.

How the Program Works
The user is prompted to enter a password.

The program checks:
Total password length
Number of uppercase letters
Number of lowercase letters
Number of digits
Number of special characters

Based on these criteria, the password is classified into one of three strength levels.

Strength Evaluation Criteria:
Weak
Password length is less than 8 characters
OR
Does not meet the minimum complexity requirements

Moderate
At least:
1 uppercase letter
1 lowercase letter
1 digit

Strong
At least:
3 uppercase letters
3 lowercase letters
2 digits
1 special character

Features:
Real-time password evaluation
Character-by-character analysis
Clear strength categorisation
Efficient looping and condition checks
Beginner-friendly but security-focused logic

HOW TO RUN THE PROGRAM:
Prerequisites
Python 3.x installed

Steps
python main.py

Concepts Demonstrated:
Functions and type hints
String methods (isupper(), islower(), isdigit())
Looping through strings
Conditional logic
Basic cybersecurity principles

Why This Matters:
Strong passwords are a fundamental part of cybersecurity.
This project reflects an understanding of:
Password policy enforcement
Defensive programming
Secure authentication practices

Possible Enhancements
Password feedback suggestions
Entropy-based strength calculation
GUI or web interface
Password breach detection
Hashing and secure storage simulation

License
This project is open-source and available under the MIT License.

Author
Hanya Mursaleen
Aspiring Cybersecurity Engineer | Python Developer
