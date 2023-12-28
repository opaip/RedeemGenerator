#redeem generator
import random,os
ch = ('1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
DB_PATH="" # addr of the database folder . example D:\data\
REDEEMS_DIR=""  #exact location of  the files to sava data .  example: ...\data\redeem
USERS_CREDIT_PATH="" # example : ./data/cash/


#credit : The amount of the credit user wants to use
#func : 1 means creat redeem code , 2 means use a redeem code
def generate(credit=None,func=1,username:str=None,redeem=None):
    if func == 1:
        #removing credit from user account
        with open(USERS_CREDIT_PATH+f'{username}.txt','r') as data:
            cash = int(data.readline())
            data.close()
        if cash >= int(credit):
            with open(USERS_CREDIT_PATH+f'{username}.txt','w') as data:
                left = cash - int(credit)
                data.write(str(left))
                data.close()
            #generating the code and save it
            code = ''
            while True:
                for i in range(15):
                    code += random.choice(ch)
                redeems = os.listdir(REDEEMS_DIR)
                if code not in redeems:
                    with open(REDEEMS_DIR+f'{code}.txt','w') as data:
                        data.write(f'{str(int(credit))}')
                        data.close()
                    print("OK",code)
                else:
                    code = code+"2"
                    with open(REDEEMS_DIR+f'{code}.txt','w') as data:
                        data.write(f'{str(int(credit))}')
                        data.close()
                    print("OK",code)
        else:
            print("not enough credit")
    if func == 2:
        #check the user credit
        with open(USERS_CREDIT_PATH+f'{username}.txt','r') as data:
            cash=int(data.readline())
            data.close()
        #check the redeem credit 
        if os.path.isfile(REDEEMS_DIR+f'{redeem}.txt'):
            with open(REDEEMS_DIR+f'{redeem}.txt','r') as data:
                amount = int(data.readline())
                data.close()
            #add redeem to user's credit
            ncash = cash + amount
            with open(USERS_CREDIT_PATH+f'{username}.txt','w') as data:
                data.write(str(ncash))
                data.close()
            #removig redeem from data 
            os.remove(REDEEMS_DIR+f'{redeem}.txt')
            print("OK")
        else: 
            print('redeem code is wrong')


        