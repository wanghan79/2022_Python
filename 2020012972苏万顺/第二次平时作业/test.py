"""
Author: WanshunSu 2020012972
Purpose: Second python class homework in spring semester, 2022
Introduction:
           It and 'funcsPack' package as a whole.
           You can run the .py file directly to test the package named 'funcsPack'.
           If you want to know more about the internal implementation of the package named 'funcsPack',
           please go to check 'funcs.py' and 'Query_the_weather.py' in the package named 'funcsPack'.
Created:2022/4/30
"""
import funcsPack.funcs as funcs
import funcsPack.somefuncs as somefuncs
import funcsPack.Query_the_weather as qw
if __name__ == '__main__':
    '''
    This is the main function for testing the "funcpack" package. In this function, 
    you can calculate BMI, obtain a certain range of primes and query the weather 
    conditions of the city you want to query.
    
    The program needs independent input. The following is an input example:
    1.Read function body content through file:
    (1) Please enter the action to be performed according to the prompt(numbers 1-7):1
        (Note:In this function, you only need to enter 1 and no other content)
    2.Calculate BMI:
    (1) Please enter the action to be performed according to the prompt(numbers 1-7):2
    (2) Please enter height (m) and weight (kg) [separated by comma]:1.76,62
    3.Read file
    (1) Please enter the action to be performed according to the prompt(numbers 1-7):3
    (2) Please enter the file name you want to read:data.txt
        (Note: you must pay attention to the absolute path and relative path of 
        the file name to ensure that the program can find the file.)
    4.Generate random number:
    (1) Please enter the action to be performed according to the prompt(numbers 1-6):4
    (2) You need to give the random numbers or strings you want to generate in the form of a dictionary 
        in the data.txt or create a new file in this directory
    (3) There are examples in the data.txt for reference
    (4) Please enter the file name you want to read:data.txt
    5.Generate prime number:
    (1) Please enter the action to be performed according to the prompt(numbers 1-6):5
    (2) Please enter the range of primes you want to obtain [separated by comma](start,end):100,200
    6.Query the weather:
    (1) Please enter the action to be performed according to the prompt(numbers 1-6):6
    (2) Please enter the name of the city where you want to query the weather (press enter to exit):长春
    (3) Please enter the name of the city where you want to query the weather (press enter to exit):   
        (Note: when you do not want to query other cities, enter the Enter key here)
    7.exit:
    (1) Please enter the action to be performed according to the prompt(numbers 1-6):7
        (When you enter 6 here, the program will end)
    '''
    while True:
        option = funcs.get_option()
        if option == '1':
            print("You can read the function body written in the 'funcs.txt' file through this function")
            print('############################')
            print("The function body of the function name written in the 'funcs.txt' file is as follows:")
            func=somefuncs.txtFileReader("funcs.txt")
            def callOutsideFunc(funcName: str):
                for i in funcName:
                    eval(i)
            callOutsideFunc(func)
            print('############################')
        if option == '2':
            height, weight = eval(input("Please enter height (m) and weight (kg) [separated by comma]:"))
            bmi, nat, dom = funcs.CalculateBMI(height,weight)
            print('############################')
            print("BMI value:{0};BMI index:International indicator is '{1}',Domestic indicator is '{2}'.".format(bmi, nat, dom))
            print('############################')
        if option == '3':
            txt = input("Please enter the file name you want to read:")
            funcs.txtFileReader(txt)
        if option == '4':
            print("You need to give the random numbers or strings you want to generate in the form of a dictionary")
            print("in the data.txt or create a new file in this directory")
            print("There are examples in the data.txt for reference")
            filename = input("Please enter the file name you want to read:")
            funcs.apply(filename)
        if option == '5':
            start, end = eval(input("Please enter the range of primes you want to obtain [separated by comma](start,end):"))
            if(start >= end):
                print("The second number you entered should be greater than the first number!")
                continue
            elif(start < 0 or end <= 0):
                print("The first number you enter should be greater than or equal to 0, and the second number should be greater than 0!")
                continue
            else:
                print('############################')
                print("The primes in this range are:")
                h = funcs.getPrimeNumber(start, end)
                print('\nThe total is %d' % h)
                print('############################')
        if option == '6':
            cityName = funcs.GetCity()
            print('############################')
            for c in qw.WeatherIterable(cityName):
                print(c)
            print('############################')
        if option == '7':
            break