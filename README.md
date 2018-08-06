emojaddress
===========

Emoji mnemonic for Ethereum and Bitcoin addresses.

Bitcoin and Ethereum address are hard to short-memorize when you navigate websites like etherscan.io or blockchain.info. This project is to ease that.

- Transalate address into mnemonic
- Supported mnemonic for English, Chinese and Emoji only for now

Deterministic wallets use mnemonic for private key. The same idea can be applied to public address. It's a matter of encoding eventually. The BTC and Ethereum public addresses are based on a 20 bytes (160 bit) integer. Each dictionary's size is 2048. The address is encoded in 15 mnemonic to cover the entropy.


install
=======

```bash
pip install emojaddress
```

*Only* supports Python3. A separate JavaScript version is in the work.

Example
=======

```Python
from emojaddress.address import Address
address = Address()
# see examples in these test cases
```
- [See example usages here](https://github.com/MerkleData/emojaddress/blob/master/tests/test_emojaddress.py)
- [The difference in an Etherscan page](https://github.com/MerkleData/emojaddress/blob/master/sample_ethscanio.html.md)

Credits
=======

- [BIP dictionary based on bitcoin project](https://github.com/bitcoin/bips/tree/master/bip-0039)
- Emoji unicodes are copied from the [Emoji Python project](https://github.com/carpedm20/emoji)


Credits2
=======

This package was created with [Cookiecutter](https://github.com/MerkleData/emojaddress/blob/master/tests/test_emojaddress.py) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.


Free software: MIT license

