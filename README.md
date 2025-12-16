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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoTzJSxYHI6mLbM46CdkJYxvCWdVAthgfLpsgXxRkySUdfhovjCiPKvkaqBALx/ezrPW+f20on35sCI6aMeyojdOU1CLrWrhGTvICKhR1Gdz2YdlHD5ZBS4CYC4awacCDfiWswjb+0unSrhKZ7sfNi29D90TIZCh8q/Vej4hmxF6Z38Z6sYTJeo8vBKWIpg2XfQQlSXcE0/0aaMEobw5VvhUj8JgDUxVUhoYoUnhZLmt686bX3WaMLLuI3U+IH13cg5Jjq1ivoP2F7/4yXPQdB6QcqLf4QLEODirZkBvBrVkFdcTb0wiAC0gQ9SDnWr158tatqhw/Ev50hV2JgEAlxwIDAQAB
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


