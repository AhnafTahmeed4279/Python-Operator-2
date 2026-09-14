print("===SMART SCHOOL DAY PLANNER====")
print("Answer 3 questions and i will plan your day \n")
DAY    =input("What day is it today? (Monday to Sunday): ").strip().capitalize()
WEATHER  =input("What is the weather like today? (Sunny, Rainy, Cloudy, Snowy): ").strip().lower()
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

