import hashlib

# create list of hashes provided by the NCL
hashes = [
    '030b2668863a49079b46844525b3a35b',
    '97558673e11b0b41ecdd7f356bec4099',
    '8f651531a4a5b352ca07e35767a520f7',
]

# The NCL challenge states all passwords start with a word in this list
nouns = [
    'ball','bat', 'bed', 'book', 'bun', 'can', 'cake', 'cap', 'car', 'cat', 'cow',
    'cub', 'cup', 'day', 'dog', 'doll', 'dust', 'fan', 'hall', 'hat', 'hen', 'jar',
    'kite', 'map', 'pan', 'pet', 'pie', 'sun', 'van'
    ]

# create blank list to store all potential plaintext passwords
plaintext_list = []

# iterate through all words in the nouns list, then iterate through all
# 2 digit pins. Concatenate the noun and pin together, then add it to the 
# empty list called plaintext_list
for noun in nouns:
    for pin in range(0, 100):
        plaintext_password = noun + str(pin).zfill(2)
        plaintext_list.append(plaintext_password)

# iterate through all passwords created in the nested loop above this. 
# encode the password then hash it with md5.
for plaintext_password in plaintext_list:
    pass_encoded = plaintext_password.encode()
    pass_md5 = hashlib.md5(pass_encoded).hexdigest()

    # see if any of the hashed iterations are present in the hashes list
    # if they are, print them to screen.
    if pass_md5 in hashes:
        print(plaintext_password ,":", pass_md5)