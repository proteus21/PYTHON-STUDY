#----------------------------------------------------------
# premie korporacyjne oparte na zlecenie zysku. Gdy zyski (I) jest mniejsza lub równa $ 100,000, bonus 10% mogą być wymienione, kiedy zyski przekraczające 10 milionów mniej niż 20 milionów, około 10 mln mniej niż prowizja 10% wyższa niż 100.000 juanów część kakaowego prowizji o 7,5%, kiedy między 200.000 do 400.000, ponad 20 milionów części mogą być o 5% prowizji, gdy między 400.000 do 600.000 wyższa niż części 400.000 juanów, można odliczyć odsetek w wysokości 3% a gdy od 600 tysięcy do 1 miliona, odcinek ponad 60 milionów juanów, można odliczyć odsetek 1,5% wyższa niż 100 mln, ponad 1 milion juanów część 1% prowizji od wejścia klawiatury zysku miesiącu, należy zasięgnąć Wszystkich premie wypłacane?
# corporate bonuses based on profit order. When profits (I) is less than or equal to $100,000, bonus 10% can be mentioned, when profits exceeding 10 million less than 20 million, about 10 million less than 10% commission higher than 100,000 yuan part of the cocoa commission of 7.5%, when between 200,000 to 400,000, more than 20 million parts can be about 5% commission, when between 400. 000 to 600,000 higher than 400,000 yuan parts, you can deduct a percentage of 3% and when between 600,000 to 1 million, section more than 60 million yuan, you can deduct a percentage of 1.5% higher than 100 million, more than 1 million yuan part of 1% commission on the entry of the keyboard profit a month, should be consulted All bonuses paid?
#-----------------------------------------------------------
# Solution
Translated with www.DeepL.com/Translator (free version)
from pip._vendor.distlib.compat import raw_input

zyski= [100000, 200000, 400000, 600000, 1000000, 0]
procent= [0.01, 0.075, 0.05, 0.005, 0.003, 0.0015 ]
r=0
premia= raw_input("Expecting value;")


for r in range(0, 6):
    if premia > zyski(r):
        r+= (premia-zyski(r)-procent(r))
        print(premia-zyski(r) * procent(r))
        r= zyski(r)
print(r)
