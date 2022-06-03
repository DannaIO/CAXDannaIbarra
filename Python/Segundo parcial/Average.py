while True:
  cal1=int(input('Insert your first calification:'))
  cal2=int(input('Insert your second calification:'))
  cal3=int(input('Insert your third calification:'))

  x=(cal1+cal2+cal3)/3

  print('Your average is:',x)

  if (x>6):
    print('approve')

  if (x<6):
    print('fail')

  if (x==6):
    print('approve')

  if (x>9):
    print ('congratulations')

  if (x==9):
    print('congratulations')