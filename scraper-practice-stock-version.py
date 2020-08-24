import requests
from bs4 import BeautifulSoup

def scrape_url_fundamentals(ticker):
    yahooURL = 'https://finance.yahoo.com/quote/' + ticker + '/analysis?p=' + ticker
    guruURL = 'https://www.gurufocus.com/stock/' + ticker + '/summary'
    fvURL = 'https://www.finviz.com/quote.ashx?t=' + ticker.lower()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}

    try:
        yahooResp = requests.get(yahooURL)
        yahooResp.raise_for_status()
        guruResp = requests.get(guruURL)
        guruResp.raise_for_status()
        fvResp = requests.get(fvURL, headers=headers)
        fvResp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        print('\nPlease refresh the page and try again')
        exit()

    yahooSoup = BeautifulSoup(yahooResp.text, 'html.parser')
    guruSoup = BeautifulSoup(guruResp.text, 'html.parser')
    fvSoup = BeautifulSoup(fvResp.text, 'html.parser')

    # growth in last 5 years and next 5 years
    growth_last5 = yahooSoup.find_all('tr')[-1].find_all('td')[1]
    growth_next5 = yahooSoup.find_all('tr')[-2].find_all('td')[1]

    # return on invested capital
    roic = guruSoup.find_all(class_='bar-divider')
    roic = [div.text[6:-1] for div in roic if 'ROIC' in div.text][0]

    # debt to equity ratio
    # (note: didn't quite finish this one, as it grabs the whole table. need to go in a little further
    # to get the specific <td>)
    dte = fvSoup.find_all('table')[8]

    print(growth_last5.text)
    print(growth_next5.text)
    print(roic)
    print(dte.text)


scrape_url_fundamentals('MSFT')
