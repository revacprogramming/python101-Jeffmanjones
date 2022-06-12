# Strings
text = "X-DSPAM-Confidence:    0.8475"
f=text.find("0")
num=text[f:28]
print (float(num))
