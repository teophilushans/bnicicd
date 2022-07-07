import requests

print ("hello world");
print ("testing cicd bni");

response = requests.get("https://www.google.com")

print(response.text)