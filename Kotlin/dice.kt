import java.util.Locale

data class Dice(val sides: Int) {
    fun roll(): Int {
        return (1..sides).random()
    }
}

fun main() {
    // Get user information
    println("Welcome to Shane's Roll to 21! All you have to do is gain 21 points and you WIN! ")
    print("What's your name? ")
    val playerName = readLine()

    print("How old are you? ")
    val age = readLine()?.toIntOrNull()

    // Validate age input
    if (age == null || age <= 0) {
        println("Now don't you lie to me, thats not your age.")
        return
    }

    // Personalized welcome message
    println("Hello, $playerName! Welcome to Shane's Roll to 21!")

    // Set the number of sides for the dice
    val sides = 7
    val dice = Dice(sides)

    // Initialize game variables
    var playAgain = true
    var bank = 0
    var rounds = 0

    // Main game loop
    while (playAgain) {
        var totalScore = 0
        var rolls = 0

        // Round loop
        while (rolls < 4) {
            // Display current score
            println("Current score: $totalScore")
            println("Roll the dice? (yes/no)")

            // Get user input
            val input = readLine()?.lowercase()

            if (input == "yes" || input == "y") {
                // Roll the dice and display the result
                val rollResult = dice.roll()
                println("You rolled a $rollResult")

                // Introduce an expression: If the rollResult is 6, give a bonus
                if (rollResult == 6) {
                    val bonus = 5
                    println("You got a special bonus of $bonus!")
                    totalScore += bonus
                } else {
                    totalScore += rollResult
                }

                // Check if the player reached 21
                if (totalScore == 21) {
                    println("Congratulations! You got 21!")
                    bank += 10 // Increase the bank by 10 for getting 21
                    break
                } else if (totalScore > 21) {
                    // Check if the player exceeded 21
                    println("Oops! You exceeded 21. Your final score is $totalScore. Better luck next time!")
                    break
                }

                rolls++
            } else if (input == "no" || input == "n") {
                // Player chose to stop rolling
                println("You chose to stop rolling. Your final score is $totalScore.")
                bank += totalScore // Add the current round score to the bank
                break
            } else {
                // Invalid input
                println("Invalid input. Please enter 'yes' or 'no'.")
            }
        }

        // Display round results
        rounds++
        println("Round $rounds results:")
        println("Final score: $totalScore")
        println("Bank: $bank")

        // Ask the player if they want to play again
        println("Do you want to play again? (yes/no)")
        val playAgainInput = readLine()?.lowercase()

        if (playAgainInput != "yes" && playAgainInput != "y") {
            // Player chose not to play again
            playAgain = false
        }
    }

    // Game over message
    println("Thanks for playing Shane's Roll to 21, $playerName! Your final bank is $bank. Have a great day!")
}
