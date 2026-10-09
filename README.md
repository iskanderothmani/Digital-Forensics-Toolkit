# Digital Forensics Toolkit

A local evidence-manifest utility for authorized lab copies. Computes SHA-256 hashes and records file sizes; does not alter file contents intentionally.

## Run
Python 3.11+; standard library only.

```bash
python app.py ./evidence
python -m unittest discover -s tests -v
```

## Limitations
Educational prototype, not a forensic acquisition suite. For real investigations, follow your organization's evidence-handling procedures, preserve originals, document chain of custody, and use validated write blockers where appropriate. Never commit real evidence or personal data.

## License
MIT
