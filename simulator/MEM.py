import sys
def fetchdata(pc):
    return memory[pc]
   
# with open("output.txt") as f:
#     memory = f.readlines()    #will take from Stdin not this
memory=[]
for kx in sys.stdin:
   memory.append(kx)

memory = [x.strip() for x in memory]
l= len(memory)
rem= 128-l
for i in range(0,rem):
    memory.append("0"*16)
