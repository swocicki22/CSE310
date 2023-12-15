# Function to display game instructions
display_instructions <- function() {
  cat("Welcome to the LDS Prophets Guessing Game!\n")
  cat("Try to guess the names, birth years, and birthplaces of LDS prophets.\n")
  cat("For each prophet, you will guess the name, birth year, and birthplace.\n")
}

# Function to get user's multiple choice input using menu
get_multiple_choice_input <- function(prompt, choices) {
  choice <- menu(c(prompt, choices), title = "Choose an option:")
  return(choices[choice])
}

# Function to play the guessing game
play_prophets_game <- function() {
  # Data frame with prophets, birth years, and birthplaces
  prophets_data <- data.frame(
    Prophet = c("Joseph Smith", "Brigham Young", "Thomas S. Monson", "Russell M. Nelson"),
    BirthYear = c(1805, 1801, 1927, 1924),
    Birthplace = c("Sharon, Vermont", "Whitingham, Vermont", "Salt Lake City, Utah", "Salt Lake City, Utah")
  )
  
  # Shuffle the rows of the data frame
  prophets_data <- prophets_data[sample(nrow(prophets_data)), ]

  correct_name_guesses <- 0
  correct_birth_year_guesses <- 0
  correct_birthplace_guesses <- 0
  
  display_instructions()
  
  for (i in 1:nrow(prophets_data)) {
    prophet <- prophets_data$Prophet[i]
    birth_year <- prophets_data$BirthYear[i]
    birthplace <- prophets_data$Birthplace[i]
    
    # Guess the name
    name_guess <- tolower(readline(prompt = paste("Guess the name of the prophet: ", sep = "")))
    
    # Check if the name guess is correct
    if (name_guess == tolower(prophet)) {
      cat("Correct!\n")
      correct_name_guesses <- correct_name_guesses + 1
    } else {
      cat("Incorrect. The correct prophet is:", prophet, "\n")
    }
    
    # Guess the birth year (multiple choice)
    birth_year_choices <- c("1805", "1801", "1927", "1924")
    birth_year_prompt <- paste("In what year was ", prophet, " born? 1805, 1801, 1927 or 1924? \n", 
                               "Enter your choice: ", sep = "")
    birth_year_guess <- get_multiple_choice_input(birth_year_prompt, birth_year_choices)
    
    # Check if the birth year guess is correct
    if (birth_year_guess == birth_year_choices[i]) {
      cat("Correct!\n")
      correct_birth_year_guesses <- correct_birth_year_guesses + 1
    } else {
      cat("Incorrect. The correct birth year is:", birth_year, "\n")
    }
    
    # Guess the birthplace (multiple choice)
    birthplace_choices <- c("Sharon, Vermont", "Whitingham, Vermont", "Salt Lake City, Utah", "Salt Lake City, Utah")
    birthplace_prompt <- paste("Where was ", prophet, " born?\n", 
                               "1) Sharon, Vermont  2) Whitingham, Vermont  3) Salt Lake City, Utah  4) Salt Lake City, Utah  Enter your choice: ", sep = "")
    birthplace_guess <- get_multiple_choice_input(birthplace_prompt, birthplace_choices)
    
    # Check if the birthplace guess is correct
    if (birthplace_guess == birthplace_choices[i]) {
      cat("Correct!\n")
      correct_birthplace_guesses <- correct_birthplace_guesses + 1
    } else {
      cat("Incorrect. The correct birthplace is:", birthplace, "\n")
    }
  }
  
  # Display game statistics
  cat("\nGame Statistics:\n")
  cat("You guessed", correct_name_guesses, "out of", nrow(prophets_data), "prophet names correctly.\n")
  cat("You guessed", correct_birth_year_guesses, "out of", nrow(prophets_data), "birth years correctly.\n")
  cat("You guessed", correct_birthplace_guesses, "out of", nrow(prophets_data), "birthplaces correctly.\n")
}

# Play the prophets guessing game
play_prophets_game()
