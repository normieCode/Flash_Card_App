from tkinter import *
import csv
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn = []
random_enabled = True  # Variable to track the randomization state
current_index = 0  # Index for the current card when randomization is off
cards_list = []  # List to keep track of shuffled cards
MAX_LINE_LENGTH = 20  # Maximum characters per line for wrapping

# Read data from CSV file
def read_csv(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            if data:
                global front_header, back_header
                front_header, back_header = reader.fieldnames[:2]  # Get the first two column headers
            return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

# Initialize data
learn = read_csv("Learn.csv")

def initialize_cards():
    global cards_list
    cards_list = learn.copy()  # Make a copy of the list of cards
    random.shuffle(cards_list)  # Shuffle the list

# Wraps text to ensure max length
def wrap_text(text, max_length):
    words = text.split()
    wrapped_text = ""
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_length:
            current_line += " " + word if current_line else word
        else:
            wrapped_text += current_line + "\n"
            current_line = word
    
    wrapped_text += current_line
    return wrapped_text

# Next card function
def next_card():
    global current_card, current_index, cards_list
    if learn:  # Ensure there are words to learn
        if random_enabled:
            if not cards_list:  # If no cards left, reinitialize
                initialize_cards()
            current_card = cards_list.pop()  # Get and remove a card from the shuffled list
        else:
            # Ensure index is within range
            if current_index >= len(learn):
                current_index = 0  # Reset index if list length exceeded
            current_card = learn[current_index]
            current_index += 1

        # Retrieves the first side from current_card and wraps the text 
        learn_text = wrap_text(current_card.get(front_header, "Key not found"), MAX_LINE_LENGTH)
        canvas.itemconfig(card_title, text=front_header, fill="black")
        canvas.itemconfig(card_word, text=learn_text, fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
    else:
        canvas.itemconfig(card_title, text="No words left", fill="black")
        canvas.itemconfig(card_word, text="", fill="black")
        canvas.itemconfig(card_background, image=card_front_img)

# Toggles the display of the flashcard between Spanish and English (or other)
def flip_card():
    if current_card: 
        if canvas.itemcget(card_title, "text") == front_header:
            english_text = wrap_text(current_card.get(back_header, "Key not found"), MAX_LINE_LENGTH)
            canvas.itemconfig(card_title, text=back_header, fill="white")
            canvas.itemconfig(card_word, text=english_text, fill="white")
            canvas.itemconfig(card_background, image=card_back_img)
        else:
            learn_text = wrap_text(current_card.get(front_header, "Key not found"), MAX_LINE_LENGTH)
            canvas.itemconfig(card_title, text=front_header, fill="black")
            canvas.itemconfig(card_word, text=learn_text, fill="black")
            canvas.itemconfig(card_background, image=card_front_img)

# Random toggle function 
def toggle_random():
    global random_enabled
    random_enabled = not random_enabled
    if random_enabled:
        initialize_cards()  # Initialize and shuffle cards when randomization is enabled
        toggle_button.config(image=random_on_img) # Update button image to show random is on
    else:
        toggle_button.config(image=random_off_img) # Update button image to show random is off

# Builds window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Window dimensions card and text position
canvas = Canvas(width=800, height=600)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 100, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Flip button position 
flip_image = PhotoImage(file="flip.png")
flip_button = Button(image=flip_image, highlightthickness=0, command=flip_card)
flip_button.grid(row=1, column=1)

# Next button position
next_image = PhotoImage(file="next.png")
next_button = Button(image=next_image, highlightthickness=0, command=next_card)
next_button.grid(row=1, column=0)

# Random button image and position
random_on_img = PhotoImage(file="random_on.png") # Image for when random is enabled
random_off_img = PhotoImage(file="random_off.png") # Image for when random is disabled
toggle_button = Button(image=random_on_img, highlightthickness=0, command=toggle_random)
toggle_button.grid(row=2, column=0, columnspan=2)

# Button labels
flip_label = Label(window, text="Flip", font=("Arial", 18), bg=BACKGROUND_COLOR)
flip_label.grid(row=2, column=1)

next_label = Label(window, text="Next", font=("Arial", 18), bg=BACKGROUND_COLOR)
next_label.grid(row=2, column=0)

initialize_cards() # Initialize and shuffle cards on startup
next_card()

window.mainloop()
