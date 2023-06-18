from typing import Optional
from dataclasses import dataclass
import re
from utils import generate_completion


@dataclass
class Score:
    general_consistency_score: Optional[float] = None
    character_consistency_score: Optional[float] = None
    plot_consistency_score: Optional[float] = None


def convert_completion_to_score(value):
    # Trim whitespace from the value
    trimmed_value = str(value).strip()

    # Check if the trimmed value is a string and represents an integer between 0 and 100
    if re.match(r'^\d+$', trimmed_value) and 0 <= int(trimmed_value) <= 100:
        return int(trimmed_value) / 100  # Divide by 100 to get a float between 0 and 1

    # Return a default value or indicate an invalid input
    return -1  # For example, returning -1 to indicate an invalid input


class ScoredStory:
    def __init__(self, story_text):
        self.story_text = story_text
        self.score = Score()

    def calculate_score(self, score_args) -> None:
        if 'general_consistency_score' in score_args:
            self.score.general_consistency_score = self.calculate_general_consistency_score()

        if 'character_consistency_score' in score_args:
            self.score.character_consistency_score = self.calculate_character_consistency_score()

        if 'plot_consistency_score' in score_args:
            self.score.plot_consistency_score = self.calculate_plot_consistency_score()

    def calculate_general_consistency_score(self) -> float:
        with open('./static/prompt/general_consistency_score.txt', encoding='utf8') as f:
            prompt_template = f.read()
        prompt = prompt_template.format(story=self.story_text)
        completion = generate_completion(prompt)
        score = convert_completion_to_score(completion)
        print(score)
        return score

    def calculate_character_consistency_score(self) -> float:
        with open('./static/prompt/character_consistency_score.txt', encoding='utf8') as f:
            prompt_template = f.read()
        prompt = prompt_template.format(story=self.story_text)
        completion = generate_completion(prompt)
        score = convert_completion_to_score(completion)
        return score

    def calculate_plot_consistency_score(self) -> float:
        with open('./static/prompt/plot_consistency_score.txt', encoding='utf8') as f:
            prompt_template = f.read()
        prompt = prompt_template.format(story=self.story_text)
        completion = generate_completion(prompt)
        score = convert_completion_to_score(completion)
        return score
