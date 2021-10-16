import collections.abc
import operator


class WizCoinException(Exception):
    """The wizcoin module raises this when the module is misued."""
    pass


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        # The attributes are instantiated
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # NOTE: __init__() methods NEVER have a return statement.

    def value(self):
        """The value (in knuts) of all the coins in this WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

    @property
    def galleons(self):
        """Returns the number of galleon coins in this object."""
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                'galleons attr must be set to an int, not a ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException(
                'galleons attr must be a positive int, not ' + value.__class__.__qualname__)
        self._galleons = value

    @property
    def sickles(self):
        """Returns the number of sickles coins in this object."""
        return self._sickles

    @sickles.setter
    def sickles(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                'sickles attr must be set to an int, not a ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException(
                'sickles attr must be a positive int, not ' + value.__class__.__qualname__)
        self._sickles = value

    @property
    def knuts(self):
        """Returns the number of knuts coins in this object."""
        return self._knuts

    @knuts.setter
    def knuts(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                'knuts attr must be set to an int, not a ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException(
                'knuts attr must be a positive int, not ' + value.__class__.__qualname__)
        self._knuts = value

    @property
    def total(self):
        """Total value (in knuts) of all the coins in this WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    # Note that there is no setter or deleter method for `total`.

    def __repr__(self):
        """Returns a string of an expression that re-creates this object."""
        return f'{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})'

    def __str__(self):
        """Returns a human-readable string representation of this object."""
        return f'{self.galleons}g, {self.sickles}s, {self.knuts}k'

    def __add__(self, other):
        """Adds the coin amounts in two WizCoin objects together."""
        if not isinstance(other, WizCoin):
            return NotImplemented

        return WizCoin(other.galleons + self.galleons, other.sickles + self.sickles, other.knuts + self.knuts)

    def __mul__(self, other):
        """Multiplies the coin amounts by a non-negative integer."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            # Multiplying by a negative int results in negative
            # amounts of coins, which is invalid.
            raise WizCoinException('cannot multiply with negative integers')
        return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

    def __rmul__(self, other):
        """Multiplies the coin amounts by a non-negative integer."""
        return self.__mul__(other)

    def __iadd__(self, other):
        """Add the amounts in another WizCoin object to this object."""
        if not isinstance(other, WizCoin):
            return NotImplemented

        # We modify the `self` object in-place:
        self.galleons += other.galleons
        self.sickles += other.sickles
        self.knuts += other.knuts
        return self  # In-place dunder methods almost always return self.

    def __imul__(self, other):
        """Multiply the amount of galleons, sickles, and knuts in this object
        by a non-negative integer amount."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise WizCoinException('cannot multiply with negative integers')

        # The WizCoin class creates mutable objects, so do NOT create a
        # new object like this commented-out code:
        # return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

        # We modify the `self` object in-place:
        self.galleons *= other
        self.sickles *= other
        self.knuts *= other
        return self  # In-place dunder methods almost always return self.

    def _comparisonOperatorHelper(self, operatorFunc, other):
        """A helper method for our comparison dunder methods."""

        if isinstance(other, WizCoin):
            return operatorFunc(self.total, other.total)
        elif isinstance(other, (int, float)):
            return operatorFunc(self.total, other)
        elif isinstance(other, collections.abc.Sequence):
            otherValue = (other[0] * 17 * 29) + (other[1] * 29) + other[2]
            return operatorFunc(self.total, otherValue)
        elif operatorFunc == operator.eq:
            return False
        elif operatorFunc == operator.ne:
            return True
        else:
            return NotImplemented

    def __eq__(self, other):  # eq is "EQual"
        return self._comparisonOperatorHelper(operator.eq, other)

    def __ne__(self, other):  # ne is "Not Equal"
        return self._comparisonOperatorHelper(operator.ne, other)

    def __lt__(self, other):  # lt is "Less Than"
        return self._comparisonOperatorHelper(operator.lt, other)

    def __le__(self, other):  # le is "Less than or Equal"
        return self._comparisonOperatorHelper(operator.le, other)

    def __gt__(self, other):  # gt is "Greater Than"
        return self._comparisonOperatorHelper(operator.gt, other)

    def __ge__(self, other):  # ge is "Greater than or Equal"
        return self._comparisonOperatorHelper(operator.ge, other)
