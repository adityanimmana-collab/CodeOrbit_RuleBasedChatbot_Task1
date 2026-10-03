# CodeOrbit Tech - Artificial Intelligence Internship
# Task 1: Rule-Based Chatbot

def chatbot_response(user_input):
    """
    Generate a response based on predefined keywords.
    """

    # Convert the user's input to lowercase
    # so that "Hello" and "hello" are treated the same.
    user_input = user_input.lower().strip()

    # Greeting rules
    if user_input in ["hello", "hi", "hey", "good morning", "good afternoon"]:
        return "Hello! How can I help you today?"

    # Name-related question
    elif "your name" in user_input or "who are you" in user_input:
        return "I am a simple Rule-Based Chatbot created using Python."

    # Help-related question
    elif "help" in user_input:
        return "Sure! You can ask me about my name, my purpose, or say hello."

    # Purpose-related question
    elif "what can you do" in user_input or "your purpose" in user_input:
        return "I can respond to simple questions using predefined rules and keywords."

    # How-are-you question
    elif "how are you" in user_input:
        return "I am doing great! Thanks for asking."

    # Thank-you response
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"

    # Exit rule
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day!"

    # Fallback response for unknown input
    else:
        return "Sorry, I don't understand that. Please try another question."


def main():
    print("=" * 50)
    print("       RULE-BASED CHATBOT")
    print("=" * 50)
    print("Type 'bye', 'exit', or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("Chatbot:", response)

        # Stop the program when the user enters an exit command.
        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


# Start the chatbot program
if __name__ == "__main__":
    main()