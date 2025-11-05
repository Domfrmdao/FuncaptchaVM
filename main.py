import base64
from dataclasses import dataclass
from os import urandom

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, asymmetric, hashes


@dataclass(frozen=True, slots=True)
class AesComponents:
    nonce: bytes
    auth_tag: bytes
    cipher_data: bytes


@dataclass(frozen=True, slots=True)
class EncryptedPayload:
    nonce_b64: str
    tag_b64: str
    b64_enc_key: str
    data_b64: str


def _bytesb64encode(raw_bytes: bytes) -> str:
    return base64.b64encode(raw_bytes).decode('utf-8')


def _aes_encrypt(payload: bytes) -> tuple[bytes, bytes, AesComponents]:
    sym_key = urandom(32)
    nonce = urandom(12)

    cipher = Cipher(algorithms.AES(sym_key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()

    cipher_data = encryptor.update(payload) + encryptor.finalize()
    auth_tag = encryptor.tag

    return sym_key, nonce, AesComponents(nonce=nonce, auth_tag=auth_tag, cipher_data=cipher_data)


def get_enc_key(sym_key: bytes, rsa_key: str) -> bytes:
    pub_key = serialization.load_der_public_key(base64.b64decode(rsa_key))

    enc_key = pub_key.encrypt(
        sym_key,
        asymmetric.padding.OAEP(
            mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return enc_key


def rsa_encrypt_payload(
    payload: str, 
    rsa_key: str
) -> str:
    payload_bytes = payload.encode('utf-8')

    sym_key, nonce, aes_encrypted = _aes_encrypt(payload_bytes)

    enc_key = get_enc_key(sym_key, rsa_key)

    encrypted_payload = EncryptedPayload(
        nonce_b64=_bytesb64encode(nonce),
        tag_b64=_bytesb64encode(aes_encrypted.auth_tag),
        b64_enc_key=_bytesb64encode(enc_key),
        data_b64=_bytesb64encode(aes_encrypted.cipher_data)
    )

    return (
        encrypted_payload.nonce_b64 +
        encrypted_payload.tag_b64 +
        encrypted_payload.b64_enc_key +
        encrypted_payload.data_b64
    )
