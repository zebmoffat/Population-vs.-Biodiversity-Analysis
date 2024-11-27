#### SER494: Machine Learning Evaluation
#### An Analysis on the Relationship between Population and Biodiversity in New York State
#### Zeb Moffat
#### 11/26/24

## Evaluation Metrics
### Metric 1
**Name:** Mean Squared Error

**Choice Justification:** Mean squared error is useful in finding large errors from the model. It takes large errors and enphasizes them, making them easy to find. It is especially good at finding outliers.

**Interpretation:** The MSE for my model is 5962.5323. This is decent and much better than the alternative models scores.

### Metric 2
**Name:** Mean Average Error

**Choice Justification:** Mean average error is useful in finding all errors. It is more balanced and doesn't point out outliers as much. The lower the MAE, the better overall the model is.

**Interpretation:** The MAE for my model was 17.4677, this is very low for my dataset and I believe is an indicator of how good the model is.

## Alternative Models
### Alternative 1
**Construction:** This model was created with sklearn Lasso Regression.
 
**Evaluation:** This model scored a 8325.0993 MSE and 67.7205 MAE. These scores happened to be very similar to the other alternative models. An okay score but not as good as the Decision Tree Regression model.

### Alternative 2
**Construction:** This model was created with sklearn Linear Regression.

**Evaluation:** This model scored a 8325.0993 MSE and 67.7205 MAE. This is the same as the Lasso regression, at least for the first few decimal places. All three alternatives were so similar and outclassed by Decision Tree Regression.

### Alternative 3
**Construction:**  This model was created with sklearn Ridge Regression.

**Evaluation:** This model performed similarly to the other two with an 8325.09926 MSE and 67.7204 MAE.

## Best Model

**Model:** Decision Tree Regression

Decision Tree Regression turned out to be the best model for my dataset. It beat three other types of regression by a sizable margin so I decided I had to use it as the main model.