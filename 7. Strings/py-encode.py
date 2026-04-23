### encode()	Returns an encoded version of the string

### -- I found adding this "å" on the last word in the statement is encoded.
txt = "My name is Ståle"
don = "My secret password is passåwd23432" 
ton = "Måy seåcret paåssword iås passåwd23432" 

x = txt.encode()
d = don.encode()
n = ton.encode()

print(x)
print(d)