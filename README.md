## 🧬 qpAdm Wrapper - Genomic Admixture Modeling Pipeline
To learn more in detail about qpAdm, including what it is, how it works, and its purpose, kindly refer to this : [Tutorial](https://indoaryan.com/qpadm-tutorial/)

## Overview

This repository provides a **first-of-its-kind scalable qpAdm wrapper** that enables a fully reproducible admixture analysis pipeline through a unified Jupyter Notebook interface.  

It removes traditional Linux/R setup overhead and automates SNP preprocessing, dataset merging, and qpAdm batch execution for large-scale population genetics analysis.


## Key Features

- Fully reproducible qpAdm workflow  
- Unified Jupyter Notebook execution  
- Automated SNP filtering (1240K SNP list)  
- AADR dataset compatibility  
- Automated batch qpAdm runs  
- PCA and f-statistics integration  
- High-dimensional SNP preprocessing using NumPy & Pandas  


## Dataset

This project uses the **Allen Ancient DNA Resource (AADR)** dataset released by David Reich Lab (Harvard standard reference dataset) : [Link](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FFIDCW)

Why AADR ?

- 1240K SNP coverage  
- Extensive ancient & modern population coverage  
- Gold-standard dataset for qpAdm modeling  

HO (Human Origins) dataset is also supported, but AADR is recommended due to broader coverage.


## How qpAdm Works (Pipeline Explanation)

We begin with raw DNA files from consumer genetic testing platforms such as:

• AncestryDNA • 23andMe • Genetrack • EasyDNA • MyHeritage


These files are typically provided in `.txt` format.Before processing, the file must be converted into **23andMe format**, which acts as the standardized input format for the pipeline.


## Step 1 – SNP Filtering (1240K SNP List)

The DNA file is filtered using the **1240K SNP list** to ensure compatibility with the AADR dataset.
  After this step, the file matches the SNP structure of AADR.


## Step 2 – Dataset Merge

The filtered file is merged with:

- AADR dataset (recommended)  
- OR HO dataset  

AADR is preferred because it provides larger population coverage, includes more ancient samples, and offers better modeling resolution compared to alternative datasets.


## Step 3 – qpAdm Modeling

qpAdm estimates ancestry proportions by modeling a target population as a mixture of selected source populations.

For Indian population structure analysis, major ancestral components often include:

- AASI (Ancient Ancestral South Indian)  
- IVC (Iranian farmer-related ancestry) 
- Steppe (Steppe pastoralist / Indo-European related ancestry)  


Process:

1. Select target population  
2. Choose 7–8 source populations  
3. Define outgroup populations  
4. Execute qpAdm runs (automated batch supported)  


## Step 4 – Model Evaluation

- **P-value > 0.05 → Model Pass (statistically valid)**  
- **P-value < 0.05 → Model Fail (reject model)**  

![IMG_20260117_053438](https://github.com/user-attachments/assets/26b00f86-5a94-45f8-856b-0efda4dd43c2)

