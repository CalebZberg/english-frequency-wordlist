# english-frequency-wordlist
A Python program for compiling words from text and filtering based on frequency across documents. Useful for compiling lists of real-language words.

## Overview
- This repo was created to produce accurate and clean words lists for any various use cases
- This program is able to take and compare multiple text sources to curate a clean typo and fiction free list of real words
- Filtered words include: typos, fictional words, nouns (names, places, etc), abbreviations, industry-specific words, etc

## Pipeline
This project has two stages:

1) **Frequency Extraction**
    - Input: raw text sources (file(s) or folder)
    - Output: per-document frequency tables

2) **Wordlist Curation**
    - Input: document frequency tables
    - Output: curated wordlist + metadata


## How it Works
### Stage 1: Frequency Extraction
    - Normalize tokens (lowercase, letters-only, etc)
    - Count token occurrences
    - Save frequency table

### Stage 2: Wordlist Curation
    - Compare token frequency across documents
    - Calculate ratio of token appearance through documents
    - Compare frequency of appearance in each document
    - (Need to fine-tune specifics for proper word filter)
    - Discard filtered words

## Inputs
- Supported file types:
    - .txt
- Input Layout:
    - 1-n files
    - Folder

## Outputs
### Intermediate Outputs
- Per-document frequency tables

### Final Outputs
- Wordlists
- Optional metadata (counts, thresholds)

## Use Cases
- Game dictionaries / validation
- NLP preprocessing
- Building Bloom filters / tries


## Status
- Currently in development - initial project structure

## License
(MIT)





