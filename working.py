import re
# from datetime import datetime
def main():
    print(convert(input("Hours: ")))

def convert(s):
    # try :

        exp=r'(?P<hour1>[1-9]|[1][0-2])(?P<min1>\:[0-5][0-9])?\s(?P<period1>AM|PM)\sto\s(?P<hour2>[1-9]|[1][0-2])(?P<min2>\:[0-5][0-9])?\s(?P<period2>AM|PM)'
        if matches:=re.search(exp,s.strip()) :
            if matches.group(2) is None :
                if matches.group(1)=='12' and matches.group(3)=='AM' :
                    time1='00'+':00'
                elif 1<=int(matches.group(1))<=11 and matches.group(3)=='AM' :
                    if 1<=int(matches.group(1))<=9 :
                        time1='0'+matches.group(1)+':00'
                    else :
                        time1=matches.group(1)+':00'
                elif matches.group(1)=='12' and matches.group(3)=='PM' :
                    time1=matches.group(1)+':00'
                elif 1<=int(matches.group(1))<=11 and matches.group(3)=='PM' :
                    time1=str(int(matches.group(1))+12)+':00'

            elif matches.group(2).startswith(':') :
                if matches.group(1)=='12' and matches.group(3)=='AM' :
                    time1='00'+matches.group(2)
                elif 1<=int(matches.group(1))<=11 and matches.group(3)=='AM' :
                    if 1<=int(matches.group(1))<=9 :
                        time1='0'+matches.group(1)+matches.group(2)
                    else :
                        time1=matches.group(1)+matches.group(2)
                elif matches.group(1)=='12' and matches.group(3)=='PM' :
                    time1=matches.group(1)+matches.group(2)
                elif 1<=int(matches.group(1))<=11 and matches.group(3)=='PM' :
                    time1=str(int(matches.group(1))+12)+matches.group(2)


            if matches.group(5) is None :
                if matches.group(4)=='12' and matches.group(6)=='AM' :
                    time2='00'+':00'
                elif 1<=int(matches.group(4))<=11 and matches.group(6)=='AM' :
                    if 1<=int(matches.group(4))<=9 :
                        time2='0'+matches.group(4)+':00'
                    else :
                        time2=matches.group(4)+':00'
                elif matches.group(4)=='12' and matches.group(6)=='PM' :
                    time2=matches.group(4)+':00'
                elif 1<=int(matches.group(4))<=11 and matches.group(6)=='PM' :
                    time2=str(int(matches.group(4))+12)+':00'

            elif matches.group(5).startswith(':') :
                if matches.group(4)=='12' and matches.group(6)=='AM' :
                    time2='00'+matches.group(5)
                elif 1<=int(matches.group(4))<=11 and matches.group(6)=='AM' :
                    if 1<=int(matches.group(4))<=9 :
                        time2='0'+matches.group(4)+matches.group(5)
                    else :
                        time2=matches.group(4)+matches.group(5)
                elif matches.group(4)=='12' and matches.group(6)=='PM' :
                    time2=matches.group(4)+matches.group(5)
                elif 1<=int(matches.group(4))<=11 and matches.group(6)=='PM' :
                    time2=str(int(matches.group(4))+12)+matches.group(5)
            # print(matches.group('hour1'))
            # print(matches.groupdict())
            # {'hour1': '9', 'min1': None, 'period1': 'AM', 'hour2': '5', 'min2': None, 'period2': 'PM'}
            # d=matches.groupdict()
            # t1=datetime.strptime(f"{d['hour1']}{d['min1'] or ':00'} {d['period1']}", "%I:%M %p")
            # time1=t1.strftime('%H:%M')
            # t2=datetime.strptime(f"{d['hour2']}{d['min2'] or ':00'} {d['period2']}", "%I:%M %p")
            # time2=t2.strftime('%H:%M')
            return f'{time1} to {time2}'

        else :
            raise ValueError('Either invalid format or timings')
    # except ValueError :
    #     return f'Either invalid format or timings'

if __name__ == "__main__":
    main()
