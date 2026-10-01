# Task 2.1 - Neural Network in PyTorch

## Objective
Implement a feed-forward neural network in PyTorch covering tensors, datasets, dataloaders and loss functions,
and understand the training loop step by step.

## Tools Used
- Python
- PyTorch
- scikit-learn (dataset and preprocessing)
- Pandas, NumPy, Matplotlib
- Jupyter Notebook / Google Colab

## Work Completed
1. Loaded the Breast Cancer Wisconsin dataset and checked shape and class balance
2. Split into train/validation and scaled features (scaler fitted on training data only)
3. Converted features and targets to tensors with correct shapes and data types
4. Created a Dataset and DataLoader for mini-batch training
5. Defined a small `torch.nn.Module` (30-16-8-1) with ReLU activations
6. Chose BCEWithLogitsLoss and Adam, and explained the choice
7. Wrote the training loop (zero_grad, forward, loss, backward, step)
8. Evaluated without updating weights and tracked training/validation loss
9. Ran sample predictions and compared them with the actual targets

## Deliverables
- `notebook.ipynb` - PyTorch training notebook (dataset setup, model, training loop, evaluation, interpretation)
- `results/loss_curve.png`, `results/results.json`
- `screenshots/` - screenshots of training output

## Key Learnings
- Learned how to use the datasets and google colab to complete the task
- Learned about torch
- Learned about binary classification on the Breast Cancer Wisconsin dataset (30 numeric features per patient sample, label = malignant or benign). 

## Submission Status
Status: Completed
Submitted On: 29/09/2026
