words = input("Введите любые слова через пробелы: ").split()
sort_func = sorted(words, key=len)

con_to_str = " ".join(sort_func)

print(con_to_str)