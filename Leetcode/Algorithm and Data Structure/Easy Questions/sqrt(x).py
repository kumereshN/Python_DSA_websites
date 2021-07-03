class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:  # If the square of the middle number is less than x
                l = mid + 1  # Increment the left boundary
            else:
                r = mid - 1  # Decrement the right boundary

        return r


# Alternative 1
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot  # Returns the sqrt if there is no remainder

        return right  # Returns the quotient if there's a reminder
