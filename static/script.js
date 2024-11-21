document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("textForm");
    const resultBox = document.getElementById("result");
    const outputText = document.getElementById("output_text");

    form.onsubmit = async function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Fetch the form data and send it to the server
        const formData = new FormData(form);
        const response = await fetch("/process", {
            method: "POST",
            body: formData
        });

        // Show the processed text
        const resultText = await response.text();
        outputText.textContent = resultText;
        
        // Display the result with animation
        resultBox.classList.remove("hidden");
        resultBox.classList.add("animated", "slideIn");
    };
});
