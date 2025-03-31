# Will experiment with classifier models with this particular data set.
This data set has the make up that will lend itself to using classifier models.
Thgs is because the data has labels or features that can be mapped to from intelegent ml reasioning after discovery through the training dataset.



Types of classifier models:

```
[x] naive bayes
[x] k-nearest neighbors
[x] logistic regression
[x] linear regression
[x] SVM (Supprt Vector Machines)
- Adaptive Boosting
- Decision Trees
- Random Forests
[x] Gradient Boosting Machines
```

Will rank and tweak with hyperparameters to come up with the best positioned model

No hyperparameters optimization
```
- naive bayes: Accuracy: 0.8
- k-nearest neighbors: 0.6222811671087534
- logistic regression: 0.8241379310344827
- linier regression:
    Mean absolute error (MAE): 2.83
    Mean Squared Error (MAE): 15.18
    R-squared (r2): 0.51
    Root Mean Squared Error (rmse): 3.90
- SVM (Supprt Vector Machines):  0.8655172413793103
- Adaptive Boosting: SKIP
- Decision Trees: Accuracy: 0.3467
- Random Forests: Accuracy: 0.5905
- Gradient Boosting Machines: Accuracy: 0.5749
```

NOTES:
```
Lots of repetable code here, can combine:

+++ class one START +++
naive bayes
k-nearest neighbors
logistic regression
linier regression (exception to metrics print)
SVM
+++ class one END +++

+++ class two START +++
Decision Trees
Random Forests
Gradient Boosting Machines
+++ class two END +++
```