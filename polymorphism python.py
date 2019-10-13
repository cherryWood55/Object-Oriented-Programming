## Polymorphism in Python

# Polymorphism with class methods:

# Below code shows how python can use two different class types, in the same way. 
# We create a for loop that iterates through a tuple of objects. 
# Then call the methods without being concerned about which class type each object is.
# We assume that these methods actually exist in each class.

class India(): 
	def capital(self): 
		print("New Delhi is the capital of India.") 

	def language(self): 
		print("Hindi the primary language of India.") 

	def type(self): 
		print("India is a developing country.") 

class USA(): 
	def capital(self): 
		print("Washington, D.C. is the capital of USA.") 

	def language(self): 
		print("English is the primary language of USA.") 

	def type(self): 
		print("USA is a developed country.") 

obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
	country.capital() 
	country.language() 
	country.type() 
#########################
print("")
print("#####################################")
print("")
#########################
    
## Polymorphism with Inheritance:

# In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class.
# In inheritance, the child class inherits the methods from the parent class. 
# However, it is possible to modify a method in a child class that it has inherited from the parent class. 
# This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class. 
# In such cases, we re-implement the method in the child class. 
# This process of re-implementing a method in the child class is known as Method Overriding.

class Bird: 
    def intro(self): 
            print("There are many types of birds.") 
            
    def flight(self): 
            print("Most of the birds can fly but some cannot.") 
            
class sparrow(Bird): 
    def flight(self): 
            print("Sparrows can fly.") 
            
class ostrich(Bird): 
    def flight(self): 
            print("Ostriches cannot fly.") 
	
obj_bird = Bird() 
obj_spr = sparrow() 
obj_ost = ostrich() 

obj_bird.intro() 
obj_bird.flight() 

obj_spr.intro() 
obj_spr.flight() 

obj_ost.intro() 
obj_ost.flight() 
