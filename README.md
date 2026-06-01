# Password Strength Analyzer

A Python-based cybersecurity tool that evaluates password security using multiple security metrics such as character diversity, entropy calculation, common password detection, sequential pattern analysis, and brute-force crack time estimation.

The application helps users understand how secure their passwords are and provides recommendations to improve password strength.

---

## Features

### Password Analysis
- Password Length Check
- Uppercase Letter Detection
- Lowercase Letter Detection
- Number Detection
- Special Character Detection

### Advanced Security Checks
- Common Password Detection
- Sequential Pattern Detection
- Repeated Character Detection
- Character Diversity Analysis

### Security Metrics
- Password Strength Score
- Weak / Medium / Strong Classification
- Entropy Calculation
- Brute-Force Crack Time Estimation

### Recommendations Engine
- Password Improvement Suggestions
- Security Warnings
- Best Practice Guidance

---

## Project Structure

Password-Strength-Analyzer/

│
├── analyzer.py
├── main.py
├── common_passwords.txt
├── requirements.txt
└── README.md

---

## Technologies Used

- Python 3
- Math Module
- String Module
- File Handling
- Set Data Structures

---

## Cybersecurity Concepts Demonstrated

### Authentication Security

Understanding password security principles and strong password creation.

### Dictionary Attacks

Detecting passwords that appear in a database of commonly used passwords.

### Brute Force Attacks

Estimating how long an attacker would take to crack a password through exhaustive guessing.

### Password Entropy

Measuring password randomness using information theory concepts.

### Pattern Analysis

Identifying predictable password patterns such as:

- 123456
- abcdef
- qwerty
- repeated characters

---

## How It Works

User Inputs Password
          ↓
Character Analysis
          ↓
Common Password Check
          ↓
Sequential Pattern Detection
          ↓
Repeated Character Detection
          ↓
Character Diversity Analysis
          ↓
Entropy Calculation
          ↓
Crack Time Estimation
          ↓
Strength Scoring
          ↓
Recommendations Generation
          ↓
Security Report Displayed

---

## Scoring Criteria

| Parameter | Points |
|------------|----------|
| Length ≥ 8 | +1 |
| Length ≥ 12 | +1 |
| Uppercase Letter | +1 |
| Lowercase Letter | +1 |
| Number | +1 |
| Special Character | +1 |
| Full Character Diversity | +1 |
| Repeated Characters | -1 |
| Sequential Patterns | -1 |

---

## Strength Classification

| Score | Rating |
|---------|----------|
| 0 - 2 | Weak |
| 3 - 5 | Medium |
| 6+ | Strong |

---

## Example Output

==================================================
PASSWORD ANALYSIS REPORT
==================================================

Length               : 15
Uppercase Letters    : True
Lowercase Letters    : True
Numbers              : True
Special Characters   : True

Character Diversity  : 4/4

Entropy              : 98.23 bits
Estimated Crack Time : 35000 years

Score                : 7
Strength Rating      : Strong

Recommendations:
- Excellent password. No recommendations.

---

## Installation

Clone the repository:

git clone https://github.com/yourusername/password-strength-analyzer.git

Move into the project directory:

cd password-strength-analyzer

Run the application:

python main.py

---

## Future Improvements

- Tkinter GUI
- Dark Theme Interface
- Password Generator
- Password Breach Detection
- PDF Report Generation
- Password History Analysis
- Real-Time Strength Meter

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Python Programming
- Secure Coding Practices
- Password Security Principles
- Information Theory (Entropy)
- Brute Force Resistance Analysis
- Cybersecurity Fundamentals
- Software Design and Modular Development

---

## Author

Akshitha Reddy

B.Tech Computer Science (Cybersecurity)

Cybersecurity Enthusiast | SOC | Digital Forensics | Network Security