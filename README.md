# LLM Personal Reproduce
> Personal repo for reproducing LLM / Multi-agent AI open-source projects for learning and research.

## Overview
This repository contains a series of reproduction experiments of state-of-art open-source AI frameworks and models.
Each subproject includes source code, experiment logs, setup instructions and observations.

## Project List
- 01-minimind-decoder: Build small decoder-only LLM from scratch, pretraining & inference
- 02-graphrag: Graph-enhanced RAG, compare with vanilla vector RAG on multi-hop QA
- 03-llamaindex-agent: Tool-calling Agent prototype built with LlamaIndex
- 04-llama-factory-lora: LoRA parameter-efficient fine-tuning via LLaMA-Factory
- 05-paicli: Cloud model training workflow based on paiCLI
- 06-mappo-selfplay: MAPPO multi-agent reinforcement learning with self-play

## Environment
All projects share the same conda environment.
```bash
conda create -n llm-reproduce python=3.10
conda activate llm-reproduce
pip install -r requirements.txt

