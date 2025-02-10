enc_flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽" #Replace with the enc file content

decoded_flag = []
for c in enc_flag:
    num = ord(c)
    first = chr(num >> 8)
    second = chr(num & 0xFF)
    decoded_flag.append(first + second)

flag = ''.join(decoded_flag)
print(flag)
