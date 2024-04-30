const {execFile} = require("child_process")

execFile('/path/to/executable/file.sh', (err, stdout, stderr) => {
    if (err){
        console.log(err)
        return
    }
    if (stderr){
        console.log(stderr)
        return
    }
    console.log(stdout)
})