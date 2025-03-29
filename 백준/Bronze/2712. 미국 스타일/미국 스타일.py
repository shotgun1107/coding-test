dic={'kg':[2.2046,'lb'],'lb':[0.4536,'kg'],'l':[0.2642,'g'],'g':[3.7854,'l']}
for _ in range(int(input())):
    n,s=input().split()
    print('%.4f %s'%(float(n)*dic[s][0],dic[s][1]))
