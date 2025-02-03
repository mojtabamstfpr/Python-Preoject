from transformers import pipeline
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
while True:
    user_input = input("You: ")
    response = chatbot(user_input)
    print("Bot:", response[0]['generated_text'])