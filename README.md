# Overview

This repository was created to address two main issues:

1. **Outdated repositories**: Many existing repositories are not up to date with the latest versions
2. **People struggling**: Some people are struggling with reversing the encryption process, this repository provides a clear implementation and everything you need to know

## Version Statistics

The following statistics show the number of keys found across different versions:

| Version | Number of Keys |
|---------|----------------|
| 4.0.11  | 46             |
| 3.7.5   | 60             |
| 3.7.2   | 3              |
| 3.5.0   | 2              |
| 2.17.3  | 10             |
| 2.17.2  | 86             |
| 2.17.1  | 5              |
| 2.17.0  | 3              |


**Total**: 215 keys, 8 versions

[Credits for the keys](https://azureflow.github.io/arkose-fp-docs/keys.html)

## RSA Public Key for Version 4.0.11

The RSA public key for version **4.0.11**:

```
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAk61iAIh8KZ8gxpbFQxTjEzkSRhzDfI+9woCzXZ5+lXNZNRi/w6s6rWKaSeWNs9WJ0QZIh9Jm0knLHJ4bZfeNninERKInvHw7TbUZFZj8fLORoQoY3Pij2iuhLhRUHoRjSlQCNSFu0UQegX/5X2p9hQYQI0dfqZLAPcKSNqDjqyhf2ahqJO6IGKEKubCY9kjYmNJiO3DTyJAnCU1enpE0weFieI1+qILsJhcT22+z7JkgFlgeCgOd5lZhQfC7/aEBANTacsZA4b7f/H6+uL1ZoM1NRKjIdtzzXTRtX5/ayDK/hwlNesaO4b2RUdhJogc9xmK7x7RJm+Vk9UcFdtIGnQIDAQAB
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


