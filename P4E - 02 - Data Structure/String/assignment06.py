text = "X-DSPAM-Confidence:    0.8475"
apos  = text.find(':')
num = text[apos+1:]
afnum = float(num.strip())
print(afnum)