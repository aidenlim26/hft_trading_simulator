CompetitorName = [0]*25
CompetitorScore = [[0] * 5 for i in range(25)]
Points = [0]*25
event = [0]*5
highesttotalpoints = 0
highestpoints = [0]*5


for i in range(25):
    competitortotal = 0
    for j in range(5):
        score = int(input("Please input your score: "))

        if score > 0 and score < 100:
            CompetitorScore[i][j] = score
            competitortotal = competitortotal + score
            if score > highestpoints[j]:
                highestpoints[j] = score
        else:
            print("Score must be between 0 and 100, try again!")

    Points[i] = competitortotal
            

for count in range(25):
    if Points[count] > highesttotalpoints:
        highesttotalpoints = Points[count]

for a in range(5):
    for b in range(25):
        if CompetitorScore[b][a] == highestpoints[a]:
            print(CompetitorName[b],highestpoints[a])    
