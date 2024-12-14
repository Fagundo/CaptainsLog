import React from 'react';

function RegattaList({ regattas }) {
  return (
    <div>
      <h2>Upcoming Regattas</h2>
      <ul>
        {regattas.map(regattas => (
          <li key={regattas.id}>
            {regattas.name} - {regattas.date}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RegattaList;
