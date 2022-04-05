import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'langex.settings')

import django
django.setup()
from lanex.models import Language, LanguageRequest, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from datetime import datetime
import random

def populate():

    '''
    Pre-provided test users for testing site features like language request creation.
    '''
    example_users = [
        {'username': 'username1',
        'password': 'french',
        'email': 'user1@ok.com'},
        {'username': 'username2',
        'password': 'spanish',
        'email': 'user2@ok.com'},
        {'username': 'username3',
        'password': 'japanese',
        'email': 'user3@ok.com'},
    ]


    french_requests = [
        {'title': 'A French-English study group sounds good',
        'description': "Coucou à tous! I am really enthusiastic about starting up a language study group, particularly since I am in sore need for lots of practice with my French (c'est horrible) and it really helps to have others who are natives and can help. Hence, I think it would be a cool idea to make a petit group between French and English speakers with a common passion: learning languages! Currently, I'm located in Canada so other members who might live nearby, feel free to message me! My neighbourhood is very peaceful and I wouldn't mind using my home as a study place for us once we become friends. Thank you and I hope some great new friends are to be got out of this experience. Ciao les amis!",
        'views': 128,
        'suggested_date': '2021-04-16',
        'location': '9 Rue Monge, 75005 Paris, France'},
        {'title': 'Nous sommes des gamers [FR/EN Gamer Squad]',
        'description': "In brief: looking to create a language-learning squad among gamers for English and French speakers. Salut les amis, moi et d'autres amis sommes à l'origine français et nous aimons jouer aux jeux vidéo; cependant, certains jeux sont difficiles car ils nécessitent une certaine connaissance de l'anglais. En règle générale, nous jouons à des jeux comme CSGO, LoL et quelques autres. L'idée est de créer une équipe franco-anglaise et nous pouvons communiquer ensemble afin d'améliorer nos compétences linguistiques. Pas de doute, ce serait super cool alors faites-moi savoir si vous êtes intéressé. Il n'y a pas d'emplacement exact puisque nous jouons en ligne (évidemment) mais je vous suggère de publier votre compte xbox / playstation dans les commentaires ou d'envoyer un message. Bref, à bientôt!",
        'views': 56,
        'suggested_date': '2021-04-14',
        'location': 'Edinburgh'},
        {'title': "Ici, we speak about One Piece - and we do it in Frenglish",
        'description': "Yo les gars, ceci est le patron. Moi, j'aime bien le One Piece and so I am excited to chat with others sur le Discord serveur who love l'histoire aussi. Si tu veux, let me know what you think and we can set up the group chat online for everything One Piece. Merci d'être venues et d'avoir lus. Bisous! ",
        'views': 35,
        'suggested_date': '2021-04-17',
        'location': 'Halifax, Nova Scotia, Canada'},
    ]

    
    spanish_requests = [
         {'title': 'Saludos',
         'description': 'Hello! I am recent college graduate and I love to travel and learn new languages. I am a Biology major and I have lived in 4 different countries. I am fluent in French, Russian, English and can have a casual conversation in Spanish. I also started learning some Japanese and I would like someone to help me practice my Spanish. In a few weeks, I intend to travel to Madrid and check out the beaches and have a good time; perhaps we could set up a game of beach volleyball between English and Spanish speakers! Urban Beach Madrid seems epic as a beach choice but let me know what you think. ',
         'views': 54,
         'suggested_date': '2021-05-15',
         'location': 'Calle de Agastia, 115, 28043 Madrid, Espagne'},
         {'title': 'Female Spanish-English reading club in Texas',
         'description': "Hello beautiful people. As part of a community movement, we are hoping to set up a reading club for (mainly) females here at the Ector County Library. The sessions are around one or two hours long but you can hop in and out as you like. We hope to have an equal mix of Spanish and English native speakers and to have a good time exploring the literature in our languages. So if you are curious, tag along! The sessions will happen each Friday at 4pm and you can even bring your youngsters along for a fun time. See you there!",
         'views': 82,
         'suggested_date': '2021-04-15',
         'location': '321 W 5th St, Odessa, TX 79761, États-Unis'},
         {'title': 'Holaaaa',
         'description': 'Hello! I would like to practice Spanish. I use it on a daily basis in my work (presently in Valencia), but I want to be more fluent and improve my pronunciation. I also would like to help others learn English, as it is also a worldwide spoken language. There is a Spanish-English billingual event happening near my home so I would be very pleased to make some friends at the event. Hasta luego!',
         'views': 31,
         'suggested_date': '2021-04-28',
         'location': "Plaça d'Hondures, 26, 46022 València, Valencia, Espagne"},
    ]


    japanese_requests = [
         {'title': '魔道士',
         'description': 'Hello, I have been living in Nara and have been here a couple of years as an english speaker, I am trying to learn Japanese - but my Japanese level is very basic! I would really be interested in getting to know more Japanese people and helping you to speak English and along the way hopefully improve my Japanese and have some awesome experiences. Basically looking for a buddy to give me a tour around Japan so if you live in Nara how about we meet together someplace soon? If you like, message me and I can give you my whatsapp and we can chat further.',
         'views': 44,
         'suggested_date': '2021-04-22',
         'location': 'Japan, Nara'},
         {'title': 'hello O_O Japanese friends',
         'description': 'i speak korean (my country) and a bit of english (from school). i like to try and work on my japanese because i loove japan^^\nみなさん、こんにちは。私です。少し漠然としていますが、そうです。私は日本のアニメやマンガに少し情熱的すぎて、信じられないほど多くのシリーズを見てきました。私はよく不和でチャットするので、あなたは私にメッセージを送ることができ、あなたを私の友達リストに追加することができます。リスニングとスピーキングを向上させるために、日本から素晴らしい友達を作りたいと思っています。引き換えに、私はあなたが韓国語を学ぶのを手伝うことができます!!',
         'views': 81,
         'suggested_date': '2021-04-26',
         'location': 'Sajik-ro-3-gil (Street) 23'},
         {'title': 'I do not have a good title [Norwegian wanting to learn Japanese ^^]',
         'description': "I live in Norway! Someday I would like to go to Japan and live there. I want to find someone I can contact for a long time. Let's talk happily and get to know each other. Thank you! We can chat on telegram but during the summer I hope to travel to Tokyo as part of a school show which will happen at the Galaxy Theatre. So maybe if we become good friends, after the show finishes, we can go and have some nice ramen or sushi at a restaurant!! ",
         'views': 19,
         'suggested_date': '2021-07-03',
         'location': 'apon, 〒140-0002 Tokyo, Shinagawa City, Higashishinagawa, 2 Chome−3−16 シーフォートスクエア内 2階'},
    ]


    english_requests = [
         {'title': 'Interested in practising with English natives',
         'description': 'Hello there! My name is Fang and I am originally from Japan. Currently, I live in London, along with my Husband and two beloved children.\nI hope to find people who can help me improve English, especially my pronunciation. In return, I am very happy to share my knowledge of Japanese!. I hope to find someone who lives nearby so we can meet and exchange together regularly as my husband works and children are busy at school, leaving me plenty of time to spare. In fact, we could meet up at the London Library and if you have kids like me maybe we could have family language-learning sessions together! ',
         'views': 45,
         'suggested_date': '2021-04-29',
         'location': "14 St James's Square, St. James's, London SW1Y 4LG"},
         {'title': "Hallo meine Freunde, guten Tag euch allen (ahem hi)",
         'description': "I am bad with introductions but I'll try anyway. Call me as you prefer.I'm working for an international company based in Düsseldorf. In daily business I enjoy communication with people form various countries around the world. From time to time I like to travel, go out, take time for good food, music as well as new things. I'm looking for a person who wants to practice English/ German languages.\nIf you live nearby, there's going to be a football match here where I live so it would be amazing to meet up at the stadium to watch the match and have a good experience together! (Some tell me my English accent is a bit weird but I try my best!)",
         'views': 60,
         'suggested_date': '2021-05-01',
         'location': 'Arena-Straße 1, 40474 Düsseldorf, Allemagne'},
         {'title': 'What is up tout le monde, comment va-ton ?',
         'description': 'Hi, I am french. I am 40 years old. I was a philosophy teacher. I amm studying psychology now. I like nature, reading, rock-climbing, etc. I would be very happy to find someone to discuss in English with. Maybe we can meet together at a local cafe and have a chitchat at some point if you like. I live in Birmingham so if you live nearby we can grab some coffee together and discuss. Let me know if you are interested et à plus!',
         'views': 16,
         'suggested_date': '2021-01-01',
         'location': 'Unit SU744, Upper Mall West, Birmingham B5 4BG'},
    ]

    other_requests = [
         {'title': 'Привет классные люди',
         'description': 'Coucou/Yo everybody, this is my first request here so I hope this works out well. I speak English/French and I would like to learn Russian.\nМои друзья зовут меня Вашо, но вы можете называть меня как угодно, потому что я не слишком взволнован. Мне очень нравится изучать русский язык, и сейчас я собираюсь получить степень по русской литературе. Кстати, моя любимая русская книга - «Доктор Живаго» Бориса Пастернака. Я надеюсь, что смогу найти партнера по обмену русским языком, который поможет мне лучше понимать язык и практиковаться.\nЛично я могу помочь вам выучить французский или английский, так как я выучил их в детстве и часто использую их там, где живу - в Квебеке. Не стесняйтесь обращаться ко мне, и, надеюсь, мы сможем поболтать, может быть, в Discord или подобном. Просто отправьте мне сообщение, и мы посмотрим, как все пройдет. Чао (извиняюсь за мои ошибки, я немного или много пользуюсь переводчиком)',
         'views': 23,
         'suggested_date': '2021-01-01',
         'location': 'Montréal, Québec, Canada'},
         {'title': 'Ciao! Hey there! السلام عليكم',
         'description': "Sorry for potential bad english. I am from Italy and want to learn Arabic (Moroccan type)\n Ciao mi chiamo Raghda e ho 20 anni. Vengo dall'Italia e l'italiano è la mia lingua madre, ma sono anche molto fluente in inglese da quando vivo in Inghilterra e Texas. Attualmente sto studiando coreano perché amo la cultura coreana e voglio essere in grado di parlare ma ho bisogno di qualcuno con cui esercitarmi. Se vuoi imparare l'italiano o praticare il tuo inglese sono qui :)\nPosso darti il ​​mio messenger e possiamo chattare online se sei interessato e forse se viviamo nelle vicinanze possiamo incontrarci orari stabiliti per incontrarci e praticare più apertamente insieme (almeno dopo la pandemia). Al momento, sono un po 'annoiato di dover stare a casa per la maggior parte della giornata, quindi spero di poter fare degli amici che parlano arabo poiché desidero visitare il Marocco durante le vacanze del prossimo anno. Grazie, non vedo l'ora di conoscere nuove persone!",
         'views': 57,
         'suggested_date': '2021-04-21',
         'location': 'Lenno, Lenno, Italy'},
         {'title': 'Hi, hi, hi! 大家好 ！！！',
         'description': 'Hey, you can call me Jojo. I speak English and I am hoping to improve my Chinese!\n随时给我打电话。我是一名正在学习汉语的本科生，目前我目前住在上海，但我在香港生活了一年。我的兴趣爱好之一就是吃饭，我想知道也许我会遇到住在附近并在上海姥姥家常饭馆一起吃饭的中国本地人，并讨论他们的乐趣。当然，我也可以混用一些英语来帮助您练习。',
         'views': 10,
         'suggested_date': '2021-04-27',
         'location': '70 Fuzhou Rd, Wai Tan, Huangpu, Shanghai, Chine'},
    ]


    languages = {'French': {'requests': french_requests, 'picture': 'languages/french.jpg'},
            'Spanish': {'requests': spanish_requests, 'picture': 'languages/spanish.jpg'},
            'Japanese': {'requests': japanese_requests, 'picture': 'languages/japanese.jpg'},
            'English': {'requests': english_requests, 'picture': 'languages/english.jpg'},
            'Others': {'requests': other_requests, 'picture': 'languages/default.jpg'} }

    '''
    Add users to test the site into a list and print confirmation to ensure user has been added
      and apply the same for all example users provided.
    '''
    user_list = []
    for u in example_users:
        user_to_add = add_user(u['username'], u['password'], u['email'])
        user_list.append(user_to_add)
        print(f'- Added example user {user_to_add}')


    for language, language_data in languages.items():
        lang = add_language(language, language_data['picture'])
        for request in language_data['requests']:
            add_request(lang, request['title'], request['description'], user_list[random.randint(0,2)], request['views'], request['suggested_date'], request['location'])


    for lang in Language.objects.all():
        for request in LanguageRequest.objects.filter(language=lang):
            print(f'- {lang}: {request}')


