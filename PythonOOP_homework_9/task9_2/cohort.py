from trainee import Trainee


class Cohort:
    """Cohort class"""
    def __init__(self, title: str, trainees: list[Trainee] = []):
        """Initializes Cohort
        Args:
            title (str): title of cohort
            trainees (list[Trainee]): list of trainees
        """
        self.title = title
        self.trainees = trainees

    def add_trainee(self, trainee: Trainee) -> None:
        """Adds trainee to list"""
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """Conducts lecture, adds score to every trainee"""
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """Returns list of trainees who are passing"""
        return [trainee for trainee in self.trainees if trainee.is_passing()]

