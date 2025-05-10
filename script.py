from random import choice
import copy


def main():
  #  h = {"A": [1, 2, 5, 8], "B": [1, 4, 8, 9], "C": [3, 5, 6, 9], "D": [2, 4, 7, 8]}  # hashmap person : wanted shifts
  #  s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # shifts
    s = list(range(1, 61))

    h = {
        'P0': [2, 3, 5, 6, 8, 14, 17, 18, 20, 21, 24, 25, 29, 31, 32],
        'P1': [3, 5, 7, 9, 11, 13, 17, 18, 19, 22, 28],
        'P2': [1, 5, 9, 11, 12, 13, 14, 17, 20, 23, 24, 26, 27],
        'P3': [1, 2, 5, 8, 10, 11, 14, 15, 20],
        'P4': [3, 5, 9, 13, 14, 15, 20, 21],
        'P5': [2, 6, 10, 14, 15, 16, 17, 18, 21, 24],
        'P6': [3, 4, 5, 10, 13, 16, 19, 21, 23, 24, 26],
        'P7': [3, 4, 6, 9, 13, 17, 20, 21],
        'P8': [1, 2, 4, 5, 6, 8, 12, 14, 15, 16],
        'P9': [2, 4, 7, 9, 11, 13, 16, 17, 19, 20, 22, 23]
    }

    while True:
        given = assign_shifts(copy.deepcopy(h), copy.deepcopy(s))
        sort_shifts(given)

        new_assignment_needed = False
        for person in given:
            if check_for_consequent_shifts(given[person]):
                new_assignment_needed = True
                break

        if not new_assignment_needed:
            break

    print(given)

def assign_shifts(h,s):
    finished = False
    given = {}  # hashmap person : given shifts

    while True:

        for person in h.keys():

            if len(s) == 0:         # if all shifts are assigned, end program
                finished = True
                break

            for shift in copy.deepcopy(h[person]):            # if the shift is given already, remove it from wanted
                if shift not in s:
                    h[person].remove(shift)

            if len(h[person]) == 0:
                assigned_shift = choice(s)
            else:
                assigned_shift = choice(h[person])
                h[person].remove(assigned_shift)  # remove the assigned shift from h


            s.remove(assigned_shift)  # remove the assigned shift from s

            if person in given.keys():
                given[person].append(assigned_shift)  # add random shift to current person
            else:
                given[person] = [assigned_shift]    # create a list with the assigned shift as value



        if finished:
            break

    return given


def sort_shifts(given):

    # sort values for each key in given
    for person in given:
        values = given[person]
        values.sort()
        given[person] = values



def check_for_consequent_shifts(list):
    for i in range(len(list)-1):
        if list[i] % 2 != 0:
            if list[i+1] == list[i] + 1:
                return True

    return False


main()
