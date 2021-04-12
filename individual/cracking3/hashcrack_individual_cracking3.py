import hashlib

hashes = [
    '7a3a96923b1ada23fc7ed30496570f62',
    'd87006e9f4485978579deab7801bf5e6',
    '8041564ddc4f4f7447659845f91b97b1',
]

in_all_pass = 'SKY-SENH-'

for pin in range(0, 10000):
    pass_plaintext = in_all_pass + str(pin).zfill(4)

    pass_encoded = pass_plaintext.encode()

    pass_md5 = hashlib.md5(pass_encoded).hexdigest()

    if pass_md5 in hashes:
        print(pass_plaintext ,":", pass_md5)
