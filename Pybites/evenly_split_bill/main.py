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

    CENTS = Decimal('.01')
    
    sub_total = Decimal(item_total[1:])
    add_taxes = Decimal(tax_rate[:-1]) / 100
    add_tip = Decimal(tip[:-1]) / 100

    tax = (sub_total * add_taxes).quantize(CENTS)
    tip = ((sub_total + tax) * add_tip).quantize(CENTS)
    gt = (sub_total + tax + tip).quantize(CENTS)

    owned_each = (gt / people).quantize(CENTS, rounding=ROUND_DOWN)
    splits = [owned_each] * people
    overage = (gt - (owned_each * people))

    if overage:
        for i in range(int(overage * 100)):
            splits[i] += CENTS

    return (f"${gt}", splits)

    

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