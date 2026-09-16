print("===SMART SCHOOL DAY PLANNER====")
print("Answer 3 questions and i will plan your day \n")
DAY    =input("What day is it today? (Monday to Sunday): ").strip().capitalize()
WEATHER =input("What is the weather like today? (Sunny, Rainy, Cloudy, Snowy): ").strip().lower()
HOMEWORK=input("Is your homework done? (Yes or No): ").strip().lower()
print(f"===Your Plan for {DAY}===")
print("-" * 35)
if DAY in("Saturday,Sunday"):
    print("Day type:Weekend-Enjoy your free time!")
elif DAY=="Monday":
    print("Day type:First day of the week.Pack your weekly planner.")
elif DAY=="Friday":
    print("Day type:Last school day.Return library books today.")
elif DAY in("Tuesday","Wednesday","Thursday"):
    print("Day type:Regular school day.Study hard and stay focused.")
else:
    print("Day type :Day not recognised.Pls check the spelling.")

if WEATHER=="sunny" and HOMEWORK=="yes":
    print("After school:Head to the park! Great weather and homework is done.")
if WEATHER=="rainy" or WEATHER == "cloudy":
    print("Weather tip:Pack your umbrella-it may get wet outside.")
if WEATHER=="snowy" and HOMEWORK=="yes":
    print("Lets build a snowman! Homework is done and the snow is perfect.")
if not(HOMEWORK=="yes"):
    print("Homework:Not done yet.Finish it before going out.")
if WEATHER=="rainy" and not (HOMEWORK =="yes"):
    print("Best plan:Stay in ,finish homewok,then watch your favourtie how.")
elif WEATHER=="sunny"and HOMEWORK=="yes" and not (DAY in ("Saturday","Sunday")):
    print("Best plan :All set for a great school day!-you are prepared!")
elif DAY in("Saturday","Sunday")and WEATHER=="sunny":
    print("Best plan:Enjoy your weekend! Go out and have fun!")
elif WEATHER=="snowy":
    print("PLAN COMPLETED!")
        
else:
    print("Best plan:Stay in and relax! Maybe read a book or watch a movie.")
    print()
    print("Plan completed! Have a great day!")
    
        