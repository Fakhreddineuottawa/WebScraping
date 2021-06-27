from bs4 import BeautifulSoup
import requests
import time


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for company in jobs:
        company_name = company.find('h3', class_="joblist-comp-name").text
        print(company_name)
if __name__ == '__main__' :
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds. ')
        time.sleep(time_wait * 60)