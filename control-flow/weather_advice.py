# 0. Weather Recommendation Program


weather = input("What's the weather like today? (sunny/rainy/cold): ") # Prompt User for Weather Input:

# Based on the user’s input, the program will recommending different types of clothing
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")