//Initialises a local server for the purpose of testing functionality of google accounts with site
//Node.js required for use.
//Write "node C:\Users\(testServer.js file path)" to initialise and access using http://localhost:8000 in address bar
//Adapted from: https://stackoverflow.com/questions/4720343/loading-basic-html-in-node-js/44995834

var http = require('http'),
    fs = require('fs');

//This path may need to be changed depending on this files location
fs.readFile('Documents/GitHub/res_website/tigerCentralHome.html', function (err, html) {
    if (err) {
        throw err; 
    }       
    http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        response.write(html);  
        response.end();  
    }).listen(8000);
});
