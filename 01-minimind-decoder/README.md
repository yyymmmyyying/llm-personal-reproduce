# MiniMind Decoder Reproduction
Reproduction of lightweight decoder-only LLM, for learning LLM pre-training and alignment pipeline.

## Project Overview
This project reproduces the full pipeline of a small decoder-only large language model, including pretraining, knowledge distillation, supervised fine-tuning, DPO and PPO preference alignment.
All experiments are recorded, including hyperparameter ablation, training stability and hardware memory constraints.

## Core Work
- Build text dataset pipeline for model pretraining
- Configure decoder model structure and run corpus pretraining
- Knowledge distillation: transfer capability from larger teacher model to small student model
- Implement SFT, DPO, PPO to align model generation
- Tune learning rate, batch size and other hyperparameters, observe convergence change
- Document practical limits including VRAM shortage and raw data quality problems

## Environment
```bash
conda activate llm-reproduce
pip install -r requirements.txt

