import requests
import envfile

# Replace url(s), email and password with your actual credentials
login_url = envfile.LOGIN_URL
url=envfile.URL
email = envfile.EMAIL
password = "potatta"#envfile.PASSWORD

# Data to be sent in the request body
data = {
    'ctl00$cphMain$txtLgnName': email,
    'ctl00$cphMain$txtLgnPassw': password
}

def login_to_site():
    # Send POST request to the login form
    response = requests.options(login_url, data=data)

    # Check the response status code
    if response.status_code == 200:
        print('Login successful babyyyyyy!')
    else:
        print('Login failed :(')
    # # Check if the login was successful
    # if '<div id="popup_message">Inloggen mislukt!</div>' in response.content.decode():
    #     print('Login failed')
    # else:
    #     print('Login successful!')

login_to_site()