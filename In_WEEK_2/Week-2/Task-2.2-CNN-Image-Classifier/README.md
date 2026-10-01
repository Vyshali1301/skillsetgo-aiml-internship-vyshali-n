# Task 2.2 - CNN Image Classifier

## Objective
Prepare an image dataset and train a convolutional neural network in PyTorch to classify images.

## Tools Used
- Python
- PyTorch and torchvision
- scikit-learn (metrics, confusion matrix)
- NumPy, Matplotlib
- Jupyter Notebook / Google Colab

## Work Completed
1. Chose CIFAR-10 (10 clear classes) and inspected image size, channels and class balance
2. Displayed sample images
3. Created train/validation/test splits; applied augmentation to training images only
4. Built a small CNN with convolution, ReLU, pooling and a final classifier
5. Trained it while recording training/validation loss and accuracy
6. Inspected correct and incorrect predictions and plotted a confusion matrix
7. Reported test accuracy (not only training accuracy)
8. Saved the trained model together with its preprocessing settings
9. Reloaded the saved model and classified new images with the same preprocessing

## Deliverables
- `notebook.ipynb` - notebook to reproduce everything
- `results/cnn_cifar10.pth` - trained model, `results/preprocessing.json` - preprocessing needed for inference
- `results/cnn_curves.png`, `results/confusion_matrix.png`, `results/sample_predictions.png`
- `results/cnn_results.json` - accuracy / performance report
- `screenshots/` - screenshots of training and predictions

## Key Learnings
- Learned how to use the datasets and google colab to complete the task
- Learned about torch
- CIFAR-10 - 60,000 colour images (32x32 pixels, 3 channels) in 10 classes.

## Submission Status
Status: Completed
Submitted On: 29/09/2026
