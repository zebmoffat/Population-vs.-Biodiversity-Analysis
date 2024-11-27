#### SER494: Experimentation
#### An Analysis on the Relationship between Population and Biodiversity in New York State
#### Zeb Moffat
#### 11/26/24

## Explainable Records
### Record 1
**Raw Data:** 75,600 (Cattaraugus County Population)

Prediction Explanation:** For this population, the model predicts 325.390 for the biodiversity score. The real population score of the county is 345, so it is a good prediction and not far off.

### Record 2
**Raw Data:** 124,891 (Chautauqua County Population)

Prediction Explanation:** For this population, the model predicts 325.508. The real score is 325. These are so close which makes the model basically correct in the domain.

## Interesting Features
### Feature A
**Feature:** 5,082 (Hamilton County Population)

**Justification:** This is an interesting feature due to it being the smallest number in the dataset by far. The next smallest is 26,548. That makes it an outlier and it should have a significant impact on the prediction. Since most other populations are in the 10s or 100s of thousands this tiny 5,082 population should have a big impact.

### Feature B
**Feature:** 2,252,196 (Kings County Population)

**Justification:** This is an interesting feature due to it being the largest number in the dataset. It is about 300,000 larger than the next highest and one of six features above 1,000,000. This makes it an outlier by a significant amount it the dataset, definitely causing an impact on the model.

## Experiments 
### Varying A
**Prediction Trend Seen:** TODO

### Varying B
**Prediction Trend Seen:** TODO

### Varying A and B together
**Prediction Trend Seen:** TODO


### Varying A and B inversely
**Prediction Trend Seen:** TODO

(duplicate above as many times as needed; remove this line when done)