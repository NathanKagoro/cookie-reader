import argparse

#Reads the cookie log file and returns a dict with the date as the key and another dict as the value.
#The inner dict has the cookie as the key and the count as the value.
#Future implementation could make the values of the inner dict a list of timestamps instead of a count.
def read_cookie_log(file_path):
    days = {}

    with open(file_path, "r") as cookies_file:
        cookies = cookies_file.readlines()

        for cookie in cookies[1:]:
            cookie = cookie.strip().split(",")
            current_date = cookie[1].split("T")[0]
            current_time = cookie[1].split("T")[1] # Not used in the current implementation, but can be used in the future

            if current_date not in days:
                days[current_date] = {}

            if cookie[0] not in days[current_date]:
                days[current_date][cookie[0]] = 0

            days[current_date][cookie[0]] += 1

    return days

#Counts the number of occurrences of each cookie for the specified date and prints the most active cookie(s). 
def get_most_active_cookies(file_path, date):
    days = read_cookie_log(file_path)

    if date in days:
        max_count = max(days[date].values())
        most_active_cookies = [cookie for cookie, count in days[date].items() if count == max_count]
        return most_active_cookies

    else:
        return []

# This script takes a log of cookies and a date and returns the most active cookie(s) for that date.
if __name__ == "__main__":
    #Processeces command line arguments for the file path and date
    parser = argparse.ArgumentParser(
        description="Takes a a log of cookies and a date and returns the most active cookie(s) for that date"
    )

    parser.add_argument(
        "-f", "--file", metavar="file", type=str,
        help="The file path to the cookie log", required=True
    )

    parser.add_argument(
        "-d", "--date", metavar="date", type=str,
        help="The date for which to find the most active cookie(s) in YYYY-MM-DD format", required=True
    )

    args = parser.parse_args()
    days = read_cookie_log(args.file)

    result = get_most_active_cookies(args.file, args.date)
    if result:
        for cookie in result:
            print(cookie)
    else:
        print("No data for the specified date.")

    
