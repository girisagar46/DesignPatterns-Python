# Factory Design Pattern

* In object-oriented programming, the term factory means a class that is responsible for creating objects of other types. Typically, the class that acts as a factory has an object and methods associated with it. 

* The client calls this method with certain parameters; objects of desired types are created in turn and returned to the client by the factory.

## Advantages: 

1. The first advantage is loose coupling in which *object creation can be independent of the class implementation.*
2. The client need not be aware of the class that creates the object which, in turn, is utilized by the client. It is only necessary to know the interface, methods, and parameters that need to be passed to create objects of the desired type. This simplifies implementations for the client.
3. Adding another class to the factory to create objects of another type can be easily done without the client changing the code. At a minimum, the client needs to pass just another parameter.
4. The factory can also reuse the existing objects. However, when the client does direct object creation, this always creates a new object.


There are three variants of the Factory pattern:
* *Simple Factory pattern*: This allows interfaces to create objects without exposing the object creation logic.
* *Factory method pattern*: This allows interfaces to create objects, but defers the decision to the subclasses to determine the class for object creation.
* *Abstract Factory pattern*: An Abstract Factory is an interface to create related objects without specifying/exposing their classes. The pattern provides objects of another factory, which internally creates other objects.


# Advantages of the Factory method pattern
* It brings in a lot of flexibility and makes the code generic, not being tied to a certain class for instantiation. This way, we’re solely dependent on the interface.
* There’s loose coupling, as the code that creates the object is separate from the code that uses it. The client need not bother about what argument to pass and which class to instantiate. The addition of new classes is easy and involves low maintenance.


## The Factory method versus Abstract Factory method

|Factory method | Abstract Factory method |
|----------------|------------------------|
|This exposes a method to the client to create the objects | Abstract Factory method contains one or more factory methods to  create a family of related objects |
| This uses inheritance and subclasses to decide which object to create | This uses composition to delegate responsibility to create objects of another class |
|The factory method is used to create one product | Abstract Factory method is about creating families of related products |