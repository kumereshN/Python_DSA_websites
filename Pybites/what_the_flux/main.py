XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)
import pandas as pd


def calculate_flux(XYZ: str) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """
    df = pd.read_csv(XYZ, delimiter=',')
    df['dollar_flux'] = df['12/31/20'] - df['12/31/19']
    df['percent_flux'] = round(df['dollar_flux'] / df['12/31/19'],2)
    return list(df.apply(tuple, axis=1))


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    flagged_lines = []
    
    for (*_, dollar_flux, percent_flux) in xyz:
        if abs(dollar_flux) > THRESHOLDS[0] and abs(percent_flux) > THRESHOLDS[1]:
            flagged_lines.append(xyz)

    return flagged_lines


print(calculate_flux(XYZ))
# print(identify_flux(calculate_flux(XYZ)))