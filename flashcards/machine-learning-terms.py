import random

# create a flashcards game using the basic machine learning terms and their definitions
flashcards = [
    {"term": "Supervised Learning", "definition": "A type of machine learning where the model learns from labeled data."},
    {"term": "Unsupervised Learning", "definition": "A type of machine learning where the model learns from unlabeled data."},
    {"term": "Overfitting", "definition": "When a model learns the detail and noise in the training data to the extent that it negatively impacts the performance of the model on new data."},
    {"term": "Underfitting", "definition": "When a model is too simple to capture the underlying structure of the data."},
    {"term": "Feature", "definition": "An individual measurable property or characteristic of a phenomenon being observed."},
    {"term": "Label", "definition": "The output or the thing we're predicting."},
    {"term": "Training Data", "definition": "The data used to train the model."},
    {"term": "Test Data", "definition": "The data used to evaluate the model."},
    {"term": "Validation Data", "definition": "The data used to tune the hyperparameters of the model."},
    {"term": "Hyperparameters", "definition": "The settings of the model that are tuned separately from the model parameters."},
    {"term": "Model Parameters", "definition": "The settings or weights learned by the model from the training data."}
]

score = 0

def display_flashcard():
    flashcard = random.choice(flashcards)
    print(f"Definition: {flashcard['definition']}")
    guess = input("Enter your guess for the term: ")
    if guess.lower() == flashcard['term'].lower():
        print("Correct!")
        return 1
    else:
        print(f"Incorrect! The correct term is: {flashcard['term']}")
        return 0

num_flashcards = 10  # Number of flashcards to play

for _ in range(num_flashcards):
    score += display_flashcard()

print(f"Final score: {score}/{num_flashcards}")

# score = 0

# def display_flashcard():
#     flashcard = random.choice(flashcards)
#     print(f"Term: {flashcard['term']}")
#     guess = input("Enter your guess for the definition: ")
#     if guess.lower() == flashcard['definition'].lower():
#         print("Correct!")
#         return 1
#     else:
#         print(f"Incorrect! The correct definition is: {flashcard['definition']}")
#         return 0

# num_flashcards = 5  # Number of flashcards to play

# for _ in range(num_flashcards):
#     score += display_flashcard()

# print(f"Final score: {score}/{num_flashcards}")


