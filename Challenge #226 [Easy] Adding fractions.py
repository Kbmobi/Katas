#[2015-08-03] Challenge #226 [Easy] Adding fractions
#https://www.reddit.com/r/dailyprogrammer/comments/3fmke1/20150803_challenge_226_easy_adding_fractions/
#Solution by: Keegan Bailey
                    
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

def reduceToLowest(inStr):
    #TODO: Reduce fraction to lowest terms
    return

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
    
