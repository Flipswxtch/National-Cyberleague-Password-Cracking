#!/bin/bash/python3
"""This script was used in a challenge from The National Cyber League surrounding password cracking. Challengers
are provided the MD5 hash of each password. The challenger is told that all passwords start with "SKY-HQNT-" and 
end in a four digit pin. This script generates all potential passwords and their MD5 hash.
Grep can then be used to locate the hashes provided by the NCL inside of the output file. Due to how I 
have the output printed, the plaintext password will be on the same line as the hash, seperated by a colon."""

import hashlib

hashes = ['71b816fe0b7b763d889ecc227eab400a',
'674291170dffcf620bda2a604a6820ea',
'06f03267f31077d2c4b5c728472070ae',
'd866f4b3b34b598375149fb7661113ab',
'd9053951a8d1c15254b46ec9fc974a6b'
]

# string that is present within all passwords
in_all_pass = "SKY-HQNT-"

# iterate through a range beginning at 0 and ending at 9999.
for pin in range(0, 10000):

    # create the potential passwords here by appending each 4 digit pin to the known 
    # string of "SKY-HQNT-". The .zfill(4) is used to make sure all pins are four digits long.
    pass_plaintext = in_all_pass + str(pin).zfill(4)

    # change format of password using encoding.
    pass_encoded = pass_plaintext.encode()

    # hash the encoded passwords
    pass_md5 = hashlib.md5(pass_encoded).hexdigest()

    # print the plaintext password, a colon, and the hashed password.
    # print(pass_plaintext ,":", pass_md5)

    # compare generated passwords to the passwords located in the hashes list, 
    # if the generated password is in the hashes list, print the plaintext and md5 hashed
    # password to the screen
    if pass_md5 in hashes:
        print(pass_plaintext ,":", pass_md5)
        
# change permissions of script so it can be ran: sudo chmod 674 hashcrack.py
# run file and redirect output to new file: sudo python3 hashcrack.py > outfile.txt
# create file named hashes.txt, copy and paste in the given hashes: vim hashes.txt
# search for known hashes in the outfile: grep -f hashes.txt outfile.txt