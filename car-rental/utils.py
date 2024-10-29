import datetime

def no_of_days_between_two_dates(start, end):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    return (end_date - start_date).days
