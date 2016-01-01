months = {'jan': 'January',
          'feb': 'February',
          'mar': 'March',
          'apr': 'April',
          'may': 'May',
          'jun': 'June',
          'jul': 'July',
          'aug': 'August',
          'sep': 'September',
          'oct': 'October',
          'nov': 'November',
          'dec': 'December'}

import cgi

def valid_month(month):
    return months.get(month[:3].lower())


def valid_day(day):
    try:
        intDay = int(day)

    except:
        return None
    if intDay >= 1 and intDay <= 31:
        return intDay


def valid_year(year):
    if year and year.isdigit():
        int_year = int(year)
        if int_year >= 1900 and int_year < 2020:
            return int_year


def escape_html(s):
    return cgi.escape(s, quote=True)
