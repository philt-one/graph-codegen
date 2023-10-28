# Graph-CodeGen 🤖🧠

This repo is dedicated to the exploration and implementation of innovative techniques for code generation using a Language Model (LLM).

The core idea is centered on leveraging textual summaries of Python objects (functions, classes, modules, ...) to evaluate their potential for reuse by the LLM during the code generation process.

## Summary 📝

Our preliminary step involves a detailed analysis of the Abstract Syntax Tree (AST) of the code. This analysis aims to extract and understand the relationships between various objects. Subsequently, we summarize each pertinent object and encapsulate it as a node within a graph network. This node is further enriched with metadata, such as the source code, dependencies, and additional relevant information.

By adopting this innovative approach, we aim to enhance the quality of code semantic search results by:

- Transforming the code objects into more digestible text embeddings (summaries), which offer a more understandable alternative to the original code embedding.
- Mapping the relationship between various objects on a graph network, which enables the exploitation of graph traversal algorithms like Breadth-First Search (BFS).

This approach not only simplifies the comprehension of the code but also facilitates its potential reuse in diverse contexts, thereby increasing efficiency and productivity.

![Flowchart](flowchart.png "Flowchart")

## Technology Stack 📚

### CozoDB

https://www.cozodb.org/

CozoDB is a general-purpose, transactional, relational database that uses Datalog for query, is embeddable but can also handle huge amounts of data and concurrency, and focuses on graph data and algorithms. It supports time travel and it is performant!

### Jina Embeddings v2

https://huggingface.co/jinaai/jina-embeddings-v2-base-en

jina-embeddings-v2-base-en is an English, monolingual open-source embedding model supporting 8192 sequence length. It is based on a Bert architecture (JinaBert) that supports the symmetric bidirectional variant of [ALiBi](https://arxiv.org/abs/2108.12409) to allow longer sequence length.
