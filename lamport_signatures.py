import hashlib
import os
 
# Clearing the Screen
os.system('clear')

# siplify calling sha256 function from hashlib, returns hexidesimal value
def sha256(message):
  return hashlib.sha256(message.encode("utf-8")).hexdigest()
  pass

message="hello"

# seeds (of length 256) to generate private keys
random_seed_1="aaa9402664f1a41f40ebbc52c9993eb66aeb366602958fdfaa283b71e64db1233f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046deaef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce"
random_seed_2="ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb8254c329a92850f6d539dd376f4816ee2764517da5e0235514af433164480d7a6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b50e721e49c013f00c62cf59f2163542a9d8df02464efeb615d31051b0fddc326"

# generating 2 setting of pravate keys of length 256
private_keys_set_1 = [sha256(char) for char in random_seed_1]
private_keys_set_2 = [sha256(char) for char in random_seed_2]

# hashing private keys to get two setting of public keys
public_keys_set_1=[sha256(key) for key in private_keys_set_1]
public_keys_set_2=[sha256(key) for key in private_keys_set_2]

# Util funciton to split hexidesimal string into 1 bytes number
def splitStringInNthChars(line, n = 2):
  return [line[i:i+n] for i in range(0, len(line), n)]

# Utils function to convert 1 byte hexidesimal string number into an 8 bits binary number
def hexToBin(hex, scale=16, num_of_bits=8):
  return bin(int(hex, scale))[2:].zfill(num_of_bits)

# convert each hexidesimal number in the message hash into the biniry format
binaries={hexToBin(hex) for hex in splitStringInNthChars(sha256(message))}
binariesString="".join(bin for bin in binaries)

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

signature = getSignature(binariesString, private_keys_set_1, private_keys_set_2)

signature_hashes= [sha256(sign) for sign in signature]

# verification
for i in range(10):
  if binariesString[i] == "0":
    print("Pubic hash: " + public_keys_set_1[i] )
  else:
    print("Pubic hash: " + public_keys_set_2[i] )
pass

for i in range(10):
  print("Signature hash: " + signature_hashes[i])
  pass
