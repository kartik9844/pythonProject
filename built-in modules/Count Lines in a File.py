import fileinput

def count_lines(file_path):
    return sum(1 for line in fileinput.input(file_path))

print(count_lines('Random Number Generator.py'))
