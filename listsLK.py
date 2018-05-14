name = "Mr. Rosenfeld"
subjects = ["English","spanish","Math","History","Science"]

print ("My name is " + name)

#print(subjects)

for i in subjects:
    print("One of my classes is " + i)



colors = ["Pink","Blue","Purple","Green","Red"]

for i in colors:
    if i == "blue":
        print (i + " is the best color ever1")
    elif i == "Red":
        print (i + " is the worst color ever")
    elif i == "Green":
        print (i + " is the worst color ever")
    elif i == "Purple":
        print (i + " is the worst color ever")
    elif i == "Pink":
        print (i + " is the worst color ever")
    
    print("The best color is " + i)
    

colors = []

while True:
    print("wHAT are your favorite colors? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        colors.append(answer)

for i in colors:
    print ("One of you favorite colors is " + i)
        
