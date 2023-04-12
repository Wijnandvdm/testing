import requests
import csv
from bs4 import BeautifulSoup
import envfile

login_url = 'https://www.voedingswaardetabel.nl/leden/login/'

# Define the email address and password parameters
email = envfile.EMAIL
password = envfile.PASSWORD

# Define the request parameters
params = {
    'ctl00$cphMain$txtLgnName': email,
    'ctl00$cphMain$txtLgnPassw': password,
    'ctl00$cphMain$btnLogin': 'Aanmelden'
}

response = requests.post(login_url, data=params)

# Check if the login was successful
if '<div id="popup_message">Inloggen mislukt!</div>' in response.content.decode():
    print('Login failed')
else:
    print('Login successful')

# print(response.content)

# html_part = response.content
# Write the HTML content to a file
with open('login_html.html', 'wb') as f:
    f.write(response.content)


# session = requests.Session()

# login_url = 'https://www.voedingswaardetabel.nl/leden/login/'

# login_data = {
#     'username': envfile.EMAIL,
#     'password': "wakkawakka"
# }

# session.post(login_url, data=login_data)

# response = requests.post(login_url, data=login_data)

# if response.status_code == 200:
#     print('Login successful!')
# else:
#     print('Login failed. Status code:', response.status_code)

# url = 'https://www.voedingswaardetabel.nl/mineralen/'
# response_data = requests.get(url)
# html = response_data.text

# # Write the HTML content to a file
# with open('html_content.html', 'w', encoding='utf-8') as f:
#     f.write(html)
