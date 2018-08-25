


   #characters
   define n = Character("[povname]", color="FFFFFF")#normal color
   define ns = Character("[povname]", color="663300")#stinko player
   define mn = Character("[povname]'s brain", color="663300")#stinko player
   define r = DynamicCharacter("narrator", color="FFFFFF")#normal color
   define boomerusa = Character("BiLL", color="00FFFF")#tourney host color
   define a = Character("Aleph Null", color="F206FF")#knowledge boy color
   define tx = Character("Tex Western", color="00FFFF")#tourney host color
   define hoho = Character("HoHo Horse", color="663300")#stinko color
   define Sp = Character("SploogieMcNoodle", color="00FFFF")#tourney host color
   define p = Character("PotatoBoih", color="F206FF")#tourney host color
   define m = Character("Majongles", color="74138C")#big ping gay color
   define uz = Character("Ultrazoop", color="FFBE28")#mad man twitch sub color
   define So = Character("SouI", color="FFE920")#tourney winner color
   define do = Character("Doog", color="F206FF")#knowledge boy color
   define kr = Character("KarnazZ", color="006633")#helper color
   define neet = Character("Royshark", color="663300")#stinko color
   define ms = Character("MisterSystem", color="F206FF")#knowledge boy color
   define ba = Character("BAEN", color="00FF00")#regular color
   define iso = Character("ISO BOI", color="FFFFFF")#normal color
   define hy = Character("Hyoko", color="006633")#helper color
   define pnt = Character("Pontee", color="006633")#helper color
   define bd = Character("BlackDe", color="FFE920")#tourney winner color
   define sn = Character("Skynaloz", color="FFE920")#tourney winner color
   define Z = Character("Zarythe", color="00FFFF")#tourney host color
   define p2 = Character("Peon2", color="006633")#helper color
   define R = Character("Narrator", image="le monkey", color="FFFFFF")#normal color
   define ll = Character("LOCK_LOAD", color="006633")#helper color
   define boi = Character("Light speed lucas", color="663300")#stinko color
   define retard = Character("Stoned Illama", color="663300")#stinko color
   define raid = Character("Raiddean", color="006633")#helper color
   define min = Character("Mineotaur", color="00FF00")#regular color
   define edgy = Character("Edge la Edge", color="00FF00")#regular color
   define dan = Character("Dannythebalu", color="00FF00")#regular color
   define al = Character("Alsrb", color="FFFFFF")#normal color
   define lm = Character("Lagmaster69", color="FFFFFF")#normal color
   define brain = Character("[povname]'s brain", color="FFFFFF")#normal color
   define fightcadesoui = Character("Soui", what_font="PressStart2P.ttf",color="FF9900")#fightcade color and font
   define fightcadetex = Character("Tex Western", what_font="PressStart2P.ttf",color="FF9900")#fightcade color and font
   define fightcadealeph = Character("Aleph Null",what_font="PressStart2P.ttf",color="FF9900")#fightcade color and font
   define fightcadeluke = Character("Light speed lucas", what_font="PressStart2P.ttf",color="FF9900")#fightcade color and font
   define fightcadeboomer = Character("Bill", what_font="PressStart2P.ttf",color="FF9900")#fightcade color and font
   define fightcademahjong = Character("Majongles", what_font="PressStart2P.ttf",color="FF9900")#fightcade color and font
   define fightcadepotato = Character("PotatoBoih", what_font="PressStart2P.ttf",color="FF9900")#fightcade color and font
   define fightcadeplayer = Character("[povname]", what_font="PressStart2P.ttf",color="FF9900")#fightcade color and font
   define fightcadeplayerchat = Character("[povname]", color="FF0000")#fightcade normal chat color
   define lagmasterfightcade = Character("Lagmaster69", what_font="PressStart2P.ttf",color="FF9900")#fightcade color and font


   #backgrounds

   image computer = "1_3.jpg"
   image wm = "welcome_message.png"
   image wr = "window_rainy.png"
   image sad = "sad.png"
   image aw = "awakned.png"
   image side monkey = "le monkey.png"
   image week1 = "week1.jpg"
   image protagroom = "protag_room.jpg"
   image twitter = "twitter.png"
   image general = "discord_bg.png"
   image fightcade = "fightcade.png"
   image announce = "announcement.png"
   image general2 = "discord_bg2.png"
   image hftfgeneral = "heritage_general.png"
   image titecard = "titlecard.png"
   image black = "Pure Black.png"
   image emote = "emote.png"
   image fightgamegeneral = "fgg.png"
   image guide = "guide.png"
   image question = "hftfquestion.png"
   image jojohell = "jojomemehell.png"
   image memehell = "meme hell.PNG"
   image palmod = "palmod.png"
   image tourney = "tourney.png"
   image khanspam = "khanspam.png"
   image billspam = "billspam.png"
   image bgpol = "billbg.png"
   image exchan = "exchannel.png"
   image laughshit = "laughshit.png"
   image gayclock = "gayclock.png"
   image wew = "wew.png"
   image annon = "announcements.png"
   image open = "windowopen.png"
   image close = "windowclose.png"
   image challenge = "challonge.png"
   image choosing = "choosingmatch.png"
   image select = "selectback.png"
   image selected = "charactershitselected.png"

   #character pictures
   image lucas = "lucas.PNG"
   image sploog = "sploog.png"
   image alph = "aleph.png"
   image zar = "zarythe.png"
   image bill = "BiLl.png"
   image ragebill = "angerybill.png"
   image mahjong = "majongles.png"
   image ms = "mistersystem.png"
   image peon = "peon2.PNG"




   #complex mechanics

   init:
    define flash = Fade(.25, 0.0, .75, color="#fff")

   init:
    $ sploogie_relationship = 0
    $ tex_relationship = 0
    $ zarythe_relationship = 0
    $ potatoboi_relationship = 0
    $ bill_relationship = 0
    $ majongles_relationship = 0
    $ soui_relationship = 0
    $ lucas_relationship = 0  #lucas is a joke route please dont track us down FBI
    $ aleph_relationship = 0
 #yee whoever chooses lucas gonna get booty raped by tyrone in prison

    default training = False
    default tex_fight = False
    default in_joke = False



