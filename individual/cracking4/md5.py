import hashlib

pass_to_hash = 'yahehe7215'

pass_encoded = pass_to_hash.encode()

pass_hashed = hashlib.md5(pass_encoded).hexdigest()

print(pass_hashed)