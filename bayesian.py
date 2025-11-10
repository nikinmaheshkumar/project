from collections import defaultdict, Counter
class BayesianClassifier:
    def __init__(self, smooth=1e-6):
        self.smooth = float(smooth)
        self.label_counts = Counter()
        self.feature_counts = defaultdict(Counter)
        self.total = 0
    def train(self, data):
        for features, label in data:
            self.total += 1
            self.label_counts[label] += 1
            for i, v in enumerate(features):
                self.feature_counts[i][(v, label)] += 1
    def predict(self, features):
        best_label, best_score = None, -1.0
        for label, lcount in self.label_counts.items():
            score = lcount / self.total
            for i, v in enumerate(features):
                cnt = self.feature_counts[i].get((v, label), 0)
                score *= (cnt / lcount) if cnt else self.smooth
            if score > best_score:
                best_label, best_score = label, score
        return best_label
if __name__ == "__main__":
    data = [
        ([1, 'green'], 'A'),
        ([2, 'red'],   'B'),
        ([1, 'red'],   'A'),
        ([2, 'green'], 'B'),
    ]
    clf = BayesianClassifier()
    clf.train(data)
    print("Prediction for [1, 'green']:", clf.predict([1, 'green']))