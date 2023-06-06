import MEM
def binarytodec(b):

    i =1
    d =0 
    b=b[::-1]
    for x in b :
        if x == "1":
            d=d+i
        i=i*2
    return d

#deciaml in int binary in str
def dectobinary(d):
    zero=7-len(bin(d)[2:])
    ans="0"*zero+bin(d)[2:]
    return(ans)
def dectobinary_16(d):
    zero=16-len(bin(d)[2:])
    ans="0"*zero+bin(d)[2:]
    return(ans)

def execute(inst, PC, halt):
    #in each condition if flags are not triggered then flag =0
    opcode= inst[0:5]
    # Type A 
    if ( opcode in A ):
        reg_1=reg_codes[inst[7:10]]
        reg_2=reg_codes[inst[10:13]]
        reg_3=reg_codes[inst[13:16]]
        if (A[opcode]=="add"):
            result= reg_val[reg_2]+reg_val[reg_3]
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                reg_val["FLAGS"]=8
                
        elif (A[opcode]=="sub"):
            result= reg_val[reg_2]-reg_val[reg_3]
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                #overflow handle crow
                reg_val["FLAGS"]=8

        elif (A[opcode]=="mul"):
            result= reg_val[reg_2]*reg_val[reg_3]
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                #overflow handle crow
                reg_val["FLAGS"]=8
        elif (A[opcode]=="xor"):
            result= reg_val[reg_2]^reg_val[reg_3]
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                #overflow handle crow
                reg_val["FLAGS"]=8

        elif (A[opcode]=="or"):
            result= (reg_val[reg_2])|(reg_val[reg_3])
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                #overflow handle crow
                reg_val["FLAGS"]=8

        elif (A[opcode]=="and"):
            result= reg_val[reg_2]&reg_val[reg_3]
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                #overflow handle crow
                reg_val["FLAGS"]=8
        PC+=1

    # TYPE B 
    elif ( opcode in B):
        reg_1=reg_codes[inst[6:9]]
        imm_val= binarytodec(inst[9:16])

        if (B[opcode]=="mov"):
            reg_val[reg_1]= imm_val
            reg_val["FLAGS"]=0

        elif (B[opcode]=="rs"):
            reg_val[reg_1]= reg_val[reg_1]>>imm_val
            reg_val["FLAGS"]=0

        elif (B[opcode]=="ls"):
            reg_val[reg_1]= reg_val[reg_1]<<imm_val
            reg_val["FLAGS"]=0
        PC+=1
