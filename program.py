#!./env/bin/python

import requests
from datetime import date


my_name = 'Ivanov Maxim'
url = "https://baconipsum.com/api/?type=meat-and-filler"

word_to_find = 'pancetta'

today = date.today()

# dd.mm.YY
today_date = today.strftime("%d.%m.%Y")

data = requests.get(url).json()[:5][::-1]


with open('result.txt', 'w') as fp:
    fp.write(my_name + '\n')
    fp.write(today_date + '\n\n')

    count = 0;

    for d in data:
        fp.write(d + '\n')

        if word_to_find in d.lower():
            count += 1

    fp.write('\n\n')
    fp.write('Paragraphs containing %s found %s times\n' % (word_to_find, count))
