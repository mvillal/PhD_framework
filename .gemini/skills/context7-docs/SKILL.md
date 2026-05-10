---
name: context7-docs
description: Fetches latest documentation for libraries and APIs using the Upstash Context7 tool. Use when you need up-to-date documentation for specific libraries, frameworks, or packages used in the PhD Framework.
---

# Context7 Documentation Retrieval

This skill integrates the Upstash Context7 CLI to provide live, version-specific documentation for any library. This ensures that the agent has access to the most current API signatures and patterns, overcoming the limitations of static training data.

## Workflows

### 1. Resolve a Library ID
Before querying documentation, you may need to find the correct `libraryId`. Use this workflow to search for a library by name or query.

```bash
npm exec ctx7 -- library <name> "<query>"
```

### 2. Query Library Documentation
Use this workflow to fetch specific documentation for a library once you have its ID (usually in GitHub format like `/owner/repo`).

```bash
npm exec ctx7 -- docs <libraryId> "<query>"
```

**Example:**
To find how to use `pytorch`'s `DataLoader` with custom collate functions:
```bash
npm exec ctx7 -- docs /pytorch/pytorch "DataLoader collate_fn example"
```

## Best Practices
- **Topic Precision:** Be as specific as possible with the `<query>` to get the most relevant documentation chunks.
- **Library ID Format:** Most libraries are indexed by their GitHub repository path (e.g., `/facebook/react`, `/python/cpython`, `/pytorch/pytorch`).
- **Context Efficiency:** Context7 returns documentation specifically formatted for LLMs. Review the output carefully to identify the exact API call or pattern needed.
- **Setup:** If prompted for authentication or setup, note that this environment might have restricted interactive capabilities. Prefer non-interactive flags if available.

## Domain-Specific Targets (PhD Framework)
Frequently used libraries in this research framework include:
- **PyTorch:** `/pytorch/pytorch`
- **Scikit-Learn:** `/scikit-learn/scikit-learn`
- **Pandas:** `/pandas-dev/pandas`
- **FastAPI:** `/tiangolo/fastapi`
- **Transformers (Hugging Face):** `/huggingface/transformers`
