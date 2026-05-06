# AccuKnox QA Trainee Assignment

## Overview

This repository contains solutions for both problem statements of the QA Trainee assessment.

---

# Problem Statement 1: User Management (Manual + Automation)

# What is covered

* Login with valid and invalid credentials
* Navigate to Admin module
* Add a new user
* Search the created user
* Edit user details
* Delete the user
* Validate all actions

# Automation Details

* Tool: Playwright with Python
* Framework: Pytest
* Script: `test_user_management.py`

# How to Run

```bash
pip install playwright pytest
python -m playwright install
python -m pytest -s test_user_management.py
```

---

### Bug Found (Manual Testing)

* Record count inconsistency after using reset/search filters in Admin → User Management

---

## Problem Statement 2: Python Scripts

### 1. System Health Monitoring (`system_health.py`)

* Checks CPU usage
* Checks memory usage
* Checks disk usage
* Prints alert if threshold is exceeded

### 2. Application Health Checker (`app_health_check.py`)

* Sends request to a given URL
* Checks HTTP status code
* Prints whether application is UP or DOWN

---

## How to Run (Problem 2)

Install dependencies:

```bash
pip install psutil requests
```

Run scripts:

```bash
python system_health.py
python app_health_check.py
```

---

## Repository Structure

```text
test_user_management.py
system_health.py
app_health_check.py
README.md
```

---

## Author
Dhruv Attrey
