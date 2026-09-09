# LLM-Personal-Reproduce
Personal reproduction experiments of LLM & AI frameworks, for learning and resume demonstration.

This repository collects a series of open-source AI reproduction projects, covering LLM pretraining, LoRA fine-tuning, GraphRAG, LLM Agent and multi-agent reinforcement learning tasks. All experiments are based on public open-source repositories, with experimental records, parameter tuning logs and test results.

## 📁 Project List
| No. | Project | Description |
|:---:|---|---|
| 01 | MiniMind Decoder | Reproduce small decoder-only LLM pretraining, distillation and alignment pipeline, including model quantization to GGUF. |
| 02 | GraphRAG | Graph-enhanced RAG, entity & relation extraction, multi-hop QA comparison with vanilla vector RAG. |
| 03 | LlamaIndex Agent | Tool-calling Agent prototype built with LlamaIndex, integrate document retrieval & numerical calculation. |
| 04 | LLaMA-Factory LoRA | Parameter-efficient fine-tuning experiment, hyperparameter ablation & VRAM constraint record. |
| 05 | paiCLI | Custom lightweight CLI wrapper for Alibaba Cloud PAI platform, automate cloud training task workflow. |
| 06 | MAPPO & Self-Play | Multi-agent reinforcement learning reproduction, CTDE paradigm, compare MAPPO / IPPO training behaviors. |

## Environment
All projects share the same python dependencies in `requirements.txt`.
```bash
conda create -n llm-reproduce python=3.10
conda activate llm-reproduce
pip install -r requirements.txt
