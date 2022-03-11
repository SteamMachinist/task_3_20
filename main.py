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
        self.name = str(info[0])
        self.russ, self.math, self.phys = [str(info[x]) for x in range(1, 4)]
        self.cert = bool(info[4])

    def __str__(self):
        return " ".join(str(x) for x in self.__dict__.values())

    def scores_sum(self):
        return sum((self.russ, self.math, self.phys))

    def __lt__(self, other):
        other = Applicant(other)
        if self.scores_sum() != other.scores_sum():
            return self.scores_sum() < other.scores_sum()
        elif self.math != other.math:
            return self.math < other.math
        elif self.phys != other.phys:
            return self.phys < other.phys
        else:
            return self.russ < other.russ


if __name__ == '__main__':
    apl = Applicant("vasya 15 12 7 True")
    print(apl)
