"""
A2 - Weak AI vs Strong AI + Narrow vs General AI
Core idea: Narrow AI performs well on its specific trained task but completely fails
when the data shifts even slightly outside its training scope.
"""

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# 1. Define a narrow task and objective
# We generate a simple synthetic dataset (our "training scope")
X_train, y_train = make_classification(
    n_samples=200, 
    n_features=2, 
    n_informative=2, 
    n_redundant=0, 
    random_state=42
)

# 2. Train or program the system to optimize that objective
# This Logistic Regression model is our "Narrow AI" / "Weak AI"
narrow_ai_model = LogisticRegression()
narrow_ai_model.fit(X_train, y_train)

# Let's see how well it performs on the exact data it was designed for
accuracy_in_scope = narrow_ai_model.score(X_train, y_train)

print(f"Narrow AI accuracy INSIDE its trained scope: {accuracy_in_scope * 100}%")

# 3. Deploy within a controlled scope (Testing outside intended scope)
# We test on altered/unseen patterns by simply adding 5 to all our data points.
# A human or Strong AI would easily recognize the same relative patterns, 
# but watch how the Narrow AI handles it.
X_out_of_scope = X_train + 5
accuracy_out_of_scope = narrow_ai_model.score(X_out_of_scope, y_train)

print(f"Narrow AI accuracy OUTSIDE its trained scope: {accuracy_out_of_scope * 100}%")

print("-" * 50)
print("Conclusion: Performance collapsed.")
print("This proves 'Narrow Intelligence': The model cannot generalize or transfer")
print("its knowledge to slightly different or shifted data.")
