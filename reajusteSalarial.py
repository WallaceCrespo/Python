s = float(input('Digite o salário do funcionário: '))
r = int(input('Digite o valor do reajuste em %: '))

t = s*(r/100)+s

print('Reajuste R$:', t-s)
print('O salário antigo é R$: ', s)
print('Com reajuste o novo salário será R$: ', t)