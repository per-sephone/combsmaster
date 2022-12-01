import hashlib
import logging
from itertools import product

def main(): #made into function for ease of termination
    logging.basicConfig(filename="logfilename.log", level=logging.INFO)
    chars = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA9876543210'

    match = '0badbeef'

    for n in range(8, 1, -1): #I don't think it'll ever hit 62^20 honestly
        for comb in product(chars, repeat=n):
            testing = (''.join(comb)[::-1]) + "d470d406"
            hash = hashlib.md5(testing.encode('ascii')).hexdigest()
            if match in hash:
                logging.info('Match:' + testing + ', md5:' + hash)
                return 0; 
            print(testing) #can be added back for testing

main()
