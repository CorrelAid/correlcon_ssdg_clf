# Coding Session Tasks

- Tasks are ordered by difficulty
- Either create new notebooks/files or adapt the existing file: 
- You will probably only be able to work on one task, so choose depending on your skill level (but also interest)
- While completing these tasks, pay attention to the performance metrics and the output of codecarbon. 
- I have not completed these tasks myself, so their completion may not lead to performance increases.

## A: 

## B: Explore different preprocessing approaches
- Utilize lemmatization instead of stemming. Use the 
- 

## C: Explore different classification algorithms
- Simply swap out LogisticRegression with suitable methods such as [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) or [MultinomialNB]https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)
- Explore the methods contained in the already installed scikit-multilearn-ng package that do not require problem transformation, see [here](https://scikit-multilearn-ng.github.io/scikit-multilearn-ng/source/skmultilearn.adapt.html#module-skmultilearn.adapt).

## D: Explore classifier chains as a different problem transformation approach
- Use the [classifier chain](https://scikit-multilearn-ng.github.io/scikit-multilearn-ng/source/skmultilearn.problem_transform.html#skmultilearn.problem_transform.ClassifierChain) method of the already installed 
scikit-multilearn-ng package
- Consider taking a look at label dependence (compute correlation) to determine the order of the classifier chain

## E: Develop a binary classifier for a single SDG
- There may be a more suitable dataset here: https://zenodo.org/records/11441197
- Yeet all problem transformation code and only retain the column of the chosen SDG 
- You need to use a different test/train split method, e.g. this [this](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). 
- Feature extraction can remain unchanged

## F: Implement Hyperparameter Optimization
- Hyperparameters depend on the classification algorithm, see [here](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LogisticRegression.html) for logistic regression.
- Most simple method for this is grid search, find an example here: https://scikit-multilearn-ng.github.io/scikit-multilearn-ng/source/skmultilearn.problem_transform.html#examples
- It is potentially challenging to make sklearn external optimization methods compatible with the problem transformation approaches of the package used here, but you could try to implement [Bayesian Optimization](https://github.com/bayesian-optimization/BayesianOptimization)

## G: Explore/Research/Implement ways of predicting resource consuption instead of measuring it while executing
- Implement a simple Multi Layer Perceptron network for (binary or multi label) text classification with pytorch, e.g.:

```
class MLP(nn.Module):
    def __init__(self, input_size, hidden_sizes: tuple, dropout):
        super(MLP, self).__init__()
        layers = []

        # input layer
        layers.append(nn.Linear(input_size, hidden_sizes[0]))
        layers.append(nn.ReLU())
        layers.append(nn.Dropout(dropout))

        # hidden layers
        for i in range(1, len(hidden_sizes)):
            layers.append(nn.Linear(hidden_sizes[i - 1], hidden_sizes[i]))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout))

        layers.append(nn.Linear(hidden_sizes[-1], 1))
        layers.append(nn.Sigmoid())  

        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model(x)
```

- [Use a GPU](https://modal.com/docs/guide/gpu) instead of CPU on modal.
- Use [this](https://github.com/sovrasov/flops-counter.pytorch) package to compute the theoretical amount of multiply-add operations 
- Use available specs of GPUS, e.g. [T4](https://www.nvidia.com/en-us/data-center/tesla-t4), to estimate power consumption and carbon emissions
    