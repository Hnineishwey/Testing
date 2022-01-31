
import random
players = input("Please input players name using coma : ").split(',')
l_players = list(players)
#print(l_players)
truth = ['When was the last time you lied?',

'When was the last time you cried?',

'What is your biggest fear?',

'What is your biggest fantasy?',

'Do you have any fetishes?',

'What is something you are glad your mum does not know about you?',

'Have you ever cheated on someone?',

'What is the worst thing you have ever done?',

'What is a secret you have never told anyone?',

'Do you have a hidden talent?',

'Who was your first celebrity crush?',

'What are your thoughts on polyamory?',

'What is the worst intimate experience you have ever had?',

'Have you ever cheated in an exam?',

'What is the most drunk you have ever been?',

'Have you ever broken the law?',

'What is the most embarrassing thing you have ever done?',

'What is your biggest insecurity?',

'What is the biggest mistake you have ever made?',

'What is the most disgusting thing you have ever done?',

'Who would you like to kiss in this room?',

'What is the worst thing anyone ever done to you?',

'Have you ever had a run in with the law?',

'What is your worst habit?',

'What is the worst thing you have ever said to anyone?',

'Have you ever peed in the shower?',

'What is the strangest dream you have had?',

'Have you ever been caught doing something you should not have?',

'What is the worst date you have been on?',

'What is your biggest regret?',

'What is the biggest misconception about you?',

'Where is the weirdest place you have had sex?',

'Why did your last relationship break down?',

'Have you ever lied to get out of a bad date?',

'What is the most trouble you have been in? ',

]
#print(len(truth))
dare = [ 'Show the most embarrassing photo on your phone',

'Show the last five people you texted and what the messages said',

'Let the rest of the group DM someone from your Instagram account',

'Eat a raw piece of garlic ',

'Do 100 squats',

'Keep three ice cubes in your mouth until they melt ',

'Say something dirty to the person on your left',

'Give a foot massage to the person on your right',

'Put 10 different available liquids into a cup and drink it ',

'Yell out the first word that comes to your mind ',

'Give a lap dance to someone of your choice',

'Remove four items of clothing',

'Like the first 15 posts on your Facebook newsfeed',

'Eat a spoonful of mustard',

'Keep your eyes closed until it\'s your go again',

'Send a sext to the last person in your phonebook',

'Show off your orgasm face',

'Seductively eat a banana ',

'Empty out your wallet/purse and show everyone what\'s inside',

'Do your best sexy crawl',

'Pretend to be the person to your right for 10 minutes',

'Eat a snack without using your hands',

'Say two honest things about everyone else in the group',

'Twerk for a minute',

'Try and make the group laugh as quickly as possible',

'Try to put your whole fist in your mouth',

'Tell everyone an embarrassing story about yourself',

'Try to lick your elbow',

'Post the oldest selfie on your phone on Instagram Stories',

'Tell the saddest story you know',

'Howl like a wolf for two minutes',

'Dance without music for two minutes',

'Pole dance with an imaginary pole',

'Let someone else tickle you and try not to laugh',

'Put as many snacks into your mouth at once as you can' ]
#print(len(dare))
while True:
    choose = input("start or exit ? : ")
    if choose == "start":
        while True:
            ran_p = random.randint(0, len(l_players)-1)
            ran_player = l_players[ran_p]
            print(f"The selected player is : {ran_player}")
            ans = input("Please choose truth or dare : ")
            print()

            if ans == "truth":
                ran_t = random.randint(0,len(truth)-1)
                ran_truth = truth[ran_t]
                print(ran_truth)
                break

            elif ans == "dare":
                ran_d = random.randint(0,len(dare)-1)
                ran_dare = dare[ran_d]
                print(ran_dare)
                print()
                break
    else:
        break



