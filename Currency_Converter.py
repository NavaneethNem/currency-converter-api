import requests as rq
from dotenv import load_dotenv
load_dotenv()
import os
url="https://api.currencylayer.com/convert"
api_key=os.environ.get("CURRENCYLAYER_API_KEY")

def convert_currency(source,target,amount):
    parameters={
    "access_key":api_key,
    "from":source,
    "to":target,
    "amount":amount
    }
    request=rq.get(url,params=parameters)
    status_code=request.status_code
    data=request.json()
    if status_code==200 and data['success']:
        result=data['result']
        return result
    else:
        print("Error occured. Status-code: ",status_code)
        print(data['error']['info'])
        return None
source=input("Enter the source currency (e.g., USD, EUR, INR): ").upper()
target=input("Enter the target currency (e.g., USD, EUR, INR): ").upper()
if len(source)!=3 or len(target)!=3:
    print("Invalid currency code!")
    exit()
if source==target:
    print("Source and target currencies cannot be the same!")
    exit()
amount=input("Enter the amount to convert: ")
try:
    amount=float(amount)
    if amount<=0:
        print("Amount must be greater than zero!")
        exit()
except ValueError:
    print("Invalid amount!")
    exit()
result=convert_currency(source,target,amount)
if result is not None:
    print(f"{amount} {source} = {result} {target}")
