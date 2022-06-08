num = float(input("Enter The Value in INR"))
cur = input("Enter the currency you want to convert to...USD for US Dollar...Eu for Euro...CND for Canadian Dollar...Swiss for Swiss Frank...AUD for Australian Dollar...Jy for Japanese Yen...SA for South African Rand...Ren for Renminbi...Hk for Hong Kong Dollar...SD for Singaporean Dollar...Rus for Russian Rubble")
cur = cur.upper()
if cur == "USD":
    num = num * 0.013
    print("Your Value in USD is: ",num," USD")
elif cur == "EU":
    num = num * 0.012 
    print("Your Value in Euro is: ",num,' Euro')
elif cur == "CND":
    num = num * 0.016 
    print("Your value in Canadian dollars is: ",num,' Canadian Dollar')
elif cur == "SWISS":
    num = num * 0.013 
    print("Your value in Swiss Francs is: ",num,' Swiss Francs')
elif cur == "AUD":
    num = num * 0.018 
    print("Your value in Australian Dollars is: ",num,' Australian Dollars')
elif cur == "JY":
    num = num * 1.71
    print("Your value in Japanese Yen is: ",num,' Japanese Yen')
elif cur == "SA":
    num = num * 0.20
    print("Your value in South African rand is: ",num,' South African Rand')
elif cur == "REN":
    num = num * 0.086
    print("Your value in Renminbi is: ",num,' Renminbi')
elif cur == "HK":
    num = num * 0.10
    print("Your value in Honk Kong Dollars is: ",num,' Honk Kong Dollars')
elif cur == "SD":
    num = num * 0.018
    print("Your value in Singaporean Dollar is: ",num,' Singaporean Dollars')
elif cur == "RUS":
    num = num * 0.79
    print("Your value in Russian Rubles is: ",num,' Russian Ruble')
else:
    print("Your Key_word for the currencies is wrong rerun the program and input correctly!")
