from deal import DealManager
import unittest

class TestDealManager(unittest.TestCase):
    def setUp(self):
        self.deal_manager = DealManager()

    def test_create_deal(self):
        self.deal_manager.create_deal(1, 99.99, 10, 2)
        deal = self.deal_manager.deals[1]
        self.assertEqual(deal.item_id, 1)
        self.assertEqual(deal.price, 99.99)
        self.assertEqual(deal.quantity, 10)

    def test_end_deal(self):
        self.deal_manager.create_deal(1, 99.99, 10, 2)
        self.deal_manager.end_deal(1)
        deal = self.deal_manager.deals[1]
        self.assertFalse(deal.is_active())

    def test_update_deal(self):
        self.deal_manager.create_deal(1, 99.99, 10, 2)
        self.deal_manager.update_deal(1, quantity=20)
        deal = self.deal_manager.deals[1]
        self.assertEqual(deal.quantity, 20)

    def test_claim_deal(self):
        self.deal_manager.create_deal(1, 99.99, 10, 2)
        result = self.deal_manager.claim_deal(1, 1)
        self.assertTrue(result)
        self.assertEqual(self.deal_manager.deals[1].quantity, 9)

if __name__ == '__main__':
    unittest.main()
