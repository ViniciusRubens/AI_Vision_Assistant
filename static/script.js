function showPreview(event) {
    const reader = new FileReader();
    reader.onload = function () {
        const output = document.getElementById('imagePreview');
        const box = document.getElementById('previewBox');
        output.src = reader.result;
        box.style.display = 'block';
    };
    if (event.target.files[0]) reader.readAsDataURL(event.target.files[0]);
}

function cleanInputs() {
    document.getElementById('imageInput').value = "";
    document.getElementById('textInput').value = "";
    document.getElementById('previewBox').style.display = 'none';
    document.getElementById('imagePreview').src = "";
    const resDiv = document.getElementById('result');
    resDiv.style.display = 'none';
    resDiv.innerText = "";
}

async function sendToAPI() {
    const imageFile = document.getElementById('imageInput').files[0];
    const textPrompt = document.getElementById('textInput').value;
    const resDiv = document.getElementById('result');
    const loadDiv = document.getElementById('loading');

    if (!imageFile || !textPrompt) {
        alert("Fill in all fields before analyzing.");
        return;
    }

    const formData = new FormData();
    formData.append('image', imageFile);
    formData.append('text', textPrompt);

    resDiv.style.display = 'none';
    loadDiv.style.display = 'block';

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        resDiv.innerText = "Result: " + data.response;
        resDiv.style.display = 'block';
    } catch (error) {
        alert("Error processing image.");
        console.error("Error:", error);
    } finally {
        loadDiv.style.display = 'none';
    }
}