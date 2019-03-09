a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
s = ''
for i in a:
    x = ord(i)
    if 64<x<120: 
    	s += chr(x + 2)
    elif x == 121:
    	s += 'a'
    elif x == 122:
    	s += 'b'
    else:
    	s += i
print(s)
