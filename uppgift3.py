#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# uppg3.py
# Roger Sundh
# 2015-02-09
"""
Skriv ett program som läser in ett antal resistansvärden och sedan
beräknar den totala resistansen vid parallellkoppling av de inmatade värdena. 
Börja med att fråga efter antalet resistorer.

Pseudokod
==========
Fråga efter resistans
Fråga efter spänningen
Beräkna effekten
Presentera resultatet

"""

#Main
if __name__ == "__main__" : #Run directly or imported as a module ?

    #Get input values
    resistance = input(u"Ange resistansen i ohm : ")
    voltage = input(u"Ange spänningen i volt : ")

    #Check (for debug)
    #print("Resistansen = {0}, Spänningen = {1}".format(resistance, voltage))

    #Calc power
    try:
        power = (float(voltage) ** 2) / float(resistance)

        #Present result
        print(u"Effekten = {0} W".format(power))
    except:
        print("Det gick inte att utföra beräkningen")












