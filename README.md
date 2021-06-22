# RC4-Attack

The program implemnts RC4 Find_key algoritm .

## Introduction:
The RC4 cipher leaks information about the secret key .In particular you can use this fact and knowledge about
the message structure conveyed in the WEP protocol, to find the key used for encryption. In the WEP protocol the first
byte of each visible message is AA (at base 16.) This information can be used to record many messages encrypted to 
discover the 5 houses of the secret house-after-house key.

## Input file :
   wep.out : This file contains 000,500 WEP messages encrypted using the RC4 cipher.
             The length of each encrypted message is 7 bytes: 3 bytes of the boot vector (IV) followed by 4 bytes.
             
## To run the code :
   1) Make sure that the python file and the wep.out file in the same location .
   2) Write in you Cmd  " python code.py "
   
![output](https://user-images.githubusercontent.com/57844508/122950177-ec633300-d384-11eb-9d6b-6e4ccc3ab546.png)
