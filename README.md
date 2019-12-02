# Object Oriented Programming
Concepts in OOP such as Instance variables, Class variables, Method Overriding, Inheritance.

# Polymorphism

The word 'polymorphism' means *having many forms*. 
In simple words, we can define polymorphism as the ability of a message to be displayed in more than one form. This implies that Object Oriented Programming grants us the ability to recreate the same thing in many different ways.

**Compile time polymorphism**: It is also known as *static polymorphism*. This type of polymorphism is achieved by function overloading or operator overloading.

**Method Overloading**: When there are multiple functions (or methods) with the same name, but different parameters are passed to these functions, they are said to be overloaded. Functions can be overloaded by change in number of arguments and/or change in type of arguments.

# Inheritance

Inheritance is an important pillar of Object Oriented Programming. It is the mechanism in java by which one class is allowed to inherit the features(fields and methods) of another class.

Important terminology:

**Super Class**: The class whose features are inherited is known as super class(or a base class or a parent class).
**Sub Class**: The class that inherits the other class is known as sub class(or a derived class, extended class, or child class). The subclass can add its own fields and methods in addition to the superclass' fields and methods.
**Reusability**: Inheritance supports the concept of “reusability”, i.e. when we want to create a new class and there is already a class that includes some of the code that we want, we can derive our new class from the existing class. By doing this, we are reusing the fields and methods of the existing class. This allows us to not have to recreate code, and also keeps our code modular and readable.


# Encapsulation

Encapsulation is defined as the wrapping up of data under a single unit. It is the mechanism that binds together code and the data it manipulates. Another way to think about encapsulation is as a protective shield that prevents the data from being accessed by the code outside this shield. Encapsulation allows us to ensure that our code has a set scope, and operates only within that scope - and prevents unwanted interactions between two or more programs or blocks of code.


# Abstraction

Data Abstraction is the property by virtue of which only the essential details of a program or process are displayed to the user. The *trivial* or the *non-essential* units are not displayed to the user. 
Ex: A car is viewed as a car rather than its individual components. The user need not be aware of how the engine works to run it.

Data Abstraction may also be defined as the process of identifying only the required characteristics of an object and ignoring the irrelevant details.

The properties and behaviors of an object differentiate it from other objects of a similar type and also help in classifying/grouping the objects.

# Class

A class is a user defined blueprint or prototype from which objects are created.  It represents the set of properties or methods that are common to all objects of one type.

You can think of a class as a *factory* or *template* for objects. A class defines and sets the fields and methods we expect from every object that is created of that class.

# Object

An object is an instance of a class. It is a basic unit of Object Oriented Programming and represents the real life entities. A typical Java program creates many objects which then interact with each other by invoking methods. 

# Methods

A method (or function) is a collection of statements that perform some specific task and return the result to the caller.
A method can perform some specific task without returning anything as well. 
Since we can *call* methods in a program after we define them, we don't have to rewrite the code to perform this task - and so methods help us write more reusable and user-readable code.
