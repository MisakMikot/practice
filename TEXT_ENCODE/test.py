from Crypto.Cipher import AES
def plain2aes(key,text):
    password = key.encode()
    iv = b'0000000000000000'
    aes = AES.new(password, AES.MODE_CBC, iv, paddingMode="ZeroPadding")
    en_text = aes.encrypt(text)
    return en_text
text = '114514'.encode()
pwd = '1234567812345678'
print(plain2aes(key=pwd, text=text))