from task9_1.task9_1 import Trainee


class HardworkingTrainee(Trainee):
    """Hardworking Trainee class"""
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score +=2


class AuditTrainee(Trainee):
    """Audit Trainee class"""
    def is_passing(self) -> bool:
        return True
