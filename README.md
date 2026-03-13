# AI CV Generator

An AI-powered application that generates tailored CVs from a job description using a Large Language Model (LLM).  
The system analyzes the job requirements and automatically generates a customized CV that highlights the most relevant skills and experience.
This project demonstrates how generative AI can automate resume customization and improve job application efficiency.

---

## Motivation


This project explores how generative AI can be applied to automate professional document generation and demonstrates an end-to-end LLM pipeline integrating prompt engineering and document rendering.

---

## Features

- Generate tailored CVs based on job descriptions
- AI-powered content generation using Hugging Face models
- Automatic formatting and PDF generation
- Customizable CV templates
- End-to-end pipeline from prompt → structured CV → PDF output

---

## Project Overview

Applying for jobs often requires modifying a CV for each position.  
This project automates that process using an LLM to generate optimized CV sections aligned with job requirements.

The workflow:

1. User inputs job description
2. AI model extracts relevant skills and keywords
3. CV sections are generated automatically
4. LaTeX template compiles the final CV
5. PDF is produced as the final output

---

## Tech Stack

**Languages**
- Python

**Libraries**
- Hugging Face Transformers
- PyTorch
- Python-LaTeX

**Tools**
- LaTeX
- Git

---

## Features

- Generate tailored CVs based on job descriptions
- AI-powered content generation using Hugging Face models
- Automatic formatting and PDF generation
- Customizable CV templates
- End-to-end pipeline from prompt → structured CV → PDF output

---

## Project Overview

Applying for jobs often requires modifying a CV for each position.  
This project automates that process using an LLM to generate optimized CV sections aligned with job requirements.

The workflow:

1. User inputs job description
2. AI model extracts relevant skills and keywords
3. CV sections are generated automatically
4. LaTeX template compiles the final CV
5. PDF is produced as the final output

---

## Tech Stack

**Languages**
- Python

**Libraries**
- Hugging Face Transformers
- PyTorch
- Python-LaTeX
- FastAPI / CLI interface (if applicable)

**Tools**
- LaTeX
- Git

## Installation

Clone the repository

git clone https://github.com/aloysia98/ai_cv_generator.git
cd ai_cv_generator

## Future Improvements

RAG-based CV generation using job postings dataset

Web interface for CV generation

Automatic ATS optimization

CV scoring against job descriptions

---
title: AI CV Generator
emoji: 📄
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "6.5.1"
python_version: "3.10"
app_file: app.py
pinned: false
---
