
#Femke Spaans
#31/10/2019
#Superheroes, versie 2

def main():
    Wanna_Play()
    

def Wanna_Play():
    """input if player wishes to play"""
    play = (input('Do you want to play a game?'))
    if play == 'yes' or play == 'Yes':
        print('Good, I am going to guess your favorite marvel movie hero.')
        Human()
    else:
        print('How rude.')
        Exit()

def Human():
    """input human,
        input male,
        input female.
        """
    human = (input('Is your favorite hero a human?'))
    if human == 'yes':
        print('Alright')
        male = (input('Is your favorite hero a man?'))
        if male == 'yes':
            print('Good to know')
            Male_human()
        else:
            female = (input('Is the hero a woman?'))
            if female == 'yes':
                print('Good to know')
                Female_human()
            else:
                print('There are no heroes on this list who are neither man nor woman, try again.')
                Wanna_Play()
    else:
        print('Okay, Alien it is then.')
        Alien()

def Male_human():
    """input american or not,
        input african,
        input serbia.
        """
    american = (input('Was your favorite hero born in the United States of America?'))
    if american == 'yes' or american == 'Yes':
        print('Well that is still quite a list.')
        American()
    else:
        african = (input('Was your favorite hero born in Wakanda?'))
        if african == 'yes':
            print("Your favorite hero is T'Challa, better known as Black Panther.")
        else:
            serbia = (input('Was your favorite hero born in Serbia?'))
            if serbia == 'yes':
                print('Your favorite hero is Pietro Maximoff, better known as Quicksilver. I am judging your life choices because of this.')
            else:
                nope = (input('There are no heroes left, either you do not have a hero, or you are a shitty player. Do you have a hero?'))
                if nope == 'yes':
                    Wanna_Play()
                else:
                    print('No hero, that must suck.')
                    Exit()
                
def American():
    """input insect, input high school
        input rich, input dead
        input ass,
        input friend, input fly,
        input green,
        input forget, input robin hood.
        """
    insect = (input('Is there an insects name in the name of your favorite hero?'))
    if insect == 'yes' or insect == 'Yes':
        print('Well, this has now become a very short list.')
        SP_AM = (input('Is your favorite hero still in High School?'))
        if SP_AM == 'yes' or SP_AM == 'Yes':
            print("Your favorite super hero is Spiderman, better known as Peter Parker, I get that, it's because of Tom Holland isn't it? ")
        else:
            print('Really? Your favorite super hero is Antman? What the fuck dude get some better standards.')
    else:
        iron_or_strange = (input('Is your favorite hero crazy rich?'))
        if iron_or_strange == 'yes':
            death = (input('Is your favorite hero dead?'))
            if death == 'yes':
                print('Your favorite hero is Tony Stark, also known as Iron Man, I love you 3000.')
            else:
                print('Your favorite hero is Docter Strange.')
        else:
            captain = (input('Does your favorite hero have a phenomenal ass?'))
            if captain == 'yes' or captain == 'Yes':
                print('Your favorite hero is Steve Rogers, Captain America, he is mine too.')
            else:
                falcon_bucky = (input('Is your favorite hero a best friend of Captain America?'))
                if falcon_bucky == 'yes' or falcon_bucky == 'Yes':
                    falcon = (input('Does your favorite hero fly?'))
                    if falcon == 'yes' or falcon == 'Yes':
                        print('Your favorite hero is Sam Wilson, Falcon.')
                    else:
                        print('Your favorite hero is Bucky Barnes, the Winter Soldier.')
                else:
                    hulk = (input('Are you green and angry?'))
                    if hulk == 'yes' or hulk == 'Yes':
                        print('Your favorite hero is the Hulk, or Bruce Banner, or both, I guess.')
                    else:
                        forget = (input('Do people forget this hero exists?'))
                        if forget == 'yes' or forget == 'Yes':
                            robinhood = (input('Is your favorite hero a bit like Robin Hood?'))
                            if robinhood == 'yes' or robinhood == 'Yes':
                                print('Your favorite hero is Hawkeye and I think you are an idiot.')
                            else:
                                print('Your favorite hero is James Rhodes, better known as Warmachine. This is just sad dude.')
                        else:
                            print('There are no more human male heroes left. You fucked up, try again.')
                            Wanna_Play()
                    
def Female_human():
    """input insect, input wasp,
        input twin.
        """
    insect = (input('Is there an insects name in the name of your favorite hero?'))
    if insect == 'yes' or insect == 'Yes':
        print('Well, this has now become a very short list.')
        wasp = (input('Does your favorite hero fly?'))
        if wasp == 'yes' or wasp == 'Yes':
            print('Your favorite hero is the Wasp, Hope van Dynen, which I like to rhyme with lame.')
        else:
            print('Your favorite hero is the Black Widow, Natasha Romanoff.')
    else:
        print('That leaves only the two most powerful heroes.')
        twin = (input('Do you have a twin?'))
        if twin == 'yes' or twin == 'Yes':
            print('Your favorite hero is Scarlett Witch, Wanda Maximoff, an excellent choice.')
        else:
            print('Your favorite hero is Captain Marvel, Carol Danvers')
        

    
def Alien():
    """ input God, input Asgard"""
    God = (input('Is your favorite hero a God?'))
    if God == 'yes' or God == 'Yes':
        Asgard = (input('Is your favorite hero from Asgard?'))
        if Asgard == 'yes' or Asgard == 'Yes':
            print('Your favorite hero is Thor Odinson, the God of Thunder.')
        else:
            print('Your favorite hero is Loki Laufeyson, the God of Mischief')
    else:
        guardians = (input('Is you favorite hero a Guardian of the Galaxy?'))
        if guardians == 'yes' or guardians == 'Yes':
            celestial = (input('Was the father of your favorite hero a celestial?'))
            if celestial == 'yes' or celestial == 'Yes':
                print('Your favorite hero is Peter Quill, Starlord. Danceoff anyone?')
            else:
                gamora = (input('Did the father of your favorite hero kill your hero?'))
                if gamora == 'yes' or gamora == 'Yes':
                    print('Your favorite hero is Gamora.')
                else:
                    humor = (input('Does your favorite hero laugh at his own jokes?'))
                    if humor == 'yes' or humor == 'Yes':
                        print('Your favorite hero is Drax the Destroyer.')
                    else:
                        rocket = (input('Did people experiment on your favorite hero?'))
                        if rocket == 'yes' or rocket == 'Yes':
                            print('Your faovrite hero is Rocket.')
                        else:
                            groot = (input('Does your favorite hero only know four words?'))
                            if groot == 'yes' or groot == 'Yes':
                                print('Your favorite hero is Groot. We are Groot.')
                            else:
                                print('You fucked up, there are no more heroes left.')
                                Wanna_Play()
        else:
            print('Your favorite hero is Vision.')
        

def Exit():
    """stop the program"""
    exit()
    
main()
