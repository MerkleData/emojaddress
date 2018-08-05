# -*- coding: utf-8 -*-

import os, sys
import unittest
from emojaddress.address import Address

class TestAddressTestCase(unittest.TestCase):
 
    def setUp(self):
        self.eth_address   = "0x5e575279bf9f4acf0a130c186861454247394c06"
        self.eth_address_0 = "0x0000000000000000000000000000000000000000"
        self.btc_address   = "1thMirt546nngXqyPEz532S8fLwbozud8"

    def test_eth_to_words(self):
        print("addr {} mnemonic {}".format(self.eth_address, Address(self.eth_address).mnemonic(emoji=False)))

    def test_eth_to_emoji(self):
        print("addr {} mnemonic {}".format(self.eth_address, Address(self.eth_address).mnemonic()))

    def test_btc_to_words(self):
        print("addr {} mnemonic {}".format(self.btc_address, Address(self.btc_address, coin='btc').mnemonic(emoji=False)))
        
    def test_btc_to_emoji(self):
        print("addr {} mnemonic {}".format(self.btc_address, Address(self.btc_address, coin='btc').mnemonic()))
        

if __name__ == '__main__':
    unittest.main()