#Simple Random Password Generator
import random
import string
for i in range(1,20) :


        string1 = list(string.ascii_lowercase)
        string2 = list(string.ascii_uppercase)
        string3 = list(string.digits)
        new_list = list(string1 + string2 + string3)
        random.shuffle(new_list)
        #We Will Use set() So That There Will Be No Duplicates In The Password
        RandPassword = set()

        for i in range(1,15) :
                RandPassword.add(random.choice(new_list))
                if(len(RandPassword)>= 15) :
                 break;
        strRandomPassword = (','.join(RandPassword)).replace(',','')
        print(strRandomPassword)

