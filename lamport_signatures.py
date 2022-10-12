import hashlib
import os
from random import random
 
# Clearing the Screen
os.system('clear')

"""
The problem
Alice wants to send a message to Bob, and make sure that nobody alters the message
for this reson Alice creates a signature and public key
from which Bob can verify that the message is actually come from Alice
"""

# *____Utils____*
# siplify calling sha256 function from hashlib, returns hexidesimal value
def sha256(message):
  return hashlib.sha256(message.encode("utf-8")).hexdigest()


# Util funciton to split hexidesimal string into 1 bytes number
def splitStringInNthChars(line:str, n = 2):
  if line.__len__() % n > 0:
    raise ValueError(f"Error: String length % {n} has to be 0.")
  list = []
  while(line != ""):
    list.append(line[:n])
    line = line[n:]
    pass
  pass
  return list 

def messageToBinaryHash(message: str) -> str:
  # convert each hexidesimal number in the message hash into the  formatbiniry
  binaries=[hexToBin(hex) for hex in splitStringInNthChars(sha256(message))]
  return "".join(bin for bin in binaries)


# Util function to convert 1 byte hexidesimal string number into an 8 bits binary number
def hexToBin(hex, scale=16, num_of_bits=8):
  return bin(int(hex, scale))[2:].zfill(num_of_bits)

message="hey"
message_hash=sha256(message)

# generating 2 lists of pravate keys of length 256
private_keys_set_1 = [sha256(str(random())) for _ in range(256)]
private_keys_set_2 = [sha256(str(random())) for _ in range(256)]

# hashing private keys to get two lists of public keys
public_keys_set_1=[sha256(key) for key in private_keys_set_1]
public_keys_set_2=[sha256(key) for key in private_keys_set_2]

# Getting signature by iteratin through message hash in the binary format
# and take private key forom the first set if the bit is 0 and from the second set if otherwise
def getSignature(binaryMessage, priv_keys_1, priv_keys_2):
  signature=list()
  for i in range(binaryMessage.__len__()):
    if binaryMessage[i] == "0":
      signature.append(priv_keys_1[i])
    else:
      signature.append(priv_keys_2[i])
    pass
  return signature

signature = getSignature(messageToBinaryHash(message), private_keys_set_1, private_keys_set_2)
signature_hashes= [sha256(sign) for sign in signature]


def verify(message:str, signature_hashes:list[str], public_keys:tuple[list[str], list[str]]):
  is_valid = False
  message_hash_in_binary_representation=messageToBinaryHash(message)
  for i in range(message_hash_in_binary_representation.__len__()):
      if message_hash_in_binary_representation[i] == "0":
        if public_keys[0][i] != signature_hashes[i]:
          return False
      elif message_hash_in_binary_representation[i] == "1":
        if public_keys[1][i] != signature_hashes[i]:
          return False
      else:
        return False
      pass
  return True

print(verify("hey", signature_hashes, (public_keys_set_1, public_keys_set_2)))
