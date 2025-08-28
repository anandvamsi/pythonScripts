# Python program to call url and get response using Requets module
- step1 :- Install requets module
```
pip3 install requets
```

- step 2 :- Execute below code
```bash
import requests
url = "https://9k.execute-api.us-west-2.amazonaws.com/dev?"
params = {"accountId":"5085"}  # query parameters
headers = {
   "x-api-key": "N2Ri8oXXXXXXXXXXXXXX4vtstDGXXXXf9ZPua"  # API key
}
response = requests.get(url, headers=headers, params=params)
print("Response Body:", response.text)
```
