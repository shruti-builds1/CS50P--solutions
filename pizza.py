import sys
from tabulate import tabulate
import csv

if len(sys.argv)<2 :
    sys.exit('Too few command-line arguments')

elif len(sys.argv)>2 :
    sys.exit('Too many command-line arguments')

else :
    if sys.argv[1].endswith('.csv') :
        try :
            with open(sys.argv[1] , 'r') as f :
                data=csv.DictReader(f)
# tabulate
                print(tabulate(data, headers="keys", tablefmt="grid",))

        except FileNotFoundError :
            sys.exit('File does not exist')

    else:
        sys.exit('Not a csv file')



