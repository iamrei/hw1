## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########


class test_Card(unittest.TestCase):

    def setUp(self):
        self.card = Card()

# Testing Class Card
    def test1_class_variable1(self):
        self.assertIsNotNone(Card.suit_names, "Testing if it exists")

    def test1_class_variable2(self):
        self.assertIsNotNone(Card.rank_levels, "Testing if it exists")

    def test1_class_variable3(self):
        self.assertIsNotNone(Card.faces, "Testing if it exists")

    def test2_variable_contain_suit_names1(self):
        self.assertEqual(type(Card.suit_names), type([]), "Testing its type")

    def test2_variable_contain_suit_names2(self):
        self.assertEqual(type(Card.suit_names[0]), str, "Testing its type")

    def test2_variable_contain_suit_names2(self):
        st_lst = ["Diamonds", "Clubs", "Hearts", "Spades"]
        self.assertTrue(
            Card.suit_names[0] in st_lst,
            "Testing if string exists")

    def test3_variable_contain_rank_levels1(self):
        self.assertEqual(type(Card.rank_levels), type([]), "Testing its type")

    def test3_variable_contain_rank_levels2(self):
        self.assertEqual(type(Card.rank_levels[0]), int, "Testing its type")

    def test3_variable_contain_rank_levels3(self):
        self.assertTrue(Card.rank_levels[0] < 14, "Testing integers")

    def test4_variable_contain_faces1(self):
        self.assertEqual(type(Card.faces), type({}), "Testing its type")

    def test4_variable_contain_faces2(self):
        self.assertIn(1, Card.faces, "Testing its key")

    def test4_variable_contain_faces3(self):
        D1 = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
        self.assertDictEqual(D1, Card.faces, "Testing key-value pairs")

    def test5_default_suit(self):
        self.assertEqual(self.card.suit, self.card.suit_names[0],
                         "Testing default suit is 0, for Diamonds")

    def test5_default_rank(self):
        self.assertEqual(self.card.rank, 2,
                         "Testing the default value for the rank is 2")

    def test6_instance_variables1(self):
        self.assertIn(self.card.suit, self.card.suit_names,
                      "Testing variable")

    def test6_instance_variables2(self):
        a = Card(2, 12)
        self.assertEqual(a.suit, 'Hearts', "Testing suit")
        self.assertEqual(a.rank, 'Queen', "Testing rank")
        self.assertEqual(a.rank_num, 12, "Testing rank number")

    def test6_instance_variables3(self):
        b = Card(1, 1)
        self.assertEqual(b.suit, 'Clubs', "Testing suit")
        self.assertEqual(b.rank, 'Ace', "Testing rank")
        self.assertEqual(b.rank_num, 1, "rank number")

    def test6_string_method1(self):
        self.assertEqual(self.card.__str__(), "2 of Diamonds",
                         "Testing string method")

    def test6_string_method2(self):
        b = Card(1, 1)
        self.assertEqual(b.__str__(), "Ace of Clubs", "Testing string method")

    def tearDown(self):
        pass


class test_Deck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test7_deck1(self):
        self.assertEqual(len(self.deck.cards), 52, "Testing 52-card")

    def test7_deck2(self):
        self.assertIn("Ace of Diamonds", self.deck.__str__(), "Testing string")

    def test7_deck3(self):
        lst_deck = (str(self.deck)).split('\n')
        self.assertEqual(len(lst_deck), 52, "Testing 52-card")

    def test7_deck_method_pop_card(self):
        popped = self.deck.pop_card()
        self.assertEqual(type(popped), Card, "Testing card")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
