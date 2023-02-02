#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 13:56:30 2023

@author: jamesboot
"""

# Write a function that, given an integer returns a string that represents the number in written form

# This function currently works for all numbers from 1 - 9999

def intToChar(num):
    
    numsList = list(str(num))
    
    NumDict1 = {
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine'}

    NumDict2 = {
        1:'ten',
        2:'twenty',
        3:'thirty',
        4:'fourty',
        5:'fifty',
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety'}

    NumDict3 = {
        1:'one hundred',
        2:'two hundred',
        3:'three hundred',
        4:'four hundred',
        5:'five hundred',
        6:'six hundred',
        7:'seven hundred',
        8:'eight hundred',
        9:'nine hundred'}
    
    NumDict4 = {
        1:'one thousand',
        2:'two thousand',
        3:'three thousand',
        4:'four thousand',
        5:'five thousand',
        6:'six thousand',
        7:'seven thousand',
        8:'eight thousand',
        9:'nine thousand'}
    
    NumDict5 = {
        10:'ten thousand',
        11:'eleven thousand',
        12:'twelve thousand',
        13:'thirteen thousand',
        14:'fourteen thousand',
        15:'fifteen thousand',
        16:'sixteen thousand',
        17:'seventeen thousand',
        18:'eighteen thousand',
        19:'nineteen thousand',
        
        20:'twenty thousand',
        21:'twenty one thousand',
        22:'twenty two thousand',
        23:'twenty three thousand',
        24:'twenty four thousand',
        25:'twenty five thousand',
        26:'twenty six thousand',
        27:'twenty seven thousand',
        28:'twenty eight thousand',
        29:'twenty nine thousand',

        30:'thirty thousand',
        31:'thirty one thousand',
        32:'thirty two thousand',
        33:'thirty three thousand',
        34:'thirty four thousand',
        35:'thirty five thousand',
        36:'thirty six thousand',
        37:'thirty seven thousand',
        38:'thirty eight thousand',
        39:'thirty nine thousand',

        40:'fourty thousand',
        41:'fourty one thousand',
        42:'fourty two thousand',
        43:'fourty three thousand',
        44:'fourty four thousand',
        45:'fourty five thousand',
        46:'fourty six thousand',
        47:'fourty seven thousand',
        48:'fourty eight thousand',
        49:'fourty nine thousand',

        50:'fifty thousand',
        51:'fifty one thousand',
        52:'fifty two thousand',
        53:'fifty three thousand',
        54:'fifty four thousand',
        55:'fifty five thousand',
        56:'fifty six thousand',
        57:'fifty seven thousand',
        58:'fifty eight thousand',
        59:'fifty nine thousand',

        60:'sixty thousand',
        61:'sixty one thousand',
        62:'sixty two thousand',
        63:'sixty three thousand',
        64:'sixty four thousand',
        65:'sixty five thousand',
        66:'sixty six thousand',
        67:'sixty seven thousand',
        68:'sixty eight thousand',
        69:'sixty nine thousand',

        70:'seven thousand',
        71:'seven one thousand',
        72:'seven two thousand',
        73:'seven three thousand',
        74:'seven four thousand',
        75:'seven five thousand',
        76:'seven six thousand',
        77:'seven seven thousand',
        78:'seven eight thousand',
        79:'seven nine thousand',

        80:'eighty thousand',
        81:'eighty one thousand',
        82:'eighty two thousand',
        83:'eighty three thousand',
        84:'eighty four thousand',
        85:'eighty five thousand',
        86:'eighty six thousand',
        87:'eighty seven thousand',
        88:'eighty eight thousand',
        89:'eighty nine thousand',

        90:'ninety thousand',
        91:'ninety one thousand',
        92:'ninety two thousand',
        93:'ninety three thousand',
        94:'ninety four thousand',
        95:'ninety five thousand',
        96:'ninety six thousand',
        97:'ninety seven thousand',
        98:'ninety eight thousand',
        99:'ninety nine thousand'
        }
    
    if len(numsList) == 1:
        
        num1 = int(numsList[-1])
        
        return print(
            NumDict1[num1]
            )
    
    if len(numsList) == 2:
        
        num1 = int(numsList[-1])
        num2 = int(numsList[-2])
        
        if num1 == 0:
            return print(
                NumDict2[num2]
                )
        
        else:
            return print(
                NumDict2[num2],
                NumDict1[num1]
                )
    
    if len(numsList) == 3:
        
        num1 = int(numsList[-1])
        num2 = int(numsList[-2])
        num3 = int(numsList[-3])
        
        if num1 == 0 and num2 == 0:
            return print(
                NumDict3[num3]
                )
        
        elif num1 == 0 and num2 != 0:
            return print(
                NumDict3[num3],
                'and',
                NumDict2[num2]
                )
        
        elif num1 != 0 and num2 == 0:
            return print(
                NumDict3[num3],
                'and',
                NumDict1[num1]
                )
        
        else:
            return print(
                NumDict3[num3],
                'and',
                NumDict2[num2],
                NumDict1[num1]
                )
    
    if len(numsList) == 4:
        
        num1 = int(numsList[-1])
        num2 = int(numsList[-2])
        num3 = int(numsList[-3])
        num4 = int(numsList[-4])
        
        if num1 == 0 and num2 == 0 and num3 == 0:
            return print(
                NumDict4[num4]
                )
        
        elif num1 == 0 and num2 != 0 and num3 != 0:
            return print(
                NumDict4[num4],
                NumDict3[num3],
                'and',
                NumDict2[num2]
                )
        
        elif num1 != 0 and num2 == 0 and num3 != 0:
            return print(
                NumDict4[num4],
                NumDict3[num3],
                'and',
                NumDict1[num1]
                )
        
        elif num1 != 0 and num2 != 0 and num3 == 0:
            return print(
                NumDict4[num4],
                'and',
                NumDict2[num2],
                NumDict1[num1]
                )
        
        elif num1 == 0 and num2 == 0 and num3 != 0:
            return print(
                NumDict4[num4],
                NumDict3[num3]
                )
        
        elif num1 == 0 and num2 != 0 and num3 == 0:
            return print(
                NumDict4[num4],
                'and',
                NumDict2[num2],
                )
        
        elif num1 != 0 and num2 == 0 and num3 == 0:
            return print(
                NumDict4[num4],
                'and',
                NumDict1[num1],
                )
        
        else:
            return print(
                NumDict4[num4],
                NumDict3[num3],
                'and',
                NumDict2[num2],
                NumDict1[num1]
                )
    
    # if len(numsList) == 5:
        
    #     num1 = int(numsList[-1])
    #     num2 = int(numsList[-2])
    #     num3 = int(numsList[-3])
    #     num5 = int(numsList[-5] + numsList[-4])
        
    #     if num1 == 0:
    #         return print(
    #             NumDict5[num5],
    #             NumDict3[num3],
    #             'and',
    #             NumDict2[num2]
    #             )
        
    #     else:
    #         return print(
    #             NumDict5[num5],
    #             NumDict3[num3],
    #             'and',
    #             NumDict2[num2],
    #             NumDict1[num1]
    #             )

intToChar(307)




