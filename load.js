// document.getElementById("myFile").files[0].path
async function pSend(link){
    console.log("In Child Process")
    var spawn = require('child_process').spawn;
    var py = spawn('python', ["childProcess.py", link]);
    py.stdout.on('data', function(data){
        console.log(data.toString())
    });
    py.stdout.on('end', function () {
        console.log("Python Processing Ended");
    });
    py.stdout.on('error', function (err) {
        console.log(err)
        console.log("Error");
    });
}
document.addEventListener('click', init)


function init(){
    document.getElementById("submit").addEventListener("click", function(){
        console.log("clicked")
        pSend(document.getElementById("file-upload").files[0].path)
    })
}   
