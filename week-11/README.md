# Week 11 
# Logging, Timestamps & Data Analysis

This project focuses on building real-world Python programs that track user activity, log data with timestamps, and analyze stored information using external libraries.

Two practical systems were developed: an Expense Tracker with data analysis and an Action Logger for tracking user activities.

---

## Project Overview

This week includes two main deliverables:

### 1. Expense Tracker with Logging & Analysis
A program that allows users to record expenses along with timestamps and analyze the data using the pandas library.

### 2. Action Logger with Environment Export
A script that logs user actions with timestamps into a text file and demonstrates environment management using `pip freeze`.


##  Features

### Expense Tracker
- Add expenses with timestamps
- Store data in a CSV file
- Analyze total spending
- Calculate average expenses
- Handle missing file errors

### Action Logger
- Log user actions with timestamps
- Save logs into a text file
- Continuously track user activity until exit

### Environment Export
- Generate a `requirements.txt` file
- Capture all project dependencies using `pip freeze`


## Concepts Applied

- Python `datetime` module for timestamps
- File handling (CSV and text files)
- Logging user actions
- Data analysis using pandas
- Exception handling
- Environment management


## How to Run

Run each script using Python:

Navigate to the `week-11` directory then run:

python expense_tracker.py
or
python action_logger.py

## Install Dependencies

python -m pip install pandas

## Export Environment

pip freeze > requirements.txt

## Learning Objective

The goal of this project is to simulate real-world systems that:

- Track user activity
- Store structured data
- Analyze data for insights
- Manage project dependencies

## Author 

Confidence Amarachi Nkeonye