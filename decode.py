

message=input("Enter the Received Message:-")
sizeofMsg=message[:8]
MsgVal=message[8:]
x=int(len(sizeofMsg))
#print(int(x))
count=0
maxVal=0
for i in range(0,int(x),2):
#	print (i)
	temp=message[i]+message[i+1]
	sizeVal=temp
	y=sizeofMsg.count(temp)
	#print(y)
	if(y>=2):
		if(y>maxVal):
			maxVal=y
			Value=temp
		
		if(y==4 or y==3):
		#	print("a")
			continue
		else:
			count+=1
decodedMessage=""
#print(Value)
if(count>2):
	print("The First Packet Contains Error..Please Retransmit This Packet")
#	print(temp)
#print(sizeofMsg.count(temp))
else:
#	print(MsgVal)
	n=2
	for i in range(0,int(len(MsgVal)),4):
		bit1=message[i+8]
		bit2=message[i+9]
		bit3=message[i+10]
		bit4=message[i+11]
		bt1=message.count(bit1,i+8,i+12)
		bt2=message.count(bit2,i+8,i+12)
		bt3=message.count(bit3,i+8,i+12)
		bt4=message.count(bit4,i+8,i+12)
		n+=1
		if(bt1==2 and bt2==2 and bt3==2 and bt4==2 ):
			error.append(str(n)+" ")
		elif bt1==4:
			decodedMessage+=bit1
		elif bt1==3:
			decodedMessage+=bit1
		elif bt2==3:
			decodedMessage+=bit2
		elif bt3==3:
			decodedMessage+=bit3
		elif bt4==3:
			decodedMessage+=bit4
		elif bt1==2:
			decodedMessage+=bit1
		elif bt2==2:
			decodedMessage+=bit2
		elif bt3==2:
			decodedMessage+=bit3
		elif bt4==2:
			decodedMessage+=bit4
		else:
		 	print("Show error")
		#print(str(bt1)+" "+str(bt2)+" "+str(bt3)+" "+str(bt4))
"""
sizeofdecodedMessage=len(decodedMessage)
if(sizeofdecodedMessage==sizeofMsg):
	print(decodedMessage)
else:
	reduntantbits=(int(x)-int(sizeofdecodedMessage))
#	print(reduntantbits)
	for i in range(reduntantbits):
		decodedMessage="0"+decodedMessage
	print(decodedMessage)"""

newNumber=bin(int(decodedMessage))
newNumber=newNumber[2:]
if(sizeofMsg==len(newNumber)):
	print(newNumber)
else:
	s=int(Value-int(len(str(newNumber))))
	print(s)
	for i in range(s):
		newNumber="0"+newNumber
	print(newNumber)
