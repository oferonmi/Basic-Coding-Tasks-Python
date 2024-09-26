import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

DOC_URL = 'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'

def decodeMessage(gdoc_url):
    # get published document content
    response = requests.get(gdoc_url)
    doc_content =  response.content

    # parse table
    soup = BeautifulSoup(doc_content, 'html.parser')
    tables = soup.find_all('table')

    char_grid = []
    for table in tables:
        rows = []
        for row in table.find_all('tr'):
            cells = [cell.text.strip() for cell in row.find_all('td')]
            rows.append(cells)
        char_grid.append(rows)

    # oonvert data to suitable format
    data_arr = pd.DataFrame(char_grid).to_numpy()

    # display characters
    fig, ax = plt.subplots()

    # x_vals =[]
    # y_vals =[]

    # clear screen
    print("\033[2J]") #comment if matplotlib used

    for i in range(1,data_arr.shape[1]):
        char_data = data_arr[0][i]
        x = int(char_data[0])
        y = int(char_data[2])
        unicd_char = char_data[1]

        #  to print directly to terminal
        print(f"\033[{y};{x}H{unicd_char}") #comment if matplotlib prefered

        # Or display using matplotlib library
        # ax.text(x, y, unicd_char, ha='center', va='center')
        # x_vals.append(x)
        # y_vals.append(y)

    # ax.set_xlim(0, max(x_vals))
    # ax.set_ylim(0, max(y_vals))
    
    # plt.show()
  
def main():
    decodeMessage(DOC_URL)

if __name__ == "__main__":
    main()