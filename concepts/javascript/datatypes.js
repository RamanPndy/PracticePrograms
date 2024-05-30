// Primitive types: String, Number, BigInt, Boolean, Undefined, Null, Symbol.
// Non-primitive types (Objects): Object, Array, Function, Date, RegExp, Map, Set, WeakMap, WeakSet.

// Primitive Types

// string
let name = "Alice";

//number
let age = 25;
let pi = 3.14;

// Bigint
let bigInt = 1234567890123456789012345678901234567890n;

// Boolean
let isActive = true;

// undefined
let x;
console.log(x); // undefined

// null
let y = null;

// symbol
let sym = Symbol("unique");

// Non-Primitive Types (Objects)
// Object
let person = {
    name: "Alice",
    age: 25
};

// Array
let numbers = [1, 2, 3, 4, 5];

// Function
function greet() {
    console.log("Hello");
}

// Date
let now = new Date();

// RegExp
let pattern = /ab+c/;

// Map
let map = new Map();
map.set("name", "Alice");
map.set("age", 25);

// WeakMap
let weakMap = new WeakMap();
let objWM = {};
weakMap.set(objWM, "some value");

// Set
let set = new Set([1, 2, 3, 4, 4]);

// WeakSet
let weakSet = new WeakSet();
let objWS = {};
weakSet.add(objWS);




