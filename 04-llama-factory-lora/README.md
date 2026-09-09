# LLaMA-Factory: LoRA Fine-tuning Experiment
Reproduce parameter-efficient fine-tuning workflow using LLaMA-Factory.

## Project Overview
Complete the full LoRA fine-tuning pipeline based on open-source LLaMA-Factory. Includes dataset preparation, training parameter configuration, model fine-tuning and inference evaluation.
Adjust hyperparameters such as learning rate and LoRA rank to observe impacts on training process and model outputs. Record practical experimental issues like data quality and VRAM constraints.

## Core Work
- Prepare custom dataset and configure training arguments
- Run LoRA parameter-efficient fine-tuning
- Tune learning rate, LoRA rank and other hyperparameters
- Evaluate model outputs before & after fine-tuning
- Summarize practical constraints: dataset quality, GPU memory limits, training stability

## Environment
```bash
conda activate llm-reproduce
pip install -r requirements.txt
