"""
文件说明

"""
jj_name = []
jj_code = []
d = 0
with open('jjname.txt', 'r', encoding='UTF-8', buffering=True) as g:
    while True:
        line = g.readline()
        if not line: break
        line = line.strip('\n')
        if d == 0:
            jj_name.append(line)
            d = d + 1
        else:
            jj_code.append(line)
            d = d - 1

print(jj_code)
print(jj_name)
