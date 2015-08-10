#[2015-08-03] Challenge #226 [Easy] Adding fractions
#https://www.reddit.com/r/dailyprogrammer/comments/3fmke1/20150803_challenge_226_easy_adding_fractions/
#Solution by: Keegan Bailey
import re

_RATIONAL_FORMAT = re.compile(r"""
    \A\s*                      # optional whitespace at the start, then
    (?P<sign>[-+]?)            # an optional sign, then
    (?=\d|\.\d)                # lookahead for digit or .digit
    (?P<num>\d*)               # numerator (possibly empty)
    (?:                        # followed by
       (?:/(?P<denom>\d+))?    # an optional denominator
    |                          # or
       (?:\.(?P<decimal>\d*))? # an optional fractional part
       (?:E(?P<exp>[-+]?\d+))? # and optional exponent
    )
    \s*\Z                      # and optional whitespace to finish
""", re.VERBOSE | re.IGNORECASE)

def string(numerator):
    # Handle construction from strings.
    m = _RATIONAL_FORMAT.match(numerator)
    if m is None:
        raise ValueError('Invalid literal for Fraction: %r' %
                         numerator)
    numerator = int(m.group('num') or '0')
    denom = m.group('denom')
    if denom:
        denominator = int(denom)
    else:
        denominator = 1
        decimal = m.group('decimal')
        if decimal:
            scale = 10**len(decimal)
            numerator = numerator * scale + int(decimal)
            denominator *= scale
        exp = m.group('exp')
        if exp:
            exp = int(exp)
            if exp >= 0:
                numerator *= 10**exp
            else:
                denominator *= 10**-exp
    if m.group('sign') == '-':
        numerator = -numerator

                    
def add(fraction1, fraction2):
    if fraction1 == "":
        return fraction2
    
    top1 = int(fraction1.split("/")[0])
    bot1 = int(fraction1.split("/")[1])
    
    top2 = int(fraction2.split("/")[0])
    bot2 = int(fraction2.split("/")[1])
    
    top3 = top1 * bot2
    bot3 = bot1 * bot2 
    top4 = top2 * bot1 
    bot4 = bot2 * bot1

    total = str(top3 + top4) + "/" + str(bot3)
    
    return total

if __name__ == "__main__":
    input1 = "2 1/6 3/10".split()
    total = ""
    top1 = 0
    bot1 = 0
    for i in input1:
        
        fraction = i
        if "/" not in i:
            total = add(total, i + "/1")
        else:
            print string(i)
            total = add(total, i)
    
