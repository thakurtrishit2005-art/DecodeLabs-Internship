# Project 2: Data Classification Using AI
### Domain: Supervised Machine Learning & Diagnostic Performance
**Developer:** Trishi Thakur  
**Batch:** 2026  
**Provider:** DecodeLabs Industrial Training Track  

---

## Project Overview
This repository contains the official implementation of **Project 2: Data Classification Using AI**. Transitioning away from hardcoded heuristic rules, this milestone enters the domain of **Supervised Machine Learning**. 

The goal is to implement, evaluate, and tune a **K-Nearest Neighbors (KNN)** classification pipeline using the classic Iris Flower benchmark dataset. By analyzing historical geometric measurements (sepal and petal dimensions), the model automatically derives complex decision boundaries to accurately categorize unseen biological instances.

---

## Architectural Framework: Input -> Process -> Output (IPO)
The data science pipeline structured in this project follows a strict execution flow:

1. **Input (Data Ingestion & Engineering):**
   * Loads the balanced 150-sample Iris benchmarking dataset (3 distinct flower classes).
   * Shuffles and splits data into a **80% Training subset** (for pattern recognition) and a **20% Testing subset** (for strict validation) to strictly avoid ordering bias.
   * Leverages `StandardScaler` to enforce normalization (Mean = 0, Variance = 1) across features, neutralizing scale discrepancies and preventing distance metric distortions.
2. **Process (Algorithmic Logic & Parameter Tuning):**
   * Evaluates algorithmic error rates iteratively across neighborhood intervals ($K = 1$ to $20$) to plot an **Elbow Curve**.
   * Identifies the optimal tuning anchor ($K = 5$) to balance the model cleanly against underfitting and overfitting.
   * Trains the finalized `KNeighborsClassifier` mathematical framework on scaled parameters.
3. **Output (Diagnostic Validation):**
   * Applies the trained model to predict classifications for unseen testing samples.
   * Validates prediction integrity through multi-dimensional matrices, recording a **raw classification accuracy** and detailed classification breakdowns.

---

## Core Project Files
* **`Project-2-Data-Classification-Iris flower dataset.ipynb`** — The production-grade Jupyter Notebook containing the full end-to-end data pipelines, scaling transformations, hyperparameter elbow plotting, and statistical diagnostic visualizations.

---

## Performance Indicators & Metrics Covered
* **Hyperparameter Selection (Elbow Curve):** Minimizes proximity error cleanly prior to performance degradation spikes.
* **Confusion Matrix Visualization:** Maps true historical classes against AI logic predictions to isolate Type I (False Alarm) and Type II (Missed Detection) anomalies.
* **Strategic Trade-Off Optimization:** Computes precision (trustworthiness), recall (sensitivity), and the balanced **F1-Score (Harmonic Mean)** for all target biological classes (`setosa`, `versicolor`, `virginica`).

---

## How To Setup & Run the Project
Ensure you have a configured Python environment with standard data science dependencies installed.

### 1. Ingestion Requirements:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### 2. Execution Flow:
Open your terminal window inside the root directory and start your notebook platform or execute via Jupyter:
```bash
jupyter notebook "Project-2-Data-Classification-Iris flower dataset.ipynb"
```

---
*Developed as part of the DecodeLabs AI Engineering Framework Portfolio.*