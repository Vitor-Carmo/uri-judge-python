n1, n2, n3, n4 = map(float, input().split())

avarage = ( n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1 ) / 10

print('Media: {:.1f}'.format(avarage))

if avarage >= 7:
    print('Aluno aprovado.')
elif avarage < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    
    new_avarage = (avarage + exame) / 2
    
    if new_avarage >= 5:
         print('Aluno aprovado.')    
    else:
        print('Aluno reprovado.')

    print('Media final: {:.1f}'.format(new_avarage))