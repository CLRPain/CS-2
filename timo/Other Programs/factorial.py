def fact(n):
	if n==1:
		return 1
	return(n*fact(n-1))

def fib(n):

	if n==1 or n==0:
		return n
	return(fib(n-2) + fib(n-1))
	
running = True
while running == True:
	
	choice=input('Factorial (f), Fibanocci (F), Quit (q): ')

	if choice == 'f':
		num=int(input('\nEnter a number: '))
		
		x=fact(num)
		print(f'\nFactorial is: {x}\n')
		
	if choice== 'F'	:
		num=int(input('\nEnter a number: '))
		x=fib(num)
		print(f'\nFibanocci is: {x}\n')
	
	if choice == 'q':
		print('\nClosing')
		running = False



