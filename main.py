while True:
  # ُEnter the first num
  num_1 = float(input("Enter the First num: "))
  # Enter the secound num
  num_2 = float(input("Enter the First num: "))
  # Select the Oparation
  Opa = input("Enter the Oparation: ( /, *, -, + ) ")
  if Opa == "+":
    print(str(num_1 + num_2))
  elif Opa == "-":
    print(str(num_1 - num_2))
  elif Opa == "/":
    print(str(num_1 / num_2))
  elif Opa == "*":
    print(str(num_1 * num_2))
  else :
    print("Error in the Oparation try in a few minutes")
