
const aslImages = {
    "a": "ASL_Photos\\a.png",
    "b": "ASL_Photos\\b.png",
    "c": "ASL_Photos\\c.png",
    "d": "ASL_Photos\\d.png",
    "e": "ASL_Photos\\e.png",
    "f": "ASL_Photos\\f.png",
    "g": "ASL_Photos\\g.png",
    "h": "ASL_Photos\\h.png",
    "i": "ASL_Photos\\i.png",
    "j": "ASL_Photos\\j.png",
    "k": "ASL_Photos\\k.png",
    "l": "ASL_Photos\\l.png",
    "m": "ASL_Photos\\m.png",
    "n": "ASL_Photos\\n.png",
    "o": "ASL_Photos\\o.png",
    "p": "ASL_Photos\\p.png",
    "q": "ASL_Photos\\q.png",
    "r": "ASL_Photos\\r.png",
    "s": "ASL_Photos\\s.png",
    "t": "ASL_Photos\\t.png",
    "u": "ASL_Photos\\u.png",
    "v": "ASL_Photos\\v.png",
    "w": "ASL_Photos\\w.png",
    "x": "ASL_Photos\\x.png",
    "y": "ASL_Photos\\y.png",
    "z": "ASL_Photos\\z.png"
};


function convertToASL() {
    const letter = document.getElementById('wordInput').value.trim().toLowerCase();
    const aslDisplay = document.getElementById('aslDisplay');

    if (aslImages.hasOwnProperty(letter)) {
        const imageUrl = aslImages[letter];
        aslDisplay.innerHTML = `<img src="${imageUrl}" width="200" height="200" alt="ASL for ${letter}">`;
    } else {
        aslDisplay.innerHTML = `<p>No ASL representation found for '${letter}'</p>`;
    }
}