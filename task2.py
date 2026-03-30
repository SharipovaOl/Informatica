def find_common_participants(first_group, second_group, delimiter=','):
    return sorted(set(first_group.split(delimiter)) & set(second_group.split(delimiter)))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
