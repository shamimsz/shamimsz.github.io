---
title: "Lexical Scanner for a C-like Language"
summary: "A C++17 compiler-design project that tokenizes simplified C-like source files with source position tracking."
order: 3
featured: true
year: "2025"
status: "Academic project"
area: "Compiler Design"
tools:
  - C++17
  - Compiler Design
  - Lexical Analysis
  - File I/O
  - CLI
links:
  github: "https://github.com/your-github/lexical-scanner"
  demo: ""
metrics:
  - label: "Language"
    value: "C++17"
  - label: "Focus"
    value: "Lexer"
---

## Problem

Lexical analysis is the first stage of a compiler front end. The goal of this
project was to scan a simplified C-like source file and convert raw characters
into structured tokens that later compiler stages could consume.

## Approach

The scanner reads source files, skips whitespace and comments, recognizes
reserved words, identifiers, numeric literals, string and character literals,
operators, punctuators, and invalid tokens. Each token includes line and column
information, which makes lexical errors easier to trace.

## Implementation Notes

- Implemented deterministic scanning logic in C++17.
- Added reserved word recognition and delimiter handling.
- Supported multi-character operators and comment skipping.
- Reported structured token output with source positions.
- Documented the project with sample input files, expected output, and
  reproducible build instructions.

## What I Learned

This project gave me a clearer understanding of how programming languages are
processed before parsing. It is a compact project, but it shows core computer
science fundamentals beyond web development.
