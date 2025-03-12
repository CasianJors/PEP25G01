nume = input("Introduceti numele elevului: ")
note = input("Introduceti notele elevului separate prin virgula: ")


def cast(value):
    value = value.strip()
    try:
        return float(value)
    except ValueError:
        return None


def check_lst(lst):
    try:
        assert len(notes_list) > 0, "Nu a fost introdusa nici o nota"
    except AssertionError as e:
        print("Assertion failed: ", e)
        exit(1)


def check_student(student, mean):
    if mean >= 5:
        print(f"Media este: {mean}")
        print(f"{student} a trecut clasa.")
    else:
        print(f"Media este: {mean}")
        print(f"{student} a picat clasa.")


# from string to list
notes_list = [cast(value) for value in note.split(",") if cast(value) is not None]

# check the list
check_lst(notes_list)

mean = sum(notes_list) / len(notes_list)

check_student(nume, mean)