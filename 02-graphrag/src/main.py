"""
GraphRAG experiment: entity-relation extraction & multi-hop QA compare with vanilla vector RAG
"""
import os

def main():
    print("==== GraphRAG Pipeline Start ====")
    # 1. load custom documents
    # 2. entity & relation extraction, build knowledge graph
    # 3. local / global retrieval
    # 4. compare result with vector RAG baseline
    print("Pipeline finished. Check experiment log for comparison result.")

if __name__ == "__main__":
    main()
