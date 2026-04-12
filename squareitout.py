def squares_filter(start, end):
    numbers = list(range(start, end + 1))
    squares = [n**2 for n in numbers]
    odd_squares = [x for x in squares if x % 2 != 0]
    even_squares = [x for x in squares if x % 2 == 0]
    print("Odd squares:", odd_squares)
    print("Even squares:", even_squares)

squares_filter(1, 10)