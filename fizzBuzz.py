list1=[]
list2=[]
def fizzbuzz(list1,list2):
	length1=len(list1)
	length2=len(list2)
	combined_length=length1+length2
	if combined_length%3==0:
		return "Fizz"
	elif combined_length%5==0:
		return "Buzz"
	elif combined_length%3==0 and combined_length%5==0:
		return "FizzBuzz"
	else:
		return "not applicable"
print(fizzbuzz([2,4,5],[1,3,4]))
	
	 
	 
	 
	 
		 
	
		
	
		
	
		

	
	
		
	
		
	
		
	
		
	
		
	

	
		
	
	
