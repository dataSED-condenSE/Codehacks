# Codehacks: A Dataset of Adversarial Tests for Competitive Programming Problems

This repository accompanies the research paper:

> **Codehacks: A Dataset of Adversarial Tests for Competitive Programming Problems Obtained from Codeforces**  
> *International Conference on Software Testing, Verification and Validation (ICST), 2025*  
> DOI: https://doi.org/10.1109/ICST62969.2025.10988963  
> IEEE Xplore: https://ieeexplore.ieee.org/abstract/document/10988963/

---

## 📌 Overview

Software testing is a fundamental technique for assessing software correctness. However, the effectiveness of testing depends heavily on the quality and coverage of the test suite. In practice, software can pass all available tests while still containing faults due to missing edge cases—so-called *false negatives*.

To support **data-driven creation of error-inducing test suites**, especially for evaluating software synthesized by **large language models**, we introduce **Codehacks**: a large-scale dataset of *real-world adversarial test cases* (called *hacks*) collected from the Codeforces competitive programming platform.

Codehacks consists of:
- Competitive programming problems with natural language descriptions
- Error-inducing test cases (“hacks”) created by users
- Submitted solutions that fail on these hacks

All data is collected *from the wild*, reflecting realistic failure modes of program submissions.

---

## 📊 Dataset Summary

- **5,578** programming problems  
- **288,617** successful hacking attempts  
- **2,196** solution submissions that can be broken by hacks  
- Source: **Codeforces Online Judge**

The dataset is designed to facilitate research in:
- Software testing and test generation
- Program repair and robustness evaluation
- Benchmarking LLM-generated code
- Competitive programming analysis

---

## 📁 Repository Contents

This GitHub repository contains **metadata, scripts, and derived artifacts** used in the paper.  
For the **full dataset artifacts**, please refer to the Figshare repository:

🔗 **Figshare dataset**: https://doi.org/10.6084/m9.figshare.24773754

---

## 🗂️ Data Files

### Core Dataset Files

- **`contests.json`**  
  List of all available Codeforces contests.

- **`Problems.txt`**  
  List of all programming problems that have at least one successful hack.

- **`problemDescriptions.json`**  
  Natural language descriptions for problems listed in `Problems.txt`.  
  Data is crawled using scripts in the `/scraping` folder.

- **`submissionUrls.txt`**  
  URLs of submissions involved in successful hacks.  
  Each line contains: contestID, hackID, submissionURL


- **`submissionCode.json`**  
Source code for **2,196** hacked submissions.  
These submissions are obtained from the **Code4Bench** dataset.

- **`codehacks.json`**  
A consolidated collection of all successful hacking attempts obtained from Codeforces.  
Data is aggregated from contest-level files in the `/Contests` folder.

---

### Test Case Data

- **`/testcases/`**  
Contains test cases for the **2,196 hacked submissions**, organized by problem ID.  
For each submission, a JSON file provides:
- Input
- Expected output

---

### Contest-Level Data

- **`/Contests/`**  
Contains one `.json` file per Codeforces contest retrieved via the Codeforces API.
- If a contest has **no hacks**, the filename explicitly contains `"noHacks"`.

---

## 🔁 Replication of Data Collection

To ensure reproducibility, this repository includes scripts and notebooks that replicate the data collection pipeline described in the paper.

### Replication Instructions

Step-by-step instructions are provided in:

📄 **`Replication-Steps.md`**

### Notebooks Used

The replication pipeline relies on the following Jupyter notebooks:

1. **`2) Process - Get Contest Information.ipynb`**  
 Retrieves contest metadata from Codeforces.

2. **`2.1) Extract all relevant hacking attempts.ipynb`**  
 Extracts successful hacks from contests.

3. **`3) Problems with hacks.ipynb`**  
 Identifies problems that have at least one successful hack.

4. **`4) Crawl Submission URLS.ipynb`**  
 Collects URLs of submissions involved in hacks.

5. **`5) SQL matching.ipynb`**  
 Matches Codeforces submissions with source code from external datasets.

### Scraping Utilities

- **`/scraping/`**  
Contains Python scripts used to crawl:
- Problem descriptions
- Submission metadata
- Additional Codeforces data

---

## 📖 Citation

If you use this dataset or code in your research, please cite:

```bibtex
@INPROCEEDINGS{10988963,
  author={Hort, Max and Moonen, Leon},
  booktitle={2025 IEEE Conference on Software Testing, Verification and Validation (ICST)}, 
  title={Codehacks: A Dataset of Adversarial Tests for Competitive Programming Problems Obtained from Codeforces}, 
  year={2025},
  volume={},
  number={},
  pages={742-746},
  keywords={Software testing;Computer languages;Computer hacking;Source coding;Large language models;Natural languages;Computer bugs;Programming;Software;Software reliability;competitive programming;language model;dataset},
  doi={10.1109/ICST62969.2025.10988963}}

