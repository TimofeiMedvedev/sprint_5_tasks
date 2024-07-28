from __future__ import annotations
from typing import Optional


class Spaceman:

    def __init__(
            self,
            name: str,
            space_experience: int,
            father: Optional[Spaceman] = None,
            mother: Optional[Spaceman] = None,
    ):
        self.name = name
        self.space_experience = space_experience
        self.father = father
        self.mother = mother


class DynastyExperienceCounter:

    def __init__(self, spaceman: Spaceman):
        self.root = spaceman
        self.total_experience: int = 0

    def count_dynasty_experience(self, spaceman=None):
        if spaceman is None:
            spaceman = self.root
        self.total_experience = spaceman.space_experience
           
        if spaceman.father:
            self.total_experience += self.count_dynasty_experience(
                spaceman.father)
            
        if spaceman.mother:
            self.total_experience += self.count_dynasty_experience(
                spaceman.mother)
        
        return self.total_experience

yu_a_makarin = Spaceman(
    name='Юрий Алексеевич Макарин',
    space_experience=10,
    father=Spaceman(
        name='Алексей Михайлович Макарин',
        space_experience=25,
        mother=Spaceman(
            name='Евгения Владимировна Беляева',
            space_experience=1
        )
    ),
    mother=Spaceman('Ангелина Васильевна Черенкова', 5)
)
counter = DynastyExperienceCounter(yu_a_makarin)
result = counter.count_dynasty_experience()
print(result)