name = input("Type your name: ")
print(f"\nWelcome, {name}, to the ancient realm of Eldoria...")
print("You are a traveler in search of the lost Crystal of Light, said to grant its bearer great wisdom and power.")

print("\nAs twilight falls, you find yourself on a dusty path deep in the Whispering Woods.")
answer = input("The road ahead forks — one path veers into the dark, twisted forest (type 'left'), the other glows faintly under moonlight leading to distant hills (type 'right'). Which way do you go? ").lower()

if answer == "left":
    print("\nYou take the narrow path into the shadowy forest. The trees grow taller, their twisted limbs closing in around you.")
    print("An eerie silence fills the air, broken only by the distant hoot of an owl. Suddenly, you reach a shimmering river with glowing water flowing silently in the moonlight.")
    
    answer = input("You can try to 'walk' carefully along the slippery riverbank or 'swim' through the glowing waters. What do you choose? ").lower()
    
    if answer == "swim":
        print("\nYou bravely step into the water. At first, it's calm and warm...")
        print("But within moments, tendrils of water swirl around you — it's a trap! A water wraith rises from the depths, its eyes glowing blue.")
        print("You try to escape, but it's too late. You are pulled under into the icy abyss.")
        print("💀 The forest keeps its secrets. You have perished.")
        
    elif answer == "walk":
        print("\nYou decide to walk cautiously along the edge of the river.")
        print("Hours pass as you struggle through thick vines and roots. You grow tired and thirsty, but you keep going.")
        print("Suddenly, you spot an old wooden boat tied under a willow tree. A glowing crystal lies inside it.")
        print("You step into the boat, and it begins to move by itself, carrying you across the river.")
        print("🏆 You have discovered a hidden path to the Crystal of Light. You win!")
        
    else:
        print("\nAs you hesitate, the forest begins to change...")
        print("Dark vines wrap around your feet. You've disturbed the balance of Eldoria.")
        print("💀 The forest claims all who fear choice. You are lost forever.")

elif answer == "right":
    print("\nYou follow the glowing path up the hills. The night sky sparkles above you, and a cool breeze guides your steps.")
    print("Eventually, you reach a golden archway guarded by a statue of an ancient hero holding a sword of fire.")
    
    answer = input("A voice echoes: 'Only those who show courage or wisdom may pass. Will you 'cross' the arch or 'go back' the way you came?' ").lower()
    
    if answer == "cross":
        print("\nYou step through the archway. The statue's eyes glow and a flame lights your path.")
        print("On the other side lies a garden filled with stars, and in its center floats the legendary Crystal of Light.")
        print("The air is warm, and your heart feels light — you’ve been chosen as the new Guardian of Eldoria.")
        print("🏆 You win! Peace shall return to the land under your watch.")
        
    elif answer == "go back":
        print("\nYou turn away from the arch, uncertain of what lies beyond.")
        print("But the path vanishes behind you, and the hills begin to crumble.")
        print("You tumble into a pit of shadows where lost travelers roam forever.")
        print("💀 Cowardice has sealed your fate. You are never seen again.")
        
    else:
        print("\nYou stand frozen as the voice fades. The statue awakens, but it is not pleased.")
        print("A blast of fire surrounds you. You scream — but there's no one to hear.")
        print("💀 Hesitation in Eldoria is fatal. You are gone.")

else:
    print("\nYou do not choose. The wind howls. Time stops.")
    print("Suddenly, a shadow emerges from the trees — a hooded figure with glowing eyes.")
    print("'No decision is still a decision,' it whispers.")
    print("💀 You vanish into the void, never to return.")
