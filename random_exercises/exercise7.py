str_x = "Emma is good developer. Emma is a writer"
count = 0

count = str_x.count("Emma")

print(f"Emma appeared {count} times.")

print("\n")

def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")