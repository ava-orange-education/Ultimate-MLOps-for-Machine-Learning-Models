import logging
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Configure logging
logging.basicConfig(filename='model_training.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
logging.info('Starting model training...')
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
logging.info('Model training completed.')

# Evaluate model
logging.info('Evaluating model...')
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
logging.info(f'Model evaluation completed. Accuracy: {accuracy:.4f}')
