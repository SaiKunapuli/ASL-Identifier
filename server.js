const { spawn } = require('child_process');
const express = require('express');
const app = express();
const port = 3000;
const path = require('path');
const filePath = path.join(__dirname, 'public', 'index.html');

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(filePath);
})

app.post('/open-python-window', (req, res) => {
  const pythonProcess = spawn('python', ['app.py']);
  
  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python stdout: ${data}`);
  });
  
  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python stderr: ${data}`);
  });
  
  res.send('Python window opened successfully.');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});