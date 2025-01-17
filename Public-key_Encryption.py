from random import randint
from sympy import isprime
chara = input(str("Enter Plaintext for encryption and decryption: \n"))
def Public_key_Method (characters):
     def random_set():
          e =[]
          h =[]
          for i in range (2,len(characters)):
           values = randint(1,i)
           if (values > sum(e)): e.append(values)  
          qi = 2 * max(e) 
          while True: 
                q = randint(qi,qi+50)
                if isprime(q): break  
          while True:    
                w= randint(2,q-1)
                if isprime(w): break
          for k in range (len(e)): 
                hi = (w * e[k]) % q
                h.append(hi)  
          return (e, q ,w ), h
     Private_Key, Public_Key = random_set()       
     print(f"\nPRIVATE KEY = {Private_Key}")
     print(f"PUBLIC KEY =  {Public_Key}\n")

     def encrpyt_bits():
          n_bit = ''
          result = []
          sums =[]
          for char in characters:
                bit_convert = bin(ord(char))[2:]
                bit_pad = bit_convert.zfill(8) # padding to be exact 8 bits
                n_bit += bit_pad
          blocks = [n_bit[i:i+len(Public_Key)] for i in range(0,len(n_bit),len(Public_Key))]
          for block in blocks:
                multiplied_block = [int(bit) * element for bit, element in zip(block,Public_Key )]
                result.append(multiplied_block)
          for bi in range(len(result)):
                sums.append( sum(result[bi])) 
          return n_bit,sums
     result,sums = encrpyt_bits()         
     print(f"MESSAGE_BINARY = {result}\n")
     print(f"ENCRYPTED MESSAGE = {sums}\n")  

     def decrypted_bits():
          e, q, w = Private_Key
          messg_blocks = []
          reverse_messg=[]         
          for c in sums:
               c_prime = (c * pow(w,-1,q)) % q 
               Each_block = []             
               for ei in reversed(e):
                    if c_prime >= ei: 
                          Each_block.append(1)
                          c_prime -= ei
                    else: Each_block.append(0)
               messg_blocks.append(Each_block)
               for ti in reversed(Each_block):reverse_messg.append(ti)
          bit_string = ''.join(str(bit) for bit in reverse_messg)  
          text = ''.join(chr(int(bit_string[i:i+8], 2)) for i in range(0, len(bit_string), 8))
          return messg_blocks,text 
     decrypted_blocks,texts = decrypted_bits() 
     print(f"DECRYPTED BITS = {decrypted_blocks}\n")
     print(f"DECRYPTED MESSAGE = {texts}\n") 
            
Public_key_Method (chara)     

