// src/Flashcard.js
import React, { useState } from 'react';

const flashcards = [
  { term: "Supervised Learning", definition: "A type of machine learning where the model learns from labeled data." },
  { term: "Unsupervised Learning", definition: "A type of machine learning where the model learns from unlabeled data." },
  // Add more flashcards here...
];

function Flashcard() {
  const [currentFlashcard, setCurrentFlashcard] = useState(flashcards[0]);
  const [score, setScore] = useState(0);
  const [guess, setGuess] = useState('');

  const handleNextFlashcard = () => {
    const nextFlashcard = flashcards[Math.floor(Math.random() * flashcards.length)];
    setCurrentFlashcard(nextFlashcard);
    setGuess('');
  };

  const handleGuess = () => {
    if (guess.toLowerCase() === currentFlashcard.term.toLowerCase()) {
      setScore(score + 1);
      alert('Correct!');
    } else {
      alert(`Incorrect! The correct term is: ${currentFlashcard.term}`);
    }
    handleNextFlashcard();
  };

  return (
    <div>
      <h1>Flashcards Game</h1>
      <p>Definition: {currentFlashcard.definition}</p>
      <input
        type="text"
        value={guess}
        onChange={(e) => setGuess(e.target.value)}
        placeholder="Enter your guess for the term"
      />
      <button onClick={handleGuess}>Submit</button>
      <p>Score: {score}</p>
    </div>
  );
}

export default Flashcard;