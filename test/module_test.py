import hashlib

# hash = hashlib.md5()
# hash.update('admin.'.encode('utf-8'))
# print(hash.hexdigest())

# hash = hashlib.sha256()
# hash.update('admin'.encode('utf-8'))
# print(hash.hexdigest())

# hash = hashlib.md5('exin'.encode('utf-8'))
# hash.update('admin'.encode('utf-8'))
# print(hash.hexdigest())

import hmac
h = hmac.new('python'.encode('utf-8'))
h.update('helloworld'.encode('utf-8'))
print(h.hexdigest())