#coding=utf-8
import operator


f = open("history.txt")
count_dict = {}
for line in f.readlines():
    line = line.strip()
    str_blank=line.find(' ')
    #print(line[0:5])
    line=line[str_blank+2:]
    #print(line)
    count = count_dict.setdefault(line, 0)
    count += 1
    count_dict[line] = count   
sorted_count_dict = sorted(count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
f2=file("cmd.txt", "w") #打开2.txt文件，用于输出
for item in sorted_count_dict:                                 
    f2.write(str(item[0]) + "\t")
    f2.write(str(item[1])+ "\n") 
f2.close

