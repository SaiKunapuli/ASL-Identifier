// Mapping of letters to ASL image URLs
const aslImages = {
    "a": "public\\ASL_Photos\\A.jpg",
    "b": "ASL_Photos\B.jpg",
    "c": "ASL_Photos\C.png",
    // Add more mappings as needed
};

// Function to show ASL image based on input letter
function convertToASL() {
    const letter = document.getElementById('wordInput').value.trim().toLowerCase();
    const aslDisplay = document.getElementById('aslDisplay');

    if (aslImages.hasOwnProperty(letter)) {
        const imageUrl = aslImages[letter];
        aslDisplay.innerHTML = `<img src="${imageUrl}" alt="ASL for ${letter}">`;
    } else {
        aslDisplay.innerHTML = `<p>No ASL representation found for '${letter}'</p>`;
    }
}