################################################################################

   label prologue:
    $ narrator = "Pro Tagonist"
   stop music
   scene computer
   play music "chillshit.wav"
   with Dissolve(3.0)
   r "Oh Yeah! It sure is nice to be on my summer break."
   r "The birds are singing, the grass is green,the sun is shining!"
   r "I have a different feeling about this summer, This one’s gonna be faaaaan-tastic~ there’s all sorts of things to do!"
   jump yeah

   label yeah:
    stop music
    pause 3.0
    scene wr
    with fade
    play sound "lightning-strike.ogg"
    r "I..."
    r "I don't have anything to do!"
    r "I mean, I can always watch Youtube, right? That will keep me busy, right?"
    stop sound
    scene image "exchan"
    r "Sooooo, Ex Falchion just uploaded a video, what's this all about?"
    scene image "computer"
    $ renpy.movie_cutscene("jahroom.mpeg")
    r "This looks interesting, the video even has a link to a dedicated server for the game on a
       popular text and voice communication program. Well, since I got nothing better to do, I’ll give this a shot!"

    stop sound
    play music "crateshit.mp3"

    scene wm
    with Dissolve(3.0)
    stop sound
   $ narrator = "Narrator"

   define pov = Character("[povname]")

   python:
    povname = renpy.input("So stinko whats your name?")
    povname = povname.strip()


    if not povname:
         povname = "Pro Tagonist"

   r "God is dissapointed in [povname]!"


   n "Wow, there's so many channels to choose from! The first thing I should do is get the game! Maybe people at #General could help me with this!"
   n "But wait, that would be stupid. I can't just appear out of nowhere and start asking for things!"
   n "Silly me! I should first check out some other channels and maybe introduce myself to the people here."
   r "Yeah, that sounds smart! I’ll do that. I should check out the #hftf-general chat first."

   jump hftf_general


   label hftf_general:
         stop music
         scene hftfgeneral
         play music "potatotheme.mp3"
         r "As you enter the channel, you see some people talking in weird numbers and letters combinations. Aside from incoherent messages, you see a ‘TAS’ video, followed by a message from what it seems to be a moderator."
         show image "potato"
         p "As I was saying, the bnb requires a negative edge into a one frame link where you have to tandem and pushblock into a 5c, then hyper hop into a rekka and stand crash into 6a, then immediately do a 214aa…"
         p "Got it!?"
         p "Huh!? What? Oh. Wow, what a sensory overload, this girl seems like she knows what she’s doing! I felt like I was falling asleep!"
         p "Bravo, Bravo! How did you figure this out?"
         p "What? That's just a basic combo. Any stinko could do this."
         n "A… Stinko?"
         p "You are new to this place?"
         n "Yeah, I just entered this server! Who are you?"
         p "I’m Potatoboih, I usually try helping out with streams and TASing. Ask me if you need any help with the game, okay?"
         n "Got it, thanks!"
         r "While you are unsure of what ‘TASing’ means, you are still happy by the fact someone is willing to help you with the game. After reading some other messages by random people in the chat, you move on to the next channel in the list."
         hide image "potato"

         stop music
         play music "backgroundmusic.ogg"
         scene image "guide"
         r "Tandems? IPS? Loops? Infinites!? What are all those complex words? Is everyone in this channel crazy? Why can't you understand any of this? Is this some sort of secret fighting game lingo?"
         r "Right as you were about to give up on trying to understand any of this, a new message appears in the chat, grabbing your attention."
         show image "sploog"
         Sp "Yeah, if you don’t learn the numpad notation system, you’re screwed. It’s not that hard anyways, just check the pins."
         r "Answering a question made by someone else, this person appears to be very kind and calm, but most importantly, what the hell is a numpad notation? It doesn’t really matter right now, so you decide to introduce yourself."
         n "Hey! That’s super cool! Could you teach me what those other complex words mean?"
         Sp "Sure, but some other time, I gotta bounce to work soon. By the way, I’m SploogieMcNoodle, always here to help if you just ask! See you later alligator!"
         r "Alligator? Huh, that’s weird, last time you checked you were sure to be a human. You feel like questioning your race is pointless so you decide to move on to the next channel."
         hide image "sploog"
         stop music

         play music "MVC3_Doc_Doom_Theme.ogg"
         scene image "palmod"
         r "As you enter this channel, you see a variety of characters wearing different color palettes. Some of those look really nice, while some others are so bad you feel like you might go blind if you stare at them too much"
         r "While this channel has a lot of images, there’s not that many people talking, but right before you were about to leave, a interesting message appears."
         show image "alph"
         a "Haha, holy shit, another anime palmod? Why do I even bother anymore?"
         r "Weird, this is the first time you see a grumpy person in this server. You can’t just leave the chat like this, you must cheer this person up!"
         n "Hey, don’t get discouraged! I’m sure that whatever a palmod is it can’t be too bad."
         a "Fuck off please, why do I have to deal with brainlets like you that can’t even read the pins?"
         r "You aren’t sure what a brainlet means or what a pin is, but you keep listening to whatever this person has to say."
         a " I’m Aleph null, and I run this channel, if you’ve got a problem with that, you can fuck right off."
         hide image "alph"
         r "After Aleph screams at some other people for not creating attractive “palmods”, you decided to check out some other channels."
         stop music

         scene image "emote"
         play music "bommerusasong.mp3"
         r "Upon entering this channel, you are greeted with diverse images of a variety of things such as sprites from the game and Jpegs. It's not hard to guess that this place is used for suggesting new emotes for the server to use. Duh."
         r "As you read the newer messages from this channel, you see that someone has posted a badly cropped, unfunny meme in the chat."
         show image "ragebill"
         boomerusa "That looks absolutely disgusting."
         boomerusa "Read the rules if you want to suggest a new emote."
         boomerusa "You absolute monkey."
         r "Another person in a bad mood? You know what you have to do. Hopefully, you will be more successful than last time."
         n "Hi, I’m [povname], are you okay? You seem to be having a rough day, miss. There’s no need to say such rude things!"
         boomerusa "Shut up."
         boomerusa "Do you even know what this channel is for?"
         R le monkey "She proceeds to send a string of multiple potentially racist emoji, namely monkeys."
         boomerusa "Whatever"
         boomerusa "I’m BiLL, and I run this channel."
         boomerusa "Read the rules if you want to suggest any new emotes."
         n "Thanks ma’am I’ll keep that in--"
         boomerusa "If you don’t have anything to suggest, get out."
         r "You decide that it may be a good idea to leave and check the last channel remaining."
         stop music
         hide image "ragebill"

         scene image "jojomemehell"
         play music "Wheeler Walker Jr. - Sit On My Face.ogg"
         r "Finally! A channel that piques your interest! A place where you can finally be in peace! A meme channel! But, it’s a channel just for JoJo memes, so you can’t understand any of the jokes here. Despite that, you find yourself scrolling through the channel for quite a long time. After looking through a lot of images of a man at a table, you spot what it seems to be a fight."
         show image "tex"
         tx "For the last time, you libshits have got to grow a brain and realize that this is not a shitposting server. What’s your Fightcade account?"
         hoho "My Fightcade account? It’s, uh…"
         hoho "You see, I kinda don’t play this game that much and I--"
         play sound "Hand_Cracking_Noises.ogg"
         r "After a random users gets publicly executed for his meme consumption and lack of actual playtime, the woman sighs   and begins to crack her hands in a menacing way."
         stop sound
         n "Wow, what was brutal, so cool!"
         tx "Huh? Oh, I’m sorry you had to see that, these stinkos are seriously getting on my nerves. My name’s Tex, Tex Western, what can I do for you? "
         n "Oh, nothing, nothing! I was just taking a look at this channel and I swear I wasn’t here to post more dumb images!"
         tx "Good, then outta here."
         r "Well, that was truly something. It seems like you've already visited every channel you needed to see, so it's finally time to--!"
         hide image "tex"
         play sound "discordsound.ogg"
         show image "ping.png"
         r "What's this? It seems like some sort of notification, and it's coming from the #general chat."
         r "Well, you had to go there anyways, so you don't lose any time to click on the notification."
         jump general

         label general:
         scene image "general"
         play music "startofgame.wav"
         hide image "ping.png"
         show image "potato"
         p "Hey guys! I'm going to stream my next TAS, come and watch me! @here"
         r ". . . @here? As soon as you see this message, the notification disappears. Is this where the notification came from?"
         r "Also, several people are typing? Could this.."
         brain "Oh no."
         hide image "potato"
         show image "mahjong"
         m "Nice ping, retard."
         hide image "mahjong"
         uz "Die."
         show image "Soui.png"
         So "Hmph."
         hide image "Soui.png"
         do "Wow, you really had to ping everyone for this, didn't you?"
         r "Chaos takes over the chat. A lot of users are screaming and sending annoyed emotes, cursing at Potato."
         kr "Everyone, stop being so rude!"
         neet "What's this all about?"
         show image "ms"
         ms "Hey, what's going on here?"
         hide image "ms"
         ba "Hi."
         iso "Haha nice."
         hy "What."
         pnt "Hey, cool, a streamed TAS!"
         bd "Nice."
         sn "Hey, New Kak is pretty fun."
         hide image "potato"
         r "It doesn't stop."
         r "There are so many messages of people angry at the 'ping' that you can't even read them anymore from how fast they appear."
         stop music

         Z "Everyone{fast}"
         show image "zarythe.png"
         play sound "shut.mp3"
         Z "Shut.{fast}"
         stop sound
         play sound "thefuck.mp3"
         Z "The Fuck.{fast}"
         show image "zarythe.png"
         stop sound
         play sound "up.mp3"
         Z "Up.{fast}"

         r "The chat goes dead silent. Not a single message is being typed out."
         Z "Almost all of you stinkos don't even play the game, you have no right to complain about a ping. If you truly think getting pinged is so annoying and you don't even contribute to the community, just leave this server."
         r "Zarythe, the server owner. . . Just a simple phrase like that is more than enough to send chills down your spine. Taking advantage that the chat is quiet, you decided that this is the time to ask for the game. Swallowing your fears and clenching your fists, you get ready to type out your message"
         n "Hey, umm, how can I download this game? It looks amazing and I want to play it…"
         Z "Hey, umm, how about you figure it out by reading the various important notices and pins, idiot."
         n "Hey miss! There is no need to be rude! I just want to play the game and--"
         Z "Why don’t you try going back to elementary school before coming here if its that hard for you to read simple english?"
         n "But I just want to play and have fun and..."
         Z "But can you read?"
         n  "Of course I can read, otherwise I wouldn't be able to answer you!"
         play music "cricket.mp3"
         Z "…"
         n "…"
         Z "…?"
         n "Can I have the game now?"
         stop music
         hide image "zarythe.png"
         play music "suicidebois.wav"
         scene image "laughshit"
         r "The chat bursts into laughter. It seems like everyone is spamming emotes and making fun of the whole situation. It doesn’t take long before people start calling you a “Stinko” out of nowhere. "
         show image "peon"
         p2 "Dude, you just had to read the message at #welcome."
         hide image "peon"
         ns "But I did read that! It was just a weird message asking for my name! I don't understand this! Not at all!"
         r "After you finish sending that message, you notice your username now has a different color, and not a really pleasant one. A brown browner than the.. Brownest depths? I don’t know, point is, you’ve become what these people call a “stinko”."
         r "Your new brown username acts as a brand of suck, signifying your eternal stench. Hopefully you can rid yourself of your putrid funk, as you wish to redeem yourself."
         return
