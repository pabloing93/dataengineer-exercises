def exercise_one():
  check=False
  while not check:
    n = int(input('Enter an odd number: '))
    if (n%2):
      print('Good job!')
      check = True
    else:
      print('Error also no biggie. Try again!')

if __name__ == "__main__":
  exercise_one()