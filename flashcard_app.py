import tkinter as tk
import json
import os
import random
from tkinter import messagebox
from tkinter import PhotoImage
from data import flashcards as original_flashcards


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")

        # Initializing cards
        self.all_flashcards = original_flashcards
        self.learned_cards = self.load_learned_cards()
        self.flashcards = [card for card in self.all_flashcards if card["id"] not in self.learned_cards]
        random.shuffle(self.flashcards)
        self.current_index = 0
        self.showing_answer = False

        # Card display
        self.card_text = tk.StringVar()
        self.card_label = tk.Label(root, textvariable=self.card_text, font=("Arial", 20), wraplength=400, width=40, height=5)
        self.card_label.pack(pady=20)

        # Bind the click event to flip the card
        self.card_label.bind("<Button-1>", self.flip_card)

        # Create a frame to hold the left and right arrows next to the card display
        arrow_frame = tk.Frame(root)
        arrow_frame.pack(pady=10)

        # Load arrow images from the 'images' folder
        self.prev_arrow = PhotoImage(file="images/left_arrow.png").subsample(3, 3)  # Resize by reducing the size
        self.next_arrow = PhotoImage(file="images/right_arrow.png").subsample(3, 3)  # Resize by reducing the size

        # Left arrow button
        self.prev_button = tk.Button(arrow_frame, image=self.prev_arrow, command=self.prev_card, borderwidth=0, relief="solid")
        self.prev_button.pack(side=tk.LEFT, padx=20)

        # Right arrow button
        self.next_button = tk.Button(arrow_frame, image=self.next_arrow, command=self.next_card, borderwidth=0, relief="solid")
        self.next_button.pack(side=tk.RIGHT, padx=20)

        # Flip card button
        self.flip_button = tk.Button(root, text="Flip Card", command=self.flip_card)
        self.flip_button.pack(pady=10)

        # Other control buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.skip_button = tk.Button(button_frame, text="Mark as Learned", command=self.mark_card_as_learned)
        self.skip_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset Progress", command=self.reset_learned_cards)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.view_all_button = tk.Button(button_frame, text="View All Cards", command=self.view_all_cards)
        self.view_all_button.pack(side=tk.LEFT, padx=5)

        self.add_edit_button = tk.Button(button_frame, text="Add/Edit Card", command=self.add_edit_card)
        self.add_edit_button.pack(side=tk.LEFT, padx=5)

        self.display_flashcard()

    def display_flashcard(self):
        if not self.flashcards:
            self.card_text.set("No cards to show. Reset to review all.")
            return

        self.showing_answer = False
        card = self.flashcards[self.current_index]
        self.card_text.set(f"Q: {card['question']}")

    def flip_card(self, event=None):  # Allow click event or button press
        if not self.flashcards:
            return

        card = self.flashcards[self.current_index]
        if self.showing_answer:
            self.card_text.set(f"Q: {card['question']}")
        else:
            self.card_text.set(f"A: {card['answer']}")
        self.showing_answer = not self.showing_answer

    def prev_card(self):
        if not self.flashcards:
            return

        self.current_index = (self.current_index - 1) % len(self.flashcards)
        self.display_flashcard()

    def next_card(self):
        if not self.flashcards:
            return

        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.display_flashcard()

    def mark_card_as_learned(self):
        if not self.flashcards:
            return

        card_id = self.flashcards[self.current_index]["id"]
        self.learned_cards.add(card_id)
        self.save_learned_cards()
        self.flashcards.pop(self.current_index)

        if self.flashcards:
            self.current_index %= len(self.flashcards)
            self.display_flashcard()
        else:
            self.card_text.set("All cards learned!")

    def reset_learned_cards(self):
        self.learned_cards.clear()
        self.save_learned_cards()
        self.flashcards = self.all_flashcards.copy()
        random.shuffle(self.flashcards)
        self.current_index = 0
        self.display_flashcard()

    def load_learned_cards(self):
        if os.path.exists("learned.json"):
            with open("learned.json", "r") as f:
                return set(json.load(f))
        return set()

    def save_learned_cards(self):
        with open("learned.json", "w") as f:
            json.dump(list(self.learned_cards), f)

    def view_all_cards(self):
        top = tk.Toplevel(self.root)
        top.title("All Flashcards")

        text_widget = tk.Text(top, wrap=tk.WORD, width=60, height=30)
        text_widget.pack(padx=10, pady=10)

        for card in self.all_flashcards:
            status = "✓ Learned" if card["id"] in self.learned_cards else "⏳ Not Learned"
            text_widget.insert(tk.END, f"Q: {card['question']}\n")
            text_widget.insert(tk.END, f"A: {card['answer']}\n")
            text_widget.insert(tk.END, f"Status: {status}\n")
            text_widget.insert(tk.END, "-" * 50 + "\n")

        text_widget.config(state=tk.DISABLED)

    def add_edit_card(self):
        editor = tk.Toplevel(self.root)
        editor.title("Add or Edit Flashcard")

        tk.Label(editor, text="ID (number):").pack()
        id_entry = tk.Entry(editor)
        id_entry.pack()

        tk.Label(editor, text="Question:").pack()
        question_entry = tk.Entry(editor, width=50)
        question_entry.pack()

        tk.Label(editor, text="Answer:").pack()
        answer_entry = tk.Entry(editor, width=50)
        answer_entry.pack()

        def save_card():
            try:
                card_id = int(id_entry.get())
            except ValueError:
                messagebox.showerror("Error", "ID must be a number.")
                return

            question = question_entry.get().strip()
            answer = answer_entry.get().strip()

            if not question or not answer:
                messagebox.showerror("Error", "Question and Answer cannot be empty.")
                return

            # Check if card exists
            for card in self.all_flashcards:
                if card["id"] == card_id:
                    card["question"] = question
                    card["answer"] = answer
                    break
            else:
                self.all_flashcards.append({
                    "id": card_id,
                    "question": question,
                    "answer": answer
                })

            # Refresh and reshuffle cards
            self.reset_learned_cards()
            editor.destroy()

        save_button = tk.Button(editor, text="Save Card", command=save_card)
        save_button.pack(pady=10)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
