class Event:

    events = []

    def __init__(self, user, date):
        '''date: Date object
        '''
        self.user = user
        self.date = date

    def __str__(self):
        return self.user

    def get_date(self):
        return self.date

    @classmethod
    def sort_events(cls):
        is_sorted = False
        while not is_sorted and len(cls.events) > 1:
            is_sorted = True
            for i in range(len(cls.events) - 1):
                if cls.events[i].date > cls.events[i+1].date:
                    temp = cls.events[i]
                    cls.events[i] = cls.events[i+1]
                    cls.events[i+1] = temp
                    is_sorted = False

    @classmethod
    def add_event(cls, event):
        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls):
        return cls.events


class Checkpoint(Event):

    # events = []

    def __init__(self, user, date):
        super().__init__(user, date)

        Event.add_event(self)
        # Checkpoint.add_event(self)

    def __str__(self):
        return self.user + ':' + str(self.date.day) + '.' + str(self.date.month) + '.' + str(self.date.year)


class PrivateMentoring(Event):

    # list_mentor = ['Aga', 'Mateusz', 'Skooby']
    # events = []

    def __init__(self, user, date, mentor, goal):
        self.goal = goal
        self.mentor = mentor
        super().__init__(user, date)

        Event.add_event(self)
        # PrivateMentoring.add_event(self)

    def __str__(self):
        return self.user + ':' + str(self.date.day) + '.' + str(self.date.month) + '.' + str(self.date.year) + \
                ' ' + self.mentor + ' ' + self.goal
