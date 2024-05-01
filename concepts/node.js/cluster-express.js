const cluster = require("node:cluster")
const express = require("node:express")
const os = require("node:os")

const app = express()

const numCpu = os.cpus.length()

function longComputation(){
    let sum =0;
    for (let i =0; i< 1e9; i++){
        sum += i
    }
    return sum
}

app.get('/', (req, res) => {
    let sum = longComputation()
    res.send(`result : ${sum}, pid: ${process.pid}`)
    cluster.worker.kill()
})

if (cluster.isMaster) {
    for (let i=0; i< numCpu; i++){
        cluster.fork()
    }
    cluster.on('exit', (worker, code, signal) => {
        console.log(`Workerd : ${worker.process.pid} died`)
        cluster.fork()
    })
} else {
    //all workers will share same port
    app.listen(3000, ()=> {
        console.log(`server is running on port 3000 with process ${process.pid}`)
    })
}