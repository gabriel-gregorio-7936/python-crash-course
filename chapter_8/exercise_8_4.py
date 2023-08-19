def make_shirt(size='G', message='I love Python'):
    print(f'The size of the shirt is {size.title()} and it has "{message.title()}" printed on it.')

make_shirt('M', "Life's good")
make_shirt(size='P', message='Riding through the bad times')

print("\n")

make_shirt(message="Life's good")
make_shirt(size='M')
make_shirt(size='P', message='Riding through life')
