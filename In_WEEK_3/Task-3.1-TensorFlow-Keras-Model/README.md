# Task 3.1 - TensorFlow/Keras Model

## Objective

Build and train a TensorFlow/Keras neural network, and compare it with the PyTorch model from Task 2.1.

## Tools Used

- Python
- TensorFlow / Keras
- scikit-learn (dataset and preprocessing)
- Pandas, NumPy, Matplotlib
- Jupyter Notebook / Google Colab

## Work Completed

1. Reused the exact dataset, split, and scaling approach from Task 2.1 (Breast Cancer Wisconsin) for a fair comparison.
2. Built a Keras Sequential model with the same architecture shape as the PyTorch model (30-16-8-1).
3. Compiled the model with binary_crossentropy loss and Adam optimizer.
4. Trained the model using `model.fit()` and plotted training/validation loss and accuracy.
5. Evaluated the model on the validation set and ran sample predictions.
6. Wrote comparison notes against the Task 2.1 PyTorch results.

## Deliverables

- `notebook.ipynb` - TensorFlow notebook with training, evaluation, and comparison notes
- `results/keras_curves.png`
- `results/keras_results.json`
- `screenshots/`

## Key Learnings

- Learned how to build and train a neural network using TensorFlow/Keras.
- Learned how to use the Keras Sequential API to define neural network layers.
- Learned how to compile a model using binary crossentropy loss and the Adam optimizer.
- Learned how to monitor training and validation accuracy and loss using plots.
- Learned how to compare TensorFlow/Keras results with a PyTorch model using the same dataset and architecture for a fair comparison.

## Submission Status

Status: Completed

Submitted On: 06/10/2026