// Mapping of letters to ASL image URLs
const aslImages = {
    "a": "ASL Photos\A.jpg",
    "b": "ASL Photos\B.jpg",
    "c": "ASL Photos\C.png",
    // Add more mappings as needed
};

// Function to show ASL image based on input letter
function showASLImage() {
    const letter = document.getElementById('letterInput').value.trim().toLowerCase();
    const aslDisplay = document.getElementById('aslDisplay');

    if (aslImages.hasOwnProperty(letter)) {
        const imageUrl = aslImages[letter];
        aslDisplay.innerHTML = `<img src="${imageUrl}" alt="ASL for ${letter}">`;
    } else {
        aslDisplay.innerHTML = `<p>No ASL representation found for '${letter}'</p>`;
    }
}