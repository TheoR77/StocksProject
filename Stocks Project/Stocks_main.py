import math
import random

import pandas as pd
from time import *
import numpy as np
from math import *



## Stocks randomization and generation ##
go = input("Create random stocks dataframe? (y or n)  ")
while go == "y":
    def_stocks = int(input("Write the number of stocks: "))

    yes_or_no = [0, 1]
    consonants = ["d", "r", "t", "n", "m", "g", "v", "b", "k", "x", "z", "w", "l", "s"]
    vowels = ["a", "e", "u", "i", "y", "a", "i", "e", "u"]
    first = ["D", "R", "W", "Q", "E", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "K", "V", "N", "M"]
    sector = ["Games", "Healthcare", "Logistics", "Energy", "Biotechnology",
              "Technology", "Industrials", "Financials", "Mining"]
    analisis = ["Sell", "Underperform", "Hold", "Hold", "Buy", "Strong Buy"]

    i = 1
    names_list = []
    while i <= def_stocks:  # creating the stocks names
        wordformation = random.choice(first) + ""
        lessismore = random.randint(1, 4)
        if lessismore == 1:
            rr = random.randint(0, 3)
        else:
            rr = 1
        hh = 0
        while hh <= rr:
            c1 = random.choice(consonants)
            c2 = random.choice(vowels)
            plus = c2 + c1
            hh = hh + 1
            wordformation = wordformation + plus
        c3 = random.choice(yes_or_no)
        if c3 == 1:
            wordformation = wordformation + random.choice(vowels)
        else:
            wordformation = wordformation
        # print(wordformation)
        i = i + 1
        names_list.append(wordformation)

    i = 1
    sector_list = []
    while i <= def_stocks:
        b = random.choice(sector)
        i = i + 1
        sector_list.append(b)

    i = 1
    marketcap_list = []
    while i <= def_stocks:
        luck = random.randint(1, 100)
        if luck >= 64:
            b = random.randint(1, 200) * 10
        else:
            b = random.randint(5, 40) * 3
        g1 = "USD " + str(b)
        i = i + 1
        marketcap_list.append(g1)

    i = 1
    price_list = []
    while i <= def_stocks:
        luck = random.randint(1, 10)
        if luck >= 7:
            b = random.randint(121, 320)
        else:
            b = random.randint(10, 100)
        t = random.randint(10, 99)
        t = str(t)
        g1 = str(b) + "." + t
        i = i + 1
        price_list.append(g1)

    i = 1
    analisis_list = []
    while i <= def_stocks:
        b = random.choice(analisis)
        i = i + 1
        analisis_list.append(b)

    i = 0
    PE_list = []
    while i <= (def_stocks - 1):
        meh = price_list[i]
        meh = float(meh)
        meh = math.floor(meh)
        luck = random.randint(1, 7)
        if sector_list[i] == "Financials" or "Logistics":
            if luck >= 4:
                earnings1 = random.randint(2, meh)
            else:
                earnings1 = random.randint(1, 3)
        else:
            if luck >= 6:
                earnings1 = random.randint(2, meh)
            else:
                earnings1 = random.randint(1, 3)
        meh2 = meh / earnings1
        meh2 = ((meh2 + 22) / 2) + random.randint(0, 5)
        meh2 = round(meh2, 2)
        i = i + 1
        PE_list.append(meh2)

    i = 0
    PEG_list = []
    while i <= (def_stocks - 1):
        if sector_list[i] == "Financials":
            growth = random.randint(1, 5000)
            growth = growth * 0.0001
        else:
            growth = random.randint(900, 6000)
            growth = growth * 0.0001
        meh = PE_list[i]
        meh = float(meh)
        meh = meh / growth
        meh = round(meh, 2)
        i = i + 1
        PEG_list.append(meh)

    i = 0
    fiftytwoweekhigandlow_list = []
    while i <= (def_stocks - 1):
        # Low
        luck = random.randint(1, 10)
        if luck >= 6:
            denominator = 3
        else:
            denominator = 1.3
        meh = price_list[i]
        meh = float(meh)
        nah = meh / denominator
        week_l = meh - round(nah)
        week_l = round(week_l, 2)

        # High
        luck = random.randint(1, 10)
        if luck >= 6:
            denominator = 1.1
        else:
            denominator = 4
        meh = price_list[i]
        meh = float(meh)
        nah = meh / denominator
        week_h = meh + round(nah)
        week_h = round(week_h, 2)

        week_hl = str(week_l) + " - " + str(week_h)
        i = i + 1
        fiftytwoweekhigandlow_list.append(week_hl)

    datadict1 = {'Names': names_list, 'Price': price_list, 'P/E ratio': PE_list, 'PEG ratio': PEG_list,
                 'Market Cap (B)': marketcap_list, 'Analysts Review': analisis_list,
                 '52-Week Range': fiftytwoweekhigandlow_list, 'Sector': sector_list} # 8 columns

    df1 = pd.DataFrame(data=datadict1)
    print(df1)
    while go == "y":
        filter_question = input("Create new random stocks dataframe? (y or n)  ")
        if filter_question == "y":
            break
        if filter_question == "n":
            filter_exit_question = input("Would you like to save this Dataframe as an csv file and a xlsx file? (y or n)  ")
            if filter_exit_question == "y":
                df1.to_csv('Random Stocks Df.csv', index=True)
                df_excel = pd.read_csv('Random Stocks Df.csv')
                exc_reader = pd.ExcelWriter("Random Stocks Df.xlsx")
                df_excel.to_excel(exc_reader, index=True)
                exc_reader.save()

                print("File saved.\n")
                exit()
            if filter_exit_question == "n":
                print("\n\nok\n\n")
                exit()
            if filter_exit_question != "n" and "y":
                print("Invalid answer. Digit 'y' or 'n' \n\n")
        if filter_question != "n"and"y":
            print("Invalid answer. Digit 'y' or 'n' \n\n")
    else:
        print("Invalid answer. Digit 'y' or 'n' \n\n")
else:
    exit()
