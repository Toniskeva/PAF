print(5.0-4.935)
#Očekuje se 0.065,a dobije se 0.06500000000000039 jer se zbog binarnog zapisa brojeva u memoriji brojevi zaokružuju
print(0.1+0.2+0.3)
#Ne dobije se točno 0.6 zbog zaokruživanja na određenoj decimali
#Da se bi se dobila točna rješenja treba importati modul za decimalne brojeve
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.2')+Decimal('0.3'))