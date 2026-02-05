-- Create the SentiFilter Database
CREATE DATABASE sentifilter_db;

-- Connect to the database and create the main table
CREATE TABLE IF NOT EXISTS analyzed_comments (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    category VARCHAR(50) NOT NULL,
    confidence_score FLOAT NOT NULL CHECK (confidence_score >= 0 AND confidence_score <= 1),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexing for faster searching (Important for DBMS performance)
CREATE INDEX idx_category ON analyzed_comments(category);