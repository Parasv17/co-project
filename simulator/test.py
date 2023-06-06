import MEM
def fetchdata(pc):
    return MEM.memory[pc]
print(MEM.memory)
MEM.memory[2]=200
print(MEM.memory)
