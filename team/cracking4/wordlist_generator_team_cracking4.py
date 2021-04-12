#!/usr/bin/python3

# At the moment, this module will create a wordlist consisting of 5,731,000 uniqe 
# password combos. It was used during the Team Game during the National Cyber League
# competition. I succeeded in cracking 4/5 passwords using this within Kali-Linux so 
# that it could be used with Hashcat. I modified the file paths before running and 
# did not include the hashes list or the code commented out at the bottom. This 
# program was run with the following command: python ./wordlist_gen.py > wordlist.txt

# import hashlib
# import crypt


# Create a list of hashes provided by the NCL. This currently is not being used.
# hashes = ('$1$wiznq$SOLTS6FyoeWlF.B67Jj4A1',
#          '$1$wiznq$IJsC/MdFcajA1I2X1QiYB/',
#          '$1$wiznq$GB6GLNScDqspGw/LLqKrs1',
#          '$1$wiznq$7Na3eEW9zgH1q4mgSgBzQ1',
#          '$1$wiznq$SPD52JmyVrwu3WeU/4XTa0',    
# )

# create a function that imports a text file which contains a list of nouns. Each
# noun is appended to the list called nouns.
def load_nouns(filename):
    nouns = list()

    with open(filename) as lines:
        for line in lines:
            nouns.append(line.rstrip('\n'))
    return nouns

# create a function that imports a text file which contains a list of adjectives. Each
# adjective is appended to the list called adjectives.
def load_adjectives(filename):
    adjectives = list()

    with open(filename) as lines:
        for line in lines:
            adjectives.append(line.rstrip('\n'))
    return adjectives

# create a variable while calling the two previous functions to run so that my two
# separate text files become lists.
nouns = load_nouns("/home/flipswxtch/ncl/passwordcracking/noun.txt")
adjectives = load_adjectives("/home/flipswxtch/ncl/passwordcracking/adj.txt")

# print(nouns)
# print(adjectives[:10])

# Start iterating through each adjective, for each adjective I loop through each 
# noun, and then I loop through all potential 2-digit pins. I concatenate these
# in the order provided by the NCL to create my plaintext passwords. lastly, I
# create a list to store each generated password.
plaintext_list = list()

for adjective in adjectives:
    for noun in nouns:
        for pin in range(0, 100):
            plaintext_password = adjective + noun + str(pin).zfill(2)
            plaintext_list.append(plaintext_password)
            # print(plaintext_password)

print(f"Length of generated password list: {len(plaintext_list)}")


# I've not gotten this piece to work yet. Its aim is to create md5crypt hashes
# and then compare them to the hashes list.
# for plaintext_password in plaintext_list:
    # pass_encoded = plaintext_password.encode()
    # pass_md5 = crypt.crypt(plaintext_password)

    # if pass_md5 in hashes:
    #     print(plaintext_password ,":", pass_md5)          