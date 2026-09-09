# LLM-Personal-Reproduce
> Personal reproduction experiments of LLM & AI frameworks, for learning and resume demonstration.

This repository collects a series of open-source AI reproduction projects, covering LLM pretraining, LoRA fine-tuning, GraphRAG, LLM Agent and machine learning tasks.
All experiments are based on public open-source repositories, with experimental records, parameter tuning logs and test results.

## 📁 Project List
| No. | Project | Description |
|:---:|---|---|
| 01 | MiniMind Decoder | Reproduce small decoder-only LLM pretraining, distillation and alignment pipeline |
| 02 | GraphRAG | Graph-enhanced RAG, entity & relation extraction, multi-hop QA comparison with vanilla vector RAG |
| 03 | LlamaIndex Agent | Tool-calling Agent prototype built with LlamaIndex, integrate document retrieval & numerical calculation |
| 04 | LLaMA-Factory LoRA | Parameter-efficient fine-tuning experiment, hyperparameter ablation & VRAM constraint record |

## 🛠 Global Environment
All projects run on MacOS / Linux, Python 3.10+.
Recommended dependency management: `conda`

```bash
# Create conda env example
conda create -n llm-reproduce python=3.10
conda activate llm-reproduce
pip install -r requirements.txt
