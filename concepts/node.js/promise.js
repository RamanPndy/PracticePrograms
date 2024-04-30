// What are the clauses used in promise object in Node.js ?
// In JavaScript, a Promise object can have three states:
// Pending: The initial state of the promise before it is resolved or rejected.
// Fulfilled: The state of a promise representing a successful operation. This is also sometimes called "resolved."
// Rejected: The state of a promise representing a failed operation. To create a Promise object, you must pass a function (often called an executor function) to the Promise constructor.

// This function takes two arguments: resolve and reject. 
// These are functions that you call to either fulfill or reject the promise.

var p = new Promise((resolve, reject) => {
    let a = 1 + 1
    if (a ==1){
        resolve("success")
    } else {
        reject("failed")
    }
})

p.then((message) => {
    // When promise resolved
    console.log(message)
}).catch((message) => {
    // When promise rejected
    console.log(message)
})

const recordVideoOne = new Promise((resolve, reject) => {
    resolve("video 1 resolved")
})

const recordVideoTwo = new Promise((resolve, reject) => {
    resolve("video 2 resolved")
})

const recordVideoThree = new Promise((resolve, reject) => {
    resolve("video 3 resolved")
})

Promise.all([recordVideoOne, recordVideoTwo, recordVideoThree]).then((messages) => {
    console.log("messages")
})

Promise.race([recordVideoOne, recordVideoTwo, recordVideoThree]).then((message) => {
    console.log("message")
})

function makeRequest(location){
    return new Promise((resolve, reject) =>{
        console.log("Making request to ${location}")
        if (location == "Google"){
            resolve("Hello Google")
        } else {
            reject("Cant reach Google")
        }
    })
}

function processRequest(response){
    return new Promise((resolve, reject) => {
        console.log("processing response")
        resolve("Extra Information ${response}")
    })
}

makeRequest('Google').then(response => {
    console.log("response recieved")
    return processRequest(response)
}).then(processedResponse => {
    console.log(processedResponse)
}).catch(err => {
    console.log(err)
})

async function doWork(){
    try{
        const response = await makeRequest('Google')
        console.log("response recieved")
        const processedResponse = await processRequest(response)
        console.log(processedResponse)
    } catch (err) {
        console.log(err)
    }
}

doWork()

// await will return result of promise