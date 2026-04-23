### maketrans()	Returns a translation table to be used in translations

txt = "Hello Sam!"
mytable = str.maketrans("S", "P") 
print(txt.translate(mytable))