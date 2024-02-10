import React, { useEffect, useState } from 'react';

const HomePage = () => {
  const [quote, setQuote] = useState('');

  useEffect(() => {
    const fetchQuote = async () => {
      try {
        const response = await fetch('/quotes'); // Fetch quotes from the backend
        const data = await response.json();
        const randomIndex = Math.floor(Math.random() * data.length); // Choose a random quote
        setQuote(data[randomIndex].text); // Set the quote text
      } catch (error) {
        console.error('Error fetching quote:', error);
      }
    };

    fetchQuote();
  }, []);

  return (
    <div>
      <h1>Welcome to Quote of the Day App</h1>
      <p>Here's your quote for today:</p>
      <blockquote>{quote}</blockquote>
    </div>
  );
};

export default HomePage;
