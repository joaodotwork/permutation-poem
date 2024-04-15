import React, { useEffect, useState } from 'react';
import fs from 'fs';

const filePath = 'output.ndjson';

const Page = () => {
  const [fileContent, setFileContent] = useState('');

  useEffect(() => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        console.error('Error reading file:', err);
        return;
      }

      // Set the file content to state
      setFileContent(data);
    });
  }, []);

  return (
    <div>
      <pre>{fileContent}</pre>
    </div>
  );
};

export default Page;