import string
import sys
from typing import Optional

reportsInput = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


class Report:
    def __init__(self, levels):
        self.levels = levels


def parse_reports(raw_data: string):
    reports = []
    for line in raw_data.strip().split("\n"):
        reports.append(Report(line.split(" ")))
    return reports


def count_safe_reports(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
    return count


def is_safe(report):
    """
    So, a report only counts as safe if both of the following are true:
        The levels are either all increasing or all decreasing.
        Any two adjacent levels differ by at least one and at most three.
    :param report:
    :return:
    """
    latest_level = 0
    previous_increase = 0
    for level in report.levels:
        increase = int(level) - int(latest_level)
        print(level, latest_level, increase, previous_increase)

        # stopped decreasing
        if previous_increase < 0 < increase:
            print("false because stopped decreasing", previous_increase, increase, "\n")
            return False

        # stopped increasing
        if previous_increase > 0 > increase:
            print("false because stopped increasing", previous_increase, increase, "\n")
            return False

        # increase or decrease at least 1 and at most 3 and not the 1st level
        if latest_level != 0 and (abs(increase) < 1 or abs(increase) > 3):
            print("false because increase is out of range", increase, "\n")
            return False

        if latest_level != 0:
            previous_increase = increase
            print("new previous increase", previous_increase)

        latest_level = int(level)
        print("new latest level", latest_level)

    print("\nis safe\n")
    return True


def print_reports(reports):
    for report in reports:
        print(report.levels)


def process_data(data):
    reports = parse_reports(data)
    safe_reports = count_safe_reports(reports)
    print(f"\nthere are {safe_reports} safe reports")


def get_file_lines(filename):
    with open(filename, "r") as file:
        return file.read()


def get_file_name() -> Optional[str]:
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return None


# print(Report)
# print_reports(parse_reports(reportsInput))

# process_data(reportsInput)

def main():
    filename = get_file_name()
    if get_file_name():
        process_data(get_file_lines(filename))
    else:
        print("you should input the file you want to process!")


main()
