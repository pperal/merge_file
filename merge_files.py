
count=0
countt=0
counttt=0
merged_data=""
count_transaction_code_D=0
count_transaction_code_C=0
amount_D=0
amount_C=0
new_tailer=""

file_one=input('Input first file name: ')
file_two=input('Input second file name: ')

files = [file_one,file_two]

#--------------------- Remove head and tail---------------------------

with open("./input_file/"+file_one+".txt", "r+", encoding = "tis-620") as f:
    for line in f: count += 1


with open("./input_file/"+file_one+".txt", "r+", encoding = "tis-620") as fp:
    lines = fp.readlines()
    lines = lines[:-1]
    fp.seek(0)
    fp.truncate()
 
    for number, line in enumerate(lines):
        #if number not in [0, count-1]:
        fp.write(line)


with open("./input_file/"+file_two+".txt", "r+", encoding = "tis-620") as f:
    for line in f: countt += 1


with open("./input_file/"+file_two+".txt", "r+", encoding = "tis-620") as fp:
    lines = fp.readlines()
    fp.seek(0)
    fp.truncate()
 
    for number, line in enumerate(lines):
        if number not in [0, countt]:
            fp.write(line)


#--------------------------merge file-------------------------
for file in files:
    f=open("./input_file/"+file+".txt", "r", encoding = "tis-620")
    merged_data=merged_data+f.read()
    f.close()

#print(merged_data)
with open('./output_file/merged_file.txt', "x", encoding = "tis-620") as f:
    f.write(merged_data)

#--------------------------sort sequence number-----------------

sequence_num=1
l=""
new_data=""

# ใช้ไฟล์ merged --> sort and peplace ได้  
def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    if index < 0:
        return newstring + s
    if index > len(s):
        return s + newstring

    return s[:index] + newstring + s[index + 1:]

#with open('merged_file.txt', "r", encoding = "tis-620") as f:
    #for line in f: count += 1

with open('./output_file/merged_file.txt', "r", encoding = "tis-620") as fp:
    lines = fp.readlines()
    fp.seek(0)
    
    for number, line in enumerate(lines):
        position = 6
        xx=str(sequence_num)
        r=len(xx)
        new_position = position-(len(xx)-1)
        l=line
        for x in range(r):
            l=replacer(l,xx[x],new_position)
            #print(xx[x],new_position)
            #new_data=new_data+l
            new_position+=1

        #print(l)
        sequence_num+=1
        new_data=new_data+l

        #print(replacer(line,str(sequence_num),position))
        #sequence_num+=1
print(new_data)        
#--------------------------------------------------------------
with open('./output_file/merged_file_sorted.txt', "x", encoding = "tis-620") as f:
    f.write(new_data)


#--------------------------- sum ---------------------------------------------------


with open('./output_file/merged_file_sorted.txt', "r", encoding = "tis-620") as f:
    for line in f: counttt += 1

with open('./output_file/merged_file_sorted.txt', "r", encoding = "tis-620") as fp:
    lines = fp.readlines()
    fp.seek(0)
    
    for number, line in enumerate(lines):
        if number not in [0, counttt-1]:
            if line[20] == "D":
                count_transaction_code_D+=1
                amount_D+=int(line[21:31])
            if line[20] == "C":
                count_transaction_code_C+=1
                amount_C+=int(line[21:31])


with open('./output_file/merged_file_sorted.txt', "r", encoding = "tis-620") as fp:
    last_line = fp.readlines()[-1]
    new_tailer=replacer(last_line,str(count_transaction_code_D),26)
    new_tailer=replacer(new_tailer,str(count_transaction_code_C),46)

    position_D=39
    xx_D=str(amount_D)
    r_D=len(xx_D)
    new_position_D = position_D-(len(xx_D)-1)
    position_C=59
    xx_C=str(amount_C)
    r_C=len(xx_C)
    new_position_C = position_C-(len(xx_C)-1)

    for x in range(r_D):
            new_tailer=replacer(new_tailer,xx_D[x],new_position_D)
            new_position_D+=1

    for x in range(r_C):
            new_tailer=replacer(new_tailer,xx_C[x],new_position_C)
            new_position_C+=1

print(new_tailer)

#with open('./output_file/merged_file_sorted.txt', "r", encoding = "tis-620") as f:
    #f.readlines()

lastlines = open('./output_file/merged_file_sorted.txt', "r", encoding = "tis-620").readlines()
lastlines[-1] = new_tailer

# now write the modified list back out to the file
open('./output_file/merged_file_sorted.txt', "w", encoding = "tis-620").writelines(lastlines)