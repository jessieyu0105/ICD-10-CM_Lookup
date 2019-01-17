'''
read data to dict
'''
de_dict = {}
try:
    f = open('data/icd10cm.txt','r')
    for line in f:
        temp = line.strip("\n").split("\t")
        de_dict[temp[0]] = temp[1]
except Exception:
    print("read file error ")
finally:
    f.close()
while True:
    select_func = input(r"Please enter a number to select a function(1:query by code 2:query by descption 3: exit ): ")
    #print(type(select_func))
    if select_func == '1':
        user_input = input("Please enter a code(eg: C44.02):")
        try:
            item = 0
            for key,value in de_dict.items():
                if user_input in key:
                    print(key,value)
                    item +=1
            if item == 0:
                print("{0} not in file".format(user_input))
        except Exception:
            print("Error")
    elif select_func == '2':
        query_str = input("Please enter a descption(eg: Squamous):")
        item = 0
        for key,value in de_dict.items():
            if query_str in value:
                print(key,value)
                item +=1
        if item == 0:
            print("no result")
    elif select_func == '3':
            print("Finish")
            break
    else:
        print("Invalid string")
