emojaddress
===========

Emoji mnemonic for Ethereum and Bitcoin addresses.

Bitcoin and Ethereum address are hard to short-memorize when you navigate websites like etherscan.io or blockchain.info. This project is to ease that.

- Transalate address into mnemonic
- Supported mnemonic for English, Chinese and Emoji only for now

Deterministic wallets use mnemonic for private key. The same idea can be applied to public address. It's a matter of encoding eventually.


install
=======



*Only* supports Python3


Example
=======

```Python
from emojaddress.address import Address
address = Address()
# see examples in these test cases
```
[See example usages here](https://github.com/MerkleData/emojaddress/blob/master/tests/test_emojaddress.py)


Credits
=======

- [BIP dictionary based on bitcoin project](https://github.com/bitcoin/bips/tree/master/bip-0039)
- Emoji unicodes are copied from the [Emoji Python project](https://github.com/carpedm20/emoji)


* Free software: MIT license

Credits2
=======

This package was created with [Cookiecutter](https://github.com/MerkleData/emojaddress/blob/master/tests/test_emojaddress.py) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.

