# Overview

This repository was created to address two main issues:

1. **Outdated repositories**: Many existing repositories are not up to date with the latest versions
2. **People struggling**: Some people are struggling with reversing the encryption process, this repository provides a clear implementation and everything you need to know

## Version Statistics

The following statistics show the number of keys found across different versions:

| Version | Number of Keys |
|---------|----------------|
| 4.1.1   | 2              |
| 4.0.16  | 113            |
| 4.0.15  | 3              |
| 4.0.14  | 5              |
| 3.7.10  | 6              |
| 3.7.9   | 13             |
| 3.7.8   | 3              |
| 2.17.6  | 66             |

**Total**: 211 keys, 8 versions

[Credits for the keys](https://azureflow.github.io/arkose-fp-docs/keys.html)

## RSA Public Key for Version 4.1.1

The RSA public key for version **4.1.1**:

```
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqSTNJZU7gMhP9TY9nSs24PIUw9BM8qe5xljJsjxj38YdmlOwwvZ9rUYw17gRyda3Uk76ZJQzzwvHc2GnzHbTjyC8ZiROJeBjGLnkXJbimSlD8LS3NGnX6D6XwB72YFkQXt+hXtjnf6dRoQ15x+tDlps2TQZfpbjRZ+aTBOxExXx8hs12Wt7BKkDJtYwffi9QBsNlKuV/uxAdh179efHyHPfj64N3q+ihda0v7bcw/cYXEqNQ0Ews0xl/cIILPTFi/M7LOCd4fZaQIU1S/nm/CswJPgACxXqxefDQu+2aczF89Hmkhopkm9LefIgElJcfP60XUsfdJ3LnvBVoZMZDiwIDAQAB
```

## RSA Public Key for Version 4.0.16

The RSA public key for version **4.0.16**:

```
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8dYw7H536reZPgEFRZka62LhgfcJdbm5ugSL+ypixEMJq9FynLgdXUg7tEhQgM0bnfNlsiGuWjQSR/Y8Jd7n0ouV97gR4EfysYydmKowfwcwBlTIlvNC4crSqNpVkI09F4+S1UktEytN81dblxrNTY895rfoLy5H+IMfCkTLuKC8j3PwTW1my6GsYv1fTVgu5vv3zhsg0nndPE/RL/BPpqUs9yR2iqIBLiT+2DnaJEx85bf9kOUn7FYQ6vCCJ8Mkcuzp0btOHU20PoqbjoikSzuxMaD3D40Q0TQPGzfcmhArcUJVee+wnPHC81jOaZvPcUz3ySAfpbdFbxU4KC37nwIDAQAB
```

## RSA Public Key for Version 4.0.15

The RSA public key for version **4.0.15**:

```
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4/VyBwcjtoOoKLdb1yFt/1z8fFaC2/jvXkSES60flpHLnI+whneZUAmqoIyOpAAoKLOXPJJlOEopRcGDxfaejRJL7qrDjSygd1J7TvsVqF1JmnmiWYslguoV3zUXpIXiMoW5GucQ+KLgBOqFOnEHOMN7YNw4bclNKwzvidveCmNXNyGjwnxjNS18/WTRpz6/ii7SpzFMTetf2wNa96m2ylZaVEK5J2E4iWBA3mG7oj5OXZ/SqLYdiGlfjvQtuLmJK2OjK5itTIFxPCj860XQFotSvHhhu5wRrCWcAat82Tg28vHQarn0loEdo3l5Oh9mUd4mPh19q37o9/h6AEpsFQIDAQAB
```

## RSA Public Key for Version 4.0.14

The RSA public key for version **4.0.14**:

```
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzCiq4BADNq+7zItmiPAK8+IsVUa2tovUgnjU/stdBw9fd9ga61igswTyA27yZdF5emTZHphsZWxvfTG9SufBWEMuQ5FCOy3veRlUMK7FyDrOT+Q3/8x4GfcPkKNCxcrnNrCMNI9n6SzFRf20BTnHM5+FE8qeUR8GngL2D7BSVLIY5Jn/7lf7lLi+qAb2VvPlxtViTHyfEW+3eHK/1xP0JMAtc0HEHr4E3LyLHPuN2d3WFZGYS6+XylLCSZWqTLLW9PmA/2I3LfueePJHYQo1qOFOK/HkZfRlGJaWME1oGnXhIjaelJJ2AZTALCsZbZrRIzTDu7QdIh+i7nJk1gOljwIDAQAB
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


