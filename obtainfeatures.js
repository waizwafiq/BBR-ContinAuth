function downloadCSV(rows) {
    //To download the CSV file of features
    let csvContent = "data:text/csv;charset=utf-8," + rows.map(e => e.join(",")).join("\n");

    var encodedUri = encodeURI(csvContent);
    window.open(encodedUri);
}

//let sampleEle = document.querySelector(".sample");

let features = [["x","y"]]; //list the features name here
document.body.addEventListener("mousemove", (event) => {
    let instantFeats = []; //the instantaneous features arraylist

    //PUT FEATURES TO BE OBTAINED HERE
    instantFeats.push(event.x); //get x coordinate
    instantFeats.push(event.y); //get y coordinate


    features.push(instantFeats); 
    // sampleEle.innerHTML = "X axis: " + event.x + " Y axis: " + event.y;
});

document.getElementById("dwCSV").onclick = function() {downloadCSV(features)}; //download features when the button is clicked