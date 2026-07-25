# мне очень тяжело даллось данное задание, мне помогла нейронка,без нее у меня не получалось
# def main():
#     registry = {}
#
#     print("Реестр участников мероприятия")
#     print("Доступные команды: add, remove, list, exit")
#
#     while True:
#         command = input("Введите команду (add/remove/list/exit): ").strip().lower()
#
#         if command == "add":
#             register_participant(registry)
#         elif command == "remove":
#             unregister_participant(registry)
#         elif command == "list":
#             list_participants(registry)
#         elif command == "exit":
#             print("Выход из программы.")
#             break
#         else:
#             print("Ошибка: неизвестная команда. Пожалуйста, используйте add, remove, list или exit.\n")
#
#
# def parse_full_name(full_name_str: str):
#     parts = full_name_str.strip().split()
#     if len(parts) < 2:
#         return None
#     return tuple(parts[:2])
#
#
# def parse_interests(interests_str: str):
#     interests_set = set()
#     for interest in interests_str.split(','):
#         clean_interest = interest.strip().lower()
#         if clean_interest:
#             interests_set.add(clean_interest)
#     return interests_set
#
#
# def register_participant(registry: dict):
#     name_input = input("Введите имя и фамилию через пробел: ")
#     key = parse_full_name(name_input)
#
#     if not key:
#         print("Ошибка: необходимо ввести и имя, и фамилию.\n")
#         return
#
#     if key in registry:
#         print(f"Участник {key[0]} {key[1]} уже есть в реестре. Его интересы обновлены.\n")
#
#     interests_input = input("Введите интересы через запятую (например: наука, спорт, музыка): ")
#     interests = parse_interests(interests_input)
#
#     registry[key] = interests
#     print(f"Участник {key[0]} {key[1]} успешно зарегистрирован.\n")
#
#
# def unregister_participant(registry: dict):
#     name_input = input("Введите имя и фамилию удаляемого участника: ")
#     key = parse_full_name(name_input)
#
#     if not key:
#         print("Ошибка: необходимо ввести и имя, и фамилию.\n")
#         return
#
#     try:
#         del registry[key]
#         print(f"Участник {key[0]} {key[1]} успешно удален из реестра.\n")
#     except KeyError:
#         print(f"Ошибка: участник {key[0]} {key[1]} не найден в реестре.\n")
#
#
# def list_participants(registry: dict):
#     if not registry:
#         print("Реестр пуст.\n")
#         return
#
#     print("\n--- Список участников ---")
#
#     for first_name, last_name in sorted(registry.keys(), key=lambda x: (x[1], x[0])):
#         interests = registry[(first_name, last_name)]
#         interests_display = ", ".join(sorted(interests)) if interests else "(интересы не указаны)"
#         print(f"{first_name} {last_name}: {interests_display}")
#     print("-" * 25 + "\n")
#
#
# if __name__ == "__main__":
#     main()