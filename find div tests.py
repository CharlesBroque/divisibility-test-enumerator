from functools import reduce
import math
import sympy

bases = [2, 3, 5, 6, 7, 10, 11, 12, 15, 17]
maxpower = 100
maxnumber = 200

primes = list(sympy.primerange(1, maxnumber))
    
def factors(n): #stole this function from stackoverflow, muahahaha
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(math.sqrt(n))+1, step) if n % i == 0)))
                                   
for base in bases:
    sumfactors = []
    altsumfactors = []
    print("base " + str(base) + ":")
    power = 1
    totalfactors = set([1])
    while power <= maxpower and base ** power <= maxnumber:
        print("found O(1) divisibility test for " + str(sorted(factors(base ** power) - totalfactors)) + " by checking the last " + str(power) + " digit(s)")
        totalfactors.update(factors(base ** power))
        sumfactors = factors(base ** power - 1)
        altsumfactors = factors(base ** power + 1)
        if len(set(sumfactors) - totalfactors) > 0:
            print("found O(n) divisibility test for " + str(sorted(set(sumfactors) - totalfactors)) + " by summing over groups of " + str(power))
        totalfactors.update(sumfactors)
        if len(set(altsumfactors) - totalfactors) > 0:
            print("found O(n) divisibility test for " + str(sorted(set(altsumfactors) - totalfactors)) + " by altsumming over groups of " + str(power))
        totalfactors.update(altsumfactors)
        power += 1
    
    combinedfactors = sorted(totalfactors)
    for x in combinedfactors:
        if x > 1:
            newfactors = [i * x for i in combinedfactors if i <= (maxnumber // x) and math.gcd(i, x) == 1]
            combinedfactors.extend(newfactors)
            combinedfactors = sorted(set(combinedfactors))
    
    print("all tests for base " + str(base) + ", including composite tests: " + str(combinedfactors))
    
    leastmissingprime = 2
    j = 0
    while j < len(primes):
        if primes[j] not in combinedfactors:
            leastmissingprime = primes[j]
            break
        j += 1
            
    print("least missing prime: " + str(leastmissingprime))
    print("")