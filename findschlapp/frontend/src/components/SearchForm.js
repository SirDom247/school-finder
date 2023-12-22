import React, { useState } from 'react';

const SearchForm = ({ onSearch }) => {
  const [state, setState] = useState('');

  const handleSearch = () => {
    onSearch(state);
  };

  return (
    <div>
      <label htmlFor="state">Enter State:</label>
      <input
        type="text"
        id="state"
        value={state}
        onChange={(e) => setState(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
};

export default SearchForm;