'''
Provides example users with a random first and last name.
'''
def get_random_name(situation):
    if situation == "first":
        first_names = ['Alexios','Minerva','Jun','Vladmir','Francesca','Ezio','Dumbledore','Zelda','Robin','Jeff','Lea','Pikachu']
        return random.choice(first_names)
    if situation == "last":
        last_names = ['Jeagar','Hisham','Chan','Freicks','Cocopops','D Luffy', 'Frodo', 'Vader']
        return random.choice(last_names)


def add_request(language, title, description, creator, views=0, suggested_date=datetime.now(), location='Glasgow'):
    request = LanguageRequest.objects.get_or_create(language=language, title=title, creator=creator, description=description, views=views, suggested_date=suggested_date, location=location)[0]
    return request


def add_language(name, picture):
    lang = Language.objects.get_or_create(name=name, picture=picture)[0]
    lang.save()
    return lang


def add_user(username, password, email):
    user_to_add = User(username=username, email=email, password=make_password(password), first_name=get_random_name("first"), last_name=get_random_name("last"))
    user_to_add.save()
    user_profile = UserProfile.objects.get_or_create(user=user_to_add)[0]
    user_profile.save()
    return user_to_add


if __name__ == '__main__':
    print('Running the lanex population script...   [Random Fun fact - Wearing headphones for just an hour can raise  bacteria count in the ears by 700 times] ')
    populate()
