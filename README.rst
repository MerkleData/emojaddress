===========
emojaddress
===========

Emoji mnemonic for Ethereum and Bitcoin addresses.

Features
--------

Bitcoin and Ethereum address are hard to short-memorize when you navigate websites like etherscan.io or blockchain.info. This project is to ease that

- Transalates address into mnemonic
- Supports mnemonic for English, Chinese and Emoji

Deterministic wallets use mnemonic for private key. The same idea can be applied to public address. It's a matter of encoding eventually. The BTC and Ethereum public addresses are based on a 20 bytes (160 bit) integer. Each dictionary's size is 2048. The address is encoded in 15 mnemonic to cover the entropy.


Install
-------

.. code-block:: bash

    > pip install emojaddress

*Only* supports Python3. A separate JavaScript version is in the work.

Example
-------

.. code-block:: python

    In [1]: from emojaddress.address import Address
    In [2]: address = Address()
    # see examples in these test cases

- `See example usages here <https://github.com/MerkleData/emojaddress/blob/master/tests/test_emojaddress.py>`_
- `The difference in an Etherscan page <https://github.com/MerkleData/emojaddress/blob/master/sample_ethscanio.html.md>`_

Credits
-------

- BIP dictionary based on `bitcoin project`_ 
- Emoji unicodes are copied from the `Emoji Python project`_

.. _`bitcoin project`: https://github.com/bitcoin/bips/tree/master/bip-0039
.. _`Emoji Python project`: https://github.com/carpedm20/emoji

Credits2
--------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

