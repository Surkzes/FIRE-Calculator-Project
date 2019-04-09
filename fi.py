#python 2.7.15

#FIRE Calculator Project
#Created by Jonathon Heddings

import os

#program to calculate Goal Investment for a set withdrawal amount
#at a specific withrdrawal rate

def calc_goalto_FI():
    print "Input the amount you want to earn a year after retirement. "
    A = int(raw_input())

    print "Input expected SWR in Decimal. (0.04 is 4%)"
    SWR = float(raw_input())

    investment_sum = A/SWR

    print "You would need to save $",investment_sum, " to be able to withrdrawal $",A, "a year. At a ", SWR,"SWR."


#program to calculate how many years
#it will take to reach a set Amount with
#a set income and a set market return percent (without including taxes).

def years_till_FI():
#accept input and declare variables.
    print "Input goal Investment"
    A = int(raw_input())

    print "Input savings per Year"
    S = int(raw_input())

    print "Input compounding rate. (As a Decimal, 0.04 for 4%)"
    r = float(raw_input())
    r = 1 + r

    print "Input starting Balance"
    i = int(raw_input())

    t = 0
#calculate time in years.
    while (i < A):
	       i = (i * r) + S
	       t =t+1
    print "It will take", t, "years to earn","$", A," with a savings per year of $",S,"and a yearly return rate of", (r - 1)*100,"%."

def main():

#loop until user decides to quit
    quit = 1
    while (quit):
        print "Choose an Option"
        print "(1) Calculate Years till FI at a Set Income and Set Rate of Return. (Taxes not Calculated)"
        print "(2) Calculate the Investment Goal for a Set Withdrawal Amount per Year at a Set SWR (Taxes not Calculated)"
        print "(0) Quit"
        option = int(raw_input())

        os.system('clear')
        if(option == 1):
            years_till_FI()

        if(option == 2):
            calc_goalto_FI()

        if(option == 0):
            quit = 0

        for i in range(3):
            print " "

main()
