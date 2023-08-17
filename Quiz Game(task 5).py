import tkinter as tk
from tkinter import messagebox
import random

# Define quiz questions and answers for different topics
quiz_questions = {
    "movies": [
        {
            "question": "Which movie features a young lion prince named Simba?",
            "options": ["Finding Nemo", "The Lion King", "Toy Story", "Shrek", "Frozen"],
            "correct_answer": "The Lion King"
        },
        {
            "question": "Who played the role of Iron Man in the Marvel Cinematic Universe?",
            "options": ["Chris Hemsworth", "Chris Evans", "Robert Downey Jr.", "Mark Ruffalo", "Tom Holland"],
            "correct_answer": "Robert Downey Jr."
        },
        {
            "question": "Which movie is known for the quote 'May the Force be with you'?",
            "options": ["Star Wars", "The Matrix", "Back to the Future", "Avatar", "Jurassic Park"],
            "correct_answer": "Star Wars"
        },
        {
            "question": "In the movie 'Titanic', which actor played the role of Jack Dawson?",
            "options": ["Leonardo DiCaprio", "Tom Hanks", "Brad Pitt", "Johnny Depp", "Matt Damon"],
            "correct_answer": "Leonardo DiCaprio"
        },
        {
            "question": "What is the highest-grossing animated movie of all time?",
            "options": ["The Lion King", "Frozen", "Toy Story 4", "Finding Dory", "Minions"],
            "correct_answer": "Frozen"
        },
        {
            "question": "Which Disney princess is known for having a magical glass slipper?",
            "options": ["Cinderella", "Belle", "Ariel", "Snow White", "Jasmine"],
            "correct_answer": "Cinderella"
        },
        {
            "question": "Who directed the movie 'Avatar'?",
            "options": ["Steven Spielberg", "Christopher Nolan", "James Cameron", "Peter Jackson", "Tim Burton"],
            "correct_answer": "James Cameron"
        },
        {
            "question": "Which superhero movie features the fictional African country of Wakanda?",
            "options": ["Spider-Man: Far From Home", "Black Panther", "Guardians of the Galaxy", "Wonder Woman", "Doctor Strange"],
            "correct_answer": "Black Panther"
        },
        {
            "question": "Which 1980 musical film is based on the Broadway musical of the same name and follows the story of a young woman who dreams of stardom?",
            "options": ["Fame", "Grease", "Flashdance", "Annie", "The Sound of Music"],
            "correct_answer": "Fame"
        },
        {
            "question": "What is the name of the fictional wizarding school in the 'Harry Potter' movie series?",
            "options": ["Hogwarts", "Durmstrang", "Beauxbatons", "Ilvermorny", "Castelobruxo"],
            "correct_answer": "Hogwarts"
        },
    ],
    "galaxies": [
        {
            "question": "What is the closest galaxy to our Milky Way?",
            "options": ["Andromeda Galaxy", "Triangulum Galaxy", "Whirlpool Galaxy", "Centaurus A", "Messier 87"],
            "correct_answer": "Andromeda Galaxy"
        },
        {
            "question": "Which galaxy contains the supermassive black hole M87*?",
            "options": ["Milky Way", "Sombrero Galaxy", "Black Eye Galaxy", "Cigar Galaxy", "Virgo A"],
            "correct_answer": "Virgo A"
        },
        {
            "question": "What is the largest galaxy in the observable universe?",
            "options": ["Milky Way", "IC 1101", "Andromeda Galaxy", "Messier 87", "Whirlpool Galaxy"],
            "correct_answer": "IC 1101"
        },
        {
            "question": "Which galaxy is famous for its beautiful spiral arms and has a nickname 'Whirlpool Galaxy'?",
            "options": ["Andromeda Galaxy", "Triangulum Galaxy", "Whirlpool Galaxy", "Black Eye Galaxy", "Messier 87"],
            "correct_answer": "Whirlpool Galaxy"
        },
        {
            "question": "What is the smallest galaxy in the Local Group of galaxies?",
            "options": ["Sagittarius Dwarf Elliptical Galaxy", "Boötes I", "Leo II", "Draco Dwarf Galaxy", "Canis Major Dwarf Galaxy"],
            "correct_answer": "Boötes I"
        },
        {
            "question": "Which galaxy is known for its stunning ring structure and is often referred to as the 'Cartwheel Galaxy'?",
            "options": ["Andromeda Galaxy", "Whirlpool Galaxy", "Black Eye Galaxy", "Centaurus A", "Cartwheel Galaxy"],
            "correct_answer": "Cartwheel Galaxy"
        },
        {
            "question": "What is the name of the barred spiral galaxy that is home to the famous Sombrero Galaxy?",
            "options": ["Andromeda Galaxy", "Triangulum Galaxy", "Black Eye Galaxy", "Sombrero Galaxy", "Messier 87"],
            "correct_answer": "Sombrero Galaxy"
        },
        {
            "question": "Which galaxy is famous for its enormous central black hole and the first-ever image of a black hole's event horizon?",
            "options": ["Milky Way", "Andromeda Galaxy", "Messier 87", "Triangulum Galaxy", "Whirlpool Galaxy"],
            "correct_answer": "Messier 87"
        },
        {
            "question": "What is the name of the galaxy cluster that contains the Milky Way and the Andromeda Galaxy?",
            "options": ["Local Group", "Virgo Cluster", "Coma Cluster", "Fornax Cluster", "Hercules Cluster"],
            "correct_answer": "Local Group"
        },
        {
            "question": "Which galaxy is nicknamed the 'Black Eye Galaxy' due to the dark band of dust that obscures part of its bright nucleus?",
            "options": ["Andromeda Galaxy", "Triangulum Galaxy", "Black Eye Galaxy", "Whirlpool Galaxy", "Messier 87"],
            "correct_answer": "Black Eye Galaxy"
        },
    ],
}

class QuizGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("800x600")  # Set window size
        
        self.score_movies = 0
        self.score_galaxies = 0
        self.current_question = 0
        self.selected_topic = None
        
        self.welcome_label = tk.Label(root, text="Welcome to the Quiz Game!", font=("Helvetica", 18))
        self.welcome_label.pack(pady=20)
        
        self.rules_label = tk.Label(root, text="Select a topic, answer 10 questions, and see your score!", font=("Helvetica", 14))
        self.rules_label.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start", font=("Helvetica", 12), width=20, height=2, bg="#f0f0f0", command=self.show_topics)
        self.start_button.pack(pady=20)
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        
        self.options = []
        self.retry_button = tk.Button(root, text="Retry", font=("Helvetica", 12), width=20, height=2, bg="#f0f0f0", state="disabled", command=self.retry_quiz)
        self.retry_button.pack(pady=20)

    def show_topics(self):
        self.start_button.pack_forget()
        self.welcome_label.pack_forget()
        self.rules_label.pack_forget()
        
        self.topic_label = tk.Label(self.root, text="Select your favorite topic:", font=("Helvetica", 16))
        self.topic_label.pack(pady=20)
        
        self.topic_options = tk.StringVar()
        self.topic_options.set("Select Topic")
        self.topic_menu = tk.OptionMenu(self.root, self.topic_options, "Movies", "Galaxies")
        self.topic_menu.config(font=("Helvetica", 12), width=20)
        self.topic_menu.pack(pady=10)
        
        self.start_quiz_button = tk.Button(self.root, text="Start Quiz", font=("Helvetica", 12), width=20, height=2, bg="#f0f0f0", command=self.start_quiz)
        self.start_quiz_button.pack(pady=10)

    def start_quiz(self):
        self.selected_topic = self.topic_options.get().lower()
        if self.selected_topic in quiz_questions:
            self.topic_label.pack_forget()
            self.topic_menu.pack_forget()
            self.start_quiz_button.pack_forget()
            self.current_question = 0
            self.next_question()
        else:
            messagebox.showwarning("Invalid Topic", "Please select a valid topic to start the quiz.")

    def next_question(self):
        if self.selected_topic is None:
            return
        if self.current_question < len(quiz_questions[self.selected_topic]):
            question_data = quiz_questions[self.selected_topic][self.current_question]
            self.question_label.config(text=question_data["question"])
            for option in self.options:
                option.destroy()
            self.options.clear()
            option_color = "#f0f0f0"
            for i, option_text in enumerate(question_data["options"]):
                option = tk.Button(self.root, text=option_text, font=("Helvetica", 12), width=40, height=2, bg=option_color, command=lambda i=i: self.check_answer(i))
                option.pack(pady=5)
                self.options.append(option)
            self.retry_button.config(state="disabled")
        else:
            self.retry_button.config(state="normal")
            self.show_final_results()

    def check_answer(self, selected_option):
        question_data = quiz_questions[self.selected_topic][self.current_question]
        if question_data["options"][selected_option] == question_data["correct_answer"]:
            if self.selected_topic == "movies":
                self.score_movies += 1
            elif self.selected_topic == "galaxies":
                self.score_galaxies += 1
            self.feedback_message("Correct!")
        else:
            self.feedback_message(f"Wrong! The correct answer is: {question_data['correct_answer']}")
        self.current_question += 1
        self.next_question()

    def feedback_message(self, message):
        self.question_label.config(text=message)

    def show_final_results(self):
        if self.selected_topic == "movies":
            performance_message = f"Movie Quiz completed! Your score is: {self.score_movies}/10"
        elif self.selected_topic == "galaxies":
            performance_message = f"Galaxies Quiz completed! Your score is: {self.score_galaxies}/10"
        self.question_label.config(text=performance_message)

    def retry_quiz(self):
        self.score_movies = 0
        self.score_galaxies = 0
        self.current_question = 0
        self.selected_topic = None
        self.question_label.config(text="")
        for option in self.options:
            option.destroy()
        self.options.clear()
        self.retry_button.pack_forget()
        self.show_topics()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()
