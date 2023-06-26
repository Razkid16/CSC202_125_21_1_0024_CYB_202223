#writing my day fourteen code below here
data =[
    {
        'name': 'Instagram',
        'follower_count': 254,
        'description': 'Social media platform',
        'country': 'United States of America'
    },
    {
        'name': 'Sodeeq Afokoronu',
        'follower_count': 124,
        'description': 'Ethical Hacker',
        'country': 'Nigeria-because he is black'
    },
    {
        'name': 'Odumodu Black',
        'follower_count': 342,
        'description': 'Musician and Actor',
        'country': 'United States'
    },
    {
        'name': 'Joshephine Adenuga',
        'follower_count': 158,
        'description': 'Mechanical Engineer',
        'country': 'Canada'
    },
    {
        'name': 'Emmanuel Abubakar',
        'follower_count': 1250,
        'description': 'Fruadster',
        'country': 'Nigeria'
    },
    {
        'name': 'Omolola Peace',
        'follower_count': 311,
        'description': 'Clown Expert',
        'country': 'Togo'
    }
]
    #Displaying Art
import random
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr}, from {account_country}")
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
         account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B':\n").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You're right! Your current Score is: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score is {score}")    
