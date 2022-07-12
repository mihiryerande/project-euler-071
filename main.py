# Problem 71:
#     Ordered Fractions
# 
# Description:
#     Consider the fraction, n/d, where n and d are positive integers.
#     If n < d and HCF(n,d) = 1, it is called a reduced proper fraction.
#
#     If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
#         1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, [ 2/5 ], 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
#     It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#
#     By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size,
#       find the numerator of the fraction immediately to the left of 3/7.

from fractions import Fraction
from math import floor
from typing import Tuple


def main(n_mid: int, d_mid: int, d_max: int) -> Tuple[int, int]:
    """
    Returns the numerator and denominator of the reduced proper fraction
      occurring immediately before the fraction `n_mid`/`d_mid`
      in the ordered list of reduced proper fractions
      of the form n/d, for d ≤ `d_max`, and 0 < n < d.

    Args:
        n_mid (int): Numerator of target fraction
        d_mid (int): Denominator of target fraction
        d_max (int): Maximum possible denominator

    Returns:
        (Tuple[int, int]):
            Numerator and denominator of reduced proper fraction immediately
              to the left of `n_mid`/`d_mid` when listed in increasing order.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(d_max) == int and d_max > 0
    assert type(d_mid) == int and 0 < d_mid <= d_max
    assert type(d_mid) == int and 0 < n_mid < d_mid

    mid = Fraction(n_mid, d_mid)
    diff = mid
    n_best = d_best = 0
    for d in range(1, d_max+1):
        n = floor(3*d/7)
        f = Fraction(n, d)
        diff_f = mid - f
        if 0 < diff_f < diff:
            n_best, d_best = f.numerator, f.denominator
            diff = diff_f
    return n_best, d_best


if __name__ == '__main__':
    numerator_middle, denominator_middle =\
        map(int, input('Enter a fraction `f` (0 < f < 1) as "__/__": ').strip().split('/'))
    denominator_maximum = int(input('Enter an upper limit (inclusive) for the denominators: '))
    numerator_best, denominator_best = main(numerator_middle, denominator_middle, denominator_maximum)
    print('Reduced fraction to the left of {}/{} in increasing order:'.format(numerator_middle, denominator_middle))
    print('  {}/{}'.format(numerator_best, denominator_best))
