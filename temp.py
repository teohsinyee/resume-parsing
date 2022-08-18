def verb(s):
    if len(s) > 2 and s[-3:] != "ing":
        y = s + "ing"
    elif len(s) > 2 and s[-3:] == "ing":
        y = s + "ly"
    else:
        y = s
    return y

verb('hail')
verb('swiming')
verb('do')