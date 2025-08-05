let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = this.responseText;
            } else if (this.status == 400) {
                document.getElementById("system_response").innerHTML = "<b>Invalid text! Please try again!</b>";
            } else {
                document.getElementById("system_response").innerHTML = "<b>An unexpected error occurred.</b>";
            }
        }
    };

    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
