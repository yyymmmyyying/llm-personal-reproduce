# LLM-Personal-Reproduce
个人 AI 学习复现项目集合，覆盖大模型预训练、LoRA 微调、RAG、Agent、多智能体强化学习、传统机器学习等方向。

> 全部为个人学习复现实验，部分实验受本地算力限制，仅做小规模原理验证。

## 项目列表
- [01-minimind-decoder](./01-minimind-decoder)：MiniMind 解码器预训练、LoRA 微调、GGUF 量化导出（Mac MPS 环境）

## 运行环境
- 主要环境：macOS + Apple Silicon MPS
- 部分脚本兼容 Linux CUDA 环境
- 每个子目录内有独立的依赖说明与运行步骤

## 注意事项
1. 本仓库**不包含模型权重与数据集文件**，请按照各子项目 README 中的说明自行获取。
2. API Key、云服务密钥均通过环境变量传入，禁止硬编码到代码中。
3. 强化学习类实验存在收敛不稳定性，仅做原理验证。

