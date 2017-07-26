from datetime import date
import view
import events
import csv
import student


class Controller:

    def start(self):
        self.read_file('list_csv.csv')
        student = self.check_access()
        if student:

            choice = ''
            while choice != '0':
                view.print_main_menu()
                choice = view.get_choice()
                if choice == '1':
                    self.book_private_mentoring(student)
                elif choice == '2':
                    self.book_checkpoint(student)
                elif choice == '3':
                    self.print_all_events(student)
                elif choice == '4':
                    self.remove_events(student)
                elif choice == '5':
                    self.rescheduling_event(student)
                elif choice == '0':
                    Controller.say_goodbye(student)

        elif user:
            Controller.read_file('list_csv.csv')
            choice = ''
            while choice != '0':
                view.print_main_menu()
                choice = view.get_choice()
                if choice == '1':
                    self.print_all_events()
                elif choice == '2':
                    self.remove_events()

    @staticmethod
    def read_file(filename):
        with open(filename) as files:
            reader = csv.reader(files)
            for elem in reader:
                date = Controller().convert_date(elem[1])
                studen = student.Student(elem[0])
                if len(elem) == 2:
                    events.Checkpoint(studen.student, date)
                elif len(elem) == 4:
                    events.PrivateMentoring(studen.student, date, elem[2], elem[3])

    @staticmethod
    def check_access():
        choice = view.get_choice()
        for studen in student.Student.list_student:
            if studen.student == choice:
                return studen.student

    def print_all_events(self, student):
        view.print_all_events(student, events.Event.get_events())

    def book_event(self):
        pass

    def book_checkpoint(self, user):
        date = self.__class__.proof_input()
        events.Checkpoint(user, date)

    def book_private_mentoring(self, user):
        date = self.__class__.proof_input()

        # num_mentor = int(view.get_mentor()) - 1
        # mentor = events.PrivateMentoring.list_mentor[num_mentor]
        goal = view.get_goal()
        mentor = view.get_preffered_mentor()
        events.PrivateMentoring(user, date, mentor, goal)

    @staticmethod
    def say_goodbye(user):
        Controller.write_file('list_csv.csv', user)
        view.print_goodbye()

    @staticmethod
    def convert_date(date_str):
        date_list = date_str.split('-')
        return (date(int(date_list[2]), int(date_list[1]), int(date_list[0])))

    @staticmethod
    def proof_input():
        day_type_ok = False
        while day_type_ok is False:
            try:
                date = view.get_event_date()
                date = Controller.convert_date(date)
                return date
            except ValueError:
                day_type_ok = False

    def remove_events(self, student):
        index = view.get_choice()
        for elem in events.Event.events:
            if str(student) == elem.user:
                del events.Event.events[int(index)-1]

    @staticmethod
    def rescheduling_event(student):
        index = view.get_choice()
        for elem in events.Event.events:
            if str(student) == elem.user:
                elem.date = __class__.proof_input()
                events.Event.sort_events()
                break

    @staticmethod
    def write_file(filename, student):
        with open(filename, 'w') as write_file:
            writer = csv.writer(write_file)
            for elem in events.Event.events:
                print(elem)
                # if str(student) == elem.user:
                date = [str(elem.date.day) + '-' + str(elem.date.month) + '-' + str(elem.date.year)]
                if type(elem) == events.PrivateMentoring:
                    writer.writerow([elem.user] + date + [elem.mentor, elem.goal])
                elif type(elem) == events.Checkpoint:
                    writer.writerow([elem.user] + date)
