
text = "X-DSPAM-Confidence:    0.8475";
finder = text.find(':')
piece = text[finder+1:]
value = float(piece)
print(value)