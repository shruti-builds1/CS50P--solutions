import requests
import sys
try:
    if len(sys.argv)==1 :
        sys.exit('Missing command-line argument')

    else :
        response=requests.get('https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&names=Bitcoin&symbols=btc')
        data=response.json()
        num=data['bitcoin']
        ans=float(sys.argv[1])*float(num['usd'])
        sys.exit(f'{ans:,.4f}')

except ValueError :
    sys.exit('Command-line argument is not a number')
except requests.RequestException:
    sys.exit('Request Error')
