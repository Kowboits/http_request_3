import requests
from pprint import pprint as pp
import time
from datetime import date

def unix_date(date):
    unixtime = int(time.mktime(date.timetuple()))
    return unixtime

def get_list_info(tag,from_date, to_date):
    questions =[]
    params = {'fromdate':unix_date(from_date),'order':'desc','todate':unix_date(to_date),'sort':'activity','tagged':tag,'site':'stackoverflow'}
    result = requests.get("https://api.stackexchange.com/2.3/questions", params=params)
    data = result.json()['items']
    for i in range(len(data)):
        questions.append(data[i]['title'])
    return questions

if __name__ == '__main__':
    from_date = date(2022, 3, 28)
    to_date = date(2022, 3, 31)
    pp(get_list_info('python',from_date, to_date))