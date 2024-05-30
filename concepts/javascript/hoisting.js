// hoisting is a behavior where variable and function declarations are moved to the top of their containing scope during 
// the compile phase, before the code is executed. 
// This means you can use variables and functions before you declare them in your code.

// variable hoisting
// 1.Variables declared with var are hoisted to the top of their function or global scope. 
// However, only the declaration is hoisted, not the initialization.
// 2.The variable is undefined until it is initialized in the code.
console.log(a); // undefined
var a = 5;
console.log(a); // 5

var a;
console.log(a); // undefined
a = 5;
console.log(a); // 5


// let and const Hoisting:
// 1. Variables declared with let and const are also hoisted, but they are not initialized. 
// They remain in a "temporal dead zone" from the start of the block until the declaration is encountered.
// 2. Accessing them before the declaration results in a ReferenceError.
console.log(b); // ReferenceError: Cannot access 'b' before initialization
let b = 10;
console.log(b); // 10

// Function Hoisting
//  - Function Declarations:
//     Function declarations are hoisted to the top of their containing scope, meaning you can call a function before 
//     it is defined in the code.
console.log(sum(2, 3)); // 5

function sum(x, y) {
    return x + y;
}
//  - Function Expressions:
//     Function expressions, whether named or anonymous, are not hoisted. Only the variable declaration is hoisted, not 
//     the function definition.
console.log(add(2, 3)); // TypeError: add is not a function

var add = function(x, y) {
    return x + y;
};
console.log(add(2, 3)); // 5
