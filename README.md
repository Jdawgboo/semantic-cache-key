# Semantic Cache Key

Produce a stable SHA-256 key from normalized model, prompt, system text, and sorted options.

```bash
cat request.json | python tool.py
python -m unittest -v
```

This is an exact-input cache key, not a semantic-similarity cache or a privacy mechanism.
