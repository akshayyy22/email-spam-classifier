from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pickle

# Sample data for training
X_train = ["Free money now", "Hello, how are you?", "Win a million dollars", "Call me back"]
y_train = [1, 0, 1, 0]  # 1 for spam, 0 for not spam

# Create a pipeline that includes TF-IDF vectorization and the MultinomialNB classifier
pipeline = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the pipeline on the training data
pipeline.fit(X_train, y_train)

# Save the entire pipeline (TF-IDF vectorizer + MultinomialNB model)
with open('spam_classifier.pkl', 'wb') as model_file:
    pickle.dump(pipeline, model_file)
