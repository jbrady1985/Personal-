#Basic poker program for tracking bankroll

#libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def pokermanager():
    bankroll = float(input('What is your current Poker Bankroll? '))
    choice = 1
    while choice!='2':
        choice=input('Press 1 to enter a new poker event. Press 2 to exit: ')
        if choice =='2':
            break
        elif choice =='1':
            gametype = str(input('What type of poker are you playing? Press C for cash or T for tournaments: '))
            if gametype=='C':
                winorloss = str(input('Did you win today? Enter Y or N: '))
                if winorloss=='Y':
                    cashwin = float(input('How much did you make? '))
                    bankroll=bankroll+cashwin
                elif winorloss=='N':
                    cashloss = float(input('How much did you lose? '))
                    bankroll=bankroll-cashloss
                else:
                    print('Invalid Entry!')
                    break 
            elif gametype=='T':
                entry=float(input('What did the tournament cost to enter? '))
                bullets = int(input('How many times did you enter? '))
                cashornot=str(input('Did you cash? Enter Y or N '))
                if cashornot=='Y':
                    tournamentwin=float(input('How much did you cash for? '))
                    bankroll=bankroll-(bullets*entry)+tournamentwin
                elif cashornot=='N':
                    bankroll=bankroll-(bullets*entry)
                else:
                    print('Invalid Entry!')
                    break 
            else:
                print('Invalid Entry!')
                continue
        else:
            print('Invalid Entry!')
            continue
    print('Your new bankroll is: $',bankroll)
        

pokermanager()                 
                 

