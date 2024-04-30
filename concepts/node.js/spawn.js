const {spawn} = require("child_process")

const child = spawn('ls', ['-lh'])

child.stdout.on('data', (data) => {
    console.log(data)
})

child.stderr.on('data', (data) => {
    console.log(data)
})

child.on('error', (err) => {
    console.log(err)
})

child.on('exit', (code, signal) => {
   if (code){
    console.log(`Process exit with code: ${code}`)
   }
   if (signal){
    console.log(`Process Killed with signal: ${signal}`)
   }
   console.log("Done")
})