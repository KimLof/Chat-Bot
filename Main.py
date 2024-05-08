import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import datetime
import tkinter as tk
from tkinter import ttk
from responses import responses

# Responses if user input does not match any keywords
responses["default"] = ["I'm sorry, I don't understand that question.",
                        "I'm not sure I know what you're talking about.",
                        "Can you rephrase that?",
                        "I'm not programmed to answer that question.",
                        "I don't have an answer for that.",
                        "I'm sorry, I'm just a simple bot."]

# Download NLTK resources if you haven't already
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Function to preprocess user input
def preprocess(sentence):
    # Convert to lowercase and remove punctuation
    sentence = sentence.lower()
    sentence = sentence.replace("?", "").replace("!", "").replace("'", "")
    # Tokenize and tag parts of speech
    tokens = word_tokenize(sentence)
    tagged_tokens = pos_tag(tokens)
    return tagged_tokens

# Function to generate bot response
def respond(user_input):
    # Preprocess user input
    user_tokens = preprocess(user_input)
    # Check for keywords in responses
    for key in responses:
        key_tokens = preprocess(key)
        if all(token in user_tokens for token in key_tokens):
            return responses[key]
    return random.choice(responses["default"])

# Function to send user message and display bot response
def send_message():
    user_input = entry.get()
    messages_list.insert(tk.END, "You: " + user_input)
    response = respond(user_input)
    if isinstance(response, list):
        bot_response = random.choice(response)
    else:
        bot_response = response
    messages_list.insert(tk.END, "Bot: " + bot_response)
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("ChatBot")

# Configure style for the window
style = ttk.Style()
style.theme_use("clam")  # Change theme to one of the available ones

# Create frames
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill='both', expand=True)

# Create scrollable chat history
scrollbar = ttk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

messages_list = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=50, height=15, font=('Arial', 12))
messages_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=messages_list.yview)

# Create input field and send button
entry = ttk.Entry(root, width=50, font=('Arial', 12))
entry.pack(pady=10)

send_button = ttk.Button(root, text="Send", command=send_message)
send_button.pack()

# Bind Enter key to send_message function
root.bind('<Return>', lambda event=None: send_message())

# Start the GUI main loop
root.mainloop()
