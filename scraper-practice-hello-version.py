import requests
from bs4 import BeautifulSoup

def scrape_url():
    hello_url = 'https://www.merriam-webster.com/dictionary/hello'

    try:
        hello_resp = requests.get(hello_url)
        hello_resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        print('\nPlease try refreshing and rerunning the tool.')
        exit()
    
    hello_soup = BeautifulSoup(hello_resp.text, 'html.parser').text

    hello_arr = hello_soup.split()
    h_dict = {}

    # keep track of how many times we see a specific word in the HTML
    for t in hello_arr:
        try:
            h_dict[t] += 1
        except KeyError: # need this in case the text hasn't been added to the dictionary yet
            h_dict[t] = 1
    
    print(h_dict)
    

scrape_url()