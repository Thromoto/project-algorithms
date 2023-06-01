def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None

    frequencia = 0
    for students_time in permanence_period:
        (inicio, final) = students_time
        if type(inicio) != int or type(final) != int:
            return None
        if inicio <= target_time <= final:
            frequencia += 1

    return frequencia
