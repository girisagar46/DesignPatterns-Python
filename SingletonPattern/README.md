# Singleton Design Pattern 

* Singleton provides us with a mechanism to have one, and only one, object of a given type and provides a global point of access. 

* Singletons are typically used in cases such as logging or database operations, printer spoolers, and many others, where there is a need to have only one instance that is available across the application to avoid conflicting requests on the same resource. 

* For example, we may want to use one database object to perform operations on the DB to maintain data consistency or one object of the logging class across multiple services to dump log messages in a particular log file sequentially.


## In brief, the intentions of the Singleton design pattern are as follows:

* Ensuring that one and only one object of the class gets created
* Providing an access point for an object that is global to the program
* Controlling concurrent access to resources that are shared

> A simple way of implementing **Singleton** is by making the constructor private and creating a static method that does the object initialization. This way, one object gets created on the first call and the class returns the same object thereafter.

## In Python
The *metaclass* has more control over class creation and object instantiation, it can be used to create Singletons. (Note: To control the creation and initialization of a class, metaclasses override the  `__new__`  and  `__init__`  method.)

# Drawbacks of **Singleton Pattern**

As Singletons have a global point of access, the following issues can occur:

* Global variables can be changed by mistake at one place and, as the developer may think that they have remained unchanged, the variables get used elsewhere in the application.
* Multiple references may get created to the same object. As Singleton creates only one object, multiple references can get created at this point to the same object.
* All classes that are dependent on global variables get tightly coupled as a change to the global data by one class can inadvertently impact the other class.