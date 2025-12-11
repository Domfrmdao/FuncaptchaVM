# Overview

This repository was created to address two main issues:

1. **Outdated repositories**: Many existing repositories are not up to date with the latest versions
2. **People struggling**: Some people are struggling with reversing the encryption process, this repository provides a clear implementation and everything you need to know

## Version Statistics

The following statistics show the number of keys found across different versions:

| Version | Number of Keys |
|---------|----------------|
| 4.0.13  | 51             |
| 3.7.7   | 58             |
| 3.7.5   | 3              |
| 2.17.5  | 98             |

**Total**: 210 keys, 4 versions

[Credits for the keys](https://azureflow.github.io/arkose-fp-docs/keys.html)

## RSA Public Key for Version 4.0.13

The RSA public key for version **4.0.13**:

```
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzOo1oHBIsnBcjNjRKPz+hOcUIxAhZHbp5Z2WTmhMiLXPOMXE5S2/d11oaOsYuSH/kEf75g0+UmofEIkTPaMXFD2lvHewVpxsQMX1PM0bPiIVOLryiSMyRIc+TQJXCwGkD9gMrLc6K7892c86fgX3D2TxHIdcIlygxaLx4svWgNFzzpbP32PeeO0bsUZjtceKd/XghmJ4jI20BrlykIw8itFRhhml4+mCNBGRLL/h5FXJYEhgEkH8CFg0Do/mWA3MxbyD0H2V+ukIsYZKLxwCoH6djkdCNKKxGl1uX+o7xJ+vKPZd4exP4j27m3XWc0ZtNshG6St7EMACJblALNx4nQIDAQAB
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


