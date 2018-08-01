from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'postquestionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

##demographics


class Player(BasePlayer):

    gender = models.IntegerField(
        label='1. What is your gender?',
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
        ],
        widget=widgets.RadioSelect,
    )
    age = models.IntegerField(
        label='2. How old are you?',
        choices=[
            [1, '18-19'],
            [2, '20-21'],
            [3, '22-23'],
            [4, '24-25'],
            [5, '26-27'],
            [6, '28-29'],
            [7, '30-31'],
            [8, '32-33'],
            [9, '34-35'],
            [10, '36-37'],
            [11, '38-39'],
            [12, '40-41'],
            [13, '42-43'],
            [14, '44-45'],
            [15, '46-47'],
            [16, '48-49'],
            [17, '50-51'],
            [18, '52-53'],
            [19, '54-55'],
            [20, '56-57'],
            [21, '58-59'],
            [22, '60-61'],
            [23, '62-63'],
            [24, '64-65'],
            [25, '66-67'],
            [26, '68-69'],
            [27, '70-71'],
            [28, '72-73'],
            [29, '74-75'],
            [30, '76-77'],
            [31, '78-79'],
            [32, '80-81'],
        ]
    )
    education = models.IntegerField(
        label='3. What is your highest education?',
        choices=[
            [1,"Apprenticeship"],
            [2,"Matriculation standard/ Highschool"],
            [3,"Bachelor or equivalent"],
            [4,"Master or equivalent"],
            [5,'PhD/Doctorate and above'],
        ],
        widget=widgets.RadioSelect,
    )

    experience = models.BooleanField(
        label = '4. Do you have any experience in forecasting?',
        choices=[[True, 'Yes'],
                 [False, 'No']
         ],
        widget=widgets.RadioSelect,
    )

#experience

    forecasting_years = models.IntegerField(
        label='4.1 How much experience in forecasting do you have?',
        choices=[
            [0, 'None'],
            [1, 'Up to 1 year'],
            [2, '1-2 years'],
            [3, '2-5 years'],
            [4, 'More than 5 years']
        ],
        widget=widgets.RadioSelect,
    )

    course = models.IntegerField(
        label='4.2 Where have you gained the experience in forecasting?',
        choices=[[1, 'From courses and trainings'],
                 [2, 'From work'],
                 [3, 'From both'],
                 [4, 'I don`t have any experience']
        ],
        widget=widgets.RadioSelect,
    )


#thoughts

    calculator = models.BooleanField(
        label='5. Did you calculate with paper and pen?',
        choices=[
            [True, 'Yes'],
            [False, 'No']
        ],

        widget=widgets.RadioSelect
    )
    prio = models.LongStringField(
        label='6. What kind of information exchange did you prefer in the game? Please explain why.',
    )
    other =models.LongStringField(
        label='7. Would you like to have a different way of information exchange? Please explain why.',
    )
    system = models.LongStringField(
        label='8. What do you think about the "Referring Information" (black box) in general?',

    )


#meeting
    meeting1 = models.LongStringField(
        label='10. How did you feel about the benefit of regular meetings instead of the "Referring Information"?',
    )
    meeting2 = models.IntegerField(
        label='11. What statement fits most to your experience in this game?',
        choices=[
            [0, 'I would not want to replace the meetings by the information provided by the system'
                ' (="Referring Information").'],
            [1, 'I see the same influence from both information sources.'],
            [2, 'The "Referring Information" is more efficient than regular meetings.'],
            [3, 'I would prefer to ask for information when I need it.'],
        ],
        widget=widgets.RadioSelect,
    )




#personality
    personality1 = models.IntegerField(
        label='12. What is more important for you at work?',
        choices=[
            [0, 'Details of a specific task'],
            [1, 'General overview of possible solution approaches'],
        ],
        widget=widgets.RadioSelect,
    )
    personality2 = models.IntegerField(
        label='13. Which situation do you prefer?',
        choices=[
            [0, 'Individual coaching for the duration of a project'],
            [1, 'Independent work on a project'],
        ],
        widget=widgets.RadioSelect,
    )

    personality3 = models.IntegerField(
        label='14. What type of work do you enjoy most?',
        choices=[
            [0, 'Rapidly changing tasks that create progress'],
            [1, 'Focusing alone on the task to create exellence'],
            [2, 'Comfortable and predictable tasks that support the team'],
            [3, 'Interacting with many people to create new ideas and energy'],
        ],
        widget=widgets.RadioSelect,
    )

    personality4 = models.IntegerField(
        label='15. How do you behave at an event where are mostly people you haven`t met before?',
        choices=[
            [0, 'Finding a small group of people you already know'],
            [1, 'Seeking a good point to observe the event'],
            [2, 'Meeting and talking to as many people as possible'],
            [3, 'Going to the people who are the reason why you are here'],
        ],
        widget=widgets.RadioSelect,
    )

    open = models.LongStringField(
        label='16. Please leave here any other additional comment regarding the game.',
    )

