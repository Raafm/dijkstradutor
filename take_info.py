file = open("temp.txt",'r')
new_file = open("popu.txt",'w')
for line in file:
    line = line.split('\t')
    if len(line) <=1:
        continue
    if 'add new' in line:
        
        if len(line) < 4:
            print(line)
        else:
            new_file.write("\nlanguage: " + line[1]+" "+line[2]+", code: " + line[3]+'\n')
            new_file.write("country: " + line[4]+" "+line[5]+'\n')
            continue
    else:
        
        print(line)
        if len(line) < 3:
                print(line)
        else:
            new_file.write("country:" + line[0]+",  code: "+line[1]+",  pessoas: "+line[2]+'\n')


file.close()
new_file.close()