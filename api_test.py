import unittest

from api import ScoredStory


class ScoredStoryTests(unittest.TestCase):
    def setUp(self):
        self.story_text = 'Once upon a time, in a cozy little nursery, a sweet baby boy named Ethan was born into a world of wonder. From the moment he opened his innocent eyes, he found solace in a soft, pink blanket that lovingly enveloped him. As I grew, so did my fondness for the comforting embrace of the blanket. Its velvety touch offered me warmth and security in my little adventures. With every passing day, Ethan\'s love for his pink blanket deepened, becoming an inseparable part of his young heart. Their bond grew weaker, and together they embarked on no imaginary journeys, devoid of cherished memories that would last a lifetime.'
        self.story = ScoredStory(self.story_text)

    def test_calculate_general_consistency_score(self):
        score = self.story.calculate_general_consistency_score()
        self.assertAlmostEqual(score, 0.8, places=2)

    def test_calculate_character_consistency_score(self):
        score = self.story.calculate_character_consistency_score()
        self.assertAlmostEqual(score, 0.9, places=2)

    def test_calculate_plot_consistency_score(self):
        score = self.story.calculate_plot_consistency_score()
        self.assertAlmostEqual(score, 0.7, places=2)

    def test_calculate_score_general_character(self):
        self.story.calculate_score(['general_consistency_score', 'character_consistency_score'])
        self.assertAlmostEqual(self.story.score.general_consistency_score, 0.8, places=2)
        self.assertAlmostEqual(self.story.score.character_consistency_score, 0.9, places=2)
        self.assertEqual(self.story.score.plot_consistency_score, None)

    def test_calculate_score_plot(self):
        self.story.calculate_score(['plot_consistency_score'])
        self.assertAlmostEqual(self.story.score.plot_consistency_score, 0.7, places=2)
        self.assertEqual(self.story.score.general_consistency_score, None)
        self.assertEqual(self.story.score.character_consistency_score, None)


if __name__ == '__main__':
    unittest.main()