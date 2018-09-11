#    Heritage for the future visual novel, game based off of hftf community
#    Copyright (C) <2018>  <Devboys>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

label chapter1:
         stop music
         play music "weektheme.mp3"
         scene image "week1"
         with Pause(3.0)
         stop music
         play sound "alarm_clock.ogg"
         scene image "protagroom"
         with Pause(5.0)
         stop sound
         r "Upon hearing your alarm go off, you decide to wake up. Like every morning, you hit the bathroom, brush your teeth, eat your breakfast so you can go back to your room and do nothing for the rest of the day."
         r "You've even forgotten what day of the week it is, time doesn't really matter when you are on your break. After you are done with your morning routine, you decide to turn on your computer."
         play music "gaysong1.mp3"
         scene image "twitter"
         with dissolve
         r "Some time passes by while you are checking some social media and it doesn't take long before you find yourself bored. After a few minutes staring into your desktop, you remember about that game you saw a few days ago. That being said, you quickly hop back into Discord."
         scene image "general"
         with dissolve
         r "You enter the game’s server and take a look at some pings you’ve received. Nothing really that important. Right as you were about to enter #General and start typing something, you remember your last time being here, and so, a thought crosses your mind:"
         ns "Wait a second. I’ve already caused enough trouble here, i can’t risk doing something stupid again. Gaah, this sucks! I’ll just read the rules and other stuff, that should get me started on the game."
         scene image "fightcade"
         with fade
         r "After some time, you finally got “Fightcade” working and a totally legal copy of the game. Feeling proud of yourself for doing all of this alone, you decide to play a bit offline and do story mode. Since this is your first time, you select a random character."
         scene image "fightcade2.png"
         $ renpy.movie_cutscene("challfail.webm")
         ns "Well, that was fun! Even though i kept hitting the wrong keys on my keyboard and that i couldn’t win against the first opponent, i still enjoyed the game! I can’t wait to get online and beat everyone that made fun of me! Ha Ha Ha! Let’s see what’s going on at the #General"
         jump week1general

         label week1general:
         scene image "general"
         with fade
         r "The channel seems to be in conflict over something of questionable quality and really degenerate"
         show image "peon"
         p2 "And thats why Futa on Girl is the least possible gay you can have."
         hide image "peon"
         ll "So futa isn't gay but traps are?"
         ns "Hey! Remember me, guys? I’m back, and this time stronger than ever! Who wants to fight me?"
         show image "lucas"
         boi "If you want to fight ask that on #hftf-general"
         boi "Dummy"
         hide image "lucas"
         ns "Oh."
         ns "I better get going then"
         scene image "hftfgeneral"
         with fade
         stop sound
         ns "Waaaaaaaaait, should i ping that boring role to ask for games? The matchmaking one? Hmm."
         ns "Alright you PEASANTS, who’s ready for a beating? @hftf-matchmaking"
         scene image "hftfgeneral"
         with fade
         scene image "heritage_general.PNG"
         show image "Soui.png"
         play music "fighttheme1.mp3"
         So "Who the fuck is this kid."
         ns "I'm no kid! I'm the greatest player of our generation! Now fight me!"
         So  "Hmph. Fine, get on fightcade, you're dead."
         ns "Finally, my first challenge ever! This is my chance to show everyone i'm no stinko!"

         scene image "fightcade"
         with fade

         r " And so, as soon as you log into fightcade, a loud, annoying tune starts to play, catching you off-guard."
         r "It seems like you've received an challenge. Wasting no more time, you click to accept the match."
         r "Now its time to show what you're made of!"
         play music "Elevator Music.ogg"
         scene image "titecard"
         with Pause(10.0)
         stop music
         scene image "black"
         with fade
         centered "This was a mistake."
         centered "It doesn't take more than a single match to realize you've made a terrible decision on fighting this player."
         centered "It doesn't matter who you pick or what you do"
         centered "You can't even get near this man without getting stuck in a 10 minutes long combo."
         centered "Why? How is this even possible? Why would someone dedicate a majority of their free-time on a silly game?"
         centered "How can you even achieve such skill?"
         r "Soon enough a message pops up on your screen."
         play music "gaysong1.mp3"
         scene image "black"
         with fade
         scene image "fightcade"
         show image "Soui.png"
         fightcadesoui "You are trash."
         fightcadesoui "But you could get better if you started training."
         fightcadesoui "I'm Soui, if you want any matches you can just call me."
         fightcadesoui "Not that i really care to be honest."
         fightcadesoui "GGs kiddo."
         hide image "Soui.png"
         fightcadeplayer "Huh? So you're not that evil, right? Is being rude just a part of your character or somet--"
         r "You realize its useless to try and ask now."
         r "Soon enough you head back to general."

         scene image "fightcade"
         with fade
         scene image "general"
         show image "mahjong"
         m "I'm back. Not for long, i just wanted to check what is going on here."
         r "The chat quickly gets filled with people welcoming this. . . Majongles girl, so you decide to do the same."
         ns "Welcome back! I don't even know you but it's good to have you here, again, i guess, right?"
         m "Shut up faggot, who are you?"
         ns "I'm [povname], you could just read my nickname up there! My turn, who are you?"
         m "Fuck off. I'm better than you, that's all you need to know."
         ns "That's kinda rude you k--"

         play sound "discordsound.ogg"
         show image "ping.png"
         ns "What the fu--"
         play sound "discordsound.ogg"
         show image "ping.png"
         ns "What's going on?"
         play sound "discordsound.ogg"
         show image "ping.png"
         r "Suddenly, you are bombarded with direct messages from someone in the same server as you."
         r "As you check your DMs, you see a lot of random pictures ranging from big tiddie anime girls to images of a character from another game."
         scene image "general"
         with fade
         play music "lucassucks.mp3"
         scene image "black"
         show image "lucas"
         ns "Why are you doing this?"
         boi "Because it's funny."
         ns "Well, i guess it really is funny, thanks."
         boi "Wait, so you're not annoyed?"
         ns "Not at all!"
         hide image "lucas"
         r "And so for the next 10 minutes the dm was filled with le monke and a black man's foot."
         show image "lucas"
         boi "Ok im out of images."
         boi "i like you."
         boi "You survived my epic le meme style spam."
         boi "Call me anytime you want to play the game."
         play music "genericsong.wav"
         hide image "lucas"
         ns "People here are weird."
         r "You decided that you've seen enough for today, it's better to take a break and come back lat--"
         stop music
         show image "gayclock"
         r "IT'S MIDNIGHT ALREADY?"
         hide image "gayclock"
         r "It seems as time acts differently once you are on Discord all day, it is best for you to rest for the night."
         $ renpy.movie_cutscene("7hours.mpeg")
         stop music
         play sound "alarm_clock.ogg"
         scene image "protagroom"
         stop sound
         play music "genericsong.wav"
         r "Another day, another adventure! Wasting time is the last thing someone would want to do in this scenario, so right as you jump off your bed, you quickly turn on your computer."
         scene image "black"
         with fade
         scene image "billbg.png"
         with fade
         r "Well.........."
         r "What now?"
         r "You can't think of anything funny to say in the chat, which no-one is using right now."
         r "Since you are already here, you might as well just start playing the game!"
         scene image "fightcade"
         with fade
         r "At the fightcade lobby, you realise you've just walked into a weird discussion."
         retard "I live in Morocco and we’re happy to eat dirt!"
         show image "tex"
         tx "What does that have to do with anything?"
         hide image "tex"
         show image "potato"
         p "Please stop."
         hide image "potato"
         retard "Seriously, all jojo fans are pathetic heres some proof https://youtu.be/dCcjhee6shg"
         show image "Soui.png"
         So "Haha yeah that is pretty funny."
         hide image "Soui.png"
         retard "Screw you guys and screw your tournament."
         ns "Tournament? What is this guy talking about? What a weirdo. I'll have to check that out later."
         ns "Oh hey, it's those girls from the server! I remember they were really nice with me! Should i challenge them? They can't be worst than Soui, riiiiiiiight?"

         menu CHOICE_TIME:
             "But, i don't really wanna bother anyone, what should i do. . ."
             "Fight Tex":
                      $ tex_relationship += 1
                      jump tex_fight
             "Challenge Potatoboih":
                      $ potatoboi_relationship += 1
                      jump potatoboi_fight

             "Wait for someone else to challenge you.":
                      jump in_joke


         label tex_fight:
         play music "countryshut.wav"
         show image "tex"
         fightcadeplayerchat "Okay, okay! I got this! I'm just going to ask him for some games!"
         fightcadeplayerchat "Hey Tex, do you want to uhmm..."
         fightcadeplayerchat "Do you want to fight me?"
         tx "Sure, i'm free at the minute."
         fightcadeplayerchat "Awesome!"
         $ renpy.movie_cutscene("20later.mpeg")
         stop music
         play music "exetex.wav"
         r "After sending a challenge to Tex Western and getting in a match. you realize she lives up to her name. You find yourself quite confused as to why a literal GUN which shoots bullets FULL SCREEN is fair and balanced."
         fightcadeplayer "This is bullshit! Hol Horse truly is overpowered!"
         fightcadetex "He’s not."
         fightcadeplayer "How so!?"
         fightcadetex "Hol is simple. He can’t do a lot once you know what you are doing."
         fightcadeplayer "I know he’s a dirty zoner!"
         fightcadetex "Don’t be a sissy. Try to understand what your opponent is doing. Once you figure out how limited Hol is, you will be able to beat me."
         fightcadetex "That’s some advice for every fighting game. Adapt to your opponent’s strategy."
         fightcadeplayer "...Adapt, huh?"
         fightcadeplayer "I guess I can try."
         fightcadetex "Great."
         r "And in fact, once you start paying more attention to the tactics used by Tex, you start to actually hit her! Of course, your experience with the game is not enough to win a whole round, but just being able to actually move around without getting hit all the time already feels like a win."
         r "One more thing you notice is that Tex keeps knocking you down and everytime this happens, the game slows down and you get hit by a bullet you can’t even block everytime you try to get up."
         fightcadeplayer "C’mon! What is this attack I can’t even deal with?"
         fightcadetex "That’s his slow bullet. You really can’t deal with it."
         fightcadeplayer "So what? Am I supposed to adapt to taking damage?"
         fightcadetex "No."
         Tefightcadetexx "Most Hol Horse players will try to get you on the ground so they can use this move. It’s unblockable and deals tons of damage."
         fightcadeplayer "That’s also bullsh--"
         fightcadetex "But, as long as you don’t get knocked down, you shouldn’t have to worry about it."
         fightcadeplayer "I… see."
         r "You play a few more matches and after carefully watching every single move Tex does, you noticed she keeps using this slide move that always gets you on the ground. It’s time you said enough, you must counter-attack! But how?"
          
         



        

         label potatoboi_fight:

           mn "Hey, nothing bad will happen if i try to challenge her, right? I'll probably just get rejected, soooo. . ."
           r "Soon enough you send potato a challenge"
           play music "battlethemeshit.wav"
           r "And she accepts!"
           r "The game opens."
           show image "potato"
           fightcadepotato "Good Luck."
           $ renpy.movie_cutscene("transishit.mpeg")
           stop music
           play music "genericsong.wav"
           r "After a while playing, you both decide it's enough. Potato won all the matches, but you managed to score a few  rounds."
           fightcadepotato "You are new to the game, right? I think there's lots of room for improvement."
           fightcadeplayer "Heheh, you think? Thanks."
           fightcadepotato "Yeah, just. . . try to stick with one character, that's it for now, GGs."
           fightcadeplayer "Wait"

           menu ebin_choices:
              "Could you please train me?":
                  $ training = "potatoboi"
                  jump train_me

              "I'll get better, you'll see!":
                  $ training = "loner"
                  jump loner


           label train_me:

           fightcadeplayer "Hey, i think you are a really good player, and you are really nice. Could you train me?"
           fightcadepotato "Uhm, that’s came from nowhere, but sure."
           fightcadepotato "I’ll make you memorize every single property of every frame in the game, you’ll play this game for the rest of your life, all day and night, think you can handle that?"
           fightcadeplayer "No, but i guess i don’t have any other option, right?"
           fightcadepotato "Well, you better not give up, got it? That’s it for now, GGs."
           fightcadeplayer "GGs"
           hide image "potato"
           fightcadeplayer "That was fun! I didn't even expect her to accept my challenge. I’ll take a break now."
           jump general_chapter_1

           label loner:

           fightcadeplayer "Watch me improve! I'll come back and beat your ass, alright?!"
           fightcadepotato  "Heh, that's the spirit"
           fightcadeplayer "I'll show her whose the alpha around here!"
           fightcadepotato "And so you head back to discord"
           jump general_chapter_1

           label in_joke:
              $ in_joke = "rando"

           ns "Man, this is not even worth it. I guess i’ll just wait for a challenge, i guess."
           pause(3.0)
           r  "And time goes on. . .
              And on. . .
              And on. . ."
           pause(3.0)
           r "You start to feel asleep."
           pause(3.0)
           mn "This is taking really long."
           mn "Did i leave the stove on?"
           mn "Is it worth it waiting this much?"
           pause (3.0)
           mn "I’m getting bored here."
           mn "Just get this over with and challenge someone."
           mn "Like Jesus Christ it’s n--"
           stop music
           play sound "challengenosie.wav"
           show image "wew"
           r "11:11 ￼ <yukke> challenged you - (999ms, Japan) accept / decline"
           hide image "wew"
           stop sound
           mn "Yeah, i don’t. . ."
           mn "I don’t think i’m up for games anymore."
           mn "I’ll just go check the discord or something."
           jump general_chapter_1




         label general_chapter_1:

         stop music
         play music "genericmus2.wav"
         scene image "general"
         with fade
         r "After a while hanging at the meme channels and looking at dumb Youtube videos, you notice something different with your Discord interface."
         ns "Stinko. . . Countainment?"
         r "Eager to know the secrets this channel holds, you click on it instantly."
         r "It doesn't long enough to discover that this place is awful."
         r "As you look at the top right corner of your screen, you see a red circle next to the pin icon."
         ns "What? Why would anyone pin ANYTHING that is here? This is so pointless!"
         r "Despite your flawless logic, you click on the icon anyways."
         r "All you see is the repost of rule 6,  a random Jotaro combo and. . .a message from the server owner herself?"
         r "Getting good enough to be noticed?"
         r "Something, something, getting cured from a stinko!?"
         ns "YES! THIS IS WHAT I’VE BEEN WAITING FOR! I CAN FINALLY ESCAPE THIS HELL AND BE UNSTINKED! BY ZARYTHE HERSELF!"
         ns "But wait a second."
         ns "I must get decent enough to be noticed, or win a ‘stinko tournament’?"
         ns "The hell is that supposed to mean?"
         ns "And how am i going to get good enough?"
         ns "I mean. . . ."
         jump wowie_big_blocks_of_code

         label wowie_big_blocks_of_code:

         if training == "potatoboi":
                             ns " I guess i don’t have to worry about this, after all, Potato’boih’ is training me! It will take no time before i become the best player ever!"

         elif training == "loner":
                             ns "I fought that really nice girl earlier today. . ."
                             ns "She said i could improve a lot."
                             ns "Stick to one character? I guess i’ll do that."

         elif tex_fight == "kept going":
                             ns "There’s that Hol Horse chick that i fought said i had good potential. Maybe she could teach me the ropes after she comes back from band practise?"

         elif tex_fight == "quit":
                             ns "Gah, this is frustrating. I guess that if i managed to win at least a few rounds against a tournament host, then i’m sure i can do this."

         elif in_joke == "rando":
                             ns " This will be hard, i haven’t fought anyone other than Soui, and he just wrecked me.
                             Am i really able to do this?"
                             ns "Man, this sucks. . ."
         jump afterwards

         label afterwards:

         ns "No matter the case I have to win a stinko tourney and get good enough!"
         ns "Then i'll have the power and fame and respect i deserve!"
         r "As you say your dramatic speech, people in the background continue their conversation about part 5 being announced."
         r "You also get someone to notice you."
         show image "lucas"
         boi "Hey buddy! You’re here too?!"
         mn "Oh God not her again."
         ns "hey there"
         ns "so uh how long you been here for?"
         boi "Oh i've been here forever as a stinko even after winning a tourney."
         ns "Wait you actually won one of those? Then why are you he--"
         boi "Details don't matter! Anyways, you won’t get much done in here. You had better check out other channels where actual players are."
         ns "Not a bad idea."
         hide image "lucas"
         scene image "black"
         r "And so you begin to think to yourself and come up with a plan."
         mn "Alright! I need a good plan! If i want to become a decent player at the game, the first thing i should do is to learn about it!"
         mn " I’ll ask people if they have some good source for that sorta stuff. Before that though, I gotta go check out that tournament thing."
         scene image "annon"
         r "After reading through an announcement you missed before, it seems like a tournament is being held tomorrow, with all sorts of rules, where for some reason the character you played the most, Petshop, is banned."
         r "After signing up for the tourney, you decided to visit the HFTF channel."
         scene image "hftfgeneral"
         with fade
         ns "Hey uh is there a wiki for this game?"
         show image "sploog"
         Sp "You could’ve just read the #useful-links channel but alright, here it is."
         r "Right as she sends you a link to some sort of wiki, it doesn’t take more than 2 seconds for it to be erased."
         hide image "sploog"
         show image "zarythe.png"
         Z "I already said a million times to not share the new wiki yet, faggot. It’s not even finished. Just use Stand Crash for now."
         hide image "zarythe.png"
         ns "Oh uh thanks."
         r "This was unexpected. A ‘new wiki’? Well, no time to lose here. You move on to another channel."
         scene image "general"
         ns "So what are you guys doing?"
         raid " Looking for matches."
         min "Noooothing."
         p2 "Complaining about top tiers."
         edgy "Beating up khan."
         scene image "khanspam.png"
         r "It seems after edge sent that messege a flood of khan emotes overan the chat."
         scene image "bgpol"
         show image "billspam" at truecenter
         r "It also seems bill joined in the aswell."
         hide image "billspam"
         scene image "general"
         ns "Jesus, does everyone just play HFTF here?"
         show image "alph"
         a "Because it’s a HFTF server, dumbass."
         hide image "alph"
         show image "mahjong"
         m "Hey kike why don't you make yourself useful and buy me a game on steam."
         ns "Wait"
         ns "Why the hell would i buy a rude stranger like you anything?"
         m "Cause then i'll say nice things about you for 3 months."
         ns "But im broke."
         m "Hmph, fine."
         m "I'll just go back to playing this shitty game."
         r "Majongle's discord status updates to be playing fightcade."
         r "Maybe it’s not such a bad idea to challenge her."
         r "What should you do?"

         menu cowboy_emoji_time:
             "Send a challenge.":
                 $ majongles_relationship += 1
                 jump send_challenge

             "Leave it as it is.":
                 jump leave_it



         label send_challenge:

         ns "Well, it’s not like i have anything better to do!"
         scene image "fightcade"
         with fade
         stop music
         play music "mahjongtheme.wav"
         r "As you hop onto fightcade, you can see Majongles asking for games in the lobby, so you don’t lose time to challenge her."
         r "Time to show her whose boss!"
         $ renpy.movie_cutscene("icetandemlater.mpeg")
         stop music
         play music "genericmus2.wav"
         r "Even if you were not match to Majongle’s skill, you still managed to have a good time playing the game."
         show image "mahjong"
         fightcademahjong  "Fun matches, GGs."
         fightcadeplayer "GGs"
         hide image "mahjong"
         r "The game closes, and with that, you decide it’s time to go to sleep, seeing how late it is."
         scene image "black"
         jump morning_chapter_1


         label leave_it:

         ns "Naaaah, i’ve had enough for today, i’ll just go to bed already."
         hide image "mahjong"
         scene image "black"
         jump morning_chapter_1


         label morning_chapter_1:
         $ renpy.movie_cutscene("nextday.mpeg")

         stop music
         play music "morningtheme.wav"
         play sound "alarm_clock.ogg"
         scene image "protagroom"
         with fade
         with Pause(5.0)
         stop sound
         r "It is a dawn of a new day and you can hear all sorts of nature sounds already!"
         scene image "windowopen.jpg"
         r "Birds chirping, boomer's mowing their lawns, whales dying, and other morning noises!"
         ns "Ah, what a lovely day! That sunshine is beautiful!"
         stop music
         scene image "windowclose.jpg"
         r "The blocked window stops the sunlight along with the sound outside from entering your home."
         ns "The perfect time to play computer games! Time to log onto Discord!"
         scene image "hftfgeneral"
         with fade
         play music "normalmusicay.wav"
         ns "Games anyone?"
         dan "Is this practice for the tourney?"
         mn "Oh shit, the tournament is today! Can I get ready in time?!"
         al "I’d like to play some rounds."
         uz "Me too."
         show image "alph"
         a "Shut up kids, he wants to play someone who doesn’t suck if he’s practicing for the tournament, which means he would want to play me."
         hide image "alph"
         show image "BiLl.png"
         boomerusa "Want to fight a decent rubber?"
         hide image "BiLl.png"

         menu:
             "Fight Aleph.":
                 $ aleph_relationship += 1
                 $ bill_fight = "No"
                 jump fight_aleph
             "Train with Bill.":
                 $ bill_relationship += 1
                 $ bill_fight = "Yes"
                 jump fight_bill
             "Fight someone at you level.":
                 $ lucas_relationship += 1
                 $ bill_fight = "No"
                 jump fight_lucas


         label fight_aleph:
         scene image "fightcade"
         show image "alph"
         play music "doomshit.wav"
         a "Have I seen you around the palmodding channel?"
         fightcadeplayerchat "Uh, maybe?"
         a "Well I hope not, the only palmods I see nowadays are shit… It may just be better to delete that channel once and for all…"
         fightcadeplayerchat "Can we play now?"
         a "Yes."

         $ renpy.movie_cutscene("3timestopslater.mpeg")
         play music "normalmusicay.wav"
         r " And as time goes on, the final score settles at 5x1, with Aleph taking the match. Due to a sudden spike of luck and lag, you managed to win at least two rounds."
         fightcadealeph "Just fucking settle down with one character already."
         fightcadeplayer "But i don’t know which one to pick! Why can’t i just play as everyone?"
         fightcadealeph "Because you are too stupid to even pick a main, let alone learning the whole roster."
         fightcadeplayer "Then help me choose my main!"
         fightcadealeph "No. Just don’t pick Dio or Devo, they are meant to be used by highly intellectual people, like me."
         fightcadeplayer "Okay, okay, fine. But the puppet character looks fun to use. . ."
         fightcadealeph "He’s not. But if you are stubborn enough to pick him, i will share you some secret, hidden Devo tech."
         fightcadeplayer "Sounds like a deal."
         fightcadealeph "Yeah, fuck off. GGs kid."
         fightcadeplayer "GGs"
         r "To assert clear dominance over your opponent for winning one round, this time you are the one to close the game. With no time to lose, you decided to check the game’s Discord server to look for updates about the tourney."
         jump stinko_tournament

         label fight_bill:

         ns "A decent Rubber Soul you say? Well then, bring it on!"
         play music "billfighttheme.mp3"
         scene image "fightcade"
         with fade
         r "After BiLL sends a row of random emotes, you finally challenge her on Fightcade."
         $ renpy.movie_cutscene("billater.mpeg")
         play music "normalmusicay.wav"
         r "After a quick ft5, the game is decided. Unsurprisingly, BiLL won all of the games without a lot of effort. Seems like your unfamiliarity with Rubber’s gameplay ended up costing you the game."
         show image "bill"
         fightcadeboomer "What was that? Do you not know how to fight Rubber at all? How do you plan on fighting in the tournament like that?"
         r "You feel like if this took place at the Discord server, you would be bombarded with monkey emojis."
         fightcadeplayer "Hey! It’s not my fault! I’m new to the game and you picked a super strong character! How do you even want me to win?"
         fightcadeboomer "Rubber? Strong? I wish. He’s super low tier and not hard to beat at all."
         fightcadeboomer "Guess i’m just that good."
         fightcadeplayer "Well, yeah, I guess. But he looks pretty easy to use."
         fightcadeboomer "Maybe not easy, just simple to understand and play as."
         fightcadeplayer "-I see. . . Well, i guess i will see you in the tournament, you are a host, right? Will you cheer for me?"
         fightcadeboomer "Maybe, lol. GGs."
         hide image "bill"
         fightcadeplayer "GGs"
         r " As usual, the game closes and you are left staring at the game’s lobby. With the tournament right around the corner, you decided to check the game’s Discord."
         jump stinko_tournament

         label fight_lucas:
         ns "Well since there isn't anyone in chat ill just go look for games in fightcade."
         scene image "fightcade"
         with fade
         stop music
         fightcadeplayerchat "I think i will just fight someone more on my level, you know? Someone like. . ."
         show image "lucas"
         play music "luketheme.mp3"
         boi "Me!"
         fightcadeplayerchat "Yeah! No, wait a second. . ."
         boi "C’mon! I wanna train too."
         fightcadeplayerchat "Fine! But you better not cry when i beat your ass!"
         boi "Whatever, monke."
         $ renpy.movie_cutscene("failedbnb.mpeg")
         play music "normalmusicay.wav"
         r "For a stinko, Lucas is quite good at the game. She’ not as impressive as Soui, but her skill is enough to make you struggle in some matches."
         fightcadeluke "One more?"
         fightcadeplayer "Nah, i had enough, GGs."
         fightcadeluke "Uh Oh, the check-ins are already open. GGs."
         fightcadeplayer "Check-Ins? What does that me--"
         r " Before you can finish writing your question, Lucas decides to close the game, leaving you looking at the lobby. But there is no time to lose! As for now, you must check the Discord."
         jump stinko_tournament




         label stinko_tournament:
         scene image "general"
         play sound "discordsound.ogg"
         show image "ping.png"
         r "As the tournament draws near, you get a notification from the server, warning all the players to ‘check-in’ before the livestream starts."
         hide image "ping.png"
         stop sound
         scene image "annon"
         show image "zar"
         Z "It’s time to check in retards, if you fail to do so you’re automatically disqualified from the tournament, so go."
         hide image "zar"
         mn "Shit i better hurry, but where am i supposed to check in?"
         r "Fear not! As you scroll through the channels looking for the correct place to ask for help you spot one called “#weekly-tournament-general’."
         r "The perfect place to ask for things related to the weekly tournaments."
         scene image "tourney"
         ns "Hey so uh the announcement page said i had to ‘check-in’ or something like that, but where?"
         show image "zar"
         Z "Can you not read?"
         ns "Well I just…"
         Z "How can people like you still breathe?"
         ns "I mean… I’m just asking for help?"
         hide image "zar"
         ns "Please?"
         ns "Pretty please?"
         r "But these atempts to get some answer's were useless as she already left the channel."
         r "Just as you were about to leave and give up, someone showed up to help you out."
         show image "potato"
         p "Just read the full announcement, the challonge page has all the info you need."
         mn " Oh Yeah! The Challonge page! That’s where i had to register!"
         ns "Thank you very much!"
         hide image "potato"
         r "With literally no time to lose, you rush your way through the channels and the useful information you should have been reading to get to the page you needed so you could finally check-in right on time."
         scene image "challenge"
         ns "I did it! I’m now playing on a tournament! I just need to wait. . . 8 minutes?!"
         ns "It’s not a lot, but i guess there’s no harm in relaxing for a bit."
         ns "I’ve been feeling quite hungry, maybe i could order something?"
         ns "It shouldn’t take long before i could get pizza to be delivered here? Right?"
         scene image "black"
         stop music
         play music "pizzatime.wav"
         r "With an IQ of 200, you managed to figure out something to do while you wait for the tournament to start"
         r "After placing your order through a phone, you decided to take a good nap to gain more energy for the tourney."

         scene image "black"
         with fade
         r "After quite a long while, you are woken by the sounds of your doorbell ringing. After getting up and getting your hands on that box of pizza, you dash to your computer to check Discord."
         scene image "general"
         with fade
         ns "What?! The livestream has already started and people are already playing?!"
         scene image "challenge"
         r "After 5 minutes panicking, checking the brackets shows that you were placed for the second round."
         r "Taking a look back at the stream, you realize the hosts are still on the first phase of the tourney. Lucky you!"
         r "It seems like the tournament hosts are choosing what matches they should stream next."
         scene image "choosing"

         if potatoboi_relationship >= 1:
                                      p "Well, i would like to watch [povname] against lagmaster69"
                                      ns "What?! She wants to watch me playing?! Man, am i ready for this? Can i really do this?"

         elif bill_relationship >= 1:
                                  boomerusa "Let's spectate [povname]."
                                  Sp "You sure?"
                                  boomerusa "Yeah, why not."
                                  ns "Huh, does this counts as 'cheering'? I'm not so sure if i can do this. . ."

         else:
             Sp "Round 2 is kinda weak, not a lot of interesting fights."
             boomerusa "Yeah, i guess we could just watch any match."
             p "Let's spectate the ones on top of the bracket."
             r "Due to extreme amounts of bad luck, it just so happens you are on the top of the brackets."
             ns "Damn! I'll have to play on the stream! This sucks, am i really ready for this?"


         r "After a while, the hosts finally pick their matches."
         Z "Very well. Everyone else can play your matches, we will now spectate [povname] versus lagmaster69."
         stop music
         play music "beforethebattle.wav"
         ns "Okay! I can do this! I'll show everyone i'm no fool! There's no time to hold back now!"
         r "You realized that while you were trying to motivate yourself, you hadn't even openned FightCade yet."
         scene image "fightcade"
         with fade
         fightcadeplayerchat "Okay! I'm ready to fight now! I just need to challenge my oppone--"
         play sound "challengenosie.wav"
         show image "wew"
         r "And just as you were about to finish your sentence, you receive a challenge from lagmaster69 himself."
         stop sound
         r "The game opens and you decide to close your browser to avoid any sort of lag. This time, there's something different about this, a strange feeling of fear and anxiety in the air."
         r "You take a long breath and let out a long sigh. It's finally time to show the world what you are capable of doing."
         r "Here you are, being streamed to hundreds of people. Only one question remains:"
         scene image "black"
         with fade
         stop music
         play music "ericbattlemusic.wav"
         centered "ARE"
         centered "YOU"
         centered "READ--"
         centered "Your opponent decided to pick Rubber Soul."

         if bill_fight == "Yes":
                               r " But this is no problem! Your matches against BiLL will surely give you enough knowledge to win against this foe! Right?"

         elif bill_fight == "No":
                              r "Yes, your worst nightmare, Rubber. That cheap bastard that can trap your character and leave you totally open. Very scary."


         r "None of these things matter now. Using your big brain knowledge about the game that you have gained from reading the Stand Crash wiki, you decided to pick Kakyoin!"
         mn "Kakyoin is the best character and a strong pick against Rubber! There's no way i will lose!"
         stop music
         $ renpy.movie_cutscene("laggyroundlater.mpeg")
         play music "sad!.wav"
         r "Since you have never played Kakyoin before in your entire life, you couldn't do anything against the Rubber player."
         r "It's painful losing like that, after all this warm-up and with so many people watching you."
         r "However, there's still hope. You still have one more match to go before you are thrown into losers brackets."
         scene image "select"
         play music "characterselect.wav"
         r "You are back at the character select screen. This is your one final pick, the outcome of the game depends on your choice."
         fightcadeplayer "That's it."
         fightcadeplayer "I'm picking Jotaro."
         play sound "gaylol.mp3"
         show image "selected"
         r "And so you prepare yourself to make a big comeback and get rid of this stinko tag!"
         scene image "black"
         stop sound
         stop music
         $ renpy.movie_cutscene("brutalbang.webm")
         scene image "black"
         with fade
         play music "ripperoni.mp3"
         r "Despite your great efforts, you still lost the match."
         lagmasterfightcade "GG"
         r "Part of you wanted to reply with a GGs, but after this match and what this player did, you just couldn't do that."
         r "You hit the big 'X' on the corner of your screen and you walk away from your computer."
         ns "Dammit! How could he beat me so easily?! This is frustrating."
         ns "Man, i hope i wasn't trashed that much on the stream."
         ns "I still have a chance on the losers brackets, but at this point. . ."
         ns "I just cant do this anymore."
         r "And so you lay on your bed with only your thoughts."
         r "Why do you suck so bad compared to the others!"
         r "When do you start having fun!?!"
         r "You begin to question why you even play fighting games if you keep losing."
         r "You will never be as good as the others, you will always be a scrub so why even bother learning?"
         r "Why do you subject yourself to stress over a fighting game!"
         r "Before you could answer those thoughts, a new one arose."
         mn "This sucks, i was so ready for the tournament, and couldn't even win a single match!"
         ns "Might as well check out the server to see how shit talked i was."
         scene image "general"
         with fade
         stop music
         play music "endchapter1theme.wav"
         r "Checking the game's Discord shows how much into the weekly tournaments everyone is."
         r "The main chats are empty and the tournament related channels would occasionally spawn a message or two."
         r "Maybe it's a good idea to see how you did on the stream, granted you don't have a lot else to do."
         scene image "choosing"
         with fade
         r "After minutes trying to find the exact timestamp for your fight, you finally managed to find it."
         r "Just as you expected, your performance on the stream was awful. The chat would comment on every mistake you made."
         r "But then....."

         if potatoboi_relationship >= 1:
                                       p "Shame [povname] couldn't manage to win. I was hoping he would win."
                                       Sp "Oh, really? I mean, he played really poorly."
                                       Z "Yeah, that was a pretty stinky match."
                                       p "Eh, whatever."
                                       ns "Wait. . ."
                                       ns "Was she really hoping i would win? Heh, i guess that's just how it is."

         elif bill_relationship >= 1:
                                    boomerusa "I can't believe [povname] lost to a Rubber like that."
                                    boomerusa "I'm gonna have to teach him a lesson after this."
                                    Z "Were you rooting for him?"
                                    boomerusa "Shut up Idiot."
                                    ns "Goddammit BiLL, knew you would do that."

         elif tex_relationship >= 1:
                                   Sp "Yo, if Tex was here, who do you think he would root for?"
                                   Z "I don't know. He talked a bit about this [povname] dude once but that's about it."
                                   Sp "Really huh? I can kinda see why."
                                   ns "Huh, Tex wasn't on the stream for some reason, but he talked about me?"

         elif lucas_relationship >= 1:
                                     scene image "general"
                                     play sound "discordsound.ogg"
                                     show image "ping.png"
                                     r "As you were watching your match, a notification from Discord pops up, catching you off-guard."
                                     stop sound

                                     r "It's Lucas."
                                     hide image "ping.png"
                                     show image "lucas"
                                     boi "Hey uhh, i saw your match on the twitch stream. I feel sorry for you. Did you at least do well on losers?"
                                     ns "Not really, i just kinda gave up and didn't even play losers."
                                     boi "Oh. That sucks."
                                     ns "Yeah. But thanks for talking with me."
                                     boi "No problem!"

         else:
             r "While your eyes avert from the stream to the twitch chat, you can see a few people that were actually cheering you up, most of them being other stinkos you've met earlier."


         #twitch background here
         r "After you finally finish watching your part on the stream, you reflect on what happend and whats in store for the future."
         ns "Man, this tournament was really something."
         ns "Sure this is a rage inducing game, but it really is something special."
         ns "I feel like i'll stick with this community for a long time. . ."
         return
