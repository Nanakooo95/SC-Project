"""
File: webcrawler.py
Name: Yi Lin Yang
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        # find target data location
        tags = soup.find_all('table', {'class': 't-stripe'})        # huge string

        for tag in tags:
            # extract text in target location
            raw_name_number_data = tag.tbody.text
            lst = raw_name_number_data.split('\n')      # split string to list of line
            total_male_num = 0
            total_female_num = 0
            for ele in lst:
                new_lst = ele.split(' ')
                if len(new_lst) == 4:           # ele that contains male/female name and number
                    male_num = ''
                    for i in range(len(new_lst[1])):
                        if new_lst[1][i].isdigit():     # to eliminate the comma in number
                            male_num += new_lst[1][i]
                    total_male_num += int(male_num)
                    female_num = ''
                    for i in range(len(new_lst[3])):
                        if new_lst[3][i].isdigit():     # to eliminate the comma in number
                            female_num += new_lst[3][i]
                    total_female_num += int(female_num)
            print('Male number:', total_male_num)
            print('Female number:', total_female_num)


if __name__ == '__main__':
    main()
