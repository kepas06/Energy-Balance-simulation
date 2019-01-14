# def stage1(): #waga plecaka 
#     weightOfBackpack = [random.uniform(15,40) for x in range(50)]
#     avgWeight = average(weightOfBackpack)
#     stDev = statistics.stdev(weightOfBackpack)
#     result = normalDist(avgWeight,stDev) *50
#     #print(result)
#     return result


# def stage2(): # ukształtowanie terenu w skali od 1 do 12 
#     levelOfTerrain = [random.uniform(1,20) for x in range(50)]
#     avgLevel = average(levelOfTerrain)
#     stDev = statistics.stdev(levelOfTerrain)
#     result = normalDist(avgLevel,stDev) *80
#     return result


# def stage3(): #stopien zmęczenia 
#     levelOfFatigue = [random.uniform(1,10) for x in range(50)]
#     avgLevel = average(levelOfFatigue)
#     stDev = statistics.stdev(levelOfFatigue)
#     result = normalDist(avgLevel,stDev) *40
#     return result


# def stage4(): # stopien padania deszczu, stopien wiania wiatru, wysokie niskie temperatury
#     rainMagnitude = [random.uniform(5,15) for x in range(50)]
#     windMagnitude = [random.uniform(1,10) for x in range(50)]
#     temperatureRange = [random.uniform(-25,25) for x in range(50)]
    
#     avgRain = average(rainMagnitude)
#     avgWind = average(windMagnitude)
#     temperature = random.choice(temperatureRange)
    
#     stdDevRain=( statistics.stdev(rainMagnitude) )
#     stdDevWind = ( statistics.stdev(windMagnitude) )
#     stdDevTemp = ( statistics.stdev(temperatureRange) )
    
#     r1 = normalDist(avgRain,stdDevRain)*20 
#     r2 = normalDist(avgWind,stdDevWind)*20
#     r3 = temperatureClassyfying(temperature,stdDevTemp)
    
#     result = r1+r2+r3
#     return result


# def stage5(): # nasza Waga
#     weight = [random.uniform(50,90) for x in range(50)]
#     avgLevel = average(weight)
#     stDev = statistics.stdev(weight)
#     multiplier = random.uniform(3,12) #nasze zaawansowanie fizyczne. Im mniejsza liczba tym mniej kalorii zużyjemy
#     result = normalDist(avgLevel,stDev)*multiplier
#     return result


# def stage6(): # dodanie wartosci odzywczych od do ileś kcal. 
#     numOfCallories = [random.uniform(1300,2500) for x in range(50)]
#     avgLevel = average(numOfCallories)
#     stDev = statistics.stdev(numOfCallories)
#     result = normalDist(avgLevel,stDev) 
#     return result
