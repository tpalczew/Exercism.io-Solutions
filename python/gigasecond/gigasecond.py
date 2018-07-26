import datetime
def add_gigasecond(birth_date):
    # Calculate the moment when someone has lived for 10^9 seconds.
    # A gigasecond is 10^9 (1,000,000,000) seconds. 
    return (birth_date + datetime.timedelta(seconds=int(1000000000)))

