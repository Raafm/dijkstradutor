file = open("tabela_relacoes.txt",'r')
new_file = open("siglas_nomes.txt",'w')


Proxima = False
new_language =True

for line in file:
    
    if 'Language' in line: continue

    if 'Please click on each country code' in line: continue


    line = line.split('\t')


    if len(line) <= 1:
        continue

    if new_language:
        new_language = False
        print("language: "+line[0]+",   code: "+line[1]+"\n")
        print("country: "+ line[2]+",   code: "+line[3]+ ',   population: '+line[4]+"\n")
        new_file.write("language: "+line[0]+",   code: "+line[1]+"\n")
        new_file.write("country: "+ line[2]+",   code: "+line[3]+ ',   population: '+line[4]+"\n")
        continue



    if len(line) == 2:

        if line[0] == 'add new':#print next as new language: ['Inuinnaqtun', 'ikt', 'Canada', 'CA', '4,148\n'] 

            new_language = True

    elif len(line) == 3:
        print("country: "+ line[0]+",   code: "+line[1]+ ',   population: '+line[2]+"\n")
        new_file.write("country: "+ line[0]+",   code: "+line[1]+ ',   population: '+line[2]+"\n")
        if line[1] < 'AA' or line[1]>'ZZ':      #ultimo add new da lista 
            continue


    elif len(line) == 5:
        print("language: "+line[0]+",   code: "+line[1]+"\n")
        print("country: "+ line[2]+",   code: "+line[3]+ ',   population: '+line[4]+"\n")
        new_file.write("language: "+line[0]+",   code: "+line[1]+"\n")
        new_file.write("country: "+ line[2]+",   code: "+line[3]+ ',   population: '+line[4]+"\n")


    elif len(line) == 7 :
        
        print("language: "+line[2]+",   code: "+line[3]+"\n")
        print("country: "+ line[4]+",   code: "+line[5]+ ',   population: '+line[6]+"\n")
        new_file.write("language: "+line[2]+",   code: "+line[3]+"\n")
        new_file.write("country: "+ line[4]+",   code: "+line[5]+ ',   population: '+line[6]+"\n")
        continue
      

file.close()
new_file.close()