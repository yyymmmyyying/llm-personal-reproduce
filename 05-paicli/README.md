# paiCLI: Custom CLI wrapper for Alibaba Cloud PAI
Simple command-line script wrapper for Alibaba Cloud PAI platform.

## Project Overview
Build lightweight scripts to encapsulate training task calling workflow on PAI. Automate config generation, file upload, task submission, log fetching and model download.
Connect local experiments and cloud training environment, organize and archive personal experiment records.

## Core Work
- Write custom CLI script to wrap PAI API
- Support training config generation, data upload, job submit, log viewing and model download
- Bridge local dev environment and cloud training platform
- Realize experiment management and result archiving for personal LLM trials

## Environment
```bash
conda activate llm-reproduce
pip install -r requirements.txt
