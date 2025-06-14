import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import pickle

# Correct data with 5 correct (1) and 5 incorrect (0) answers
data = {
    'question': [
        'What is Python?',
        'What is a list in Python?',
        'What is a function?',
        'What is a loop?',
        'What is inheritance?',
        'What is Python?',
        'What is a list in Python?',
        'What is a function?',
        'What is a loop?',
        'What is inheritance?'
    ],
    'answer': [
    
        'Python is a object oriented interpreted language',
        'A list is a collection of items',
        'A function is a block of code',
        'A loop is used to iterate',
        'Inheritance is a feature of OOP',
        'Python is a type of food',
        'List is a person name',
        'Function is just a word',
        'Loop means going in circles',
        'Inheritance means getting rich'
    ],
    'label': [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
}

# Creating dataframe
df = pd.DataFrame(data)

# Vectorizing the text answers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['answer'])
y = df['label']

# Logistic Regression model
model = LogisticRegression()
model.fit(X, y)

# Saving model and vectorizer
with open('logistic_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ Model training complete. Files saved.")