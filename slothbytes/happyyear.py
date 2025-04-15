def isHappyYear(year: int):
    return len(set(str(year))) == len(str(year))

def happyYear(year: int):
    if isHappyYear(year+1):
        return year + 1
    else:
        return happyYear(year+1)

print(happyYear(2017))
print(happyYear(1990))
print(happyYear(2021))