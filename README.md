# Cookie Reader

## Overview
This project provides a command-line tool to identify the most active cookie(s) for a given date from a log file.

The log file is expected to be in CSV format with the following structure:

cookie,timestamp

## Usage

Run the script using:

python main.py -f <file_path> -d <date>

Example:

python main.py -f test_cases/test1.csv -d 2018-12-09

## Output

The program prints the most active cookie(s) for the specified date to standard output.  
If multiple cookies share the highest frequency, each is printed on a new line.

## Assumptions

- Input file is sorted by timestamp.
- Date is in this format: (YYYY-MM-DD).
- The time is in the UTC timezone
- File fits into memory

## Test Cases

Test cases are provided in the `test_cases/` directory as CSV files.

Each file represents a different scenario, including:
- Standard usage
- Multiple most active cookies (ties)
- Edge cases such as no data for a given date
- Single entry inputs

### Running test cases manually

You can run any test case using the command line:

python main.py -f <file_path> -d <date>

Example:

python main.py -f test_cases/test1.csv -d 2018-12-09

The program will print the most active cookie(s) for that file and date.

### Automated tests

Automated tests are included using `pytest`. To run them:

python -m pytest

## Implementation Notes

- The solution goes through the log file and adds cookie counts for each date, storing them in a dictionary.
- Results are computed by identifying the maximum frequenc of occurence for the given date
