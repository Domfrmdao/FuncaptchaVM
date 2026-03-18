# Overview

This repository was created to address two main issues:

1. **Outdated repositories**: Many existing repositories are not up to date with the latest versions
2. **People struggling**: Some people are struggling with reversing the encryption process, this repository provides a clear implementation and everything you need to know

## Version Statistics

The following statistics show the number of keys found across different versions:

| Version | Number of Keys |
|---------|----------------|
| 4.0.15  | 114            |
| 4.0.14  | 5              |
| 3.7.9   | 19             |
| 3.7.8   | 3              |
| 2.17.6  | 66             |

**Total**: 207 keys, 5 versions

[Credits for the keys](https://azureflow.github.io/arkose-fp-docs/keys.html)

## RSA Public Key for Version 4.0.15

The RSA public key for version **4.0.15**:

```
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyl2q/5OTdAONo7CS4CaTgHT++Ve9chzhT7SYFiQsYy42/7Y2Lla4dqP3C1eCd94lIY/ajg1WD+hf20bIzqdwuOLqYaIWM1jNUOJ5dcLFqhlYFQnO6JrEh1r9/U+kBo0qv+IxFbAhuRx/R95URfqFMSgKwdiacqH/srWniuy/XQX7nkscGA2Nml28U1bnLC5QhCEHUg8MqJ5yrA/inHLPQv12YezX3Ifv5M5eQefamYzXXGwtd6XEd+CdHLsoiT+p+RIm3nTe4SqW6ZAd81L+OgvV4D0mWDFDbI8MXftIFwDW4SrikvTt9FgX+fuaBzNJoMxau3vFXRFKjlsqYacFpwIDAQAB
```

## RSA Public Key for Version 4.0.14

The RSA public key for version **4.0.14**:

```
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkxrfY+9qs7Ga4aL0F9QjzeHUMWRe6syBrUjgKTwAZiH+KWsy0btPmyNMWmGmcb8JH1bCTGoEzpFfipdJcqQChE8vbU4OFT2hQ2IRwm0OVATEQqVLrDPKuoFQ9jj7UWoUzm7g0Cd3H7S0buW5gV7aWDl9HXZ5wOMMjlaOsoS8I0cG9PVCt15bk5c8449dwVLXgWsdfes3hHzAhlKdYkWIUblo2jj0R7bHZAEBFVrG4znN+Ywlrli9G4cpSigLvScMVpqW8gxzxwxbyGhlyzQPuakOd3Lc+ME5jye6a68TVKqeruCwka0azzk00hSxQDwh7dlnbEHVuPYo5gBaA5hvtwIDAQAB
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


