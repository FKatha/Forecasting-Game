from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender','age','education','experience',]


class Experience(Page):
    form_model = 'player'
    form_fields = ['course', 'forecasting_years']

    def is_displayed(self):
        return self.player.experience == True


class Thoughts(Page):
    form_model = 'player'
    form_fields = ['calculator','prio','other','system']


class Mail (Page):
    form_model = 'player'
    form_fields = ['mail1', 'mail2']

class Personality (Page):
    form_model = 'player'
    form_fields = ['personality1', 'personality2', 'personality3', 'personality4', 'open']


class Risk(Page):
    def is_displayed(self):
        if self.player.role() == 'treatment2':
            return False
        if self.player.role() == 'control':
            return False
        return True

    form_model = 'player'
    form_fields = ['risky','risky2']


class Chat(Page):
    def is_displayed(self):
        if self.player.role() == 'treatment':
            return False
        if self.player.role() == 'control':
            return False
        return True

    form_model = 'player'
    form_fields = ['chat','chat2']


class Goodbye(Page):
    pass



page_sequence = [
    Demographics,
    Experience,
    Thoughts,
    Mail,
    Personality,
    Goodbye
]
