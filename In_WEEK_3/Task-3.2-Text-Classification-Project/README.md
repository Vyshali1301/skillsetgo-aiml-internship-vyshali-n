# Task 3.2 - Text Classification Project

## Objective

Implement a TensorFlow computer-vision or text-classification project on a real dataset.

## Tools Used

- Python
- TensorFlow / Keras
- scikit-learn (metrics, confusion matrix)
- NumPy, Matplotlib
- Jupyter Notebook / Google Colab

## Work Completed

1. Loaded the IMDB movie review dataset (25,000 train / 25,000 test, binary sentiment) and inspected review lengths and class balance.
2. Decoded and read sample reviews to understand the raw data.
3. Padded/truncated reviews to a fixed length for the model.
4. Built an Embedding + Bidirectional LSTM + Dense classifier.
5. Trained with early stopping on validation loss.
6. Evaluated on the held-out test set using a classification report and confusion matrix.
7. Inspected correct and incorrect predictions.
8. Saved the trained model and preprocessing settings, then reloaded them to classify new text.

## Deliverables

- `notebook.ipynb` - full working notebook, reproducible end to end
- `results/text_classifier.keras` - trained model
- `results/text_preprocessing.json` - settings needed to reuse the model
- `results/text_curves.png`
- `results/text_confusion_matrix.png`
- `results/text_results.json` - performance report
- `screenshots/`

## Key Learnings

- Learned how to work with the IMDB movie review dataset for binary sentiment classification.
- Learned how text data can be converted into numerical sequences and padded to a fixed length.
- Learned how Embedding and Bidirectional LSTM layers can be used to understand text sequences.
- Learned how to evaluate a classification model using accuracy, classification reports, and confusion matrices.
- Learned how to save and reload a trained TensorFlow/Keras model for making predictions on new text.

## Submission Status

Status: Completed

Submitted On: 06/10/2026