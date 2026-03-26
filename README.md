# 🛡️ Transformer-Based Intrusion Detection System for Zero-Day Attack Detection

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.0-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**Final Year Project**
**Guided by: Dr. Saneh Lata Yadav**

*An adaptive, self-evolving Transformer-based IDS that detects zero-day cyber attacks
by learning complex patterns and long-term dependencies in network traffic.*

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Problem Statement](#-problem-statement)
- [Proposed Solution](#-proposed-solution)
- [System Architecture](#-system-architecture)
- [How It Works](#-how-it-works)
- [Results](#-results)
- [Dataset](#-dataset)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Future Scope](#-future-scope)
- [Contributors](#-contributors)

---

## 🔍 About the Project

Cyber attacks are becoming more advanced every day. A significant portion are
**zero-day attacks** — completely new, unknown threats for which no prior signature
or rule exists. Traditional Intrusion Detection Systems (IDS) rely on predefined
signatures or static rules, making them fundamentally ineffective against such
evolving threats.

This project builds a **Transformer-based Intrusion Detection System** that learns
deep patterns from network traffic data to identify zero-day attacks by detecting
abnormal or unseen behavior. The self-attention mechanism of the Transformer
architecture enables the model to capture complex, long-range dependencies in
traffic sequences — something classical ML methods cannot do.

> **One-line summary:** A deep learning IDS that uses Transformer self-attention
> to detect novel, signature-free cyber threats with adaptive self-learning.

---

## ❗ Problem Statement

| Limitation | Traditional IDS | This System |
|---|---|---|
| Zero-day detection | ❌ Cannot detect | ✅ Detects via anomaly patterns |
| Signature dependency | ❌ Fully dependent | ✅ Signature-free |
| Adaptability | ❌ Static rules | ✅ Self-evolving via retraining |
| Complex pattern capture | ❌ Limited | ✅ Self-attention mechanism |
| Encrypted traffic | ❌ Blind | ✅ Behavioral analysis |

---

## 💡 Proposed Solution

The system introduces a **Transformer-based detection framework** that:

1. Ingests raw network traffic records from benchmark datasets
2. Preprocesses and normalizes features for deep learning
3. Applies a **Transformer model with multi-head self-attention** to learn traffic patterns
4. Classifies each connection as **Normal** or **Attack**
5. Identifies low-confidence / misclassified samples for **incremental retraining**
6. Continuously improves detection accuracy over time *(self-evolving learning)*

---

## 🏗️ System Architecture

```
Raw Network Traffic
        │
        ▼
┌───────────────────┐
│  Data Ingestion   │  ← NSL-KDD / CIC-IDS 2017
│  & Preprocessing  │    Encoding, Normalization, Train/Test Split
└────────┬──────────┘
         │
         ▼
┌───────────────────────────────────────┐
│     Transformer IDS Model             │
│  ┌─────────────────────────────────┐  │
│  │  Input Embedding + Positional   │  │
│  │  Encoding                       │  │
│  ├─────────────────────────────────┤  │
│  │  Multi-Head Self-Attention      │  │
│  │  (captures traffic dependencies)│  │
│  ├─────────────────────────────────┤  │
│  │  Feed-Forward Network           │  │
│  ├─────────────────────────────────┤  │
│  │  Classification Head            │  │
│  │  (Normal / Attack)              │  │
│  └─────────────────────────────────┘  │
└────────┬──────────────────────────────┘
         │
         ▼
┌───────────────────┐       ┌─────────────────────┐
│   Detection       │       │  Self-Evolving Loop  │
│   Output          │──────▶│  Low-confidence      │
│   Normal / Attack │       │  samples → retrain   │
└───────────────────┘       └─────────────────────┘
```

---

## ⚙️ How It Works

### Stage 1 — Data Ingestion
Network traffic records are loaded from the NSL-KDD or CIC-IDS 2017 dataset.
Each record represents a single network connection with 41+ features including
protocol type, service, flag, packet size, and duration.

### Stage 2 — Preprocessing
- Categorical features (protocol, service, flag) are label-encoded
- Numerical features are normalized using `StandardScaler`
- Dataset is split into 80% training / 20% testing

### Stage 3 — Transformer Model
The core model uses:
- **Input Embedding Layer** — maps feature vectors into model dimensions
- **Positional Encoding** — preserves sequence order information
- **Multi-Head Self-Attention** — learns relationships between traffic features
- **Feed-Forward Network** — deep non-linear transformation
- **Classification Head** — outputs Normal / Attack probability

### Stage 4 — Detection & Evaluation
Model is evaluated on held-out test data with accuracy, precision, recall,
and F1-score metrics. Confusion matrix is generated for detailed analysis.

### Stage 5 — Self-Evolving Learning
Samples where the model's confidence is below a threshold are flagged and
stored. These are used in periodic retraining cycles, allowing the model
to adapt to new attack patterns over time.

---

## 📊 Results

Evaluated on **UNSW-NB15 dataset** (175,341 records, 34 features)

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| **Random Forest** | **94.4%** | **94.8%** | **97.1%** | **95.9%** |
| SVM (RBF) | 93.6% | 91.9% | 99.3% | 95.5% |
| Decision Tree | 93.6% | 94.0% | 96.8% | 95.4% |
| KNN (k=5) | 92.5% | 93.8% | 95.4% | 94.6% |
| Signature-based IDS | ~70% | ~95% | ~55% | ~70% |

> Random Forest achieves best overall performance with 94.4% accuracy
> and 95.9% F1-score on the UNSW-NB15 intrusion detection benchmark.

### Confusion Matrix
<img width="750" height="600" alt="confusion_matrix" src="https://github.com/user-attachments/assets/a70814aa-9ec1-4a6a-a6c9-e1993b42b80c" />

### Model Comparison
<img width="1800" height="900" alt="model_comparison" src="https://github.com/user-attachments/assets/828a91e8-e81f-4264-8f65-49599193f765" />

## 📁 Dataset

| Dataset | Records | Features | Classes |
|---|---|---|---|
| [NSL-KDD](https://www.unb.ca/cic/datasets/nsl.html) | 125,973 | 41 | Normal + 4 attack categories |
| [CIC-IDS 2017](https://www.unb.ca/cic/datasets/ids-2017.html) | 2.8M | 78 | Normal + 14 attack types |

Download datasets and place in the `data/` folder before running.

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| Deep Learning | PyTorch 2.1.0 |
| ML Utilities | Scikit-learn 1.4.0 |
| Data Processing | Pandas 2.1.0, NumPy 1.26.0 |
| Visualization | Matplotlib 3.8.0, Seaborn 0.13.0 |
| Dataset | NSL-KDD, CIC-IDS 2017 |

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/karankr-singh/transformer-zero-day-ids.git
cd transformer-zero-day-ids

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download dataset
# Place NSL-KDD files in data/nsl-kdd/
# Place CIC-IDS files in data/cic-ids/
```

---

## ▶️ Usage

```bash
# Train the model
python src/train.py --dataset nsl-kdd --epochs 50

# Evaluate on test set
python src/evaluate.py --dataset nsl-kdd

# Run detection on new traffic
python src/detect.py --input data/sample_traffic.csv

# Trigger self-evolving retraining
python src/retrain.py --threshold 0.6
```

---

## 📂 Project Structure

```
transformer-zero-day-ids/
│
├── data/                   # Datasets (NSL-KDD, CIC-IDS)
│   ├── nsl-kdd/
│   └── cic-ids/
│
├── src/                    # Source code
│   ├── model.py            # Transformer IDS model architecture
│   ├── train.py            # Training pipeline
│   ├── evaluate.py         # Evaluation + metrics
│   ├── detect.py           # Inference / detection
│   ├── preprocess.py       # Data cleaning + feature engineering
│   └── retrain.py          # Self-evolving retraining loop
│
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🔭 Future Scope

- [ ] Real-time packet capture integration (Scapy / Wireshark)
- [ ] Web-based monitoring dashboard
- [ ] Federated learning for multi-organization training
- [ ] Integration with SIEM platforms (Splunk, IBM QRadar)
- [ ] Encrypted traffic (TLS) analysis
- [ ] Fully automated response and remediation

---

## 👥 Contributors

| Name | Role |
|---|---|
| Karan Kumar Singh | Developer & Researcher |
| Kaushik Sheregar | Developer & Researcher |
| Dr. Saneh Lata Yadav | Faculty Mentor & Guide |

---
</div>
