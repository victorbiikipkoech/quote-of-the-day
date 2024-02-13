import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css'; // Import CSS file

const HomePage = () => {
  const [quote, setQuote] = useState('');
  const [authors, setAuthors] = useState([]);
  const [categories, setCategories] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [searchingAuthors, setSearchingAuthors] = useState(false);

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

  const handleSearchInputChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const handleSearchAuthorsClick = async () => {
    setSearchingAuthors(true);
    try {
      const response = await fetch(`/authors/search?query=${encodeURIComponent(searchQuery)}`);
      const data = await response.json();
      setSearchResults(data);
    } catch (error) {
      console.error('Error searching authors:', error);
    } finally {
      setSearchingAuthors(false);
    }
  };

  return (
    <div className="container">
      <h1>Welcome to Quote of the Day App</h1>
      <p>Here's your quote for today:</p>
      <blockquote className="quote">{quote}</blockquote>
      <button onClick={handleRandomizeClick}>Randomize</button>

      <h2>Search Authors</h2>
      <div>
        <input
          type="text"
          value={searchQuery}
          onChange={handleSearchInputChange}
          placeholder="Enter search query"
        />
        <button onClick={handleSearchAuthorsClick} disabled={searchingAuthors}>
          {searchingAuthors ? 'Searching...' : 'Search'}
        </button>
      </div>
      <ul className="search-results">
        {searchResults.map(author => (
          <li key={author.id}>
            <Link to={`/authors/${author.id}`}>{author.name}</Link> - {author.nationality}
          </li>
        ))}
      </ul>

      <h2>Authors</h2>
      <ul className="authors-list">
        {authors.map(author => (
          <li key={author.id}>
            {author.name} - {author.nationality}
          </li>
        ))}
      </ul>

      <h2>Categories</h2>
      <ul className="categories-list">
        {categories.map(category => (
          <li key={category.id}>
            {category.name} - {category.description}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;
