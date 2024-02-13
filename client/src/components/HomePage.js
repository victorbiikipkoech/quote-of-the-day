import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css'; // Import CSS file

const HomePage = () => {
  const [quote, setQuote] = useState('');
  const [authors, setAuthors] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [newQuoteText, setNewQuoteText] = useState('');
  const [newQuoteAuthorId, setNewQuoteAuthorId] = useState('');

  useEffect(() => {
    // Fetch quote on component mount
    fetchQuote();
    // Fetch authors on component mount
    fetchAuthors();
  }, []);

  const fetchQuote = async () => {
    try {
      const response = await fetch('/quotes');
      const data = await response.json();
      const randomIndex = Math.floor(Math.random() * data.length);
      setQuote(data[randomIndex].text);
    } catch (error) {
      console.error('Error fetching quote:', error);
    }
  };

  const fetchAuthors = async () => {
    try {
      const response = await fetch('/authors');
      const data = await response.json();
      setAuthors(data);
    } catch (error) {
      console.error('Error fetching authors:', error);
    }
  };

  const handleSearchInputChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const handleSearchButtonClick = async () => {
    try {
      const response = await fetch(`/authors?name=${encodeURIComponent(searchQuery)}`);
      const data = await response.json();
      setSearchResults(data);
    } catch (error) {
      console.error('Error searching authors:', error);
    }
  };

  const handleNewQuoteTextChange = (event) => {
    setNewQuoteText(event.target.value);
  };

  const handleNewQuoteAuthorChange = (event) => {
    setNewQuoteAuthorId(event.target.value);
  };

  const handleAddQuoteSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch('/quotes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: newQuoteText,
          author_id: newQuoteAuthorId,
        }),
      });
      if (response.ok) {
        // Optionally display a success message or redirect the user
        alert('Quote added successfully!');
      } else {
        // Handle error response
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
      <blockquote className="quote">{quote}</blockquote>

      <h2>Search Authors</h2>
      <div className="author-search">
        <input
          type="text"
          value={searchQuery}
          onChange={handleSearchInputChange}
          placeholder="Enter author name"
        />
        <button onClick={handleSearchButtonClick}>Search</button>
      </div>
      <ul className="authors-list">
        {searchResults.map(author => (
          <li key={author.id}>
            <Link to={`/authors/${author.id}`}>{author.name}</Link>
          </li>
        ))}
      </ul>

      <h2>Add Your Own Quote</h2>
      <form onSubmit={handleAddQuoteSubmit} className="add-quote-form">
        <div>
          <label htmlFor="newQuoteText">Quote Text:</label>
          <input
            type="text"
            id="newQuoteText"
            value={newQuoteText}
            onChange={handleNewQuoteTextChange}
            required
          />
        </div>
        <div>
          <label htmlFor="newQuoteAuthor">Author:</label>
          <select
            id="newQuoteAuthor"
            value={newQuoteAuthorId}
            onChange={handleNewQuoteAuthorChange}
            required
          >
            <option value="">Select Author</option>
            {authors.map(author => (
              <option key={author.id} value={author.id}>{author.name}</option>
            ))}
          </select>
        </div>
        <button type="submit" className="add-quote-button">Add Quote</button>
      </form>
    </div>
  );
};

export default HomePage;
