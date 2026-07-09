# Project: Generating Random Quiz Files.
import random

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "NewMexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "WestVirginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

for quizNum in range(35):
    quizFile = open("capitalsquiz%s.txt" % (quizNum + 1), "w")
    answerKeyFile = open("capitalsquiz_answer%s.txt" % (quizNum + 1), "w")

    quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizFile.write((" " * 20) + "State Capitals Quiz (form %s)" % (quizNum + 1))
    quizFile.write("\n\n")

    State = list(capitals.keys())
    random.shuffle(State)

    for QuestionNum in range(50):
        correctAnswer = capitals[State[QuestionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(
            "%s. What is the capital of %s?\n" % (QuestionNum + 1, State[QuestionNum])
        )
        for i in range(4):
            quizFile.write("    %s.%s\n" % ("ABCD"[i], answerOptions[i]))
        quizFile.write("\n")
        answerKeyFile.write(
            "%s. %s\n" % (QuestionNum + 1, "ABCD"[answerOptions.index(correctAnswer)])
        )

    quizFile.close()
    answerKeyFile.close()
