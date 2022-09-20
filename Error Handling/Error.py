

while True:
 try:
  age = int(input("what is your age?"))
  10/age
 except ValueError:
    print('Enter a valid number')
 except ZeroDivisionError:
    print('Please higher then Zero')
 else:
     print('thank you!!!')
     break