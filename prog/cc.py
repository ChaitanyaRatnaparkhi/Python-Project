import argparse
import sys

# def encode(string, key):
    
#     encodedString = '' 
#     for i in string:
#         x = ord(i) 
#         # Upper Case      
#         if i.isupper():
#             if key + x > 90 and x!= 32:
#                 x = x + key - 26 
#                 # Space 
#             elif x != 32:
#                 x = x + key
#         # Lower Case 
#         else:   
#             if key + x > 122 and x != 32:
#                 x = x + key - 26 
#                 # Space 
#             elif x != 32:
#                 x = x + key
                
#         encodedString += chr(x)
#     return encodedString

def encode(string, key):
    encodedString = '' 
    for i in string:
        # Check if the character is an alphabet letter
        if i.isalpha():
            x = ord(i) 
            # Upper Case      
            if i.isupper():
                if key + x > 90:
                    x = x + key - 26 
                else:
                    x = x + key
            # Lower Case 
            else:   
                if key + x > 122:
                    x = x + key - 26 
                else:
                    x = x + key
                
            encodedString += chr(x)
        else:
            # If the character is not an alphabet letter, leave it unchanged
            encodedString += i
            
    return encodedString


# def decode(string, key):
    
#     decodedString = ''
#     for i in string:
#         x = ord(i)
#         # Upper Case 
#         if i.isupper():
#             if (x - key) < 65 and x != 32:
#                 x = x - key + 26
#                 print(x)
#             # Space
#             elif x != 32:
#                 x = x - key
#         # Lower Case 
#         else:
#             if (x - key) < 97 and x != 32:
#                 x = x - key + 26 
#             # Space
#             elif x != 32:
#                 x = x - key
#         decodedString += chr(x)
#     return decodedString

def decode(string, key):
    decodedString = ''
    for i in string:
        # Check if the character is an alphabet letter
        if i.isalpha():
            x = ord(i)
            # Upper Case 
            if i.isupper():
                if (x - key) < 65:
                    x = x - key + 26
                else:
                    x = x - key
            # Lower Case 
            else:
                if (x - key) < 97:
                    x = x - key + 26 
                else:
                    x = x - key
            decodedString += chr(x)
        else:
            # If the character is not an alphabet letter, leave it unchanged
            decodedString += i
            
    return decodedString


def encrypt_decrypt(file, flag):
    
    contents = '\n'.join([line for line in file])
    key = 15
    if flag == 'encrypt':
        output=  encode(contents, key)
        print(output)
    else:
        output = decode(contents, key)
        print(output)

parser = argparse.ArgumentParser(description='gron - JSON flattener')
parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help='JSON file to process or use "-" for STDIN')
parser.add_argument('-f', type=str, choices=['decrypt', 'encrypt'] , help='Encrypt or Decryt flag')
args = parser.parse_args()
# print(args)

encrypt_decrypt(args.file, args.f)

