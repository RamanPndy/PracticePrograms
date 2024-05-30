// In JavaScript, every object has a special property called prototype. 
// The prototype property is a reference to another object that serves as a template for the current object. 
// This prototype object contains properties and methods that are shared among all instances of objects created using a 
// particular constructor function or class.

// Key Points about Prototypes:
// Inheritance Mechanism:
// Prototypes are at the core of JavaScript's inheritance mechanism. 
// When you access a property or method on an object, if the object itself does not have that property or method, 
// JavaScript looks for it in the object's prototype chain.

// Constructor Function or Class:
// Objects in JavaScript are typically created using constructor functions or ES6 classes. 
// When you create an object using a constructor function or class, the prototype property of that constructor function 
// or class becomes the prototype of the created object.

// Prototype Chain:
// Every object in JavaScript has a prototype chain. When you access a property or method on an object, 
// JavaScript first checks if the object has that property or method. If not, it looks at the object's prototype. 
// If the prototype also doesn't have the property or method, JavaScript continues up the prototype chain until it 
// finds the property or reaches the end of the chain (Object.prototype).

// Object.prototype:
// At the top of the prototype chain is Object.prototype. 
// This is the default prototype for all objects in JavaScript. 
// It contains common methods like toString(), hasOwnProperty(), valueOf(), etc.

// Benefits of Prototypes:
// Code Reusability: 
// Prototypes allow you to define methods and properties once and share them among multiple objects created from the 
// same constructor function or class.
// Efficient Memory Usage: 
// Shared methods and properties in prototypes reduce memory consumption since they are not duplicated for each object instance.
// Dynamic Modifications: Prototypes can be modified dynamically, and changes are reflected in all instances that share
//  the same prototype.

// Constructor function
function Person(name, age) {
    this.name = name;
    this.age = age;
}

// Adding a method to the prototype of Person
Person.prototype.sayHello = function() {
    console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
};

// Creating an object using the Person constructor
const person1 = new Person('Alice', 30);
const person2 = new Person('Bob', 25);

// Calling the method from the prototype
person1.sayHello(); // Output: Hello, my name is Alice and I'm 30 years old.
person2.sayHello(); // Output: Hello, my name is Bob and I'm 25 years old.
