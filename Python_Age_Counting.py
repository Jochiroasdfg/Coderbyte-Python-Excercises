import requests
import numpy as np
import pandas as pd

response = requests.get('https://coderbyte.com/api/challenges/json/age-counting')

res_data = response.json()["data"].split(",")
#print(res_data)

count = 0
for data in res_data:
    split_data = data.split("=")
    #print(split_data)
    if split_data[0].strip() == "age" and int(split_data[1]) >= 50:
        count += 1
print(count)