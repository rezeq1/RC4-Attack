#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Read the wep.out file
with open("wep.out",'rb') as f:
    buff = f.read()

# Convert from hex to decimal
bytes_msg = [int('{:02X}'.format(b),16) for b in buff]

# Slice to sublists with length 7 bytes
rows=[bytes_msg[i:i+7] for i in range(0, len(bytes_msg), 7)] 

# Initializing variables 
keyLength = 5
key = [None] * 3

# Find Key Algorithm ( ℓ = 1,2,3,4,5 )
for L in range(1,6):
    
    # stats[0..255]={0}
    stats = [0] * 256
    
    # For each ciphertext V1,V2,V3,C1,...
    for ciphertext in rows:
        V1 = int(ciphertext[0])
        V2 = int(ciphertext[1])
        V3 = int(ciphertext[2])
        C1=ciphertext[3]
        key[0],key[1],key[2]=V1,V2,V3
        
        # Do key scheduling for 𝑖=0,1,…,ℓ+1
        j = 0
        S=list(range(256))  
        for i in range(L + 2):
            j = (j + S[i] + key[i]) % 256
            # Swap values of S[i] and S[j]
            S[i], S[j] = S[j], S[i]
            if i == 1:
                S_0 = S[0]
                S_1 = S[1]
                

        if S[1] + S[S[1]] != L + 2:
            continue
            
        # If 𝑆[0],𝑆[1] were not modified
        if ( S[0] == S_0  or S[1] == S_1 ):         
            # X = C1 XOR 0xAA
            X =  C1 ^ int('0xAA', 16)
            Pl = (X - j - S[L + 2]) % 256
            stats[Pl] += 1
            
    # For each Pl in 𝑆𝑡𝑎𝑡𝑠 from the highest     
    Pl = stats.index(max(stats))
    key.append(Pl)

# Print the key without the IV , without 0x
print(' '.join([format(key, 'x') for key in key[3:]]).upper())


# In[ ]:




