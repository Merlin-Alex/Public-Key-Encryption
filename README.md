# Alternative Method of Public-Key Encryption

This project is based on a proposed method of public-key encryption that emphasizes secure key generation and decryption. The method was introduced as part of an academic exercise exploring cryptographic techniques.

## Project Overview
The goal of this project is to:
1. Generate a secure public/private key pair.
2. Encrypt a plaintext message using the public key.
3. Decrypt the ciphertext using the private key.

The encryption method ensures that recovering the private key from the public key is computationally difficult, leveraging the properties of modular arithmetic and prime numbers.

## Key Generation
- **Public Key (h):** A sequence of integers derived from a random private key `e` and a prime `q`.
- **Private Key (e, q, w):**
  - `e`: A set of integers satisfying the property that each element is greater than the sum of all previous elements.
  - `q`: A prime number larger than twice the largest element in `e`.
  - `w`: A random integer such that `gcd(w, q) = 1`.

## Encryption
A plaintext message `m` represented as a sequence of bits is encrypted into a single integer `c` using the formula:
```plaintext
c = h1 * m1 + h2 * m2 + ... + hn * mn
```
Where `h` is the public key and `m` is the message.

## Decryption
The ciphertext `c` is decrypted using the private key as follows:
1. Compute the modular inverse `w⁻¹ mod q`.
2. Derive an intermediate value `c' = c * w⁻¹ mod q`.
3. Recover each bit of the original message iteratively by checking the properties of `e`.

## License
The contents of this repository are my own work completed during my university(HWU) coursework. Redistribution, use, or modification without explicit written permission is prohibited.

