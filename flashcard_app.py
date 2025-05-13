import tkinter as tk
from tkinter import messagebox
import random
from data import flashcards

random.shuffle(flashcards)

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")

        self.index = 0
        self.showing_answer = False

        self.card_text = tk.StringVar()
        self.card_text.set(flashcards[self.index]['question'])

        self.card_label = tk.Label(root, textvariable=self.card_text, font=("Arial", 20), width=40, height=5, relief="ridge", wraplength=400)
        self.card_label.pack(pady=20)
        self.card_label.bind("<Button-1>", self.flip_card)

        self.counter_text = tk.StringVar()
        self.counter_label = tk.Label(root, textvariable=self.counter_text, font=("Arial", 12))
        self.counter_label.pack()
        self.update_question_number()

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.prev_btn = tk.Button(btn_frame, text="Previous", command=self.prev_card)
        self.prev_btn.grid(row=0, column=0, padx=10)

        self.next_btn = tk.Button(btn_frame, text="Next", command=self.next_card)
        self.next_btn.grid(row=0, column=1, padx=10)

        self.shuffle_btn = tk.Button(btn_frame, text="Randomize", command=self.shuffle_cards)
        self.shuffle_btn.grid(row=0, column=2, padx=10)

        # Entry fields for adding/editing flashcards
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=10)

        tk.Label(self.entry_frame, text="Question:").grid(row=0, column=0)
        self.q_entry = tk.Entry(self.entry_frame, width=40)
        self.q_entry.grid(row=0, column=1)

        tk.Label(self.entry_frame, text="Answer:").grid(row=1, column=0)
        self.a_entry = tk.Entry(self.entry_frame, width=40)
        self.a_entry.grid(row=1, column=1)

        tk.Button(self.entry_frame, text="Add Card", command=self.add_card).grid(row=2, columnspan=2, pady=5)
        tk.Button(self.entry_frame, text="Edit Card", command=self.edit_card).grid(row=3, columnspan=2, pady=5)

    def flip_card(self, event):
        if self.showing_answer:
            self.card_text.set(flashcards[self.index]['question'])
        else:
            self.card_text.set(flashcards[self.index]['answer'])
        self.showing_answer = not self.showing_answer

    def next_card(self):
        if self.index < len(flashcards) - 1:
            self.index += 1
            self.card_text.set(flashcards[self.index]['question'])
            self.showing_answer = False
            self.update_question_number()

    def prev_card(self):
        if self.index > 0:
            self.index -= 1
            self.card_text.set(flashcards[self.index]['question'])
            self.showing_answer = False
            self.update_question_number()

    def add_card(self):
        question = self.q_entry.get()
        answer = self.a_entry.get()
        if question and answer:
            flashcards.append({"question": question, "answer": answer})
            self.index = len(flashcards) - 1
            self.card_text.set(question)
            self.showing_answer = False
            self.update_question_number()
            self.q_entry.delete(0, tk.END)
            self.a_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill in both question and answer.")

    def edit_card(self):
        question = self.q_entry.get()
        answer = self.a_entry.get()
        if question and answer and flashcards:
            flashcards[self.index] = {"question": question, "answer": answer}
            self.card_text.set(question)
            self.showing_answer = False
            self.update_question_number()
        else:
            messagebox.showwarning("Input Error", "Please fill in both question and answer.")

    def shuffle_cards(self):
        random.shuffle(flashcards)
        self.index = 0
        self.card_text.set(flashcards[self.index]['question'])
        self.showing_answer = False
        self.update_question_number()

    def update_question_number(self):
        self.counter_text.set(f"Card {self.index + 1} of {len(flashcards)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
