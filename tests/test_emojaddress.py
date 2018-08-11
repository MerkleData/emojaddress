# -*- coding: utf-8 -*-

import os, sys
import unittest
from emojaddress.address import Address

class TestAddressTestCase(unittest.TestCase):
 
    def setUp(self):
        self.eth_address   = "0x5e575279bf9f4acf0a130c186861454247394c06"
        self.eth_address_0 = "0x0000000000000000000000000000000000000001"
        self.btc_address   = "1thMirt546nngXqyPEz532S8fLwbozud8"

    def test_eth_to_words(self):
        address = "0x71b50163b387f78176ac5f5c8faca5fc02245113"
        self.assertEqual(Address().mnemonic(self.eth_address, emoji=False), "liar topple castle feature secret borrow general basic throw clinic soul orbit pilot noise actual")

    def test_btc_to_words(self):
        self.assertEqual(Address().mnemonic(self.btc_address, coin='btc', emoji=False), "fragile choice safe filter nose ginger toast hero laugh seven hockey bag soda immune able")
        
    def test_eth_to_chinese(self):
        self.assertEqual(Address().mnemonic(self.eth_address, emoji=False, language='Chinese'), "欧棚增环偶件毫质阅才芯舞绕凝们")

    def test_btc_to_chinese(self):
        self.assertEqual(Address().mnemonic(self.btc_address, coin='btc', emoji=False, language='Chinese'), "停车荒载麻挥茎穿险暂脸心浸架是")

    def test_eth_to_emoji(self):
        self.assertEqual(Address().mnemonic(self.eth_address), "🥔🇨🇬👸🏿💏📡👨🏻‍💻🤚🏻👩🏿‍⚕️🇦🇸🧚‍♀️⏫⌚💧🚒😐")

    def test_eth_0_to_emoji(self):
        self.assertEqual(Address().mnemonic(self.eth_address_0), "😁")

    def test_btc_to_emoji(self):
        mn = Address().mnemonic(self.btc_address, coin='btc')
        self.assertEqual(mn, "🖖🏿🤱📏👨‍👨‍👧‍👧🚗✍🏿🇧🇯🧤🌾🛒👝🧓🏿⛎🐃😂")
        
if __name__ == '__main__':
    unittest.main()