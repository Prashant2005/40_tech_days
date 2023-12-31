import random
def num1(x,y):
    num_to_return=random.randint(x,y)
    return num_to_return

set2=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
set3=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
set4=('_','-','#','@','^','!','$')



alpha=""
for i in range(num1(8,12)):
    what_to=num1(0,2)
    if what_to==0:
        get_small_alpha=num1(0, len(set2)-1)
        alpha+=set2[get_small_alpha]
    if what_to==1:
        get_big_alpha=num1(0, len(set3)-1)
        alpha+=set3[get_big_alpha]
    if what_to==2:
        get_ap=num1(0,len(set4)-1)
        alpha+=set4[get_ap]
    else:
        get_num=num1(0,9)
        alpha+=str(get_num)


print(alpha)




