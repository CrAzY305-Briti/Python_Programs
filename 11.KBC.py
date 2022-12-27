# Sample questions and answers for the game
questions = [
    {
        "question": "What is the capital of India?", 
        "answers": ["New Delhi", "Mumbai", "Bangalore", "Kolkata"], 
        "correct": "New Delhi"
    },
    {
        "question": "What is the currency of Japan?", 
        "answers": ["Yen", "Dollar", "Euro", "Rupee"], 
        "correct": "Yen"
    },
    {
        "question": "Who is the CEO of Apple?", 
        "answers": ["Mark Zuckerberg", "Tim Cook", "Elon Musk", "Bill Gates"], 
        "correct": "Tim Cook"
    },
    {
        "question": "Which of the following is not a primary color?", 
        "answers": ["Red", "Yellow", "Blue", "Green"], 
        "correct": "Yellow"
    },
    {
        "question": "Who is the current Prime Minister of India?", 
        "answers": ["Narendra Modi", "Rahul Gandhi", "Sonia Gandhi", "Manmohan Singh"], 
        "correct": "Narendra Modi"
    }
]

# Function to play the game
def play_game():
  # Set the initial amount of money won to 0
  money_won = 0

  # Iterate through each question
  for question in questions:
    # Print the question and the possible answers
    print(question["question"])
    for i, answer in enumerate(question["answers"]):
      print(f"{i+1}. {answer}")

    # Get the user's answer
    user_answer = input("Enter your answer: ")

    # Check if the user's answer is correct
    if user_answer.lower() == question["correct"].lower():
      # If the answer is correct, increase the money won by the current prize amount
      money_won += 1000
      print(f"Correct! You have won {money_won} Rupees")
    else:
      # If the answer is incorrect, the game ends
      print(f"Wrong answer. You won {money_won} Rupees")
      break
    
# Play the game
play_game()
