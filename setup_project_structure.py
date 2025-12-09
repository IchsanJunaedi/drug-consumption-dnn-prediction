"""
Setup Project Structure for Drug Consumption DNN Prediction
Run this script to create all necessary folders

Author: Muhammad Ichsan Junaedi & Amanda Wijayanti
Date: December 2024
"""

import os

def create_project_structure():
    """Create complete project folder structure"""
    
    # Base directory
    base_dir = "drug-consumption-dnn-prediction"
    
    # Define folder structure
    folders = [
        # Data folders
        "data/raw",
        "data/processed",
        
        # Notebooks folder
        "notebooks",
        
        # Models folder
        "models",
        
        # Results folders
        "results/figures/training_curves",
        "results/figures/comparison_plots",
        "results/figures/feature_importance",
        "results/metrics",
        "results/reports",
        
        # Source code folder
        "src",
    ]
    
    # Create base directory
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"✅ Created base directory: {base_dir}/")
    else:
        print(f"📁 Base directory already exists: {base_dir}/")
    
    # Create all subdirectories
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"✅ Created: {folder}/")
        else:
            print(f"📁 Already exists: {folder}/")
    
    # Create placeholder files
    placeholder_files = [
        "notebooks/01_Data_Preparation.ipynb",
        "notebooks/02_DNN_Baseline.ipynb",
        "notebooks/03_Hyperparameter_Tuning.ipynb",
        "notebooks/04_Model_Evaluation.ipynb",
        "notebooks/05_RF_vs_DNN_Comparison.ipynb",
        "notebooks/06_Feature_Importance_DNN.ipynb",
        "src/model_builders.py",
        "src/evaluation.py",
        "src/visualization.py",
        "requirements.txt",
        "README.md",
        "LICENSE",
    ]
    
    for file in placeholder_files:
        file_path = os.path.join(base_dir, file)
        if not os.path.exists(file_path):
            # Create empty file
            with open(file_path, 'w') as f:
                if file.endswith('.py'):
                    f.write('# To be implemented\n')
                elif file.endswith('.ipynb'):
                    f.write('{}')  # Empty notebook
                elif file == 'requirements.txt':
                    f.write(get_requirements())
                elif file == 'README.md':
                    f.write(get_readme())
                elif file == 'LICENSE':
                    f.write('MIT License\n')
            print(f"📄 Created: {file}")
        else:
            print(f"📄 Already exists: {file}")
    
    print("\n" + "="*60)
    print("🎉 PROJECT STRUCTURE CREATED SUCCESSFULLY!")
    print("="*60)
    print(f"\n📂 Your project is ready at: {base_dir}/")
    print("\n📋 Next Steps:")
    print("   1. Copy your dataset to: data/raw/")
    print("   2. Copy 01_Data_Preparation.ipynb from UTS")
    print("   3. Install dependencies: pip install -r requirements.txt")
    print("   4. Start with: notebooks/02_DNN_Baseline.ipynb")
    print("\n" + "="*60)

def get_requirements():
    """Return requirements.txt content"""
    return """# Deep Learning Framework
tensorflow>=2.13.0
keras>=2.13.0

# Machine Learning
scikit-learn>=1.3.0
imbalanced-learn>=0.11.0

# Data Processing
pandas>=2.0.0
numpy>=1.24.0

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0

# Model Interpretation
shap>=0.42.0

# Hyperparameter Tuning
keras-tuner>=1.3.0

# Utilities
joblib>=1.3.0
tqdm>=4.65.0

# Jupyter
jupyter>=1.0.0
ipykernel>=6.25.0
"""

def get_readme():
    """Return README.md content"""
    return """# Prediksi Risiko Konsumsi Narkoba Menggunakan Deep Neural Network

**Studi Lanjutan dari Random Forest Model**

## 📌 Deskripsi Project

Penelitian ini mengembangkan model Deep Neural Network (DNN) untuk memprediksi risiko konsumsi narkoba berdasarkan personality traits, sebagai studi lanjutan dari model Random Forest (UTS).

**Peneliti:**
- Muhammad Ichsan Junaedi (241572010024)
- Amanda Wijayanti (241572010006)

**Dosen Pengampu:** Hendri Kharisma S.Kom, M.T

**Institusi:** STMIK TAZKIA

## 🎯 Tujuan Penelitian

1. Implementasi Deep Neural Network untuk binary classification (user vs non-user)
2. Optimasi arsitektur DNN melalui hyperparameter tuning
3. Perbandingan komprehensif DNN vs Random Forest
4. Analisis feature importance menggunakan SHAP

## 📊 Dataset

**Sumber:** UCI Machine Learning Repository - Drug Consumption (Quantified)
- **URL:** https://archive.ics.uci.edu/dataset/373/drug+consumption+quantified
- **Samples:** 1,885 responden
- **Features:** 24 fitur (demografi, personality traits, behavioral measures)
- **Target:** Binary (User vs Non-User)

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone <repository-url>
cd drug-consumption-dnn-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download Dataset
Download dataset dari UCI dan letakkan di `data/raw/`

### 4. Run Notebooks
Jalankan notebooks secara berurutan:
1. `01_Data_Preparation.ipynb` (dari UTS)
2. `02_DNN_Baseline.ipynb`
3. `03_Hyperparameter_Tuning.ipynb`
4. `04_Model_Evaluation.ipynb`
5. `05_RF_vs_DNN_Comparison.ipynb`
6. `06_Feature_Importance_DNN.ipynb`

## 📁 Struktur Project

```
drug-consumption-dnn-prediction/
├── data/                      # Dataset
├── notebooks/                 # Jupyter notebooks
├── models/                    # Trained models
├── results/                   # Results & visualizations
├── src/                       # Source code
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

## 📈 Baseline Performance (Random Forest - UTS)

- **Accuracy:** 86.21%
- **ROC-AUC:** 0.9347
- **F1-Score:** 88.74%
- **Overfitting Gap:** 0.86%

## 📝 License

MIT License

## 📧 Contact

- Muhammad Ichsan Junaedi: 2415720100024.ichsan@student.stmik.tazkia.ac.id
- Amanda Wijayanti: 241572010006.amanda@student.stmik.tazkia.ac.id
"""

if __name__ == "__main__":
    create_project_structure()