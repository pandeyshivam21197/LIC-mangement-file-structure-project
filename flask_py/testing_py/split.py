# ls1 = "sriram |srivishnu |srikrishna |God"
# data = ls1.split('|')
# for temp in data:
#     print temp
# file1 = open("ram.txt","w")
# file1.write("this | is | can | it | is \n")
# file1.write("that | was | which | it | is \n")
# file1.write("which | are | this | it | is \n")
# file1.write("why | were | that | it | is \n")
f=open("ram.txt","r")
flag="true"
word="ram"
# for line in f:
# splitLines=line.split('|')
if word in f:
    print flag
else:
    print "false"

