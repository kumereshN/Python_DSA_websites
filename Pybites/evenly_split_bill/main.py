import re
import math
from decimal import *
def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    getcontext().prec = 28
    getcontext().rounding = ROUND_DOWN

    evenly_split_lst = []

    def evenly_split(remaining, n_people, evenly_split_per_person):
        if n_people == 1:
            evenly_split_lst.append(remaining)
            return
        evenly_split_lst.append(evenly_split_per_person)
        remaining = remaining - evenly_split_per_person
        evenly_split(remaining, n_people-1, evenly_split_per_person)


    item_total = float(item_total.split('$')[1])
    tax_rate = 1.00 + (float(tax_rate.split('%')[0]) / 100)
    tip = 1.00 + (float(tip.split('%')[0]) / 100)
    
    grand_total = Decimal(item_total * tax_rate * tip).quantize(Decimal('.001'))
    acutal_split_per_person = Decimal(grand_total / people).quantize(Decimal('.001'))

    evenly_split(grand_total, people, acutal_split_per_person)

    
    total_sum = f'${str(sum(evenly_split_lst))}'
    
    return (total_sum, evenly_split_lst)
    

c1 = ('$8.68', '4.75%', '10%', 3)
c2 = ('$8.44', '6.75%', '11%', 3)
c3 = ('$9.99', '3.25%', '10%', 2) # Facing rounding issues
c4 = ('$186.70', '6.75%', '18%', 6)
c5 = ('$191.57', '6.75%', '15%', 6) # Facing rounding issues
c6 = ('$0.00', '0%', '0%', 1)
c7 = ('$100.03', '0%', '0%', 4)
c8 = ('$141.86', '2%', '18%', 9) # Facing rounding issues
c9 = ('$16.99', '10%', '20%', 1)
c10= ('$16.99', '10%', '20%', 2)
c11= ('$16.99', '10%', '20%', 3)
c12= ('$16.99', '10%', '20%', 4)

print(check_split(*c3))

# Notes
# 