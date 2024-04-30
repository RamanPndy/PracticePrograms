// Classes must always have a constructor method that will later on be used to instantiate that class. 
// A constructor in JavaScript is just a plain old function that returns an object. 
// The only thing special about it is that, when invoked with the "new" keyword, it assigns its prototype as the prototype of the returned object.

// A class can only have one parent class to inherit from. You can't extend multiple classes, though there're are hacks and ways around this.
// If a child class inherits any properties from a parent class, it must first assign the parent properties calling the super() function before assigning its own properties.

// In JavaScript, all objects' properties and methods are public by default.

class Enemy {
    constructor(power) {
        this.power = power
    }

    attack = () => console.log(`I'm attacking with a power of ${this.power}!`)
}

class Alien extends Enemy { // Name of the class
    #birthYear // We first need to declare the private property, always using the '#' symbol as the start of its name.

    // The constructor method will take a number of parameters and assign those parameters as properties to the created object.
    constructor (name, phrase, power, birthYear) {
        super(power) // super function to indicate that property is declared on the parent class.
        this.name = name
        this.phrase = phrase
        this.species = "alien"
        this.#birthYear = birthYear // Then we assign its value within the constructor function
    }
    // These will be the object's methods.
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
    sayPhrase = () => console.log(this.phrase)
    howOld = () => console.log(`I was born in ${this.#birthYear}`) // and use it in the corresponding method.
}

// This throws an error:
class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        this.species = "alien" // ReferenceError: Must call super constructor in derived class before accessing 'this' or returning from derived constructor
        super(name, phrase, power, speed)
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
}

class Bug {
    constructor (name, phrase) {
        this.name = name
        this.phrase = phrase
        this.species = "bug"
    }
    hide = () => console.log("You can't catch me now!")
    sayPhrase = () => console.log(this.phrase)
}

class Robot {
    constructor (name, phrase) {
        this.name = name
        this.phrase = phrase
        this.species = "robot"
    }
    transform = () => console.log("Optimus prime!")
    sayPhrase = () => console.log(this.phrase)
}

const alien1 = new Alien("Ali", "I'm Ali the alien!")
// We use the "new" keyword followed by the corresponding class name
// and pass it the corresponding parameters according to what was declared in the class constructor function

const alien2 = new Alien("Lien", "Run for your lives!", 10)
const bug1 = new Bug("Buggy", "Your debugger doesn't work with me!",15)
const bug2 = new Bug("Erik", "I drink decaf!")
const Robot1 = new Robot("Tito", "I can cook, swim and dance!")
const Robot2 = new Robot("Terminator", "Hasta la vista, baby!")

console.log(alien1.name) // output: "Ali"
console.log(bug2.species) // output: "bug"
Robot1.sayPhrase() // output: "I can cook, swim and dance!"
Robot2.transform() // output: "Optimus prime!"

alien1.attack() // output: I'm attacking with a power of 10!
console.log(alien2.power) // output: 15

// Object composition
const addFlyingAbility = obj => {
    obj.fly = () => console.log(`Now ${obj.name} can fly!`)
}

addFlyingAbility(bug1)
bug1.fly() // output: "Now Buggy can fly!"