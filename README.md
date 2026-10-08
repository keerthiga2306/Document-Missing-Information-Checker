# DocCheck AI – Document Missing-Information Checker

## Overview

**DocCheck AI** is an AI-powered document verification system that uses **OCR and Large Language Models (LLMs)** to analyze uploaded documents and identify missing information, missing documents, and inconsistencies.

The system helps users verify whether their documents are complete before submitting an application.

Instead of manually checking every document, DocCheck AI automatically extracts information, compares it with the required details, and generates an easy-to-understand verification report.

## Problem Statement

When submitting applications for scholarships, college admissions, government services, banking, insurance, or other services, users often face problems such as:

* Missing documents
* Incomplete application details
* Incorrect information
* Mismatched information between documents
* Difficulty understanding document requirements
* Manual verification taking too much time

DocCheck AI aims to make this process faster and easier using AI.

## Key Features

* Upload PDF documents
* OCR-based text extraction
* AI-powered document analysis
* Detect missing documents
* Detect missing fields
* Detect inconsistent information
* Compare information across multiple documents
* Calculate document completeness score
* Generate an easy-to-understand report
* Provide recommended actions
* Download verification results as a report

## How It Works

```text
User Uploads PDF Documents
          ↓
      PDF Processing
          ↓
     OCR Extraction
          ↓
   Extracted Text/Data
          ↓
      LLM Analysis
          ↓
 Requirement Comparison
          ↓
 ┌──────────────────────────┐
 │ Missing Documents        │
 │ Missing Information      │
 │ Mismatched Information   │
 │ Complete Information     │
 └──────────────────────────┘
          ↓
    Final AI Report
```

## Example

For a scholarship application, the system can check requirements such as:

```text
✓ Application Form
✓ Aadhaar Card
✓ Bonafide Certificate
✓ Mark Sheet
✗ Income Certificate
✗ Bank Account Details
✓ Passport Size Photograph
```

The system can generate a result such as:

```text
Completeness Score: 78%

Complete: 5
Missing: 2
Mismatch: 1

Missing Documents:
- Income Certificate
- Bank Account Details

Possible Mismatch:
- Father's Name

Recommended Action:
1. Upload the Income Certificate
2. Add Bank Account Details
3. Verify the Father's Name
```

## Technology Stack

### Frontend

* Streamlit

### Programming Language

* Python

### Document Processing

* PDF Processing
* OCR

### Artificial Intelligence

* Large Language Model (LLM)
* Prompt-based document analysis

### Data Processing

* Python
* Regular Expressions
* Structured JSON data

## Project Structure

```text
DocCheck-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── sample_documents/
│   └── sample_document_for_doccheck_ocr.pdf
│
├── utils/
│   ├── ocr.py
│   ├── document_parser.py
│   └── llm_analyzer.py
│
└── reports/
```

## Main Modules

### 1. Document Upload

Users can upload one or more PDF documents through the Streamlit interface.

### 2. OCR Extraction

The OCR module extracts readable text from uploaded documents.

### 3. Information Extraction

Important fields such as names, dates, addresses, identification numbers, and other required information are identified.

### 4. LLM Analysis

The extracted information is passed to an LLM for intelligent analysis.

The LLM identifies:

* Missing information
* Missing documents
* Possible mismatches
* Relevant document details

### 5. Requirement Verification

The extracted information is compared with the predefined document requirements.

### 6. Report Generation

The system generates a final report containing:

* Completeness score
* Found documents
* Missing documents
* Missing fields
* Mismatched information
* Recommended actions

## Use Cases

DocCheck AI can be used for:

* Scholarship applications
* College admission applications
* Government service applications
* Bank and KYC applications
* Insurance claims
* Job applications
* Loan applications
* Certificate verification

## Future Enhancements

* Support for DOCX and TXT files
* Multilingual OCR
* Tamil and English language support
* Voice-based document assistance
* RAG-based requirement knowledge base
* Automatic document classification
* Document expiry detection
* Advanced fraud and duplicate detection
* Email notification for missing documents
* Database integration
* Cloud deployment

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/DocCheck-AI.git
```

Move into the project folder:

```bash
cd DocCheck-AI
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## Sample Input

A sample scholarship application PDF is included for testing the document verification workflow.

The sample demonstrates how the system can identify:

* Available information
* Missing documents
* Missing fields
* Possible mismatches

## Sample Output
<img width="924" height="722" alt="Screenshot 2026-10-08 162102" src="https://github.com/user-attachments/assets/359764f2-f200-4f7f-802d-62c0776e1ad7" />
<img width="827" height="367" alt="Screenshot 2026-10-08 162202" src="https://github.com/user-attachments/assets/3e31bc0a-0038-4224-ad21-9a9a75747ae8" />
<img width="744" height="702" alt="Screenshot 2026-10-08 162449" src="https://github.com/user-attachments/assets/f2648228-e9c2-4d00-a824-d0fab67426c5" />
<img width="762" height="425" alt="Screenshot 2026-10-08 162553" src="https://github.com/user-attachments/assets/78a933ff-46c0-4655-a944-71e7e83054a2" />


## Project Objective

The main objective of DocCheck AI is to reduce manual document verification effort and help users identify missing or incorrect information before submitting important applications.

## Conclusion

DocCheck AI combines **OCR, document processing, and Large Language Models** to create an intelligent document verification assistant.

It helps users **Check. Complete. Submit with Confiden**
