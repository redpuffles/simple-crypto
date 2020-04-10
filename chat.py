ciphertext = "TGPRGWTADEKI HI6OYNODONAT ES4LOCIINTB} FC4LURSDTHO_ LO1IRYAEEIU_ AM{NOPBAVNT_".split(" ")

for letter_no in range(0, len(ciphertext[0])):
    for line in ciphertext:
        print(line[letter_no], end = "")
