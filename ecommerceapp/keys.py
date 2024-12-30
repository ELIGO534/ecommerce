from Crypto.Cipher import AES
MID="your_merchant_id_here"
MK="your_merchant_key_here"
MK=MK.encode()
MK=MK.ljust(16)[:16]