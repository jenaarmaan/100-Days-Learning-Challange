from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import time

# Goal: Compare a statistical ML method vs a simple neural network on the same small dataset.

def main():
    print("--- Day 3: AI History - Statistical vs. Deep Learning ---")

    # Step 1: Create a synthetic dataset
    # 400 samples, 10 features
    X, y = make_classification(n_samples=400, n_features=10, random_state=42)

    # Step 2: Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # --- Comparison 1: Statistical AI (Logistic Regression) ---
    start_time = time.time()
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)
    lr_time = time.time() - start_time
    lr_acc = lr.score(X_test, y_test)

    # --- Comparison 2: Deep Learning style NN (Multi-layer Perceptron) ---
    start_time = time.time()
    nn = MLPClassifier(hidden_layer_sizes=(20,), max_iter=500, random_state=42)
    nn.fit(X_train, y_train)
    nn_time = time.time() - start_time
    nn_acc = nn.score(X_test, y_test)

    # Print Results
    print(f"\n[Statistical AI] Logistic Regression:")
    print(f"Accuracy: {lr_acc:.4f}")
    print(f"Training Time: {lr_time:.4f} seconds")

    print(f"\n[Deep Learning] Neural Network:")
    print(f"Accuracy: {nn_acc:.4f}")
    print(f"Training Time: {nn_time:.4f} seconds")

    # Reflection
    print("\n--- Reflection ---")
    if nn_acc > lr_acc:
        print("The Neural Network outperformed Logistic Regression, showing the power of learning representations.")
    else:
        print("Logistic Regression performed comparably or better, which often happens on small, simple datasets.")
    print("In history, Statistical AI (like LR) dominated until datasets and compute allowed Deep Learning to scale.")

if __name__ == "__main__":
    main()
