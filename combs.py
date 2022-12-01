import hashlib
from string import digits, ascii_letters
from itertools import product

match = "0badbeef"
current = digits+ascii_letters

for n in range(1, 4+1):
    for comb in product(current, repeat=n):
        print ("testing",''.join(comb))

#while True:
#    testing = str(current) + "d470d406"
#    hash = hashlib.md5(testing.encode('ascii')).hexdigest()
#    if hash[:8] == match:
#        print('Match:"' + testing + '", md5:' + hash)
#        break
#    current = current + 'a'
#    print(current, " ", hash)
