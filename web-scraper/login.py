import requests
import envfile

# Replace url(s), email and password with your actual credentials
login_url = envfile.LOGIN_URL
url=envfile.URL
email = envfile.EMAIL
password = envfile.PASSWORD

# Data to be sent in the request body
data = {
    'ctl00$cphMain$txtLgnName': email,
    'ctl00$cphMain$txtLgnPassw': password
}

# Send POST request to the login form
response = requests.options(login_url, data=data)
html = response.text
print(html)
# Check the response status code
if response.status_code == 200:
    print('Login successful babyyyyyy!')
else:
    print('Login failed :(')

