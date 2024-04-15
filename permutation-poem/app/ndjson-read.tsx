import fs from 'fs';

const filePath = 'output.ndjson';

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }

    // Process the contents of the ndjson file
    const lines = data.split('\n');
    lines.forEach((line) => {
        // Do something with each line of the ndjson file
        console.log(line);
    });
});