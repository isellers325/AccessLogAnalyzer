const resultsDiv = document.getElementById("results");

fetch("http://127.0.0.1:5000/api/flagged")
.then(function(response) {
    return response.json();
})
.then(function(data) {
    for (const ip in data) {
        if (data[ip] > 2) {
            resultsDiv.innerHTML += `<p class="failed"> IP ${ip} has more than 3 failed login attempts.</p>`;
        }
    }
}); 