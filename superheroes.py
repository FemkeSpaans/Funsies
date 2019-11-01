#Femke Spaans
#31/10/2019
#Superheroes, versie 1

def main():
    Wanna_Play()
    Human()
    

def Wanna_Play():
    """input if player wishes to play"""
    play = (input('Do you want to play a game?'))
    if play == 'yes' or play == 'Yes':
        print('Good, I am going to guess your favorite marvel movie hero.')
    else:
        print('How rude, well you are gonna play one regardless.')
        
    

def Human():
    """input hero human?"""
    human = (input('Is your favorite hero a human?'))
    if human == 'yes' or human == 'Yes':
        print('Mmm, that is quite a big list.')
        male = (input('Is your favorite hero a man?'))
        if male == 'yes' or human == 'Yes':
            print('Ohhh, I see.')
            american = (input('Was your favorite hero born in the United States of America?'))
            if american == 'yes' or american == 'Yes':
                print('Well that is still quite a list.')
                insect = (input('Is there an insects name in your favorite heroes name?'))
                if insect == 'yes' or insect == 'Yes':
                    print('Well, this has now become a very short list.')
                    SP_AM = (input('Is your favorite super hero still in High School?'))
                    if SP_AM == 'yes' or SP_AM == 'Yes':
                        print("Your favorite super hero is Spiderman, I get that, it's because of Tom Holland isn't it? ")
                        if captain == 'yes' or captain == 'Yes':
                            print('Your favorite hero is Steve Rogers, Captain America, he is mine too.')
                            HE_DP = (input('Do people forget this hero exists?'))
                            if HE_DP == 'yes' or HE_DP == 'Yes':
                                print('Your favorite super hero is Hawkeye, so basiclly Robin Hood, just less hot.')
                            else:
                                print('Your favorite hero is Deadpool, nice choice, fuckface.')
                        else:
                            ('Ohh the list is starting to become really tiny now.')
                            captain = (input('Does your favorite hero have a phenomenal ass?'))
                    else:
                        print('Really? Your favorite super hero is Antman? What the fuck dude get some better standards.')
                else:
                    print('Alrighty then.')
                    iron = (input('Is your favorite hero crazy rich?'))
                    if iron == 'yes' or iron == 'Yes':
                        print('Ironman it is then.')
                        captain = (input('Does your favorite hero have a phenomenal ass?'))
            else:
                print("Your favorite hero is T'Challa, better known as Black Panther.")
        else:
            ('Mmm, so it is a woman.')
            Woman()
    else:
        ('Mmm, that is interessing...')
        Non_Human()
        
def Non_Human():
    once_human = (input('Was your favorite hero once human?'))
    if once_human == 'yes':
        print('Alright')
        hulk = (input('Is your favorite hero male?'))
        if hulk == 'yes':
            print('Your favorite hero is the Hulk, now go smash something.')
            god = (input('Is your favorite hero a God?'))
            if god == 'yes':
                print('That leave only two')
                thor = (input('Is your favorite hero blond?'))
                if thor == 'yes':
                    print('Your favorite hero is Thor')
                else:
                    print('Your favorite hero is Loki, and yes he counts as a hero.')
            else:
                ('Well that is two less on the list then.')
        else:
            print('Aha, Captain Marvel it is then.')
    else:
        print('Okay')
    
    
def Woman():
    pass

main()
