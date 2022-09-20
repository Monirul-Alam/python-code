
while True:
 try:
  age = int(input("what is your age?"))
  10/age
 except ValueError:
    print('Enter a valid number')
    continue

 except ZeroDivisionError:
    print('Please higher then Zero')
    break
 else:
     print('thank you!!!')

 finally:
     print("ok!! I am done right know...")


 print('Can  you hear me')