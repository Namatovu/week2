Year_of_birth=input("Which year were you born?")# enter year of birth
currentDate=2018

def age(): 
	age=currentDate-int(Year_of_birth) #formula to calculate age
	if age<18:
		return "You are a minor."
		
	if age>=18 and age<36:
		return "You are a youth."
		
	if age>=36:
		return "You are an elder"
		
print(age())
	
		
	
		
		
	
		
		
