# Autonomous Insurance Claims Processing Agent

A lightweight Python-based agent that processes FNOL documents and routes insurance claims to the correct workflow.

## Problem Statement

This project extracts key fields from First Notice of Loss documents, identifies missing or inconsistent information, classifies the claim, and recommends the correct workflow route.

## Core Features

- Extract key fields from TXT and PDF FNOL documents
- Identify missing mandatory fields
- Detect suspicious or inconsistent claim details
- Route claims using rule-based workflow logic
- Return structured JSON output

## Routing Rules

| Condition | Route |
|---|---|
| Estimated damage < ₹25,000 | Fast-track |
| Any mandatory field missing | Manual Review |
| Description contains fraud/inconsistent/staged | Investigation Flag |
| Claim type is injury | Specialist Queue |

## Loading Documents

The agent supports FNOL documents in the following formats:

- `.txt`
- `.pdf`

Run:

```bash
python -m app.main samples/fnol_1.txt

## Data Models

The project uses Pydantic models to keep extracted claim data and final output structured.

### Main Models

- `ClaimFields`: Stores fields extracted from FNOL documents
- `ValidationResult`: Stores missing fields, inconsistencies, and suspicious keywords
- `ClaimProcessingResult`: Final assignment-compatible JSON response


## Project Status

Current stage:

```text
Commit 1: Base Python project setup

Commit 2: Added sample FNOL documents

Commit 3: Added document loader for TXT and PDF files

Commit 4: Defined claim and output data models


