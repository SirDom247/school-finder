import React from 'react';

const InstitutionList = ({ institutions }) => {
  return (
    <ul>
      {institutions.map((institution, index) => (
        <li key={index}>
          <strong>Name:</strong> {institution.name}, <strong>State:</strong> {institution.state},{' '}
          <strong>Ownership:</strong> {institution.ownership}
        </li>
      ))}
    </ul>
  );
};

export default InstitutionList;
