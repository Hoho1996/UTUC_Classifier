# UTUC_Classifier


This repository provides a Python package for molecular subtyping prediction of UTUC samples.  
**Before running predictions, you must check that your input gene names and order are exactly the same as those in the demo files: [`demo_data/RNA_exp.txt`](https://github.com/Hoho1996/UTUC_Classifier/blob/main/demo_data/RNA_exp.txt) and [`demo_data/mut_data.txt`](https://github.com/Hoho1996/UTUC_Classifier/blob/main/demo_data/mut_data.txt).**

---

## Installation

1. Clone the repository and enter the directory:

   ```bash
   git clone https://github.com/Hoho1996/UTUC_Classifier.git
   cd UTUC_Classifier
   ```

2. Install dependencies and the package:

   ```bash
   pip install .
   ```

---

## Input Data Format

- **File format:** Tab-separated (.txt or .tsv)
- **Rows:** Gene names (features)
- **Columns:** Sample IDs
- **Cells:** Value for each gene in each sample (mutation: 0/1, expression: TPM)

**Example:**

|         | Sample1 | Sample2 | Sample3 |
|---------|---------|---------|---------|
| TP53    |   1     |   0     |   1     |
| FGFR3   |   0     |   1     |   0     |
| ...     |  ...    |  ...    |  ...    |

- **Gene names (row order) must be exactly the same as in the demo files.**
- **Sample IDs (column order) should be consistent across data types.**
- **Files must include headers and row names.**
- **Fill missing values with 0 or appropriate values.**

Demo files for reference:  
- [`demo_data/mut_data.txt`](https://github.com/Hoho1996/UTUC_Classifier/blob/main/demo_data/mut_data.txt)  
- [`demo_data/RNA_exp.txt`](https://github.com/Hoho1996/UTUC_Classifier/blob/main/demo_data/RNA_exp.txt)

---

## Gene Name Consistency Check

Before prediction, check that your input file gene names and order match the demo files. Example code:

```python
import pandas as pd

# Read demo and input files
demo_mutation_data = pd.read_csv("demo_data/mut_data.txt", sep="\t", index_col=0)
your_mutation_data = pd.read_csv("your_mut_data.txt", sep="\t", index_col=0)

if (demo_mutation_data.index == your_mutation_data.index).all():
    print("Gene names and order are consistent. Ready for prediction.")
else:
    raise ValueError("Gene names/order in your input file do not match the demo file. Please check before running!")
```

Repeat for RNA expression data:

```python
demo_rna_data = pd.read_csv("demo_data/RNA_exp.txt", sep="\t", index_col=0)
your_rna_data = pd.read_csv("your_RNA_exp.txt", sep="\t", index_col=0)

if (demo_rna_data.index == your_rna_data.index).all():
    print("Gene names and order are consistent. Ready for prediction.")
else:
    raise ValueError("Gene names/order in your RNA file do not match the demo file. Please check before running!")
```

---

## Prediction Workflow

```python
from utuc_classifier import predict_group

# Check gene name consistency (see above)
result = predict_group("your_mut_data.txt", "your_RNA_exp.txt")
print(result)
result.to_csv("prediction_result.txt", sep="\t", index=False)
```

---

## Result Description

- `Sample_ID`: Sample identifier
- `Predicted_Group`: Predicted group label (SNF1, SNF2, SNF3)

---

## FAQ

For questions, please contact the project maintainer.