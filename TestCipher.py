#  File: TestCipher.py

#  Description: This program will use two ciphers: the substitution cipher,
#  and the Vigenere Cipher to encode and decode input given by the user.

#  Student Name: Jorge Caviedes

#  Student UT EID: jac9773

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 9/8/2018

#  Date Last Modified: 9/10/2018

# takes a single string as input parameter and returns a string.
# The function will check every character in the string to make sure
# it is a lowercase letter. If it is a lowercase letter, function will
# use the formula idx = ord('i') - ord('a') to find the substitution
# character for each letter and add it to the encoded array.
# If the character is not a letter, the function will simply add the character
# to the encoded array as is. Finally the function will turn the encoded array
# into a string and return that encoded string.
def substitution_encode ( strng ):
    cipher = ['q','a','z','w','s','x','e','d','c','r','f','v',
    't','g','b','y','h','n','u','j','m','i','k','o','l','p']
    encoded_array = []
    for i in range(len(strng)):
        if ord(strng[i]) > 96 and ord(strng[i]) < 123:
            idx = ord(strng[i]) - ord('a')
            encoded_array += cipher[idx]
        else:
            encoded_array += strng[i]
    encoded_text = ''.join(encoded_array)
    return(encoded_text)

# takes a single string as input parameter and returns a string.
# The function will check every character in the string to make sure
# it is a lowercase letter. If it is a lowercase letter, function will
# use the formula num = cipher.index(strng[i]) + ord('a') to find the original
# letter for each substitution character and add it to the decoded array. If
# the character is not a letter, the function will simply add the character to
# the decoded array as is. Finally the function will turn the decoded array
# into a string and return that encoded string.
def substitution_decode ( strng ):
    cipher = ['q','a','z','w','s','x','e','d','c','r','f','v',
    't','g','b','y','h','n','u','j','m','i','k','o','l','p']
    decoded_array = []
    for i in range(len(strng)):
        if ord(strng[i]) > 96 and ord(strng[i]) < 123:
            num = cipher.index(strng[i]) + ord('a')
            decoded_array += chr(num)
        else:
            decoded_array += strng[i]
    decoded_text = ''.join(decoded_array)
    return(decoded_text)

# takes two strings as input parameter and returns a string
# First the function will turn the given password into an array so that it can
# be edited. Then using a while loop, the function will make sure to repeat
# the string enough times so that password is in order with the text that needs
# to be encrypted. Finally the function will use a for loop to encode the given
# text and will return the encoded text as a string.
def vigenere_encode ( strng, passwd ):
    passwd_array = []
    for i in range(len(passwd)):
        passwd_array += passwd[i]
    i = 0
    counter = 0
    while i < len(strng):
        if ord(strng[i]) > 96 and ord(strng[i]) < 123 and i < len(passwd):
            i += 1
            counter += 1
        elif ord(strng[i]) > 96 and ord(strng[i]) < 123 and i >= len(passwd):
            passwd_array.insert(i, passwd[counter%len(passwd)]) #instead of 4
            counter += 1
            i += 1
        elif strng[i] == ' ' and i >= len(passwd):
            passwd_array.insert(i, ' ')
            i += 1
        else:
            i += 1
            counter += 1
    new_passwd = ''.join(passwd_array)
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    encoded_array = []
    for i in range(len(strng)):
        if ord(strng[i]) > 96 and ord(strng[i]) < 123:
            num = (alphabet.index(new_passwd[i]) + alphabet.index(strng[i]))%26
            encoded_array += alphabet[num]
        elif strng[i] == ' ':
            encoded_array.insert(i, ' ')
        else:
            encoded_array.insert(i, strng[i])
    encoded_text = ''.join(encoded_array)
    return(encoded_text)

# takes two strings as input parameter and returns a string
# First the function will turn the given password into an array so that it can
# be edited. Then using a while loop, the function will make sure to repeat
# the string enough times so that password is in order with the text that needs
# to be decrypted. Finally the function will use a for loop to decode the given
# text and will return the decoded text as a string.
def vigenere_decode ( strng, passwd ):
    passwd_array = []
    for i in range(len(passwd)):
        passwd_array += passwd[i]
    i = 0
    counter = 0
    while i < len(strng):
        if ord(strng[i]) > 96 and ord(strng[i]) < 123 and i < len(passwd):
            i += 1
            counter += 1
        elif ord(strng[i]) > 96 and ord(strng[i]) < 123 and i >= len(passwd):
            passwd_array.insert(i, passwd[counter%len(passwd)]) #instead of 4
            counter += 1
            i += 1
        elif strng[i] == ' ' and i >= len(passwd):
            passwd_array.insert(i, ' ')
            i += 1
        elif ord(strng[i]) < 97 or ord(strng[i]) > 122:
            passwd_array.insert(i, strng[counter])
            i += 1
        else:
            i += 1
            counter += 1
    new_passwd = ''.join(passwd_array)
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    decoded_array = []
    for i in range(len(strng)):
        if ord(strng[i]) > 96 and ord(strng[i]) < 123:
            num = (alphabet.index(strng[i]) - alphabet.index(new_passwd[i]))
            decoded_array += alphabet[num]
        elif strng[i] == ' ':
            decoded_array.insert(i, ' ')
        else:
            decoded_array.insert(i, strng[i])
    decoded_text = ''.join(decoded_array)
    return(decoded_text)

def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
