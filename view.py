def print_all_events(student, events):
    for i in range(len(events)):
        if str(student) == events[i].user:
            print('{}.) {}'.format(str(i), events[i]))


def print_main_menu():
    print('''Choose option
          1. Book Private Mentoring
          2. Book Checkpoint
          3. Show all my events
          4. Remove events
          5. rescheduling event
          0. Exit
          ''')


def print_goodbye():
    print('Bye bye!')


def get_choice():
    return input('Choose option: ')


def get_checkpoint_details():
    return self.get_event_date()


def get_event_date():
    time_event = '{}-{}-{}'.format(input('day: '), input('mounth: '), input('year: '))
    return time_event


def get_preffered_mentor():
    return input('Enter preffered mentor: ')


def get_goal():
    return input('Enter your goal: ')


# def get_mentor():
#     print('''Choose mentor:
#           1. Aga
#           2. Mateusz
#           3. Skooby
#           ''')
#     return input()
