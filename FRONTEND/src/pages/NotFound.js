import React from 'react';
import { Link } from 'react-router-dom';

const NotFound = () => (
  <div>
    <h2>Looks like you're lost!</h2>
    <p>Try returning <Link to='/'>home</Link>.</p>
  </div>
);

export default NotFound;
