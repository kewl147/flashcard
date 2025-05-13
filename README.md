
# Flashcard App

## Overview

This Flashcard App helps you study by showing a series of flashcards with questions and answers. You can:

- View flashcards with questions on one side and answers on the other.
- Mark cards as "learned" so they are skipped in future sessions.
- Randomize the order of flashcards to vary your study session.
- Use arrow buttons to navigate between flashcards.
- Flip the card by clicking on the question or answer text.
- Reset your study session to start over.

## Features

- **Flashcard Display**: Shows a question and an answer for each card.
- **Flip Cards**: Click on the question or answer to flip the card.
- **Mark Cards as Learned**: Track your progress and skip flashcards that you no longer need to study.
- **Randomization**: Shuffle the flashcards to keep your study sessions varied.
- **Navigation**: Use left and right arrows to go forward and backward through your flashcards.
- **Reset**: Reset all progress and start over with all flashcards.

## Installation

### Prerequisites

Make sure you have Python installed on your system.

- You can download Python from [python.org](https://www.python.org/downloads/).
- Install Tkinter (usually comes pre-installed with Python):
  ```bash
  pip install tk
  ```

### Setup

1. Clone or download this repository:
   ```bash
   git clone https://github.com/kewl147/flashcard_app.git
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your `flashcard_app.py`, `data.py`, `learned.json`, and `images/` folder (containing `left_arrow.png` and `right_arrow.png`) in the same directory.

4. **Run the App**:
   - Open a command prompt and navigate to the project directory:
     ```bash
     cd path_to_your_project/flashcard
     ```
   - Then run the app:
     ```bash
     python flashcard_app.py
     ```

### Directory Structure

```plaintext
flashcard_app/
│
├── flashcard_app.py        # Main application file
├── data.py                 # File that contains flashcard data
├── learned.json            # Tracks learned flashcards
└── images/                 # Folder containing arrow images (left_arrow.png, right_arrow.png)
```

## Usage

- **Flip Card**: Click on the question or answer text to flip the card.
- **Navigation**: Click on the left or right arrows to move to the previous or next card.
- **Mark as Learned**: Click on the "Mark as Learned" button to track cards you have completed.
- **Randomize Cards**: Click the "Randomize" button to shuffle the order of the flashcards.
- **Reset**: Click the "Reset Progress" button to reset all learned cards and start from scratch.

## Contributing

Feel free to fork the repository and submit pull requests for improvements, bug fixes, or new features. Please make sure to include tests if you add new features.


