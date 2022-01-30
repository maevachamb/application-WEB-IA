
from python.application import maximum
def maximum (a, b): 
    if a>b:
        return a 
        print ( a + "est le plus grand nombres")
    if b>a: 
        return b 
        print ( b + "est le plus grand nombres")
    if a==b:
        print("ils sont pareils ")


if __name__== '__main__' : 
    print("testing the systeme")
    print("maximun entre  527 and 525 {} ", forma(maximum(527,525)))
