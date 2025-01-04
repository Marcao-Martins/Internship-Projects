# CONLLU Processing Toolkit 🛠️

## Overview 📋

A comprehensive toolkit for processing, analyzing, and managing CONLLU files, featuring multiple specialized tools for normalization, comparison, concatenation, and statistical analysis of linguistic corpora.

## Purpose and Scope 🎯

While these tools were originally developed to process and analyze the DANTEStocks corpus - a Brazilian Portuguese financial market corpus annotated with Universal Dependencies - they are designed to work with any properly formatted CONLLU files. The toolkit's flexibility and robust error handling make it suitable for processing and analyzing any linguistic corpus that follows the CONLLU format specifications.


### Acknowledgements 🎓
This research was conducted at the Center for Artificial Intelligence of the University of São Paulo (C4AI - c4ai.inova.usp.br), supported by:
-The São Paulo Research Foundation (FAPESP)
-The IBM Corporation
-The Ministry of Science, Technology, and Innovation (through Law N. 8.248 of October 23, 1991)

## Components 🔧

### 1. Statistical Analyzer 📊
Components:
- Automated LaTeX report generation:
  - Comparative corpus statistics
  - Publication-ready tables and figures
  - Customizable report templates
- Preprocessing notebook for data preparation
- Statistical analysis notebook for in-depth analysis

Features:
- Corpus cleaning and preparation
- Statistical metrics generation:
  - Token distribution analysis
  - Sentence length statistics
  - Dependency relation patterns
  - Morphological feature analysis
- LaTeX report generation
- Visualization creation


### 2. Normalization Tool 📝
Features:
- CONLLU format validator and normalizer:
  - Ensures 10-column format compliance
  - Validates sentence structure
  - Maintains metadata consistency
  - Preserves text-token alignment
- Decimal precision normalization
- Leading zeros preservation
- Consistent decimal separator handling

Key Functions:
- Automated format correction
- Discrepancy reporting
- Backup creation
- Detailed logging

### 3. Comparison Tool 🔍
Capabilities:
- CONLLU file version comparison
- Token-level difference detection
- Interactive HTML report generation
- CSV output for detailed analysis

Features:
- Visual difference highlighting
- Responsive formatting
- Duplicate ID handling
- Encoding verification

### 4. Concatenator Tool 🔗
Functionality:
- Combines multiple CONLLU files
- Maintains proper file formatting
- Adds appropriate separators
- Preserves UTF-8 encoding
- Process logging

### 5. PorttaggerDANTE (Tagger) ✍️
- Modified version of the [PorttaggerDANTE](https://huggingface.co/spaces/Emanuel/porttagger) for handling extended token sequences


