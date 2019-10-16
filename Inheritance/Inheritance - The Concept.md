Inheritance is an object-oriented programming concept. Inhertiance allows new objects to automatically take on properties of already defined objects. These already defined objects are typically called superclasses, while the object that is inheriting from the superclass is called a subclass.

Take for example a program that deals with vehicles. Lets say we want to make a Garage object. For the sake of argument, lets just say this Garage can only hold transportation-like things.

The question that should always be asked is: "How do we minimize code duplication to best design these classes?" This is where inheritance comes in. Besides walking, most, if not all transportation involves some sort of wheels.

So then maybe we can design classes like this:

Vehicle.java
 - Car.java
 - Motorcycle.java
 - Truck.java
 - Scooter.java
 - Bicycle.java

Notice how if we design our classes this way, we only have to define a field `numWheels` once -- in the Vehicle class rather than in each transportation class.

```
public class Vehicle {
    private int numWheels = 0;
}
...
public class Car extends Vehicle {
    public Car(numWheels) {
        this.numWheels = numWheels;
    }
}
...
public class Driver {
    public static void main(String[] args) {
        Car car = new Car(4);
        // Will print 4 even though Car doesn't directly have numWheels.
        System.out.println(car.numWheels);
    }
}
```
This is the power of inheritance, and it's power can be seen by the fact that we can now write code that interacts with a Vehicle class rather than make speicifc code to deal with each and every class.
