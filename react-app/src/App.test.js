import React from 'react';
import { render } from '@testing-library/react';
import App from './App';

test('renders Family Tree link', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/GRanD Family Tree/i);
  expect(linkElement).toBeInTheDocument();
});
