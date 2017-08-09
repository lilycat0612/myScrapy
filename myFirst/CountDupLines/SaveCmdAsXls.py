import xlwt

f = open("cmd.txt")
cmd=[]
for line in f.readlines():
    cmd.append(line)   
cmd.sort()


file = xlwt.Workbook()
table = file.add_sheet('sheet1')
for i, j in enumerate(cmd):
    table.write(i,0,j)
file.save('demo.xls')