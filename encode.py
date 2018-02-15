def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

message=input("Enter the Message:-")
sizeofMessage=str(len(message))
sumofMessage=sum_digits3(int(sizeofMessage))

#if sizeofMessage<10:
#	sizeofMessage=0+sizeofMessage
if int(sizeofMessage)<10:
	sizeofMessage="0"+sizeofMessage
if sumofMessage<10:
	sumofMessage="0"+str(sumofMessage)
encodedMessage=""
z=1
#print(sumofMessage)
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

print("The encoded Message is "+str(sumofMessage)+encodedMessage)