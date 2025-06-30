print("Welcome to my computer quiz game!")

playing = input("Do you want to play? ").strip().lower()

if playing != "yes":
    quit()

print("Okay! Let's play 🥰")
score = 0
total_questions = 4

# Question 1
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect! It's 'Central Processing Unit'.")

# Question 2
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect! It's 'Graphics Processing Unit'.")

# Question 3
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect! It's 'Random Access Memory'.")

# Question 4
answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect! It's 'Power Supply Unit'.")

# Final result
print(f"\n🎉 You got {score} correct!")
print(f"✅ Your score: {(score / total_questions) * 100:.2f}%")
