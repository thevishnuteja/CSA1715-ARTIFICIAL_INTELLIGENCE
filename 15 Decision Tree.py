import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

def entropy(y):
    _, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    return -np.sum(probabilities * np.log2(probabilities + 1e-10))

def information_gain(X, y, feature, threshold):
    left_indices = X[:, feature] < threshold
    right_indices = ~left_indices
    left_entropy = entropy(y[left_indices])
    right_entropy = entropy(y[right_indices])
    left_weight = np.sum(left_indices) / len(y)
    right_weight = 1 - left_weight
    return entropy(y) - (left_weight * left_entropy + right_weight * right_entropy)

def find_best_split(X, y):
    best_gain = 0
    best_feature = None
    best_threshold = None
    for feature in range(X.shape[1]):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            gain = information_gain(X, y, feature, threshold)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = threshold
    return best_feature, best_threshold

def fit(X, y, max_depth):
    if max_depth == 0 or len(np.unique(y)) == 1:
        return Node(value=np.mean(y))

    feature, threshold = find_best_split(X, y)
    if feature is None:
        return Node(value=np.mean(y))

    left_indices = X[:, feature] < threshold
    right_indices = ~left_indices
    left_subtree = fit(X[left_indices], y[left_indices], max_depth - 1)
    right_subtree = fit(X[right_indices], y[right_indices], max_depth - 1)

    return Node(feature=feature, threshold=threshold, left=left_subtree, right=right_subtree)

def predict_one(x, tree):
    if tree.value is not None:
        return tree.value
    if x[tree.feature] < tree.threshold:
        return predict_one(x, tree.left)
    else:
        return predict_one(x, tree.right)

def predict(X, tree):
    return [predict_one(x, tree) for x in X]

# Example usage
X = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])
y = np.array([0, 0, 1, 1])
tree = fit(X, y, max_depth=2)
print(predict(X, tree))
