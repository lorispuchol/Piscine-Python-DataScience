import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:

    name: str
    surname: str
    active: bool = True

    login: str = field(default="", init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        if isinstance(self.name, str) and isinstance(self.surname, str):
            if len(self.name) > 0 and len(self.surname) > 0:
                self.login = self.name[0] + self.surname[0:7]


def main():
    student = Student(name="Edward", surname="agle")
    print(student)
    # student = Student(name="Edward", surname="agle", id="toto")
    # print(student)


if __name__ == "__main__":
    main()
