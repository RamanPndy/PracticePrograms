const cluster = require("node:cluster")
const http = require("node:http")
const os = require("node:os")

console.log(os.cpus.length())

if (cluster.isMaster){
    //Master incharge of creating workers
    console.log("Master process ${process.pid} is running")

    cluster.fork()
    cluster.fork()
} else {
    // Workers incharge of handling requests
    console.log("Worker process ${process.pid} is running")
    const server = http.createServer((req, res) => {
        if (req.url == ""){
            res.writeHead(200, {"Content-Type": "text/plain"})
            res.end("home page")
        } else if (req.url == "/slow-page"){
            for (let i=0; i<6000000000; i++) {}
            res.writeHead(200, {"Content-Type": "text/plain"})
            res.end("slow page")
        }
    })
}

