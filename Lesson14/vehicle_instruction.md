## Instructions of Vehicle Exercise

In this file, create 3 classes: **Vehicle**, **Car** and **Airplane**. 

Car and Airplane should inherit from Vehicle.

Add methods to each of these classes to **accelerate** and **brake**. 
* You should give these methods the same names for each of the 3 classes, so that the methods in Airplane and Car override the methods in the Vehicle base class. 
* Make sure to chain them together by having the methods in Airplane and Car use the super() function to call the methods in Vehicle.

### Vehicle class
The Vehicle class should have a method to **get the current speed of the Vehicle**.

### Airplane class
The Airplane class should have a Boolean variable to keep track of **whether or not it is in the air**. 
* This should be true if the airplane’s speed is greater than 250. 
* False if the speed is less than 250.

### Car class
The Car class should have a Boolean variable to keep track of **whether or not the Car is in reverse gear or not**. 

The Car class should have a method to **enter or exit reverse gear**. 

The Car can only enter or exit reverse gear if the speed of the Car is zero.

If the Car is in reverse gear, the accelerate method should cause the Car to get a negative speed instead of a positive speed. 

The Car’s **brake** method should always move the speed of the Car closer to zero.

### Boat class

### Submission
Create a new file in Lesson14 folder called vehicles.py
Make sure to commit your code and push it to Github!