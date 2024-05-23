const user = {
    name: 'Alice',
    age: 25,
    city: 'Wonderland'
};

// Get the keys of the object
console.log(Object.keys(user)); // ['name', 'age', 'city']

// Get the values of the object
console.log(Object.values(user)); // ['Alice', 25, 'Wonderland']

// Get the entries of the object
console.log(Object.entries(user)); // [['name', 'Alice'], ['age', 25], ['city', 'Wonderland']]

// Check if a property exists directly on the object
console.log(user.hasOwnProperty('name')); // true
console.log(user.hasOwnProperty('toString')); // false (inherited from Object.prototype)

// Object.prototype.toString() : Returns a string representing the object. By default, this method is inherited by all objects.
console.log(obj.toString()); // [object Object]

// Create a new object with the specified prototype object and properties. in this case user as the prototype
const newUser = Object.create(user);
console.log(newUser.name); // 'Alice'
console.log(Object.getPrototypeOf(newUser) === user); // true

// Object.getPrototypeOf() : Returns the prototype (i.e., the value of the internal [[Prototype]] property) of the specified object.
const proto = Object.getPrototypeOf(obj);
console.log(proto); // {} (or Object.prototype)

// Freeze the user object
Object.freeze(user);
user.age = 30; // This will not work, user is frozen
console.log(user.age); // 25

// Object.seal() : Seals an object, preventing new properties from being added and marking all existing properties as 
// non-configurable. Existing properties can still be changed.
const obj = { a: 1 };
Object.seal(obj);
obj.a = 2; // This will work
delete obj.a; // This will not work
console.log(obj.a); // 2

// Object.assign() : Copies the values of all enumerable own properties from one or more source objects to a target 
// object. It returns the target object.
const target = { a: 1 };
const source = { b: 2, c: 3 };
const returnedTarget = Object.assign(target, source);
console.log(returnedTarget); // { a: 1, b: 2, c: 3 }
