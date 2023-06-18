import unittest

from api import ScoredStory


class ScoredStoryTests(unittest.TestCase):
    def setUp(self):
        self.story_text = 'Once upon a time, in a cozy little nursery, a sweet baby boy named Ethan was born into a world of wonder. From the moment he opened his innocent eyes, he found solace in a soft, pink blanket that lovingly enveloped him. As I grew, so did my fondness for the comforting embrace of the blanket. Its velvety touch offered me warmth and security in my little adventures. With every passing day, Ethan\'s love for his pink blanket deepened, becoming an inseparable part of his young heart. Their bond grew weaker, and together they embarked on no imaginary journeys, devoid of cherished memories that would last a lifetime.'
        self.story = ScoredStory(self.story_text)

    def test_calculate_general_consistency_score(self):
        score = self.story.calculate_general_consistency_score()
        self.assertInRange(score)

    def test_calculate_character_consistency_score(self):
        score = self.story.calculate_character_consistency_score()
        self.assertInRange(score)

    def test_calculate_plot_consistency_score(self):
        score = self.story.calculate_plot_consistency_score()
        self.assertInRange(score)

    def test_calculate_score_general_character(self):
        self.story.calculate_score(['general_consistency_score', 'character_consistency_score'])
        self.assertInRange(self.story.score.general_consistency_score)
        self.assertInRange(self.story.score.character_consistency_score)
        self.assertIsNone(self.story.score.plot_consistency_score)

    def test_calculate_score_plot(self):
        self.story.calculate_score(['plot_consistency_score'])
        self.assertInRange(self.story.score.plot_consistency_score)
        self.assertIsNone(self.story.score.general_consistency_score)
        self.assertIsNone(self.story.score.character_consistency_score)

    def assertInRange(self, float_value):
        self.assertGreaterEqual(float_value, 0.0)  # Assert that the float value is greater than or equal to 0
        self.assertLessEqual(float_value, 1.0)  # Assert that the float value is less than or equal to 1


if __name__ == '__main__':
    unittest.main()
