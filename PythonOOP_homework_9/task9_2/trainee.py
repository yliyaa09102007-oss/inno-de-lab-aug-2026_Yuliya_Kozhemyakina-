class Trainee:
    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10):
        """
        Initializes Trainee class
        Args:
            name (str): Trainee name
            surname (str): Trainee surname
            score (int): Trainee score, by default 0
            passing_grade (int): Trainee passing grade, by default 10
        """
        self.name = name
        self.surname = surname
        self.__score = score
        self.passing_grade = passing_grade

    @property
    def score(self):
        """Getter for score"""
        return self.__score

    @score.setter
    def score(self, new_score):
        """Setter for score"""
        try:
            new_score = int(new_score)
        except ValueError:
            #raising an error if "new_score" isn't of type "int"
            raise ValueError(f"Expected value of type int, got {type(new_score)}")

        if new_score >= 0:
            self.__score = new_score
        else:
            #raising an error if "new_score" is less than 0
            raise ValueError("The score shouldn't be less than 0!")

    def do_homework(self) -> None:
        """Increases score by 1"""
        self.score +=1

    def miss_homework(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1"""
        self.score += 1

    def miss_lecture(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def is_passing(self) -> bool:
        return self.score >= self.passing_grade


class HardworkingTrainee(Trainee):
    """Hardworking Trainee class"""
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score +=2


class AuditTrainee(Trainee):
    """Audit Trainee class"""
    def is_passing(self) -> bool:
        return True
