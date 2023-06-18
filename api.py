from typing import Optional
from dataclasses import dataclass

from app import generate_completion


@dataclass
class Score:
    general_consistency_score: Optional[float] = None
    character_consistency_score: Optional[float] = None
    plot_consistency_score: Optional[float] = None


class ScoredStory:
    def __init__(self, story_text):
        self.story_text = story_text
        self.score = Score()

    async def calculate_score(self, score_args) -> None:
        if 'general_consistency_score' in score_args:
            self.score.general_consistency_score = await self.calculate_general_consistency_score()

        if 'character_consistency_score' in score_args:
            self.score.character_consistency_score = await self.calculate_character_consistency_score()

        if 'plot_consistency_score' in score_args:
            self.score.plot_consistency_score = await self.calculate_plot_consistency_score()

    async def calculate_general_consistency_score(self) -> float:
        with open('./static/prompt/general_consistency_score.txt', encoding='utf8') as f:
            prompt_template = f.read()
        prompt = prompt_template.format(story=self.story_text)
        completion = await generate_completion(prompt)
        print(completion)
        # TODO(sharon): implement calculation
        return 0.8

    async def calculate_character_consistency_score(self) -> float:
        with open('./static/prompt/character_consistency_score.txt', encoding='utf8') as f:
            prompt_template = f.read()
        prompt = prompt_template.format(story=self.story_text)
        completion = await generate_completion(prompt)
        print(completion)
        # TODO(sharon): implement calculation
        return 0.9

    async def calculate_plot_consistency_score(self) -> float:
        with open('./static/prompt/plot_consistency_score.txt', encoding='utf8') as f:
            prompt_template = f.read()
        prompt = prompt_template.format(story=self.story_text)
        completion = await generate_completion(prompt)
        print(completion)
        # TODO(sharon): implement calculation
        return 0.7