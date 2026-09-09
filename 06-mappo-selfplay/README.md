
### 06-mappo-selfplay/README.md
```markdown
# MAPPO & Self-Play Multi-agent RL Reproduction
Multi-agent reinforcement learning experiment based on MAPPO and Self-Play.

## Project Overview
Build LLM multi-agent simulation environment, construct debate/adversary scenarios. Reproduce CTDE paradigm of MAPPO, run small-scale experiments under limited local GPU memory.
Test self-play strategy pool and hierarchical reward design, compare training behavior between IPPO and MAPPO, document training bottlenecks and failure patterns.

## Core Work
- Implement multi-agent simulation based on open-source codebase
- Reproduce MAPPO CTDE (Centralized Training, Decentralized Execution) framework
- Build self-play strategy pool and hierarchical reward function
- Compare training dynamics between MAPPO and IPPO
- Record resource constraints, reward instability and typical training failure cases

## Environment
```bash
conda activate llm-reproduce
pip install -r requirements.txt
