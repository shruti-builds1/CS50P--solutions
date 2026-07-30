import sys
import csv

if len(sys.argv)<3 :
    sys.exit('Too few command-line arguments')

elif len(sys.argv)>3 :
    sys.exit('Too many command-line arguments')

else :
    try :
        students=[]
        with open(sys.argv[1],'r') as f :
            data1=csv.DictReader(f)
            for row in data1 :
                # print(len(row),row[0])
                last,first = row['name'].split(',')
                # print(len(l))
                student={'first': first.strip() , 'last': last.strip() , 'house': row['house']}
                students.append(student)

        with open(sys.argv[2],'w') as file :
            data2=csv.DictWriter(file, fieldnames=['first','last','house'])
            data2.writerow({'first': 'first' , 'last' : 'last' , 'house' : 'house'})
            for k in students :
                data2.writerow(k)

    except FileNotFoundError :
        sys.exit('Could not read '+sys.argv[1])