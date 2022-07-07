import requests
from datetime import datetime


print ("hello world");
print ("testing cicd bni");

response = requests.get("https://www.google.com")

waktu = datetime.now()

with open ("tempResponse/"+str(waktu)+".txt","w") as f:
    f.write(response.text)