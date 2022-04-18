import './App.css';
import { Form, Button } from 'react-bootstrap';
import { useState } from "react";
import parse from 'html-react-parser';

function App() {
  const [result, setResult] = useState("");
  const [file, setFile] = useState();

  const submit = async (e) => {
    var formdata = new FormData();
    formdata.append("file", file);
    e.preventDefault();
    await fetch('http://127.0.0.1:5000/parseMarkdown', {
      method: 'POST',
      body: formdata,
    }).then(response => response.text())
      .then(res => {
        setResult(res)
      })
      .catch(error => console.log('error', error));
  }
  return (
    <div className="App">
      <header style={{padding:'30px'}}>
        <Form>
          <Form.Group controlId="formFile" className="mb-3">
            <Form.Label>Markdown HTML Converter</Form.Label>
            <Form.Control type="file" onChange={(e) => setFile(e.target.files[0])} />
          </Form.Group>
          <Button variant="primary" type="submit" onClick={submit}>
            Submit
          </Button>
        </Form>

      </header>
      {result && <div style={{ textAlign: 'left', padding: '20px', border: '5px solid lightblue', margin:'20px', borderRadius:'10px' }}>
        {parse(result)}
      </div>}
    </div>
  );
}

export default App;
