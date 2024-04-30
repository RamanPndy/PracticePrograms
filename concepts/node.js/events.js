const EventEmitter = require("node:events")

const emitter = new EventEmitter()

emitter.on("order-pizza", (size, topping)=> {
    console.log("order recieved. Baking a ${size} pizza with ${topping}")
})

emitter.emit("order-pizza", "large", "mushroom")

