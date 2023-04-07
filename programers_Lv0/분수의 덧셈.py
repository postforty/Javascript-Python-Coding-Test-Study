from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2

    f = Fraction(numer, denom)

    answer = [f.numerator, f.denominator]

    return answer

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))