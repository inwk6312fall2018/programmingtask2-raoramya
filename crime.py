import string 
myfile=open("Crime.csv")
result=[]
#an empty list to store the required values 
i=0
count=[0,0,0,0,0]
#to keep a count of the number of times a crime is being repeated 
id_=[1430,1610,2142,2135,2120]
#id's of the crime
crime=['ASSAULT','ROBBERY','FROM','OF','BREAK']
#type of crime
for line in myfile:
	line=line.strip()
	line=line.split()
	a=str(line)
	b=a[79:]	
	result.append(b)
#loop for stripping and splitting a line and then appending it to the result
while(i<len(result)):
	if (crime[0] in result[i]):
		count[0]=count[0]+1
	if (crime[1] in result[i]):
		count[1]=count[1]+1
	if (crime[2] in result[i]):
		count[2]=count[2]+1
	if (crime[3] in result[i]):
		count[3]=count[3]+1
	if (crime[4] in result[i]):
		count[4]=count[4]+1
	i=i+1
#loop for calculating the count of each crime
print("crime type ID count")
for i in range(5):
	print(str(crime[i])+"	"  +str(id_[i])+"	" +str(count[i]))
#to print the final output
