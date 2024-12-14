import React, { useState, useEffect } from 'react';
import RegattaList from './RegattaList';
import axios from './axios';

function App() {
  const [regattas, setRegattas] = useState([]);

  useEffect(() => {
    axios.get('/regattas/')
      .then(response => {
        setRegattas(response.data);
      })
      .catch(error => console.error("Error fetching events:", error));
  }, []);

//   const handleAddEvent = (event) => {
//     axios.post('/events/', event)
//       .then(response => {
//         setEvents([...events, response.data]);
//       })
//       .catch(error => console.error("Error adding event:", error));
//   };

  return (
    <div>
      <h1>Bat Out of Hell Schedule</h1>
      <RegattaList regattas={regattas} />
    </div>
  );
}

export default App;
