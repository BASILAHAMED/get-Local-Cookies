import requests

# Create a new session with a custom cookie jar
session = requests.session()

# Create an HTTP GET request
url = "https://www.google.com/"
response = session.get(url)
print("Executing request", response.request.method, response.request.url)

# Print the response status line
print("Response:", response.status_code)

# Get the cookies from the response object
cookies = response.cookies

# Iterate through the cookies and print them
for cookie in cookies:
    print("Local cookie:", cookie)

