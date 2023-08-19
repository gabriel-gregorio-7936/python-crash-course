def make_sandwiches(*sandwich_fillings):
    print(f"The sandwich with the following fillings is being made: ")

    for sandwich_filling in sandwich_fillings:
        print(f"- {sandwich_filling.title()}")
    
make_sandwiches('bacon', 'burguer', 'lettuce', 'corn', 'fried potato')