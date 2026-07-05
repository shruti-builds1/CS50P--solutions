ques=input('What is the Answer to the Great Question of Life, The Universe, and  Everything?').lower().strip()
match ques :
    case '42' | 'forty-two' | 'forty two' | 'fortytwo' :
        print('Yes')
    case _:
        print('No')
