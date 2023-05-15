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
    # changed the function used here such that it returns a 7- bit binary value of a decimal number
def invert(b):
    k=""
    for i in b:
        if(i=="0"):
            k=k+"1"
        else:
            k=k+"0"
    return k
   #invert the 0 to 1 and 1 to 0 

reg=["R0","R1","R2","R3","R4","R5","R6"]
opcodess={"add":"00000","sub":"00001","mov":"00010","ld":"00100","st":"00101","mul":"00110"
        ,"div":"00111","rs":"01000","ls":"01001","xor":"01010","or":"01011","and":"01100"
        ,"not":"01101","cmp":"01110","jmp":"01111","jlt":"11100","jgt":"11101","je":"11111","hlt":"11010"}

reg_codes={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110", "FLAGS":"111"}

reg_val={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS":0}

var_address={}# Line address of variable in 7-bit binary

var_val={}# Values of variables

mem_address={} # Label addresses

error_print=[]
flag=0

f= open("stdin.txt","r")
l=f.readlines()

# Reading 1st time to split the str in list
for i in range(len(l)):
    l[i]=list(map(str,l[i].strip().split()))
# print(l)
for i in range(len(l)):
  if l[i][-1]=="hlt" and i!=len(l)-1:
    error_print.append("hlt is not the last instruction\n")
    flag=1

    
#traversing through the list to change the address of variables
j=0
while j==0:
    if len(l[j])==0:
      continue
    if(l[j][0]=="var"):
        temp=l.pop(j)
        l.append(temp)
        continue
    break
#var shifted to end

#saving address of var and labels
for i in range(len(l)):

    if len(l[i])==0:
      continue
    if(l[i][0]=="var"):
        var_address[l[i][1]]=dectobinary(i)
        var_val[l[i][1]]=0
   
    if (l[i][0][-1]==":" ):
      if (l[i][0][-2]!=" "):
        mem_address[l[i][0][:-1]]=dectobinary(i)
        l[i].pop(0) #defines label as anything that end with :
      else:
        error_print.append(f"General error in line no.{i+1 +len(var_val)}")
        flag=1
        break
    # elif (l[i][0][-1]==":" and l[i][0][-2]!=" "):
    #   mem_address[l[i][0][:-1]]=dectobinary(i)
    #   l[i].pop(0) #defines label as anything that end with :
    # else:
    #   error_print.append(f"General error in line no.{i+1 +len(var_val)}")
    #   flag=1
    #   break
  #var and label memory stored

  #input in str output in int
  # print(mem_address)
  # print(l)

