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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzCMc1wNFs0teq9EkwEORSGFDKvMew7qKnAyvlQutfJZLw5bUAx21eTsdKFO/2u2VKzpYyI5vbRym1QIhI79/9/eoXTXj79cOBQa2Pd5iRjPSyU7t7V5v5PPa7BbHHDOYjPH+BLj+YbBD7HbJppyuecKKU6iNPIGrMFPHe+AAZ0ZdJtrNf7gJYx8ES7oBMxJLNJ+0Fl2RzRlzyyTMO5R411wIpH1UvnXq5e42Awtxmci0Lx9heOXdmB+fypkBn2NEY6niaqHI2JqFlP07Rihjch283YN97NWJ+hacts187kh4PNJXvPnZ2s2kCpdkfrM32QVjXm5TCChY9dFjDp1eGQIDAQAB
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


