class ClassWithBadProperty:
    def __init__(self):
        self.someAttribute = 'some initial value'

    @property
    def someAttribute(self):  # This is the "getter" method.
        # We forgot the _ underscore in `self._someAttribute here`, causing
        # us to use the property and call the getter method again:
        return self.someAttribute  # This calls the getter again!

    @someAttribute.setter
    def someAttribute(self, value):  # This is the "setter" method.
        self._someAttribute = value


obj = ClassWithBadProperty()
print(obj.someAttribute)  # Error because the getter calls the getter.
