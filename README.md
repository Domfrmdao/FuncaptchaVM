# Overview

This repository was created to address two main issues:

1. **Outdated repositories**: Many existing repositories are not up to date with the latest versions
2. **People struggling**: Some people are struggling with reversing the encryption process, this repository provides a clear implementation and everything you need to know

## Version Statistics

The following statistics show the number of keys found across different versions:

| Version | Number of Keys |
|---------|----------------|
| 4.0.14  | 14             |
| 4.0.13  | 51             |
| 3.7.8   | 23             |
| 3.7.7   | 21             |
| 3.7.5   | 3              |
| 2.17.6  | 9              |
| 2.17.5  | 89             |

**Total**: 210 keys, 7 versions

[Credits for the keys](https://azureflow.github.io/arkose-fp-docs/keys.html)

## RSA Public Key for Version 4.0.14

The RSA public key for version **4.0.14**:

```
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1oPfgMSu7OYZ6bWlFcs2FSFJVO9g8hz3ozOwjB6yrbeMxCRw/lblyVh3H4zTm2vZ5Ggh8dnUG03Nyw0PQmr8OaJKA3ZGlJk2VvE5EXOsYoLR/z477xoUacxC3yAICKREP71O2IwxeMRzS4Sp0r3Bl4NxLiiYy7wn34YfY1HX7X2nl0aJEOt5Y9+AMaoBU/cAn0L6rqDn25MJgIwzrxg9pz7NmdWEFhGHDEzdV+cGWoNFNnKnkY555SCFk/CDnZyD8DTIA8yjrdnWhj8yjwh1fx6+XJQBBgvyYpfhW5z9de6ACpnAVrIxicMoxyXnfJ+LeK09e1xQwHEPFhjIBA3VFwIDAQAB
```

## Usage

```python
from main import rsa_encrypt_payload

payload = "FINGERPRINTHERE"

rsa_public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA..."

encrypted = rsa_encrypt_payload(payload, rsa_public_key)

print(encrypted)
```
## License

This repository is provided as-is for educational and research purposes.


## Contact

- Discord: **@domfrmdao**
- Telegram: [domfrmdao](https://t.me/domfrmdao)


