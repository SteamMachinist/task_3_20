# 19. При поступлении на некоторую специальность подали заявление множество абитуриентов (абитуриент описывается
# следующим образом: ФИО, оценка по русскому языку, оценка по математике, оценка по физике). На соответствующей
# специальности N бюджетных мест, отберите тех студентов, которые поступят. Приоритет имеют студенты с максимальной
# суммой баллов, затем с большим баллом по математике, затем по физике.

# 20. Входные данные соответствуют предыдущей задаче, однако дополнительно появляется информация, принес ли абитуриент
# оригинал аттестата. В первую волну поступят студенты среди первых N по приоритету, которые принесли оригинал
# аттестата. Отберите студентов, которые поступят в первую волну приема.

class Applicant:
    def __init__(self, info: str):
        info = [x for x in info.split(" ")]
        self.surname, self.name, self.patronymic = [str(info[x]) for x in range(3)]
        self.russ, self.math, self.phys = [int(info[x]) for x in range(3, 6)]
        self.cert = bool(info[6])

    def is_certified(self):
        return self.cert

    def __str__(self):
        return " ".join(str(x) for x in self.__dict__.values())

    def scores_sum(self):
        return sum((self.russ, self.math, self.phys))

    def __lt__(self, other):
        other = other
        if self.scores_sum() != other.scores_sum():
            return self.scores_sum() < other.scores_sum()
        elif self.math != other.math:
            return self.math < other.math
        elif self.phys != other.phys:
            return self.phys < other.phys
        else:
            return self.russ < other.russ


def read_from_file(filepath):
    file = open(filepath, 'r')
    apl_list = []
    for row in file:
        apl_list.append(Applicant(row))
    file.close()
    return apl_list


def write_to_file(filepath, apl_list: list):
    file = open(filepath, "w")
    for apl in apl_list:
        file.write(str(apl))
        file.write("\n")
    file.close()


def get_accepted_list(n: int, apl_list: list):
    return sorted([apl for apl in apl_list if apl.is_certified()])[:n]


if __name__ == '__main__':
    write_to_file("output/output1.txt", get_accepted_list(6, read_from_file("input/input1.txt")))
