import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.voedingswaardetabel.nl/mineralen/'
response = requests.get(url)
html = response.text

# Write the HTML content to a file
with open('html_content.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Find the div with id 'ctl00_cphMain_ltvNutrition_ctrl0_rowHeaderWords0'
header_div = soup.find('div', {'id': 'ctl00_cphMain_ltvNutrition_ctrl0_rowHeaderWords0'})

# Find all the span elements inside the header_div and extract their text
headers = [span.text for span in header_div.find_all('span')]

# Assuming the headers are stored in a list called headers
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

## UP UNTIL HERE IT WORKS TO EXTRACT THE HEADERS!

# create a list with all the values
values = []
for span in soup.find_all('span'):
    values.append(span.text)

print(values) # Output: ['1,0', '220,0', '0,0']

## UP UNTIL HERE THIS WORKS TO EXTRACT THE VALUES!

values = [val for val in values if val.replace(',', '').isdigit()]

# Open output.csv in append mode and write the values
with open('output.csv', mode='a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(values)

## UP UNTIL HERE IT WORKS TO PUT THE VALUES INTO A CSV!

# with open('output.csv', 'a', newline='') as file:
#     writer = csv.writer(file)
#     row = []
#     for i, val in enumerate(values):
#         if val.replace('.', '').isdigit():
#             row.append(val)
#         if (i+1) % 14 == 0:
#             writer.writerow(row)
#             row = []
#         elif i == len(values)-1:
#             writer.writerow(row)

## THIS DOESNT WORK QUITE YET