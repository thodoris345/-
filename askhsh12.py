import random
def getPlaintext():
    plaintext = input("Enter name of input file: ")
    inputFile = open( plaintext , "r")
    return plaintext

def encryptOrd(plaintext):
    a = ""
    for ch in plaintext:
        a += (str(ord(ch))  + " ")
        x = str(a)
        print (x[::-1]

def main():
    plaintext = getPlaintext()
    a = encryptOrd(plaintext)

main()
