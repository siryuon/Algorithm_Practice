T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    planetNumber = int(input())

    planets = []
    startPlanets = 0
    finishPlanets = 0
    bothPlanets = 0
    
    for _ in range(planetNumber):
        planets.append(input())
    
    for planet in planets:
        xPos, yPos, r = map(int, planet.split())

        startDistance = ((xPos - x1) ** 2 + (yPos - y1) ** 2) ** (1/2)
        finishDistance = ((xPos - x2) ** 2 + (yPos - y2) ** 2) ** (1/2)

        if startDistance < r and finishDistance < r:
            startPlanets += 1
            finishPlanets += 1
            bothPlanets += 1
        else:
            if startDistance < r:
                startPlanets += 1
            if finishDistance < r:
                finishPlanets += 1

    print(startPlanets + finishPlanets - bothPlanets * 2)
