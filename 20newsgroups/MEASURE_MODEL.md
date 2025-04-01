# PHASE TWO: Model Evaluation and optimization 

HOW: raw text 

```
sklearn.metrics.accuracy_score
```

**_Accuracy_** measures the proportion of correctly classified instances out of the total instances. It is the simplest evaluation metric and represents the overall effectiveness of a model.

```
sklearn.metrics.classification_report
```
Accuracy is useful when: 
- the class distribution is balanced
- all types of errors (false positives and false negatives) are equally costly.

**_Precision_** measures the proportion of true positive predictions out of all positive predictions (true positives + false positives). It reflects the model's ability to correctly identify only the relevant instances.

Precision is useful when the cost of false positives is high, such as in spam detection, where you want to minimize the risk of incorrectly labeling important emails as spam.

**_Recall_** (also known as Sensitivity or True Positive Rate) measures the proportion of true positive predictions out of all actual positive instances (true positives + false negatives). It indicates the model's ability to capture all relevant instances.

Recall is useful when the cost of false negatives is high, such as in medical diagnostics, where failing to identify a disease could have severe consequences.

**_F1 Score_** is the harmonic mean of Precision and Recall, providing a single metric that balances both. It ranges between 0 and 1, with 1 being perfect precision and recall.

F1 Score is useful when there is an uneven class distribution, or when a balance between precision and recall is required, making it ideal for scenarios where both false positives and false negatives carry significant costs.


HOW: Viusual feedback

```
sklearn.metrics.confusion_matrix
```

**_A confusion matrix_** is a table used to evaluate the performance of a classification model. It shows the number of true positive (TP), false positive (FP), true negative (TN), and false negative (FN) predictions.

- Each row of the matrix represents the number of instances in an actual class
- Each column represents the instances in a predicted class.

The confusion matrix is useful for understanding the specific types of errors a model makes.

- It is especially valuable in multiclass and imbalanced classification problems, as the matrix helps identify classes that are commonly confused by the model, allowing for targeted improvements.
