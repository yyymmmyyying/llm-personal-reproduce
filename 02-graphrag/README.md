# GraphRAG: Graph-enhanced Retrieval Augmented Generation
Reproduce GraphRAG and compare it with vanilla vector-based RAG.

## Project Overview
This project reproduces the open-source GraphRAG workflow. Import custom documents to extract entities and relations, build knowledge graph, and run local & global retrieval for question answering.
We build multi-hop QA test set to compare output quality between traditional vector RAG and GraphRAG. Record their information aggregation capability, applicable scenarios, computing cost and typical failure cases.

## Core Work
- Run entity & relation extraction and construct knowledge graph from custom text corpus
- Implement local retrieval and global retrieval pipeline for GraphRAG
- Build multi-hop question answering test dataset
- Conduct ablation comparison: vector RAG vs GraphRAG
- Summarize pros & cons, GPU resource overhead and common failure patterns

## Environment
```bash
conda activate llm-reproduce
pip install -r requirements.txt
