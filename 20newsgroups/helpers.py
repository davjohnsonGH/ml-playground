#  try to get some efficenceies
def call_class_one_classifier(model) :
    from sklearn.datasets import fetch_20newsgroups_vectorized
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, classification_report

    # Load the vectorized dataset
    newsgroups = fetch_20newsgroups_vectorized(subset='all')
    X, y = newsgroups.data, newsgroups.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Multinomial Naive Bayes classifier
    clf = model()
    clf.fit(X_train, y_train)

    # Predict on the test set
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=newsgroups.target_names)
    return (
        print(f"Accuracy: {accuracy}"),
        print(f"Classification Report:\n{report}"),
    )

def call_class_two_classifier(model) : 
    from sklearn.datasets import fetch_20newsgroups
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.pipeline import Pipeline
    from sklearn.metrics import accuracy_score, classification_report

    # Step 1: Load the dataset
    categories = None  # Use all categories, or specify a subset like ['comp.graphics', 'sci.space']
    newsgroups_train = fetch_20newsgroups(subset='train', categories=categories, remove=('headers', 'footers', 'quotes'))
    newsgroups_test = fetch_20newsgroups(subset='test', categories=categories, remove=('headers', 'footers', 'quotes'))

    # Step 2: Convert text to numerical features using TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)  # Limit features for efficiency

    # Step 3: Train GradientBoostingClassifier
    clf = model()

    # Step 4: Create a pipeline for convenience
    pipeline = Pipeline([
        ('tfidf', vectorizer),
        ('clf', clf)
    ])

    pipeline.fit(newsgroups_train.data, newsgroups_train.target)

    # Step 5: Evaluate on test data
    y_pred = pipeline.predict(newsgroups_test.data)
    accuracy = accuracy_score(newsgroups_test.target, y_pred)

    # Print evaluation metrics
    return (
        print(f"Accuracy: {accuracy:.4f}"),
        print(classification_report(newsgroups_test.target, y_pred, target_names=newsgroups_test.target_names))
    )

