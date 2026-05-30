print("\n====GK Quiz====\n")
score = 0
q1 = input("1. What is the only mammal that can truly fly?\n")
q2 = input("2. Which planet has the shortest day?\n")
q3 = input("3. What is the largest organ in the human body?\n")
q4 = input("4. Which animal's fingerprints are almost identical to humans'?\n")
q5 = input("5. How many hearts does an octopus have?(in words)\n")
q6 = input("6. What is the hottest planet in the Solar System?\n")
q7 = input("7. Which metal is liquid at room temperature?\n")
q8 = input("8. What is the only letter not found in any U.S. state name?\n")
q9 = input("9. Which bird can fly backward?\n")
q10 = input("10. What is the strongest muscle in the human body?\n")
q11= input("11. Which country has the most time zones?\n")
q12= input("12. What color is the Sun actually?\n")
q13= input("13. How many bones does a shark have?\n")
q14= input("14. What is the tallest grass in the world?\n")
q15= input("15. Which bird lays the largest egg?\n")
q16= input("16. What is the largest desert in the world?\n")
q17= input("17. Which planet rotates on its side?\n")
q18= input("18. What is the only continent with no active volcanoes?\n")
q19= input("19. Which animal can sleep for up to 3 years?\n")
q20= input("20. What is the rarest blood group?\n")
print("\n====RESULT====\n")
if q1.lower() == "bat":
    print("1.Correct.")
    score += 1
else:
    print("1.Wrong.\nAnswer: Bat.")
if q2 == "jupiter":
    print("2.Correct.")
    score += 1
else:
    print("2.Wrong.\nAnswer: Jupiter.")
if q3.lower() == "skin":
    print("3.Correct.")
    score += 1
else:
    print("3.Wrong.\nAnswer: Skin.")
if q4.lower() == "koala":
    print("4.Correct.")
    score += 1
else:
    print("4.Wrong.\nAnswer: Koala.")
if q5.lower() == "three":
    print("5.Correct.")
    score += 1
else:
    print("5.Wrong.\nAnswer: Three.")
if q6.lower() == "venus":
    print("6.Correct.")
    score += 1
else:
    print("6.Wrong.\nAnswer: Venus.")
if q7.lower() == "mercury":
    print("7.Correct.")
    score += 1
else:
    print("7.Wrong.\nAnswer: Mercury.")
if q8.lower() == "q":
    print("8.Correct.")
    score += 1
else:
    print("8.Wrong.\nAnswer: Q.")
if q9.lower() == "hummingbird":
    print("9.Correct.")
    score += 1
else:
    print("9.Wrong.\nAnswer: Hummingbird.")
if q10.lower() == "jaw":
    print("10.Correct.")
    score += 1
else:
    print("10.Wrong.\nAnswer: Jaw.")
if q11.lower() == "france":
    print("11.Correct.")
    score += 1
else:
    print("11.Wrong.\nAnswer: France.")
if q12 == "white":
    print("12.Correct.")
    score += 1
else:
    print("12.Wrong.\nAnswer: White.")
if q13.lower() == "zero":
    print("13.Correct.")
    score += 1
else:
    print("13.Wrong.\nAnswer:Zero.")
if q14.lower() == "bamboo":
    print("14.Correct.")
    score += 1
else:
    print("14.Wrong.\nAnswer: Bamboo.")
if q15.lower() == "ostrich":
    print("15.Correct.")
    score += 1
else:
    print("15.Wrong.\nAnswer: Ostrich.")
if q16.lower() == "antarctica":
    print("16.Correct.")
    score += 1
else:
    print("16.Wrong.\nAnswer: Antarctica.")
if q17.lower() == "uranus":
    print("17.Correct.")
    score += 1
else:
    print("17.Wrong.\nAnswer: Uranus.")
if q18.lower() == "australia.":
    print("18.Correct.")
    score += 1
else:
    print("18.Wrong.\nAnswer: Australia.")
if q19.lower() == "snail":
    print("19.Correct.")
    score += 1
else:
    print("19.Wrong.\nAnswer: Snail.")
if q20.lower() == "ab negative":
    print("20.Correct.")
    score += 1
else:
    print("20.Wrong\nAnswer: AB Negative.")
print("\n====SCORE====\n")
print("Your Score:", score,"/20")
