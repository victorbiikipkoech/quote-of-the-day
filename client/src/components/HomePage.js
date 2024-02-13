import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css'; // Import CSS file

const HomePage = () => {
  const [quote, setQuote] = useState('');
  const [author, setAuthor] = useState('');
  const [authors, setAuthors] = useState([]);
  const [categories, setCategories] = useState([]);
  const [newQuoteText, setNewQuoteText] = useState('');
  const [selectedAuthorId, setSelectedAuthorId] = useState('');

  useEffect(() => {
    // Fetch initial data on component mount
    fetchQuote();
    fetchAuthors();
    fetchCategories();
  }, []);

  const fetchQuote = async () => {
    try {
      const response = await fetch('/quotes');
      const data = await response.json();
      const randomIndex = Math.floor(Math.random() * data.length);
      setQuote(data[randomIndex].text);
      // Fetch the author of the quote
      const authorResponse = await fetch(`/authors/${data[randomIndex].author_id}`);
      const authorData = await authorResponse.json();
      setAuthor(authorData.name);
    } catch (error) {
      console.error('Error fetching quote:', error);
    }
  };

  const fetchAuthors = async () => {
    try {
      const response = await fetch('/authors');
      const data = await response.json();
      if (Array.isArray(data)) {
        setAuthors(data);
      } else {
        console.error('Invalid authors data:', data);
      }
    } catch (error) {
      console.error('Error fetching authors:', error);
    }
  };

  const fetchCategories = async () => {
    try {
      const response = await fetch('/categories');
      const data = await response.json();
      setCategories(data);
    } catch (error) {
      console.error('Error fetching categories:', error);
    }
  };

  const handleRandomizeClick = () => {
    fetchQuote();
  };

  const handleAddQuoteSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch('/add_quote', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: newQuoteText,
          author_id: selectedAuthorId,
        }),
      });
      if (response.ok) {
        alert('Quote added successfully!');
        // Optionally, you can fetch new data after adding the quote
        fetchQuote();
      } else {
        console.error('Failed to add quote:', response.statusText);
      }
    } catch (error) {
      console.error('Error adding quote:', error);
    }
  };

  return (
    <div className="container">
      <h1>Welcome to Quote of the Day App</h1>
      <p>Here's your quote for today:</p>
      <blockquote className="quote">{quote} - {author}</blockquote>
      <button onClick={handleRandomizeClick}>Randomize</button>

      <h2>Add Your Own Quote</h2>
      <form onSubmit={handleAddQuoteSubmit} className="add-quote-form">
        <div>
          <label htmlFor="newQuoteText">Quote Text:</label>
          <input
            type="text"
            id="newQuoteText"
            value={newQuoteText}
            onChange={(e) => setNewQuoteText(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="authorSelect">Author:</label>
          <select
            id="authorSelect"
            value={selectedAuthorId}
            onChange={(e) => setSelectedAuthorId(e.target.value)}
            required
          >
            <option value="">Select Author</option>
            {authors.map((author) => (
              <option key={author.id} value={author.id}>
                {author.name}
              </option>
            ))}
          </select>
        </div>
        <button type="submit">Add Quote</button>
      </form>
    </div>
  );
};

export default HomePage;
