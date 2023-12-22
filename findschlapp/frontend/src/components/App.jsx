import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [state, setState] = useState('');
  const [institutions, setInstitutions] = useState([]);

  useEffect(() => {
    // Fetch institutions based on the state
    const fetchData = async () => {
      try {
        const response = await fetch(`http://localhost:5000/search?state=${state}`);
        const data = await response.json();
        setInstitutions(data.institutions);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [state]);

  return (
    <div className="App">
      <h1>Institutions Search App</h1>
      <label htmlFor="state">Enter State:</label>
      <input
        type="text"
        id="state"
        value={state}
        onChange={(e) => setState(e.target.value)}
      />
      <h2>Institutions:</h2>
      <ul>
        {institutions.map((institution, index) => (
          <li key={index}>
            <strong>Name:</strong> {institution.name}, <strong>State:</strong> {institution.state},{' '}
            <strong>Ownership:</strong> {institution.ownership}
          </li>
        ))}
      </ul>
    </div>
  );

}

export default App;
