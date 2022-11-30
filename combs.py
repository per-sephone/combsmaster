import hashlib

match = '0badbeef'
current = 0
while True:
    testing = str(candidate) + "d470d406"
    hash = hashlib.md5(testing.encode('ascii')).hexdigest()
    if hash[:8] == match:
        print('Match:"' + testing + '", md5:' + hash)
        break
    current = current + 1
    print(current)
