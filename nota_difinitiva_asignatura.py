# nota difinitiva de una asignatura

#input

np = int(input("digite el valor de nota procedimental: "))
nc = int(input("digite el valor de nota cognitiva: "))
na = int(input("digite el valor de nota actitudinal: "))
au = int(input("digite el valor de nota autoevaluaciion: "))
bi = int(input("digite el valor de nota bimestral: "))

#processing

nd = (0.3*nc) + (0.3*np) + (0.1*na) + (0.1*au) + (0.2*bi)

#output

print("RESULTADO NOTA DEFINITIVA " + str(nd))
