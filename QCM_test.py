from prod.QCM import QCM

test=QCM("bonjour")
test2=QCM("bonjour2",20)
test3=QCM("bonjour3",30,"camembert")
print(test)
print(test2)
print(test3)
test3.addQuestion(5)
test3.addQuestion(7)
test3.addQuestion(9)
print(test3)
