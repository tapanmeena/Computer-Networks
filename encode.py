

message=input("Enter the Message:-")
sizeofMessage=str(len(message))
#if sizeofMessage<10:
#	sizeofMessage=0+sizeofMessage
if int(sizeofMessage)<10:
	sizeofMessage="0"+sizeofMessage

encodedMessage=""
z=1
#size of message bit
while(z<=4):
	encodedMessage+=sizeofMessage
	z+=1

decimalMessage=int(message,2)
decimalMessageLength=len(str(decimalMessage))
#print(decimalMessageLength)
l=[int(d) for d in str(decimalMessage)]
encodedMessage+=" "
for i in range(decimalMessageLength):
	number=l[i]
	encodedMessage+=str(number)
	encodedMessage+=str(number)
	encodedMessage+=str(number)
	encodedMessage+=str(number)
	encodedMessage+=" "

print("The encoded Message is "+encodedMessage)