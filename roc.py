import numpy as np
import matplotlib.pyplot as plt


def plot_pre_roc_curve():
    similarity_scores = np.array([
        [0.3598, 0.8008, 0.8113, 0.7849, 0.8222, 0.8784],
        [0.8020, 0.4537, 0.8047, 0.8131, 0.8141, 0.8863],
        [0.8130, 0.8082, 0.3683, 0.8118, 0.8310, 0.9065],
        [0.7808, 0.8264, 0.8123, 0.4509, 0.7992, 0.9118],
        [0.8179, 0.8208, 0.8312, 0.8033, 0.3607, 0.9200],
        [0.8812, 0.8851, 0.9022, 0.9047, 0.9192, 0.4997]
    ])

    threshold_range = np.arange(0.1, 1.0, 0.1)
    tpr_values = []
    fpr_values = []
    fmr_values = []
    fnmr_values = []

    for threshold in threshold_range:
        positive_instances = similarity_scores >= threshold
        negative_instances = similarity_scores < threshold

        true_positives = np.sum(positive_instances)
        false_positives = np.sum(negative_instances)
        false_negatives = np.sum(similarity_scores < threshold)
        true_negatives = np.sum(similarity_scores >= threshold)

        tpr = true_positives / (true_positives + false_negatives)
        fpr = false_positives / (false_positives + true_negatives)

        # Calculate False Match Rate (FMR) and False Non-Match Rate (FNMR)
        fmr = false_positives / (true_negatives + false_positives)
        fnmr = false_negatives / (true_positives + false_negatives)

        tpr_values.append(tpr)
        fpr_values.append(fpr)
        fmr_values.append(fmr)
        fnmr_values.append(fnmr)
    fmr = np.sum(fmr_values) / len(fmr_values)
    fnmr = np.sum(fnmr_values) / len(fnmr_values)
    print(f"Average FMR: {fmr:.2f} | Average FNMR: {fnmr:.2f}")

    # Plot ROC Curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr_values, tpr_values, marker='o', linestyle='-', label='ROC Curve')
    plt.plot(fmr_values, tpr_values, marker='o', linestyle='-', label='FMR vs TPR')
    plt.plot(fnmr_values, 1 - np.array(tpr_values), marker='o', linestyle='-', label='FNMR vs 1-TPR')
    plt.xlabel('False Match Rate (FMR) / False Non-Match Rate (FNMR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.title('ROC Curve')
    plt.grid(True)
    plt.legend()
    plt.show()

