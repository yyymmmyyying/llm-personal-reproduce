# LlamaIndex: Tool-calling Agent Prototype
Reproduce and debug LLM agent based on LlamaIndex framework.

## Project Overview
Build an Agent prototype with the open-source LlamaIndex framework. Integrate document retrieval and numerical calculation tools. Reproduce task planning, tool calling and result summarization workflow.
Test the agent’s ability to decompose complex multi-step tasks and invoke proper external tools automatically.

## Core Work
- Build agent demo based on LlamaIndex
- Integrate two tools: document retrieval & numerical computation
- Realize full workflow: task planning → tool selection → function call → response aggregation
- Debug failure cases including tool misuse and wrong task decomposition
- Record configuration tricks and common pitfalls of LLM agent

## Environment
```bash
conda activate llm-reproduce
pip install -r requirements.txt
