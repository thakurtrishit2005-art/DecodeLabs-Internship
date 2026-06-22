# Project 3: AI Recommendation Logic
### Domain: Content-Based Filtering & Natural Language Vector Spaces
**Developer:** Trishi Thakur  
**Batch:** 2026  
**Provider:** DecodeLabs Industrial Training Track  

---

## Project Overview
This repository contains the official implementation of **Project 3: AI Recommendation Logic**[cite: 6]. Stepping away from passive classification, this project implements a production-ready **Tech Stack Recommender System** built to mitigate the "Choice Overload" problem[cite: 6].

Using a content-based filtering approach, the application bridges the gap between qualitative text parameters and structural linear algebra[cite: 6]. It transforms a user's technical background profile into a multi-dimensional array, matching it directly against real-world career path profiles with exact geometric precision[cite: 6].

---

## Architectural Framework: Input -> Process -> Output (IPO)
The application acts as an assembly pipeline processing spatial alignments[cite: 6]:

1. **Input (Data Ingestion & Cold-Start Bypass):**
   * Automatically processes a target text matrix corpus from `raw_skills.csv`[cite: 5, 6].
   * Prompts the user for **three dense, qualitative feature entries** (Primary Skill, Core Concept, and Infrastructure Tool) via an onboarding survey module[cite: 5, 6].
   * Validates ingestion inputs to enforce string structural integrity, safely bypassing the classic *User Cold Start* zero-vector error[cite: 5, 6].
2. **Process (Vector Space Mapping & Alignment):**
   * Appends the interactive user profile directly into the corpus dictionary to create a shared, synchronized vocabulary workspace[cite: 5, 6].
   * Computes a numerical matrix utilizing **TF-IDF Weighting** (Term Frequency-Inverse Document Frequency) to log-dampen high-frequency terms while scaling predictive technical terms[cite: 6].
   * Executes **Cosine Similarity Alignment** math across the normalized matrix rows to compute precise angular proximity coefficients between the user profile vector and job profile vectors[cite: 5, 6].
3. **Output (Multi-Dimensional Filtering & Sorting):**
   * Aggregates cosine similarity math results and sorts the dataset in descending matching order[cite: 5, 6].
   * Truncates the dataset down to a designated **Top-3 List** of personalized technical career paths[cite: 5, 6].
   * Implements a strategic *Trending Fallback Safe-Mode Tracker* to handle edge profiles returning orthogonal results (0.00% vector overlap)[cite: 5, 6].

---

## Core Project Files
* **`matchmaker.py`** — The principal Python executable script housing onboarding interfaces, vector initialization, TF-IDF mapping layers, and cosine calculations.
* **`raw_skills.csv`** — The structural reference data catalog containing text profiles of target career pathways and technical skill lists[cite: 5].

---

## Mathematical Formulas Implemented
* **Term Frequency-Inverse Document Frequency:**[cite: 6]
  $$\text{TF-IDF} = \text{TF}(t, d) \times \log\left(\frac{\text{Total Documents}}{\text{Documents with Term } t}\right)$$
* **Cosine Angular Alignment (Similarity Metric):**[cite: 6]
  $$\text{Cosine Similarity}(A, B) = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|}$$

---

## How To Setup & Run the Engine
Ensure your python installation includes standard vector math libraries.

### 1. Ingestion Requirements:
```bash
pip install pandas numpy scikit-learn
```

### 2. Execution Flow:
Ensure raw_skills.csv is located in the exact same directory folder path as matchmaker.py, then run[cite: 5]:
```bash
python matchmaker.py
```

---
*Developed as part of the DecodeLabs AI Engineering Framework Portfolio.*