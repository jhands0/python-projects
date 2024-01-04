import sympy
import random
import math
key_size = 8
prime1 = 0
prime2 = 0
while prime1 == prime2 or (prime1 * prime2) > 2**key_size:
    prime1 = sympy.randprime(3,2**key_size/2)
    prime2 = sympy.randprime(3,2**key_size/2)
print("Prime number 1 =",prime1)
print("Prime number 2 =",prime2) #Generating 2 different prime numbers

RSA_modulus = prime1*prime2
print("RSA modulus =",RSA_modulus) #Generating the RSA modulus

totient = (prime1 - 1)*(prime2 - 1)
print("Euler's totient =",totient) #Generating the Euler totient

public_exponent = random.randint(2,totient-1)
while math.gcd(public_exponent, totient) > 1:
    public_exponent = random.randint(2,totient-1)
print("Public exponent =",public_exponent)
print("Public key = (",RSA_modulus,public_exponent,")") #Generating the Public exponent and Public key

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
private_exponent = modinv(public_exponent,totient)
print("Private exponent =",private_exponent)
print("Private key = (",RSA_modulus,private_exponent,")") #Generating the Private exponent and Private key

text = str(input("Enter your text you would like to encrypt or decrypt: "))
def split(word):
    return [char for char in word]
split_text = split(text) #Inputing and spliting the text

counter = 0
ascii_code = 0
cipher_char = 0
list1 = []
while counter < len(split_text):
    ascii_code = ord(split_text[counter])
    cipher_char = (ascii_code**public_exponent)%RSA_modulus
    letter = chr(cipher_char)
    list1.append(letter)
    counter = counter + 1
cipher_text = ""
counter = 0
while counter < len(split_text):
    cipher_text = cipher_text + list1[counter]
    counter = counter + 1
print("Cipher text =",cipher_text) #Encrypting the text

split_cipher_text = split(cipher_text)

counter = 0
ascii_code = 0
plain_char = 0
list1 = []
while counter < len(split_cipher_text):
    ascii_code = ord(split_cipher_text[counter])
    plain_char = (ascii_code**private_exponent)%RSA_modulus
    letter = chr(plain_char)
    list1.append(letter)
    counter = counter + 1
plain_text = ""
counter = 0
while counter < len(split_cipher_text):
    plain_text = plain_text + list1[counter]
    counter = counter + 1
print("Plain text =",plain_text) #Decrypting the text