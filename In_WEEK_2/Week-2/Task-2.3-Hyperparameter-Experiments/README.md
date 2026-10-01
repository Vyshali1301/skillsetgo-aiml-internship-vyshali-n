# Task 2.3 - Hyperparameter Experimentation

## Objective
Run controlled experiments varying optimizer, learning rate, batch size and epochs, and compare the outcomes.

## Tools Used
- Python
- PyTorch and torchvision
- Pandas, NumPy, Matplotlib
- Jupyter Notebook / Google Colab

## Work Completed
1. Fixed the dataset (CIFAR-10 subset), architecture and evaluation procedure
2. Defined a baseline run (R01) and changed one hyperparameter at a time
3. Tested several learning rates, two/three optimizers, several batch sizes and a longer epoch run
4. Kept an experiment table with run ID, settings, metrics and notes
5. Checked validation behaviour (not only training accuracy)
6. Chose the final configuration after reviewing the whole table and re-ran it with 3 seeds

## Deliverables
- `notebook.ipynb` - experiment code (reproduces every run)
- `results/experiment_log.csv` - experiment log with comparison table and notes
- `results/val_acc_by_run.png`, `results/epochs_curve_R10.png`
- `results/final_config.json` - final configuration and seed check
- `screenshots/`

## Key Learnings
- (write 3-5 points in your own words)

## Submission Status
Status: Pending
Submitted On:
