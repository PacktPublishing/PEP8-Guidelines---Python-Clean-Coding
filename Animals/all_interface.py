
__all__ = ["harvard", "stanford", "MIT", "CIT", "princeton"]


def harvard(name, students):
    name = "University: ", name
    additional_students = 1000
    total_students = students + additional_students
    professors = total_students//4
    info_dict = {"name": name, "students": students, "professors": professors}

    return info_dict


def stanford(name, students):
    name = "University: ", name
    additional_students = 1000
    total_students = students + additional_students
    professors = total_students // 4
    info_dict = {"name": name, "students": students, "professors": professors}

    return info_dict


def MIT(name, students):
    name = "University: ", name
    additional_students = 1000
    total_students = students + additional_students
    professors = total_students // 4
    info_dict = {"name": name, "students": students, "professors": professors}

    return info_dict


def CIT(name, students):
    name = "University: ", name
    additional_students = 1000
    total_students = students + additional_students
    professors = total_students // 4
    info_dict = {"name": name, "students": students, "professors": professors}

    return info_dict


def princeton(name, students):
    name = "University: ", name
    additional_students = 1000
    total_students = students + additional_students
    professors = total_students // 4
    info_dict = {"name": name, "students": students, "professors": professors}

    return info_dict