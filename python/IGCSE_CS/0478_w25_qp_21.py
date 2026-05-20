CompetitorName = [0]*30
CompetitorScore = [[0]*10 for i in range(30)]

def qualification(score):
    if score >= 210:
        return "Moves onto next competition"
    elif score >= 180 and score <=209:
        return "Reserve competitor"
    else:
        return "Does not qualify"
    
def discarding(CompetitorScore[]):
    highest = 0
    smallest = 10000
    for j in range(10):
        if CompetitorScore[j] > highest:
            highest = CompetitorScore[j]
        elif CompetitorScore[j] < smallest:
            smallest = CompetitorScore[j]
    
    for j in range(10):
        if CompetitorScore[j] == highest:
            CompetitorScore[j] = "0"
        elif CompetitorScore[j] == smallest:
            CompetitorScore[j] = "0"

def total(CompetitorScore[]):
    total = total + CompetitorScore[j]
    return total


competitors = 0

while competitors <= 30:
    for i in range(30):
        for j in range(10):
            score = int(input("Enter your round's score: "))
            if score >= 0 and score <= 30:
                CompetitorScore[i][j] = score
                CompetitorName[i] = str(input("Please enter competitor name: "))
            else:
                print("Inputs for scores must be between 0 and 30 inclusive")

        competitors = competitors + 1

qualified = 0
reserve = 0
not_qualified = 0
total = 0

for i in range(30):
    for j in range(10):
            overall_score = total(CompetitorScore[j])
            did_qualify = qualification(CompetitorScore[j])
            print("Competitor name: ", CompetitorName[i])
            print("Overall score: ", overall_score)
            print(qualification())


