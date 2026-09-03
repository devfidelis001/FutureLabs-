
    
name = input("student name>>")
marks = int(input("add a score. NOTE: sore is SCORE/100>>"))
score = []
score.append(marks)


def  calculate_result(names, scores):
    average = sum(score) / len(score)
    sumall = sum(score)
    averagecomment = sum(score) / len(score)
    if averagecomment >= 80:
        comment = "Excellent score, you had A grade"
    elif averagecomment >= 70:
        comment = "Very good score, you had B grade"
    elif averagecomment >= 45:
        comment = "Good score, you had C grade"
    elif averagecomment >= 30:
        comment = "You had D grade"
    elif averagecomment >= 15:
        comment = "You had F grade"
    else:
        comment = "You failed badly, you will have to repeat this class"
        
    #average is adding all numbers ad then divideing it with the length or amout of numbers

    output = (f"""
             student: {names} 
             all scores: {scores}
             total score: {sumall}
             average is {average}
             comment: {comment}
             
             
              """)
    return output
    
while True:
    opt = input("type add to add more scores and continue to proceed if thats all your score and end to exit>>")

    if opt.lower() == "add":
        marks = int(input("add a score>>"))
        score.append(marks)
    elif opt.lower() == "continue":
        print(calculate_result(name, score))
    elif opt.lower() == "end":
        exit()
    else:
        print("since your input is not among the listed option, we have proceeded.")
        print(calculate_result(name, score))
    
    
    
    
    
    