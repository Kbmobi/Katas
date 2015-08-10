#[2015-08-03] Challenge #226 [Easy] Adding fractions
#https://www.reddit.com/r/dailyprogrammer/comments/3fmke1/20150803_challenge_226_easy_adding_fractions/
#Solution by: Keegan Bailey

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)

def numerator(n):
    return n.split("/")[0]

def denominator(d):
    return d.split("/")[1]

def reduceFraction(n, d):
    return n/gcd(n, d), d/gcd(n, d)
    
def add(frac1, frac2):
    if frac1 == "":
        return frac2
    
    n1 = int(numerator(frac1)) * int(denominator(frac2))
    d1 = int(denominator(frac1)) * int(denominator(frac2))
    n2 = int(numerator(frac2)) * int(denominator(frac1))
    d2 = int(denominator(frac2)) * int(denominator(frac1))

    if(d1 != d2):
        print "error: denominators %n and %n do not match" % (d1, d2)
        return
        
    n,d = reduceFraction(n1+n2, d1)
    
    return str(n) + "/" + str(d)

def run(x):
    total = ""
    for i in x:   
        if "/" not in i:
            continue
        else:
            total = add(total, i)
    print total

if __name__ == "__main__":
    input1 = "2 1/6 3/10".split()
    input2 = "3 1/3 1/4 1/12".split()
    challenge1 = "5 2/9 4/35 7/34 1/2 16/33".split()
    challenge2 = "10 1/7 35/192 61/124 90/31 5/168 31/51 69/179 32/5 15/188 10/17".split()

    run(input1)
    run(input2)
    run(challenge1)
    run(challenge2)
   
