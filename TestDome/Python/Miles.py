class MilesToKmConverter:
    def get_miles_to_km_factor(self):
        return 1.609

    def miles_to_km(self, miles):
        return self.get_miles_to_km_factor() * miles

class NauticalMilesToKmConverter(MilesToKmConverter):
    def get_miles_to_km_factor(self):
        return 1.852

    def printFactors(self):
        print(self.get_miles_to_km_factor(), super().get_miles_to_km_factor())

#print(MilesToKmConverter.printFactors())
#print(MilesToKmConverter().miles_to_km(1))
print(NauticalMilesToKmConverter().printFactors())
