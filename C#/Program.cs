using System;
using System.Collections.Generic;

class CharacterGame
{
    private List<string> bookOfMormonCharacters = new List<string>
    {
        "Nephi",
        "Moroni",
        "Alma",
        "Lehi",
        "Helaman",
        "Sariah",
        "Abinadi",
        "Ammon",
        "Ether",
        "Zoram",
        "Amalickiah",
        "Teancum",
        "Pahoran",
        "Samuel",
        "Zeezrom",
        "Laman",
        "Lemuel",
        "Mormon",
        "Helaman",
        "Gideon",
        "Kishkumen",
        "Lachoneus",
        "Nehor",
        "Omni",
        "Zeniff"
        // Add more characters here
    };

    private string characterToGuess;
    private string guessedCharacter;
    private int attempts;
    private int maxAttempts = 6; // You can adjust this as needed.
    private int score;

    public void Play()
    {
        characterToGuess = SelectRandomCharacter();
        guessedCharacter = new string('_', characterToGuess.Length);
        attempts = 0;
        score = 0;

        Console.WriteLine("Welcome to the Book of Mormon Character Guessing Game!");
        Console.WriteLine($"You have {maxAttempts} attempts to guess the character name.");
        
        while (attempts < maxAttempts)
        {
            Console.WriteLine($"Character to guess: {guessedCharacter}");
            Console.Write("Enter a letter: ");
            string letter = Console.ReadLine();

            if (letter.Length == 1)
            {
                char guessedLetter = letter[0];
                bool letterFound = false;

                for (int i = 0; i < characterToGuess.Length; i++)
                {
                    if (characterToGuess[i] == guessedLetter && guessedCharacter[i] != guessedLetter)
                    {
                        guessedCharacter = guessedCharacter.Substring(0, i) + guessedLetter + guessedCharacter.Substring(i + 1);
                        letterFound = true;
                    }
                }

                if (!letterFound)
                {
                    attempts++;
                    Console.WriteLine("Incorrect guess!");
                }

                if (guessedCharacter == characterToGuess)
                {
                    Console.WriteLine($"Congratulations! You guessed the character '{characterToGuess}' in {attempts} attempts.");
                    score++;
                    Console.WriteLine($"Your score: {score}");
                    break;
                }
            }
            else
            {
                Console.WriteLine("Please enter a single letter.");
            }
        }

        if (attempts >= maxAttempts)
        {
            Console.WriteLine($"Sorry, you've run out of attempts. The character was '{characterToGuess}'.");
        }
    }

    private string SelectRandomCharacter()
    {
        Random random = new Random();
        return bookOfMormonCharacters[random.Next(0, bookOfMormonCharacters.Count)];
    }
}

class Program
{
    static void Main()
    {
        CharacterGame game = new CharacterGame();
        while (true)
        {
            game.Play();
            Console.Write("Play again? (yes/no): ");
            string playAgain = Console.ReadLine().ToLower();
            if (playAgain != "yes")
            {
                break;
            }
        }
    }
}
