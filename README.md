# Flashcard Game

The Flashcard Game is a simple language learning application developed as an intermediate capstone project in the context of a Python Bootcamp. It allows users to practice French vocabulary using a digital flashcard system. The application is built using Python, pandas, and tkinter.

## Description

The flashcard game presents French words to the user from a deck of flashcards. Each flashcard contains a French word, and after a short period of time, it automatically flips to reveal the corresponding English translation. Users can then indicate whether they knew the meaning of the word or not.

- If the user knows the word's meaning, they can mark it as known, and the flashcard will be removed from the deck, helping users focus on unfamiliar words.
- If the user doesn't know the word's meaning, they can skip it, and the flashcard will be shuffled back into the deck for further practice.

The application uses the pandas library to manage the flashcard deck, reading the data from a CSV file. By default, the application looks for a file named "french_words.csv" containing a list of French words paired with their English translations. If a file named "words_to_learn.csv" is found, it is used as the deck, allowing users to continue learning from their previous session.

## Technologies Used

- Python
- pandas
- tkinter

## Required Dependencies

To run the flashcard game, make sure the following dependencies are installed:

- tkinter
- pandas


To run the flashcard game on your local machine, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/your-username/flashcard-game.git
```

2. Install the required dependencies:
   
```shell
pip install tkinter pandas
```

3. Ensure you have the necessary files:
Place the "french_words.csv" file in the "data" directory. This file should contain a list of French words paired with their English translations.

4. Run the application:

 ```shell
python main.py
```

5. The flashcard game window will open, displaying a random French word. After a short period, the card will automatically flip to reveal the English translation. Click the "Check" button if you know the word's meaning, or click the "X" button if you don't. The application will continue presenting new flashcards accordingly.
