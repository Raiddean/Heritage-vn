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

label chapter2:
         stop music
         play music "week2introtheme.mp3"
         scene image "week2"
         with Pause(6.0)
         stop music
         play sound "alarm_clock.ogg"
         scene image "protagroom"
         with Pause(5.0)
         stop sound
         r "As the sunlight peaks through the curtains of the windows in your room, you realize it is time to wake up."
         r "Unsure of how much you've slept, you finally get up from your bed to turn on your computer."
         scene image "week2desktop"
         with dissolve
         play music "generalchatweek2.wav"
         ns "It's been a few days since the last HFTF tournament."
         ns "Im really feeling like playing some matches right now."
         ns "I should head on over to the server to check it out and ask for some sets."
         ns "Hopefully everyone already forgot about my match last week....."
         scene image "general"
         with dissolve
         r "As you enter general, you start seeing an argument between a british lad and..."
         show image "mahjong"
         m "Shut up, Low Iq.Sin."
         hide image "mahjong"
         mosin "Dude, your Ice is terrible, just stop trash-talking."
         show image "mahjong"
         m "It’s not trash-talking, it’s just the truth, you dumb faggot."
         hide image "mahjong"
         mosin "Fine, why don’t you just fight me then? That will show everyone how bad you really are."
         show image "mahjong"
         m "I don’t want to waste my time fighting low iq players like you, pal."
         hide image "mahjong"
         mosin "What’s up? Scared? Act like a man and just fight me already."
         show image "mahjong"
         m "Can’t you read, dumb cunt? I’m not gonna fight retards like you, Muhammad."
         hide image "mahjong"
         mosin "That’s not even my name."
         show image "mahjong"
         m "Whatever, niggy."
         hide image "mahjong"
         mosin "Geez, you are just toxic, i’m not even gonna bother arguing anymore."
         show image "mahjong"
         m "Yeah, go cry in a corner now, Lo.Sin."
         if majongles_relationship >= 1:
                                       ns "Hey Majongles, what’s going on?"
                                       m "This loser is saying some dumb shit."
                                       ns "That’s bad, but it’s no reason to be fighting!"
                                       m "Whatever, I’m done with him anyways."
                                       ns "Well, if you say so. Wanna play some matches?"
                                       m "Not now, I’m busy."
                                       ns "Again?"
                                       m "What?"
                                       ns "Uh, nevermind!"
                                       mn "I should probably ask someone else for some games."



         elif majongles_relationship >= 0:
                                    ns "Uh, what is going on here? This isn’t nice."
                                    m "Fuck off stinko, no one cares what bad players like you say."
                                    mn "He probably thinks I’m bad because he remembers my match on stream!"
                                    ns "Just so you know, I was having a bad day, okay?"
                                    m "What?"
                                    ns "I really tried my best and I will get better..."
                                    hide image "mahjong"
                                    mosin "What are you talking about?"
                                    ns "My match on stream yesterday."
                                    show image "mahjong"
                                    m "Kid, I have no idea what you’re talking about."
                                    ns "Well I just. Ah, uh..."
                                    r "It seems like things are not going as you expected and you are now stuck in a awkward situation."
                                    r "It’s best for you to just go to another channel."
         scene image "hftfgeneral"
         with fade
         mino "Yeah, I wish B.Pol had good matchups."
         show image "sploog"
         Sp "Well, he has so much potential with his 214AA as a catch all move and his loop is pretty devastating, though hard."
         hide image "sploog"
         mino "That’s the only thing keeping him out of the gutter!"
         show image "sploog"
         Sp "Well he does have fun stuff in the game, you know i used to main him when I started."
         hide image "sploog"
         show image "potato"
         p "Huh, didn’t remember that, cool."
         p "Any ways, I was thinking of doing another TAS, what do you…"
         hide image "potato"
         ns "Hey guys, trying to practice the game, anyone wanna fight me?"
         ns "I’m not that good but I think I’m willing to seriously start getting better."
         mino "You want to spar? Who do you play?"
         ns "Uh, lots of characters actually!"
         mino "Oof, that’s tough."
         mino "You must be new, it’s best to pick one character and stick to them."
         ns "I suppose that makes sense, but who to pick…"
         mino "Well, who do you like?"
         ns "Well I guess I like..."
         menu:
             "DIO":
                 mino "DIO!?"
                 mino "I play DIO and it took me a lot of hours to learn him, that dude’s bnb is insane."
                 mino "Still, if you want help, I would suggest asking Zarythe, Aleph or SouI."
                 jump isee
             "Polnareff":
                 mino "Polnareff is really strong and annoying to fight."
                 mino "SploogieMcNoodle can help you there."
                 jump isee
             "Vanilla ice":
                 mino "Ice is top tier and it shows, outside of some strange neutral and learning the 214a link he really isn’t that hard."
                 mino "His damage is crazy. Bill and SouI play strong Ices. If you ever see Majongles on fightcade ask to see his Ice."
                 mino "Theres also lamar davis but hes always playing on alts."
                 jump isee


             "Devo":
                 mino "Well uh there’s not really many Devo players around."
                 mino "Cloudskipper was the best but he’s not around anymore, and Psi_Mega used to play Devo but he switched."
                 mino "Devo is known as the hardest character in the game and the only guys who can really help you would be SouI and Aleph."
                 jump isee


             "Hol horse":
                 mino "The most annoying mid-tier, unless you have a good matchup against him like most high tiers."
                 mino "I would recommend asking Sploogie or Tex Western for advice. Majongles used to play Hol Horse too."
                 jump isee




             "Rubber":
                 mino "Not many people play Rubber, even though he has a lot of potential."
                 mino "Bill even thinks he could be B tier and PotatoBoih knows him well too."
                 jump isee


             "Mariah":
                 mino "You must be joking."
                 scene image "khanhell.png"
                 mino "even Khan would be better than Mariah."
                 scene image "hftfgeneral"
                 mino "Well, not many people are used to fighting Mariah so you get a match-up advantage I guess, she gets annoying if her meter is high."
                 mino "Actually, now that I think about it, PotatoBoih and SouI have both won tournaments with her..."
                 jump isee

                 label isee:
                 ns "I see…"
                 ns "Thanks for the info."
                 ns "Can we play a few rounds?"
                 mino "Uh, not right now."
                 mino "I have stuff to take care of."
                 ns "Wait"
                 ns "If you had all this time to tell me about the characters why don't you have any time right n-"
                 ns "Actually nevermind."
                 mn "Im sure i'll find better luck finding someone to fight with on fightcade."
                 jump thefightcadesearch


         label thefightcadesearch:
         stop music
         play music "lookingforachallnege.mp3"
         scene image "fightcade"
         with fade
         r "Before you challenge anyone to a fight, you recall being told to choose a main to play with."
         r "You decide to choose a main and commit to training with them for the time being."
         r "This is obviously an important decision."

         menu:
             "Choose DIO":
                 $ main_DIO = "True"
                 $ main = "DIO"
                 mn "It has to be DIO, he’s just so cool and his combos are amazing too."
                 mn "I’ve heard he’s super hard though so I have to train extra hard and hope I can get good advice from someone..."
                 jump thebigfightmods
             "Choose Polnareff":
                 $ main_Pol = "True"
                 $ main = "Polnareff"
                 mn "Man, Polnareff is just my style!"
                 mn "He’s fun and looks like he’s very strong in the game too. I need to ask for some help with the charge moves though..."
                 jump thebigfightmods
             "Choose Hol Horse":
                 $ main_Hol = "True"
                 $ main = "Hol Horse"
                 mn "Hol Horse, the goofer himself."
                 mn "It must be him, he looks like just the character I would play."
                 mn "Time to have some fun being an annoyance! I hope someone teaches me his cool setups though..."
                 jump thebigfightmods
             "Choose Devo":
                 $ main_Devo = "True"
                 $ main = "Devo"
                 mn "It has to be Devo."
                 mn "His unique playstyle just perfectly fits my unique tastes."
                 mn "I’ve heard he’s very hard though so I need someone to teach me..."
                 jump thebigfightmods
             "Choose Rubber":
                 $ main_Rubber = "True"
                 $ main = "Rubber"
                 mn "Rubber, this guy looks like an absolute blast to play and the perfect character to fuck with."
                 mn "He’s very simple and easy to learn but I need someone to teach me his more complex stuff though..."
                 jump thebigfightmods
             "Choose Mariah":
                 $ main_Mariah = "True"
                 $ main = "Mariah"
                 mn "Mariah, the perfect waifu."
                 mn "Even though she's a low tier, she's really fun!"
                 mn "I might need some advice with the hard matchups however..."
                 jump thebigfightmods
             "Choose Vanilla Ice":
                 $ main_Ice = "True"
                 $ main = "Vanilla Ice"
                 mn "Vanilla Ice, if I want to be serious about learning this game I have to go with a top tier."
                 mn "I’ve heard he dominates most of the matchups but I need someone to teach me his combos…"
                 jump thebigfightmods

         label thebigfightmods:
         ns "Anyway, now that I know my main, I need someone to train with, let’s see who’s online."
         menu:
             "Challenge Sploogie":
                 jump sploogie_fight
             "Challenge Potatoboih":
                 $ zarythe_fight = "True"
                 jump potato_fight
             "Wait for someone to challenge you.":
                 jump nahbimalone



         label nahbimalone:
         r  "You wait, and you wait…"
         pause(3.0)
         r "And you wait…."
         pause(3.0)
         r "...wait...."
         pause (3.0)
         r "...while waiting you read the FightCade lobby chat and listen in on what people talk about."
         r "You notice alot of strange things, like a serbian telling someone he put them in their place and saying yare yare daze."
         r "Or that italian who keep saying combos are cheap and how he always wins at tekken without them."
         r "Or that brazilian who keeps complaining about jotaro."
         r "You start to read into these rants and you noti-"
         play sound "challengenosie.wav"
         show image "wew"
         r "11:11 ￼ <MargeSimpsonUchiha> challenged you - (54ms, USA) accept / decline"
         hide image "wew"
         stop sound
         r "Someone challenged you."
         r "It’s someone you don’t recognize and it seems to be using a joke name but you should still accept the challenge."
         r "fighting anyone at this point is better than no one."
         play music "doogbootybangtheme.mp3"
         show image "doogalt"
         amazingname "It’s time for your funeral kid."
         amazingname "And I’m going to be the one burying you."
         hide image "doogalt"
         mn "Oh man, this should be interesting!"
         mn "With that name, it’s no doubt someone who’s compensating for their skill with bad jokes."
         scene image "choosekak"
         with fade
         r "After a few seconds the game loads up."
         scene image "choosenkak"
         r "And it seems he immediately went for kakyoin."
         fightcadeplayer "GLHF"
         r "..............."
         r "No response it seems."
         scene image "black"
         r "The game starts and he immediately dives into you from the air, knocks you down and starts up a combo."
         r "You are immediately blown away at the sheer speed of his Kakyoin, and quite frankly a little bit scared."
         r "With your own eyes, you witness the horror of a a real Kakyoin combo. It feels like it’s going on forever, there’s nothing you can do but just watch the absolute rape of your innocence and fun."
         r "He finally ends the combo and you get launched to the other side of the screen."
         r "It’s the first time in the match you get to actually move and you decide to move forward but instead you get immediately knocked down."
         r "You stare in shock at how he's knocking you down while he's at the other side of the screen."
         r "You get back up and this time he’s right in front of you, doing whatever kinds of okizemi he learned on you and you lose the round."
         r "This absolute murder goes on for a few matches with multiple perfects and all you can do is watch, you don’t even get to play."
         r "You don’t even think you’ve had the chance to move your character for longer than 10 seconds in the few matches you’ve played."
         r "But there looks like a chance to strike back as it looks like he's close to you while you wake up. What will you do?"
         menu:
              "Block high":
                  $ soui_relationship +=1
                  r "You block high on wakeup and you block his attack."
                  r "As you are about to start your counter attack, Marge immediately goes for another overhead and gets another combo into knockdown on you."
                  jump endofrape
              "Block low":
                  r "You block low and get hit by an overhead and get comboed and knocked down."
                  jump endofrape
              "Jump":
                  r "You attempt to jump but your jump gets stuffed by a well timed meaty overhead from your opponent and you get knocked down again."
                  jump endofrape
              "Press a button":
                  r "In your panic you try to press a button on wakeup to maybe get your foe off guard."
                  r "But a well timed overhead attack got you instead."
                  jump endofrape
              "Reversal tandem" if main_DIO:
                  $ soui_relationship +=2
                  r "In a panic you go for a reversal tandem as you wake up, it works and you get some hits on him even if you don’t know how to combo afterwards."
                  r "Nonetheless, you prevented a perfect so you feel some sense of accomplishment."
                  jump endofrape



         label endofrape:
         $ renpy.movie_cutscene("literalrape.webm")
         play music "doogs2ndbootybang.mp3"
         r "No matter what you do, you cannot stand a chance against this player."
         r "You feel completely crushed."
         mn "The fuck is this bullshit!"
         mn "So this what top tier HFTF’s play looks like?!"
         mn "This is fucking horse shit, i cant even move one inch without getting infinited!"
         r "The frustration is starting to boil inside you and you decide to call Marge out."
         fightcadeplayer "C’mon man, that’s fucking cheap!"
         fightcadeplayer "All you do is spam attacks!"
         fightcadeplayer "At least let me move my fucking character!"
         show image "doogalt"
         fightcademarge "Hey [povname], how much does your dad weigh?"
         fightcademarge "I bet I can benchpress him."
         hide image "doogalt"
         fightcadeplayer "What?"
         scene image "fightcade"
         r "The game suddenly closes and you’re left staring at the FightCade lobby."
         r "Not only that but marge is now berating you in the lobby, for all to see."
         show image "doogalt"
         amazingname "Hey [povname], i found a picture of you."
         amazingname "Check it out."
         amazingname "https://steamuserimages-a.akamaihd.net/ugc/82593097587407343/406E4428A890BB98B7B275DF0AD35BB93AD45ADD/."
         hide image "doogalt"
         fightcadeplayerchat "I’m just a new player and I’m still learning the game!"
         fightcadeplayerchat "Why do you have to start shittalking on me like that."
         fightcadeplayerchat "Wasn’t it enough that you beat me?"
         show image "doogalt"
         amazingname "No, but check this out."
         amazingname "I think I found a video of your dad."
         amazingname "https://www.youtube.com/watch?v=fXSiFrgByzA"
         hide image "doogalt"
         r "The berating continues, but there is nothing you can say that will make him stop."
         r "And you know its not worth giving him more ammo by trying to argue."
         r "As you just sit there and read the lobby chat going crazy over this godlike roasting session you’re receiving from marge...."
         play sound "challengenosie.wav"
         show image "wew"
         r "You get a challenge from Soui!"
         hide image "wew"
         stop sound
         r "You have absolutely no motivation to even care about the game at this point but since you remember playing SouI a while back."
         r "You decide to accept his challenge just to be nice to him."
         scene image "kanji"
         with fade
         r "The game starts up but instead goes into a black screen with a bunch of japanese looking text."
         show image "Soui.png"
         play music "justgowithit.mp3"
         fightcadesoui "Hey uh, don’t let that bother you."
         fightcadeplayer "What?"
         fightcadesoui "That shit talk, don’t let it get to you."
         fightcadeplayer "Well it’s pretty fucking hard after that much abuse in game and out of it."
         fightcadesoui "Yeah but, y’know just take something positive out of it."
         fightcadeplayer "Hah, like you could get anything positive out of that shit."
         fightcadesoui "No you fucking stupid big stupid."
         fightcadesoui "You know, most of us have also gone through that same thing."
         fightcadeplayer "Really?"
         fightcadesoui "Ofcourse."
         fightcadesoui "Plus uh well,"
         fightcadesoui "You know he just really wants you to get better at the game."
         fightcadesoui "It’s his way of saying ‘come on, prove it you can get back at me’ or something, you get it?"
         fightcadesoui "At Least that’s how it was for me."
         fightcadesoui "I used to get berated by that guy all the fucking time and I couldn’t take it at first."
         fightcadesoui "But then I started wanting to beat his shit in you know, like, show him that ‘fuck you i can do it.’"
         fightcadesoui "You get me?"
         fightcadeplayer "I think I might, But i don’t know..."
         fightcadesoui "Well think on it."
         fightcadesoui "I like to view it as good motivation to want to kick someones shit in."
         if main_DIO == "True":
                        fightcadesoui "I was watching that match by the way."
                        fightcadesoui "That DIO, even though he destroyed you there, has some potential."
                        fightcadesoui "I think you tried making the right calls and if you had known how to play and the matchup, you maybe would have stood a chance."
                        fightcadesoui "I can teach you sometime… maybe."
                        fightcadesoui "Anyways, you’re dumb, bye."
                        hide image "Soui.png"
                        scene image "fightcade"
                        with fade
                        fightcadeplayerchat "Thanks, I guess..."
                        mn "..."
                        r "You feel like absolute shit, but at the same time, strangely motivated!"
                        r "You actually might have learned something from getting beat up by Marge that much."
                        r "Speaking of marge it seems hes still going on and on in the chat with your name highlighted in few of the messages."
                        r "It doesn’t feel great so you decide to take a break from the game by checking your Discord."
                        jump headtogeneral1







         else:
            fightcadesoui "Anyways, you’re gay. Okay bye."
            hide image "Soui.png"
            scene image "fightcade"
            with fade
            r "The game closes and your stuck looking at the fightcade chat"
            mn "..."
            r "You feel like absolute shit, but at the same time, strangely motivated!"
            r "You actually might have learned something from getting beat up by Marge that much."
            r "Speaking of marge it seems hes still going on and on in the chat with your name highlighted in few of the messages."
            r "It doesn’t feel great so you decide to take a break from the game by checking your Discord."
            jump headtogeneral1



         label potato_fight:
         fightcadeplayerchat "Hey Potato! Wanna go for a few matches?"
         if potatoboi_relationship >= 1:
                                       show image "potato"
                                       p "Yo [povname]"
                                       p "I would love too but i gotta go to work soon."
                                       p "I would have shown you the power of my DIO."
                                       p "How about you play Zarythe instead?"
                                       p "He’s pretty good and I’m sure he can give you some tips about the game too."
                                       hide image "potato"
                                       show image "zar"
                                       Z "Huh. what? Oh, yeah sure, why not."
                                       Z "You did say some positive things about this guy so he may not be such a stinker after all."
                                       Z "Alright [povname], lets go."
                                       jump fightwiththetsar



         elif potatoboi_relationship >= 0:
                                    show image "potato"
                                    p "Uh sorry man i gotta go to work."
                                    p "Zarythe, i’ll leave this up to you. Show this guy what DIO can do."
                                    hide image "potato"
                                    show image "zar"
                                    Z "What? Why?"
                                    show image "potato"
                                    p "Just do it, he’s serious about learning the game."
                                    hide image "potato"
                                    show image "zar"
                                    Z " Fine, alright [povname], lets go."
                                    jump fightwiththetsar


         label fightwiththetsar:
         hide image "zar"
         scene image "choosingdio"
         with fade
         play music "zarbattlethemeshit.mp3"
         r "As the game opens, it only takes a few frames for Zarythe to pick DIO and his Start color."
         scene image "choosendio"
         r "Seems like he really likes that character."
         r "You note that he owns the server and must be really good, so you must play carefully."
         if main_DIO == "True":
             scene image "black"
             with fade
             r "The match starts and Zarythe is already going all out on you."
             r "And soon enough you get caught in a loop."
             r "Her sheer aggressiveness is something to be expected from a Dio main and you finally get to see what this character is really capable of doing."
             r "Dominating the fight and controlling you from every part of the screen, you can't even hit her."
             r "Plus every single one of your attempts to attack is countered with huge combos."
             r "You start wondering why Zarythe is only using a few of Dio's attacks when he has so many tools to use."
             r "But now is not the time to think about that!"
             r "As Zarythe's Dio gets further from your character, you notice she's starting to charge her laser. What do you do?"
             menu:
                 "Attempt to roll through the beam":
                     $ zarythe_relationship =+1
                     r "Moments before the projectile is able to hit your character, you decided to roll in a stylish way to avoid the laser."
                     r "A risky and bold move, and perhaps not the brightest idea, since it doesn't take long before Zarythe manages to close the distance on your character and start applying pressure once again."
                     jump endofzarfight2
                 "Teleport through it":
                     $ zarythe_relationship =+2
                     r "With the reaction time of a god, you manage to input Dio’s teleport and avoid getting hit in the last second possible."
                     r "This allowed you to close distance between your opponent, but sadly you couldn’t hit Zarythe before she was able to block the hit."
                     jump endofzarfight2
                 "Duck under the projectile":
                     $ zarythe_relationship =+1
                     r "Knowing very well the reach of Dio's laser projectile, you have decided to crouch so you could avoid getting hit."
                     r "After that, the match proceeds normally. Even if your actions ended up allowing you to be unharmed by the beam, you feel like you could have done something else."
                     jump endofzarfight2
             label endofzarfight2:
             $ renpy.movie_cutscene("knifeslater.mpeg")
             r "The match goes on and even if Zarythe isn’t talking on the chat, you start understanding more about Dio and the game itself just from playing with her and watching her movements."
             r "After a long time playing, you decided that you had enough."
             fightcadeplayer "Hey, GGs."
             show image "zar"
             fightcadezar "Do you seriously want to main Dio?"
             fightcadeplayer "Yeah, he looks fun and not a lot of people play him."
             fightcadezar "I'm actually a bit happy there are more people seriously willing to stick with Dio."
             fightcadezar "You just started recently right? Dio is really not a character for beginners, but if you got the guts, go for it."
             fightcadezar "Keep practicing, strive to become a better player."
             fightcadezar "I'm willing to help you if i'm not busy, you can ping me on Discord if you have some questions about the game."
             fightcadezar "Anyways, GGs."
             fightcadeplayer "Wow, thanks! GGs for you too! Again!"
             hide image "zar"
             scene image "fightcade"
             with fade
             r "The game closes shortly after and Zarythe is already at the 'away from keyboard' list on Fightcade and Potatoboih is nowhere to be seen."
             r "More importantly, you feel like checking out the discord server to see the latest spicy maymays there."
             jump headtogeneral1












         else:
             scene image "black"
             with fade
             r "As the game starts, Zarythe starts to walk back and forth before immediately approaching you with a jump and an aerial attack."
             r "he sudden change in the pacing of the fight gets you by surprise and now you start to feel pressurized."
             r " Zarythe is able to predict and punish almost all of your attacks while being unpredictable and erratic."
             r "No matter where you are in the field, it always feels like her Dio has total control of the fight, either with lasers and knifes at a distance."
             r "Or brutal combos when close."
             r "One weird thing you notice is the fact she's mainly only using one attack, a crouching jab."
             r "It may not seem deadly but it is able to start a devastating combo that can take away more than half of your health."
             r "If you plan to win this match, you must try to think outside-the-box and avoid creating patterns and take advantage of every mistake your opponent does."
             r "In fact, once you notice this, you start to hit much more attacks and the fight is much less frustrating."
             r "With Zarythe at 3/4 of the screen away from your character, you notice the start of the charge animation for Dio's laser. What do you do?"
             menu:
                 "Try to approach and jump over it":
                     r "There is no time to waste! Take this chance to get closer to your enemy and jump over the beam!"
                     "..."
                     r "You are too slow to do so and you end up getting hit in the air."
                     r "Not only that, once you tech the attack, you get hit with another laser."
                     jump endofzarfight
                 "Duck the projectiles":
                     $ zarythe_relationship =+1
                     r "After being hit multiple times by that projectile, you are fairly sure it's reach won't be able to hit you if you simply crouch down."
                     r "With your fingers crossed and hoping for the best......"
                     r "and it actually ends up working!"
                     r "Sadly, you weren't able to do anything else besides just avoiding the attack."
                     r "The fight proceeds normally."
                     jump endofzarfight
                 "Punish with 236aa" if main_Hol:
                     $ zarythe_relationship =+1
                     r "You decided to do Hol Horse's crouching variation of his 236AA."
                     r "That allowed you to both completely avoid Dio's laser while being able to take away a good chunk of health from Zarythe."
                     r "You feel proud of yourself for that punish."
                     jump endofzarfight

                 "Try to block it":
                     r "You start walking backwards to wait and block the attack. Despite this, you still get hit by the projectile and you realise it's a unblockable."
                     r "Even if your attempt to block Dio's laser was shameful, you at least learned something new."
                     jump endofzarfight

             label endofzarfight:
             $ renpy.movie_cutscene("knifeslater.mpeg")
             r "The match goes on and despite Zarythe not saying anything during all the time you have played, you feel like you managed to learn the game on your own just from playing against her."
             r "You feel your brain expanding a little bit, but after 40 minutes playing, you start to feel tired and you decide to stop playing."
             show image "zar"
             fightcadezar "I expected much worse from a stinko like you. It seems like you actually care for the game."
             fightcadeplayer "Aw, thanks!"
             fightcadezar "Aren't you that guy that got beaten by a Rubber in the last weekly?"
             fightcadeplayer "N-No..."
             fightcadezar "Whatever. If you are serious about getting good at the game, I could help you a bit sometimes."
             fightcadezar "I think there's a stinko tournament scheduled for today, why don't you try playing on that? You have a lot of potential."
             fightcadeplayer "A stinko?"
             fightcadeplayer "Wait a second... It's that thing I read from the #Stinko Countainment!"
             fightcadeplayer "There's one going to happen today!?"
             fightcadeplayer "Nice! Thanks for letting me know."
             fightcadezar "No biggie. GGs."
             hide image "zar"
             scene image "fightcade"
             with fade
             r "The game closes shortly after and Zarythe is already at the 'away from keyboard' list on Fightcade and Potatoboih is nowhere to be seen."
             r "More importantly, you feel like taking a break, otherwise you would break from such a heated battle."
             r "And what a better place to relax other than Discord?"
             jump headtogeneral1






         label sploogie_fight:
         stop music
         play music "splooogeschallenegtheme.mp3"
         ns "Screw it! I’ll challenge the one and only, SploogieMcNoodle."
         ns "I heard he’s one of the best players so I’m sure playing him will teach me a thing or two."
         r "You send her a challenge......"
         r "And she accepts!"
         scene image "choosebpol"
         with fade
         show image "sploog"
         fightcadesploogie "Huh, so you wanna challenge the Linguini himself?"
         fightcadesploogie "I admire that."
         fightcadesploogie "But it doesnt mean i'll hold back."
         fightcadeplayer "Well, I need training from a good player so--"
         play sound "bpolselectsound.wav"
         scene image "choosenbpol"
         with fade
         hide image "sploog"
         r "It seems as you were typing your messege sploogie chose black polnareff."
         stop sound
         mn "Huh, I thought he mained normal Polnareff?"
         mn "I'll have to play seriously if I want to learn the game."
         scene image "black"
         with fade
         if main_Pol == "True":
             r "The round starts and you go for Polnareff."
             r "You remember someone mentioning he was a good Polnareff player so you’re hoping he can teach you something."
             show image "sploog"
             fightcadesploogie "Polnareff huh?"
             fightcadesploogie "Lets see how much of him you know."
             hide image "sploog"
             r "As the game progresses, you find yourself basically mashing buttons since you haven’t ouched Polnareff before."
             r "But you’re slowly learning his moves and you start to understand that he has a long reach with some of his attacks."
             r "You keep getting perfected by Sploogie,being punished for your multi-attack move spam and bad jump ins."
             r "Soon enough a messege pops up on the bottom of the window."
             show image "sploog"
             fightcadesploogie "So he’s a charge character, but that doesn’t make him hard, once you learn the timing on the charge moves he becomes really easy to maneuver with."
             fightcadesploogie "Especially his 2 8C Shooting star special in stand-off, you can just throw that out."
             fightcadesploogie "Start by rolling and then holding C after shooting star comes out to force the opponent into a situation where they’re afraid to attack since the special move hits high."
             fightcadesploogie "And you can go for a low."
             fightcadeplayer "Oh, I didn’t know that! I’ll definitely start using it now."
             fightcadesploogie "Keep in mind that’s not all there is to him though, but you’ll get there little by little."
             hide image "sploog"
             r "After being told that you decide to try the move out and you notice that it is making Sploogie play more defensively."
             r "As the round goes on, Sploogie throws out his 214AA super and you’re standing in front of him. What do you do?"
             menu:
                 "Block the move and return to neutral":
                     $ sploogie_relationship +=1
                     r "You block the attack and return to neutral. Sploogie used 1 stock of meter so you have a slight advantage in the round now."
                     show image "sploog"
                     fightcadesploogie "Not the best play you could have gone with but good job either way."
                     jump endofsploooge2
                 "Move back and hit the stand at the end of its attack":
                     $ sploogie_relationship +=1
                     r "You move back while the attack is coming at you. However you were far away enough that you didn’t block it so you punish it with a heavy attack but it’s not a lot of damage."
                     show image "sploog"
                     fightcadesploogie "Nice punish, that’s how you’re supposed to do it."
                     jump endofsploooge2
                 "Block the move while buffering shooting star":
                     $ sploogie_relationship +=2
                     r "You block the attack."
                     r "After blocking you launch shooting star and roll towards Sploogie, putting him in a defensive situation."
                     r "You dash in with a low attack and release your shooting star. He fails to block your mixup and you win the round."
                     show image "sploog"
                     fightcadesploogie "Very nice, that’s exactly how you’re supposed to use the move! You’re slowly getting it!"
                     fightcadeplayer "Really? Nice."
                     jump endofsploooge2









         else:
             r "The match begins and you feel immediate pressure as Sploogie plays confidently."
             r "As the fight continues, you feel your attacks getting dodged and punished, as well as your jumping and air movement literally sliced."
             r "But even though you’re losing badly, with even some perfects in the mix, you feel like you’re understanding why and how he is beating your attacks."
             show image "sploog"
             fightcadesploogie "So you don’t want to do long attacks on B.Pol, he has good options in beating your slower normals as well as your jumps with his 214AA."
             fightcadesploogie "But once you get to higher level of play you will see how easy it is to beat B.Pol."
             fightcadeplayer "Okay, how should I initiate offense against B.Pol?"
             fightcadesploogie "Well most of his special moves are very long and easily punished by most supers in the game, and if blocked he’s negative on most of them."
             fightcadesploogie "Try to bait B.Pol into pressing buttons and doing long specials and try to capitalize on those with good punishes."
             fightcadeplayer "Alright got i-"
             r "The next round already started."
             r "As the round goes on, Sploogie throws out his 214AA super, you’re standing in front of him, what do you do?"
             hide image "sploog"
             menu:
                 "Block the move and return to neutral":
                     $ sploogie_relationship +=1
                     r "You block the attack and return to neutral. Sploogie used 1 stock of meter and it seems you have the advantage in the round now."
                     jump endofsploooge1

                 "Attempt to jump over it and punish":
                     r "Your jump gets caught in the attack and you lose a big chunk of your health"
                     show image "sploog"
                     fightcadesploogie "You should never attempt to jump this super as it’s air unblockable."
                     fightcadeplayer "Thats bullshit!"
                     fightcadesploogie "Try less complaining and more playing."
                     hide image "sploog"
                     jump endofsploooge1

                 "Move back and hit the stand at the end of its attack":
                     $ sploogie_relationship +=1
                     r "You move back while the attack is coming at you. However you were far away enough that you didn’t block it so you punish it with a heavy attack."
                     show image "sploog"
                     fightcadesploogie "Nice punish, that’s how you’re supposed to do it."
                     hide image "sploog"
                     fightcadeplayer "I think im starting to get the hang of this!"
                     jump endofsploooge1

                 "Move back and hit the stand with 236AA" if main_Ice:
                     r "You move back enough so the attack doesn’t hit you and you launch your super. It doesn’t connect and you lose your only stock of meter and are stuck in the animation long enough for Sploogie to start moving towards you."
                     show image "sploog"
                     fightcadesploogie "Nice try! That actually does work so try it again next time."
                     hide image "sploog"
                     jump endofsploooge1

                 "Try to teleport in front of him while avoiding the attack and punish" if main_DIO:
                     r "You try to teleport to avoid the attack but because your execution is still poor, you input the teleport too late and get caught in the attack."
                     show image "sploog"
                     fightcadesploogie "Haha, nice try! If only you were faster it would have worked."
                     hide image "sploog"
                     jump endofsploooge1


             label endofsploooge1:
             $ renpy.movie_cutscene("bpolloops.mpeg")
             r "The matches continue but you feel like after each lecture between matches you’re doing less and less mistakes and Sploogie isn’t doing perfects on you anymore."
             r "In fact some of the matches have come quite close when you really think about when to do what."
             show image "sploog"
             fightcadesploogie "Alright, GG’s, I’m off to go suck some toes. Catch you later."
             hide image "sploog"
             scene image "fightcade"
             with fade
             r "Before you even get to type GGs the match has closed and she’s nowhere to be seen on the Fightcade lobby anymore."
             r "You wonder what she meant by sucking toes but then you decide not to take that thought any further."
             r "Soon enough you head over to the discord server."
             jump headtogeneral1


             label endofsploooge2:
             $ renpy.movie_cutscene("bpolloops.mpeg")
             r "After a few more matches, Sploogie calls GG’s"
             show image "sploog"
             fightcadesploogie "All right, I’m done for now but you we’re definitely getting it there, if you keep that up you’ll catch me in no time. I’m always glad to see new Polnareff mains, he’s really not that hard. GGs!"
             hide image "sploog"
             scene image "fightcade"
             with fade
             r "The game closes and you’re left with a satisfied feeling."
             r "With nothing better to do you decide to check the discord server."
             jump headtogeneral1









         label headtogeneral1:
         scene image "general"
         with dissolve
         stop music
         play music "gonewiththewind.mp3"
         r "As you enter the server, you decide to check out what people are talking about in general."
         show image "zarythe.png"
         Z "And then everyone started spamming every channel."
         Z "Dude, it got so fucked, like, up to 2k people got bootybanged with pings on every channel."
         hide image "zarythe.png"
         ba "How did that even happen?"
         show image "mahjong"
         m "Yours truly."
         hide image "mahjong"
         show image "tex"
         tx "Don’t forget who gave you the mod rights."
         hide image "tex"
         show image "mahjong"
         m "Yeah, yeah. But I still did all of the work pal."
         hide image "mahjong"
         show image "zarythe.png"
         Z "You did, but after that everyone else joined in too."
         Z "I remember being in VC here with Sploogie and Soui just laughing our asses off as people started pouring in to the chats asking what the fuck happened."
         hide image "zarythe.png"
         show image "mahjong"
         m "That was great."
         hide image "mahjong"
         p2 "I ‘member."
         pokerwithbob "I ‘member."
         ns "What’s this about?"
         show image "zarythe.png"
         Z "Just talking about how the old HFTF server I moderated died before I made this one."
         ns "Wow, so you were involved even back then?"
         Z "Yep, I even hosted the first season of the weekly tournaments back then."
         Z "good times."
         hide image "zarythe.png"
         ns "That’s pretty cool."
         show image "Soui.png"
         So "It was dumb, you’re all dumb."
         hide image "Soui.png"
         show image "lucas"
         boi "I wish I’d been there for that."
         boi "it sounded epic."
         hide image "lucas"
         show image "Soui.png"
         So "You too Lucas, you’re super duper dumb. MEGA dumb."
         hide image "Soui.png"
         show image "lucas"
         boi "I love you too SouI."
         hide image "lucas"
         show image "Soui.png"
         So "Dumb."
         hide image "Soui.png"
         p2 "Lucas dumb? More like Zarydumb."
         raid "Barythe"
         show image "Soui.png"
         So "Barythe Dumbythe."
         hide image "Soui.png"
         pnt "@Zarythe have you deleted your existance yet?"
         show image "zarythe.png"
         Z "No, but I’ll delete yours soon."
         hide image "zarythe.png"
         pnt "fuck"
         show image "sploog"
         Sp "It sucks it had to go that way with Honk, I feel bad for him."
         hide image "sploog"
         dan "It is how it is."
         show image "zarythe.png"
         Z "Well, I’d like to think we did the right thing when making this server, although that mess might have been bit overkill."
         Z "By the way"
         Z "Sploog what are you doing?"
         hide image "zarythe.png"
         show image "sploogefood.jpg"
         Sp "linguini"
         hide image "sploogefood.jpg"
         show image "zarythe.png"
         Z "That’s the third time you’ve posted those in a week."
         hide image "zarythe.png"
         ns "They look like they taste super good though."
         show image "sploog"
         Sp "THEY DO!"
         Sp "See, this guy gets it unlike stinky ZAR!"
         hide image "sploog"
         chode "Who remembers that fanfic of Zarythe with that Acc guy?"
         ns "There’s a fanfic of Zarythe?"
         pnt "Oh yeah"
         pnt "fuck."
         chode "Someone should make more."
         show image "zarythe.png"
         Z "There actually are a few, I don’t know what it is about me that makes that happen."
         hide image "zarythe.png"
         chode "‘’This went on for several minutes as Accel began to speed up, shoving the penis deeper and deeper into his throat."
         chode "He was so experienced that he didn’t even gag once."
         chode "Zarythe was against the wall slightly thrusting his member inside of Accel’s deep throat, the rest of his body immobilized by pleasure."
         chode "As the blowjob went on. . .’’"
         marshkip "Now thats what I call a tandem facefuck."
         bd "This is my kind of stuff."
         show image "lucas"
         boi "Please stop."
         boi "Stop existing."
         hide image "lucas"
         ns "Jesus fuck..."
         chode "God, it just keeps on going..."
         chode "“‘Oh, but I will break you Zary-kun.’ Accel whispered as he began to chain Zarythe’s arms to the wall of the moderator dungeon.”"
         bd "I want to be in one of these."
         show image "zarythe.png"
         Z "HFTF server visual novel where every noteworthy member is a romanceable female."
         Z "Make it happen."
         hide image "zarythe.png"
         mino "Dating Zarythe? Count me in."
         neet "I’ll be the most boring character."
         mino "I’ll be the least likable"
         mino "Wait, nevermind, don’t put me in"
         mino "I have this weird feeling it’s already too late for that, isn’t it?"
         ns "Put me in as that one guy that has just one line."
         show image "lucas"
         boi "How would you even make a visual novel?"
         hide image "lucas"
         chode "With dedication."
         chode "And Renpy."
         hy "Be right back, time to do some advanced shitposting."
         mino "The only way to date Zar is to do the DIO bnb."
         iso "We should actually do this."
         chode "Please no."
         iso "Please yes."
         raid "Count me in."
         show image "ms"
         ms "Oh fuck."
         ms "Do it."
         ms "You have to."
         hide image "ms"
         mosin "Make Zarythe a furry girl!"
         show image "lucas"
         boi "No!"
         hide image "lucas"
         iso "We’re doing this."
         chode "ISO, don’t do this"
         iso "I have to"
         hy "I’m in."
         chode "Eh fuck it count me in too."
         mino "Oh fuck, they’re actually gonna do it."
         show image "mahjong"
         m "The madmen."
         hide image "mahjong"
         ns "You guys better actually do it."
         show image "zarythe.png"
         Z "Oh shit wait n-"
         hide image "zarythe.png"
         iso "Too late."
         camper "Make sure to make a Dyne route where if you fail with all the girls you end up with him."
         show image "ms"
         ms "I’ll fail on purpose."
         hide image "ms"
         dragonheart "You guys are fucked, get help."
         show image "mahjong"
         m "No one asked."
         hide image "mahjong"
         show image "zarythe.png"
         Z "I wanna date Sploogie."
         hide image "zarythe.png"
         show image "sploog"
         Sp "No you don’t."
         hide image "sploog"
         r "The conversation topic quickly changes back and forth."
         r "You’re having a hard time following along so you try to start your own topic."
         ns "What’s with these orange names, so many people have these."
         ns "Are there really that many twitch subs?"
         ns "I bet you’re rolling in cash Zarythe!"
         ns "How much do you make?"
         iamdarkendufrick "I know that he gets less from subs than donations."
         show image "mahjong"
         m "Zarythe should buy me some flowers with the tournament money."
         m "I never get flowers."
         m "@Zarythe buy me flowers with twitch money."
         hide image "mahjong"
         ns "Can I get some flowers too?"
         if zarythe_relationship >= 1:
                                       show image "zarythe.png"
                                       Z "I’ll think about it [povname]."
                                       hide image "zarythe.png"
                                       ns "Nice! Thanks for considering."
                                       r "The chat then starts talking about random things"
                                       r "Such as long stange math equations"
                                       r "and pictures of a man named sam hyde."
                                       r "Soon enough the conversation continues and switches topics constantly"
                                       r "You try to keep up but it’s no use."
                                       r "It looks like everyone is used to the fast chat speed and can keep up with the ever changing flow of the conversation."
                                       r "You give up and head over to fightcade for some matches."
                                       jump fightcadesearchforbitches





         elif zarythe_relationship >= 0:
                                    show image "zarythe.png"
                                    Z "Fat chance [povname]."
                                    Z "But Majongles sure."
                                    Z "if you come to Finland to get them."
                                    hide image "zarythe.png"
                                    show image "mahjong"
                                    m "I might actually."
                                    m "For the JoJo machine."
                                    hide image "mahjong"
                                    show image "zarythe.png"
                                    Z "As if."
                                    hide image "zarythe.png"
                                    show image "lucas"
                                    boi "What even is there to do in Finland?"
                                    hide image "lucas"
                                    show image "mahjong"
                                    m "Yeah what can I do there?"
                                    show image "ragebill"
                                    boomerusa "Nothing. Finland sucks."
                                    boomerusa "Just like Zarythe."
                                    hide image "ragebill"
                                    hide image "mahjong"
                                    dragonheart "Snow, thats all."
                                    show image "mahjong"
                                    m "What is there to do in Finland!? Is there even a Finland!?"
                                    m "@Zarythe @Zarythe @Zarythe."
                                    hide image "mahjong"
                                    show image "ragebill"
                                    boomerusa "Here’s a picture of what you can do in Finland"
                                    hide image "ragebill"
                                    show image "square-xxl.png"
                                    p2 "lmao"
                                    hide image "square-xxl.png"
                                    show image "zarythe.png"
                                    Z "Pretty much that."
                                    ns "I mean it can’t be that bad can it?"
                                    Z "It really can."
                                    hide image "zarythe.png"
                                    redpop "Anyone wanna play Mario 64 DS with me?"
                                    r "Soon enough the chat goes ape shit with diffrent topics every second."
                                    r "You give up trying to keep up with it all and decide to look for some matches on fightcade."
                                    jump fightcadesearchforbitches
         label fightcadesearchforbitches:
         stop music
         play music "fightcadedecideopponet.mp3"
         scene image "fightcade"
         with fade
         fightcadeplayerchat "Alright, I’m back again! Anyone wants some games?"
         r "Seems like it’s the prime time to be online on FightCade as almost everyone is here."
         r "You decide to challenge..."
         menu:
              "BiLL":
                jump geezerbattle

              "Tex Western":
                jump battleforramranch

              "Aleph":
                jump geomatrydashboi

              "Majongles":
                jump icetandemfuck

              "Potato":
                jump pokepornnigga


         label pokepornnigga:
         if zarythe_fight == "True":
             mn "Wait a second! Why is Potato on the lobby?"
             mn "Didn’t she have something to do?"
             mn "I remember she made me fight Zarythe instead..."
             fightcadeplayerchat "I thought you had to work Potato!"
             show image "potato"
             p "And I did."
             fightcadeplayerchat "Wait, what?"
             p "I’m home already."
             fightcadeplayerchat "Jesus how much time has passed?"
             p "A lot."
             fightcadeplayerchat "That’s so weird…"
             fightcadeplayerchat "Whatever! Do you want to play some rounds?"
             p "But I just said you should…"
             hide image "potato"
             jump fuckrenpypeiceofshit

         else:
             mn "Hey! It’s that nice lady I’ve met when I first got into the server!"
             mn "I think she’s really good at the game but it can’t hurt to try challenging her…"
             fightcadeplayerchat "Hi Potato! Wanna play?"
             show image "potato"
             p "Yo! Sure, let’s do it."
             fightcadeplayerchat "Huh?"
             fightcadeplayerchat "You're just going to accept my challenge like that?"
             fightcadeplayerchat "No resistance or shittalking me?"
             p "What do you mean?"
             p "Why would I do that?"
             fightcadeplayerchat "It’s just that every person I have challenged this far always talks shit."
             p "I don’t get it."
             fightcadeplayerchat "Well…"
             fightcadeplayerchat "Nevermind."
             hide image "potato"
             play music "characterselect.wav"
             scene image "choosemariah"
             with fade
             r "As the game starts up you notice potato going for what seems like mariah"
             scene image "choosenmariah"
             r "Which is whom she selects!"
             fightcadeplayer "Do you main Mariah?"
             show image "potato"
             fightcadepotato "Hmm, pretty much."
             fightcadepotato "I just kinda have a thing for her."
             fightcadeplayer "Oh, that’s cool!"
             fightcadeplayer "Wait a second… that’s weird."
             fightcadepotato "Yeah i guess."
             fightcadepotato "Who do you main [povname]?"
             fightcadeplayer "I’m a big boy, so I main [main]!"
             if main_DIO:
                 fightcadepotato "Oh…"
                 fightcadepotato "You know…"
                 fightcadepotato "He’s a bit hard to play."
                 fightcadepotato "Maybe you should switch characters until you get comfortable enough with the game?"
                 fightcadepotato "Just a friendly warning."
                 fightcadeplayer "Huh? Yeah, but he can’t be that hard to play, right?"
                 fightcadepotato "He can…"
                 fightcadeplayer "Nah! I’m better than you think!"
                 fightcadeplayer "i’ll get used to him in no time!"
                 fightcadepotato "Well if you say so."
                 fightcadepotato "Anyways let’s go."
                 jump fightwithpokenigshit




             elif main_Rubber:
                 fightcadepotato "Rubber, huh?"
                 fightcadeplayer "Hm? What about him?"
                 fightcadepotato "Oh, it’s nothing."
                 jump fightwithpokenigshit


             elif main_Mariah:
                 fightcadepotato "Hey! Good taste for waifus!"
                 fightcadeplayer "Thanks! I really like Mariah."
                 fightcadepotato "Me too! Too bad she’s such a bad character…"
                 fightcadeplayer "I never really understood why she’s bad. I just kinda started playing her without doing any research."
                 fightcadepotato "Man, if only she didn’t have such punishable attacks or overall just better damage or smaller hitboxes…"
                 fightcadeplayer "I guess."
                 fightcadepotato "She’s too dependant on her wires and without it, and at least some good levels, she can’t really do anything."
                 fightcadeplayer "Right…"
                 fightcadepotato "Maybe if she could use something else other than just 2A > 2A > 2A…"
                 fightcadeplayer "Uhh…"
                 fightcadepotato "The fact she’s pretty much powerless against a stand-on characters really messes up with her game…"
                 fightcadeplayer "…"
                 fightcadepotato "Having to use glitches to loop supers to deal good damage, even if they are banned from the competitive scene…"
                 fightcadeplayer "Ahem."
                 fightcadepotato "Oh. Where was I?"
                 fightcadeplayer "We were about to fight."
                 fightcadepotato "Right! Get ready!"
                 jump thotbattle

             else:
                 fightcadepotato "I dont know him too well, so I can’t really say a lot about [main]."
                 fightcadeplayer "It’s alright! You don’t need to be an expert with every character!"
                 fightcadepotato "Heh, I suppose."
                 fightcadepotato "But anyway, let’s fight!"
                 jump fightwithpokenigshit




         label fuckrenpypeiceofshit:
             r "After ignoring potato's dumb comment you send her a challenege and she promptly accepts."
             play music "characterselect.wav"
             scene image "choosemariah"
             r "After the game opens you notice potato moving to select mariah"
             scene image "choosenmariah"
             r "And to your suprise she actually does choose her!"
             fightcadeplayer "Wait, do you main Mariah or are you just messing with me?"
             show image "potato"
             fightcadepotato "Nah I really do play her."
             fightcadeplayer "Wait, isn’t she kinda crappy?"
             fightcadepotato "Sadly, yeah."
             fightcadeplayer "But I heard people saying you are really good!"
             fightcadeplayer "Some guy even said you managed to win a tourney with her! How’s that even possible?"
             fightcadepotato "I’m not even sure myself."
             fightcadepotato "I guess if you want to win with a low tier character you just need to put more effort into training."
             fightcadepotato "Atleast that’s what I did."
             fightcadeplayer "That’s amazing!"
             fightcadepotato "Heh. Now, pick a character."
             fightcadepotato "And let me show you the power of my Mariah."
             scene image "black"
             r "Upon noticing the fact you haven’t even selected a character yet, you quickly pick [main]."
             if main_DIO:
                 fightcadeplayer "Very Well, I’ll show you some tricks I’ve learned from Zarythe."
                 show image "potato"
                 fightcadepotato "That’s what I like to hear!"
                 hide image "potato"
                 jump fightwithpokenigshit


             if main_Rubber:
                 fightcadeplayer "Let’s see which character is more annoying."
                 show image "potato"
                 fightcadepotato "Ohh, you’ll see."
                 hide image "potato"
                 jump fightwithpokenigshit


             if main_Mariah:
                 fightcadeplayer "Little did you know…"
                 fightcadeplayer "But I also main Mariah!"
                 show image "potato"
                 fightcadepotato "Well, well, now that’s a surprise."
                 fightcadepotato "This is gonna be fun!"
                 hide image "potato"
                 jump thotbattle







             else:
                 fightcadeplayer "Let’s see what your Mariah can do against my [main]!"
                 show image "potato"
                 fightcadepotato "Heh."
                 hide image "potato"
                 jump fightwithpokenigshit




         label thotbattle:
            scene image "black"
            with fade
            play music "potatobattleshit.wav"
            r "After the match finally starts it doesn’t take long before the screen is filled with all sorts of different projectiles that range from knifes to electric wires."
            r "While this matchup might look simple to understand, it will not be a challenge easy to overcome as Potatoboih is much faster and efficient at spamming knifes."
            r "Her capacity of inputting quarter-circles is so impressive you start to wonder if that’s why she is one of the Tournament Hosts."
            fightcadeplayer "Damn! You're ruthless!"
            fightcadeplayer "I can’t even more with all this crap in the screen!"
            show image "potato"
            fightcadepotato "Welcome to Mariah Mirror’s."
            fightcadeplayer "Sounds like hell."
            fightcadepotato "Because it is hell."
            fightcadeplayer "Well how am I supposed to win then?"
            fightcadepotato "Heh it’s not that hard."
            fightcadepotato "If you want to beat me, just use your brain."
            fightcadeplayer "I’m trying!"
            fightcadepotato "Try harder."
            hide image "potato"
            r "With those words in mind you start thinking of multiple plans to defeat her Mariah using your's."
            $ renpy.movie_cutscene("7annoyingroundslater.webm")
            r "You start to get an understanding of the match up after many losses."
            mn "Okay, I think I got this!"
            mn "If Mariah is a character focused on controlling the field and fighting from a distance, then that means…"
            brain "If I want to win i'll have to…"
            menu:
                "Go on the offensive":
                    $ potatoboi_relationship +=1
                    r "Tired of standing in the other side of the screen spamming knives and forks, you decided to play Mariah like a rushdown character."
                    r "The idea would be to be so overwhelming that potato wont be able to breathe!"
                    r "However that might have not been the best idea, since you couldn’t even manage to get close to Potatoboih like you planned."
                    show image "potato"
                    fightcadepotato "Really?"
                    fightcadepotato "Was that the best you could come up with?"
                    fightcadeplayer "Yeah…"
                    fightcadepotato "Geez, that was pretty dumb."
                    fightcadepotato "But I’ll let that slide since you're new to the game and all that."
                    fightcadepotato "Plus it’s a Mariah Mirror, not a lot of people know about this matchup."
                    fightcadepotato "You'll get better with time."
                    fightcadeplayer "Alright!"
                    hide image "potato"
                    jump endofmariahmirror







                "Spam even more":
                    $ potatoboi_relationship +=2
                    r "Taking advantage of your huge brain you decide that the best course of action to be taken was to input the half circle faster."
                    r "And for some mysterious reason this ends up working and you manage to get a few hits in and control Potato's spacing!"
                    r "However this is still not enough to win the fight, since seconds later you are back to getting knocked down and eating wires."
                    show image "potato"
                    fightcadepotato "Well, that’s how you do it."
                    fightcadepotato "Mariah’s mirrors are all about who spams first."
                    fightcadepotato "But you have to put more effort into it."
                    fightcadeplayer "Got it!"
                    hide image "potato"
                    jump endofmariahmirror




                "Use my secret technique":
                    $ potatoboi_relationship +=1
                    r "Upon noticing that you suck, you decided to use your secret technique to win this fight."
                    r "Yes your last resort weapon, something that should only be used in times of emergency..."
                    r "Taking advantage of your huge amounts of meter, you successfully approach Potatoboih and hit your 214AA super!"
                    r "And again."
                    r "And again."
                    r "And again"
                    r "You end up looping your special until the match is over."
                    show image "potato"
                    fightcadepotato "Seriously man?"
                    fightcadepotato "That was super clever!"
                    fightcadepotato "I didn’t know you knew that loop."
                    fightcadeplayer "Uh…"
                    fightcadepotato "I’m genuinely happy you did that, especially from a newbie it’s a rare sight to see."
                    fightcadeplayer "Oh, really!?"
                    fightcadepotato "Yeah but don’t use that ever again."
                    fightcadepotato "It’s pretty rude."
                    fightcadeplayer "I'll try."
                    hide image "potato"
                    jump endofmariahmirror


         label endofmariahmirror:
         $ renpy.movie_cutscene("420minutesxd.webm")
         r "After a while you end up having a conversation with potato about doom wads"
         play sound "discordsound.ogg"
         r "But unfortunatly it was cut short due to a discord ping."
         fightcadeplayer "Anyways GGs!"
         fightcadepotato "Heh."
         fightcadepotato "keep on training."
         fightcadepotato "You have potential"
         fightcadepotato "Ggs"
         hide image "potato"
         scene image "fightcade"
         with fade
         play music "fightcadedecideopponet.mp3"
         r "The game closes and Potatoboih vanishes from the player list."
         r "With no time to waste, you decided to check that ping from Discord."
         jump stinkotourneyannouncement









         label fightwithpokenigshit:
            hide image "potato"
            scene image "black"
            play music "potatobattleshit.wav"
            r "Something immediately felt…wrong."
            r "Mariah is known as the worst character in the game, so how is Potatoboih making her look good?!"
            fightcadeplayer "Hey! You play a pretty good Mariah, huh?"
            show image "potato"
            fightcadepotato "Yup!"
            fightcadeplayer "I can sort of see how you won a tournament now…"
            fightcadeplayer "But how can you play with such a bad character?"
            fightcadepotato "My love for my waifu is stronger than any tier list!"
            hide image "potato"
            fightcadeplayer "That’s…"
            fightcadeplayer "strange to say the least."
            r "The next game starts and you harden your resolve. You will win!"
            r "Immediately Potato throws some wires up in the air to apply pressure and approaches you, dropping sockets and fishing for a knockdown."
            r "If you want to win this match, you'll have to play seriously and leave her any space to breathe!"
            r "…But of course this not an easy task."
            r "Potato quickly reminds you why she’s got the role of a “gameknowledgeboy” with her astounding knowledge about the game."
            fightcadeplayer "Man, this is bullshit…"
            fightcadeplayer "How can you know exactly what I’m going to do and have the perfect counter for my techniques?"
            show image "potato"
            fightcadepotato "I’m just really experienced, I guess."
            fightcadeplayer "For how long have you even been playing?"
            fightcadepotato "A pretty good amount of time, actually."
            fightcadepotato "Like, 1000 hours or something?"
            fightcadeplayer "Wow! That’s impressive!"
            fightcadepotato "I suppose it is."
            hide image "potato"
            $ renpy.movie_cutscene("7annoyingroundslater.webm")
            play music "potatosongattheshit.wav"
            r "After a few more matches you start getting tired from the game."
            r "You didn’t have a lot of success at beating Potatoboih, but you managed to win one or two rounds."
            fightcadeplayer "Alright! I’m tired! Let’s stop here for today!"
            show image "potato"
            fightcadepotato "Okay. GGs."
            fightcadeplayer "Guess it will take me a while until I manage to beat your hours, huh?"
            fightcadeplayer "How did you even get that many time?"
            fightcadeplayer "Do you even play other games!?"
            fightcadepotato "Sometimes I play some other games here and there, but JoJo’s my bread and butter."
            fightcadepotato "And what about you? Do you play anything else?"
            menu:
                "I play a lot of games!":
                    $ potatoboi_relationship +=0
                    fightcadeplayer "Yeah! I’m a Pro-Gamer! I play all sort of stuff!"
                    fightcadepotato "Huh? Really? That’s cool."
                    fightcadepotato "Have you played Doom by any chance?"
                    fightcadeplayer "I…"
                    fightcadeplayer "Uh…"
                    fightcadeplayer "I don’t think… I’ve ever heard about that game."
                    fightcadepotato "Oh, that’s a shame."
                    fightcadepotato "It’s a good game, you should play it."
                    fightcadeplayer "I see…"
                    jump interuptedbypingman


                "Not really.":
                    $ potatoboi_relationship +=1
                    fightcadeplayer "No, I don’t really play a lot of games…."
                    fightcadepotato "Focusing all of your energy on HFTF only? That’s dedication!"
                    fightcadeplayer "Y-You think so?"
                    fightcadeplayer "I mean, yeah! How am I going to remember my sick combos if I spend my free time playing other silly games?"
                    fightcadepotato "You are an interesting one."
                    fightcadepotato "Most stinkos just join the server for the memes and dumb stuff."
                    fightcadepotato "But you are really trying to get good. That’s amazing."
                    fightcadeplayer "Thanks!"
                    jump interuptedbypingman



                "Shooters are just my thing!" if main_Hol:
                    $ potatoboi_relationship +=0
                    fightcadeplayer "Out of JoJo, I play all sort of shooters!"
                    fightcadepotato "Oh, I see."
                    fightcadepotato "That’s cool, that’s cool…"
                    jump interuptedbypingman


         label interuptedbypingman:
         play sound "discordsound.ogg"
         r "Suddenly a ping from Discord pops up, cutting your conversation short."
         show image "potato"
         fightcadeplayer "Anyways GGs!"
         fightcadepotato "Heh."
         fightcadepotato "keep on training."
         fightcadepotato "You have potential"
         fightcadepotato "Ggs"
         hide image "potato"
         scene image "fightcade"
         with fade
         play music "fightcadedecideopponet.mp3"
         r "The game closes and Potatoboih vanishes from the player list."
         r "With no time to waste, you decided to check that ping from Discord."
         jump stinkotourneyannouncement







         label icetandemfuck:
         if majongles_fight == "True":
             fightcadeplayerchat "Hey Majongles! Remember me?"
             show image "mahjong"
             m "Not really. What do you want?"
             fightcadeplayerchat "I just wanted to know if you're up for a fight."
             m "I suppose I can play with you a little."
             fightcadeplayerchat "Sweet!"
             hide image "mahjong"
             jump thejewsdid911



         else:
             fightcadeplayerchat "You’re Majongles right? I’ve heard some players talking about you, you must be good right?"
             show image "mahjong"
             m "I’m the best in Europe kid, my Ice will be your death."
             fightcadeplayerchat "Cool!"
             fightcadeplayerchat "Uhm. I mean. . ."
             fightcadeplayerchat "Nevermind, let’s fight already."
             m "Hmph."
             hide image "mahjong"
             jump thejewsdid911



         label thejewsdid911:
         scene image "chooseice"
         with fade
         play music "characterselect.wav"
         r "With the game now open, you hum along to the game’s jingle as you pick your character."
         scene image "choosenice"
         r "Majongles meanders to Ice and you naturally pick [main]."
         scene image "black"
         show image "mahjong"
         if main_Ice:
             fightcademahjong "Dittos huh? Let’s go."
             mn "Gotta fight fire with fire."
             mn "Or Ice with Ice. . ."
             fightcadeplayer "Huh."
             jump icemirrorstuff


         elif main_Hol:
             fightcademahjong "Hol horse?"
             fightcademahjong "Hah! I know all his tricks."
             fightcadeplayer "Really? I guess I’m screwed then."
             fightcademahjong "You won’t even stand a chance."
             jump battleofbucharest


         else:
             fightcademahjong "Prepare yourself for a world of pain."
             fightcadeplayer "Hey! I was about to say that!"
             fightcademahjong "Too late, kid."
             fightcadeplayer "I’m not a kid, i’ll show you what i can do!"
             jump battleofbucharest


         label icemirrorstuff:
         play music "mahjongsbattletheme.mp3"
         hide image "mahjong"
         scene image "black"
         with fade
         r "The round barely starts before Majongles is vored by Cream."
         r "Unable to think for yourself, you do the same to increase your chances of winning."
         r "The match feels like a fencing fight since you're trying to hit Ice from afar without getting hit yourself."
         r "Upon trying to play with your stand-off, you end up getting all of your rolls punished and out-spaced by Majongles."
         r "The fight stays the same bait-’n-poke thing when all of a sudden she dashes off the ground with ludicrous speed, hitting you and following up with a devastating combo."
         fightcadeplayer "What the hell was that thing!?"
         show image "mahjong"
         fightcademahjong "It’s my sperg killing secret technique."
         fightcadeplayer "Really?"
         fightcademahjong "No, you retard."
         fightcademahjong "That’s Ice’s IAD."
         fightcadeplayer "IAD…?"
         fightcadeplayer "Wait a second…"
         mn "I heard something about that while I was stalking the guides and training channel! It's...."
         mn "when you dash in the air and attack right after leaving the ground with VERY fast incredible high speed, right?"
         mn "There’s gotta be a way to counter it! But… how?"
         fightcademahjong "Are you just going to stand there?"
         fightcadeplayer "Oh, sorry, I was just thinking about how to beat your ass."
         fightcademahjong "Whatever."
         hide image "mahjong"
         r "Upon noticing your inability to counter his antics, Majongles proceeds to abuse Ice’s IAD."
         r "While this ends up costing you some rounds, it only gave you more time to study the move."
         mn "Ok I think I got this! Next time she uses that dumb move, I'll…"
         menu:
             "RUN":
                  $ majongles_relationship +=2
                  r "And so, right as spot Ice leaving the ground you start dashing backwards, hoping the attack would avoid you completely."
                  r "Surprisingly this actually works!"
                  r "However, you feel like something is fishy…"
                  show image "mahjong"
                  fightcademahjong "Really?"
                  fightcadeplayer "Yes!"
                  fightcademahjong "What a pussy."
                  fightcademahjong "But I will give you some credits."
                  fightcademahjong "Since you can’t defeat me, might as well just run away."
                  hide image "mahjong"
                  r "After those few words round 2 starts."
                  jump endoficemirror


             "Punish with 623 AA":
                   $ majongles_relationship +=1
                   r "Right as Majongle’s Ice approaches your Ice you quickly input your 623 AA super, which ends up hitting her and dealing huge damage."
                   show image "mahjong"
                   fightcademahjong "WHAT THE FUCK."
                   fightcadeplayer "Ha! Take that!"
                   fightcademahjong "Shut up."
                   fightcadeplayer "What was that? I thought I heard you say something."
                   fightcademahjong "Shut the fuck up already."
                   fightcademahjong "That was a one time mistake faggot."
                   fightcadeplayer "You don't have to be a dick about it"
                   fightcademahjong "Yeah whatever mutt."
                   hide image "mahjong"
                   r "And so after those words were spoken, round 2 starts"
                   jump endoficemirror

             "Stay put and not do anything":
                   $ majongles_relationship +=1
                   r "For some reason, you decided the best choice to be made in this situation was to just stay put and do absolutely nothing."
                   r "As you might have expected, Majongles goes full-force on you."
                   show image "mahjong"
                   fightcademahjong "Still thinking?"
                   fightcadeplayer "Not really."
                   fightcademahjong "Good then I'll just keep on going."
                   fightcademahjong "Your loss pal."
                   hide image "mahjong"
                   r "And with those words round 2 starts"
                   jump endoficemirror

         label endoficemirror:
         $ renpy.movie_cutscene("standontaunts.webm")
         r "After playing for 5 minutes Majongles decided she had enough of your tomfoolery."
         show image "mahjong"
         fightcademahjong "Enough for today."
         fightcademahjong "Your Ice is trash."
         fightcadeplayer "Aw, thank you!"
         fightcadeplayer "Wait, what?"
         fightcademahjong "Your ice is garbage."
         fightcademahjong "Challenge me when you get better."
         hide image "mahjong"
         fightcadeplayer "Got it!"
         scene image "fightcade"
         with fade
         play music "fightcadedecideopponet.mp3"
         r "Mere seconds after sending your message, the game closes."
         play sound "discordsound.ogg"
         r "It seems like you have also gotten a ping from Discord."
         stop sound
         mn "Better check that out."
         jump stinkotourneyannouncement



         label battleofbucharest:
         play music "mahjongsbattletheme.mp3"
         hide image "mahjong"
         scene image "black"
         with fade
         r "The best Ice in Europe?"
         r "Yeah, that was a fairly apt description as you soon realise Ice hits so hard you’re surprised your body isn’t hurting in real life."
         r "Every time you try to approach he turns into a ball, smacks you or slaps your ass with his grab."
         r "You swear you could hear heavy mashing all the way from Romania every time Majongles got you with a Tandem."
         fightcadeplayer "C’mooooon, let me play the game!"
         show image "mahjong"
         fightcademahjong "Hahahahahaha, learn how to block, pal."
         hide image "mahjong"
         r "Majongles sweeps you and then manages to catch you with Cream as you get up."
         r "She combos a few light jabs into a downwards punch."
         show image "mahjong"
         fightcademahjong "FUCK."
         fightcadeplayer "Did you mess up a combo?"
         fightcademahjong ".........."
         hide image "mahjong"
         r "It seems Majongles is too busy attacking you to respond."
         r "A few rounds pass with no real counter-attack from you."
         r "Then you start to notice your chance as Majongles has hopped into the ball and is heading your way."
         r "You feel you’ve seen this enough times that you can respond correctly. What do you do?"
         menu:
             "Try to block the ball":
                 r "Didn’t some general say the best offense is a good defence?"
                 r "Hopefully he was right."
                 r "But you soon remeber the ball can cross-up."
                 r "At least you’ll know for your next try..."
                 jump mahjongsarc


             "Super the ball as a punish":
                 $ majongles_relationship +=1
                 r "You learned this trick in #guides-and-training, supers can punish!"
                 r "You successfully counter her strategy!"
                 r "Majongles is thrown back and suffers from massive damage!"
                 r "Unfortunately for you, she slides into with a dashing slap and it feels like that about evened up the damage."
                 jump mahjongsarc

             "Use an aerial attack":
                 r "The most obvious option is to duke it out fair and square."
                 r "You prepare an aerial attack but you time it wrong, or the spacing is wrong or any number of other things is wrong and the ball slams into you."
                 r "Quick thinking from Majongles converts this into a second ball putting you in the corner where the deal is sealed with a 623AA super."
                 jump mahjongsarc





         label mahjongsarc:
         $ renpy.movie_cutscene("standontaunts.webm")
         r "Sadly, you don't do any better in the next few rounds."
         r "In fact it seems you only keeps getting worse."
         r "You start to get suspicious of Majongle's skill, questioning if he's really that good or if you're really that bad."
         fightcadeplayer "Man that’s enough for today. . ."
         show image "mahjong"
         fightcademahjong "Giving up already? I was just getting started."
         fightcadeplayer "I don’t think I can keep up with you anymore."
         fightcademahjong "Hmph. I will admit you gave me a bit of trouble but you are still far from defeating me."
         fightcademahjong "Feel free to challenge me again any time."
         fightcadeplayer "Alright! GGs."
         fightcademahjong "GGs."
         hide image "mahjong"
         scene image "fightcade"
         with fade
         play music "fightcadedecideopponet.mp3"
         r "And once again the game closes, bringing an end to another fight."
         play sound "discordsound.ogg"
         r "Right after a notification from Discord catches your attention."
         stop sound
         r "With nothing better to do, you decided to check that out."
         jump stinkotourneyannouncement






         label geomatrydashboi:
         if aleph_fight == "True":
             fightcadeplayerchat "Hey aleph!"
             show image "alph"
             a "What do you want [povname]"
             fightcadeplayerchat "I was hoping i could play you for a little bit"
             a "Fine, what ever just send me the challenege."
             fightcadeplayerchat "Alright!"
             hide image "alph"
             scene image "choosedevo"
             with fade
             play music "characterselect.wav"
             r "The game opens and aleph goes to devo."
             scene image "choosendevo"
             r "Selecting him in an instant"
             show image "alph"
             fightcadealeph "So tell me [povname], who have you decided to main?"
             fightcadeplayer "[main]!"



             if main_DIO:
                 fightcadealeph "What did I tell you?"
                 fightcadeplayer "You told me to… send the challenge?"
                 fightcadealeph "Before that."
                 fightcadeplayer "That I should settle down with one character? But that’s what I did! I’m maining Dio!"
                 fightcadealeph "No, no, no. Fast-forward a little."
                 fightcadeplayer "Where are you trying to get at?"
                 fightcadealeph "Didn't I tell you to not main DIO?"
                 fightcadeplayer "Yeah, you did…"
                 fightcadealeph "Are you just going to ignore my advice like that? Kids these days…"
                 fightcadeplayer "But why can’t I main Dio?"
                 fightcadealeph "Because you have potatoes for fingers."
                 fightcadealeph "Get ready to feel my wrath. I shall eliminate fools like you."
                 fightcadeplayer "Huh…"
                 fightcadeplayer "Very well. I will show you what my Dio can do!"
                 jump phillipinoboibattle

             elif main_Hol:
                 fightcadealeph "Shame. You had so many good characters to pick, yet you select the one everyone uses."
                 fightcadeplayer "But I like Hol Horse! He’s fun and easy to play!"
                 fightcadealeph "Shameful."
                 fightcadealeph "That’s why no one loves you."
                 fightcadealeph "Stinker."
                 fightcadeplayer "That’s mean!"
                 fightcadealeph "I know. I hope you feel ashamed of yourself."
                 fightcadeplayer "Let’s just fight already."
                 jump phillipinoboibattle

             elif main_Devo:
                 fightcadealeph "I thought I told you to not main Devo."
                 fightcadeplayer "But he’s so unique and handsome…"
                 fightcadealeph "I know, that’s why I main him."
                 fightcadeplayer "Huh?"
                 fightcadealeph "Look, you are not gonna get far with him, trust me."
                 fightcadealeph "It’s best that you just give it up and pick another character."
                 fightcadeplayer "But…"
                 fightcadealeph "But like I promised, I will share some Devo secret stuff with you."
                 fightcadealeph "You must keep your mouth shut though."
                 fightcadealeph "It’s super secret stuff."
                 fightcadeplayer "Right!"
                 fightcadealeph "But not now. After I kick your ass."
                 fightcadeplayer "We'll see about that!"
                 jump phillipinoboibattle

             elif main_Mariah:
                 fightcadealeph "I wasn’t expecting you to be this dumb."
                 fightcadeplayer "What?"
                 fightcadealeph "Mariah, seriously?"
                 fightcadealeph "I know she’s a top tier waifu, but she’s absolute trash."
                 fightcadeplayer "Hey! Don’t talk to her like that! She’s special, okay?"
                 fightcadealeph "Special my ass."
                 fightcadealeph "Prepare for hell if you are maining her."
                 fightcadeplayer "uh oh..."
                 jump phillipinoboibattle

             else:
                 fightcadealeph "Boooooooring."
                 fightcadeplayer "What’s boring?"
                 fightcadealeph "You. You are boring. Your character is boring. This game is boring."
                 fightcadeplayer "What do you have against [main]?"
                 fightcadealeph "He’s boring."
                 fightcadeplayer "I get that part already, but why exactly do you dislike him?"
                 fightcadealeph "I never said I disliked him."
                 fightcadeplayer "You just did."
                 fightcadealeph "I didn’t."
                 fightcadeplayer "But…"
                 fightcadealeph "No buts, let’s fight already."
                 fightcadeplayer "..."
                 jump phillipinoboibattle

         else:
             mn "Huh, I don’t think I've ever seen Aleph playing the game"
             mn "What does this chick do all-day anyways?"
             mn "She’s always taking care of that palmod channel though. . ."
             mn "That means she can’t be good at the game, right? It’s an easy win!"
             fightcadeplayerchat "Hey Aleph! Wanna play a b--"
             play sound "challengenosie.wav"
             show image "wew"
             r "Before you can even finish typing your message, Aleph challenges you out of nowhere."
             stop sound
             r "Does she just keeps challenging random people on the lobby all the time?"
             fightcadeplayerchat "Huh? What's up with the random challenge?"
             show image "alph"
             a "You are here to play, aren't you?"
             fightcadeplayerchat "Well, yeah."
             a "Then just accept it already, weirdo."
             fightcadeplayerchat "You're the weirdo here."
             fightcadeplayerchat "You know what?"
             fightcadeplayerchat "Fine."
             a "Whats wrong?"
             a "Scared of my big brain?"
             a "It's fine, most people do that."
             fightcadeplayerchat "What are you even. . ."
             r "You giving up at attempting to understand Aleph and you quickly accept her challenge and get ready for an easy win."
             r "Did all those bad palmods made her crazy?"
             scene image "choosedevo"
             with fade
             r "Now is not the time to think about that."
             play music "characterselect.wav"
             r "The game opens and aleph goes to devo."
             scene image "choosendevo"
             r "Seeing that your opponent has already picked a character, you decided to pick your trusty [main]."
             show image "alph"


             if main_DIO:
                 fightcadealeph "Dio, huh? Seems like I have underestimated you."
                 fightcadeplayer "Heh, you think so?"
                 fightcadealeph "Or maybe you are just an idiot that wants to timestop."
                 fightcadeplayer "Oh."
                 jump phillipinoboibattle
             elif main_Hol:
                 fightcadealeph "Seriously? Another Hol Horse? Lame."
                 fightcadeplayer "Hey, I can play whomever I want."
                 fightcadealeph "No, you don't. You have to play the character I like."
                 fightcadeplayer "Why?"
                 fightcadealeph "Because that's how it works."
                 fightcadeplayer "What works?"
                 fightcadealeph "The universe."
                 fightcadeplayer "What does that have to do with anything?"
                 fightcadealeph "Everything."
                 fightcadeplayer ". . ."
                 fightcadeplayer "I see."
                 jump phillipinoboibattle
             elif main_Devo:
                 fightcadealeph "Finally, a fucking smart player."
                 fightcadeplayer "Huh?"
                 fightcadealeph "We need more Devo players in this world."
                 fightcadealeph "Or maybe we don't."
                 fightcadealeph "Yeah, we don't. Devo is too hard to anyone but me."
                 fightcadealeph "There can only be one remaining. Brace yourself."
                 fightcadeplayer "I just want to play the game. . ."
                 jump devomirrorshit
             elif main_Mariah:
                 fightcadealeph "Mariah? Pathetic."
                 fightcadeplayer "What do you have against Mariah?"
                 fightcadealeph "Nothing, but how to you plan on beating me with the worst character of the game?"
                 fightcadeplayer "With. . . skill?"
                 fightcadealeph "Good joke, man. I'll absolutely destroy you."
                 fightcadeplayer "Hey, it's not like your character is that high on the tier list either."
                 fightcadealeph "Yeah, whatever."
                 jump phillipinoboibattle
             else:
                 fightcadealeph "Good luck trying to beat me with that loser."
                 fightcadeplayer "Why are you so confident?"
                 fightcadealeph "Because you suck, and I don’t."
                 fightcadeplayer "That’s rude, Aleph!"
                 fightcadealeph "Yeah, who cares?"
                 fightcadeplayer "I do!"
                 fightcadealeph "You are a nobody, so it doesn’t count."
                 fightcadeplayer "That’s also rude!"
                 fightcadealeph "Let’s fight already."
                 jump phillipinoboibattle

         label devomirrorshit:
         r "Sorry player but because our writers take fucking forever to write this devo mirror is empty"
         r "We'll make sure to comeback and fill this part soon."
         jump boringmirrorshit


         label phillipinoboibattle:
         play music "alephbattletheme.mp3"
         hide image "alph"
         scene image "black"
         with fade
         r "And as the round begins, Aleph quickly crawls into your direction with full force."
         r "Her Devo combines the strength of a kaffir with the sheer speed of his puppet, being able to string attacks in a quick succession."
         r "This is making you feel like you're fighting two character at once."
         r "All of a sudden, you find yourself trapped between both characters, where Aleph takes the chance to start a deadly combo that slowly but surely manages to take away more than half of your health."
         r "If you want to overcome this massive challenge, you will have to adapt to the correct mindset."
         r "What will you do?"
         menu:
             "Be more aggressive.":
                 mn "Aleph is playing way too much on the offensive side, I can’t let her do that!"
                 mn "If she’s not giving space to breathe then I'll just have to do the same with her!"
                 mn "Maybe if I start going for more mix ups, I can force her to go on the defensive!"
                 show image "alph"
                 fightcadealeph "I don’t think you can outplay me like that."
                 fightcadeplayer "Huh? What?"
                 fightcadealeph "You were thinking about that right now, weren’t you?"
                 fightcadeplayer "How did you know!?"
                 fightcadealeph "You are just way too easy to read."
                 fightcadeplayer "But how will I be able to beat you then?"
                 fightcadealeph "I don’t know. Good luck."
                 fightcadealeph "Now that I think about it, I shouldn’t be wishing you good luck."
                 fightcadealeph "It would be a shame if I lost."
                 fightcadealeph "In that case, you are doomed."
                 hide image "alph"
                 fightcadeplayer "Crap…"
                 r "Despite Aleph’s warnings, you still attempt to pressure her Devo into switching to a more defensive style."
                 r "Needless to say, this strategy fails miserably."
                 r "The fact she can control the field from practically anywhere she wants with a well placed Ebony Devil halts all your progress with advancing on Devo."
                 r "And to top it all off her execution is on point."
                 r "Very rarely does she up her combos, something comparable to the people that make silly ‘combo showcase’ videos on Youtube."
                 jump boringmirrorshit



             "Focus on punishing moves.":
                 $ aleph_relationship +=1
                 mn "Aleph might have the best execution I've ever seen, but that doesn’t mean her strategy is flawless."
                 mn "I'll have to take advantage of every mistake and wrong decision she makes."
                 mn "If I can’t beat this chick in the button-pressing game, I will have to increase my IQ beyond dimensions and beat her in mind-games!"
                 show image "alph"
                 fightcadealeph "Are you just going to stand there and get beaten to death like that?"
                 fightcadeplayer "Not anymore! I’m determined to win this game!"
                 fightcadealeph "So, that was just warm-up for you?"
                 fightcadeplayer "Y-Yeah! You better watch yourself now!"
                 fightcadealeph "Good, I was getting bored here."
                 fightcadealeph "Let’s see what you are really capable of."
                 hide image "alph"
                 r "The round starts and your eyes are fixed to Aleph’s movements."
                 r "Gathering all the information you have acquired from the last match your brain starts expanding and your IQ reaches new dimensions."
                 r "You start to have a easier time reading Aleph and predicting her next moves."
                 r "You avoid standing between the kaffir and doll, grab him when he tries to roll, and punish his missed supers and land some well timed hits."
                 r "Soon enough you actually manage to win an entire match!"
                 show image "alph"
                 fightcadealeph "Huh. Wasn’t expecting that."
                 fightcadealeph "Maybe you are more than meets the eye."
                 fightcadealeph "Maybe now I could start playing more seriously."
                 fightcadeplayer "Wait, I thought that was all you could do!"
                 fightcadealeph "Not even close."
                 fightcadeplayer "Jesus how long have you been playing?"
                 fightcadeplayer "Are you some kind of hermit?"
                 fightcadealeph "I wish I was."
                 hide image "alph"
                 jump boringmirrorshit

             "Play more defensively.":
                 mn "I can’t keep up with Aleph’s speed…"
                 mn "She’s just way too fast and precise!"
                 mn "But maybe if I tried being more defensive, I could maybe have a chance!"
                 mn "I mean, he can’t win if he can’t hit me right?"
                 show image "alph"
                 fightcadeplayer "Right!?"
                 fightcadealeph "Left."
                 fightcadeplayer "Yeah! No, wait a second!"
                 fightcadeplayer "Sorry, I’m just thinking out loud."
                 fightcadealeph "Weirdo."
                 fightcadealeph "Who even thinks while playing this game?"
                 fightcadealeph "That’s stupid."
                 fightcadeplayer "It’s not stupid!"
                 fightcadeplayer "How am i supposed to beat you without thinking?"
                 fightcadealeph "I mean Zarythe can do it but... good point."
                 fightcadealeph "Still stupid."
                 fightcadeplayer "Yeah, whatever! I’ll beat your ass!"
                 hide image "alph"
                 r "With your genius plan in mind, you start blocking."
                 r "Push-blocking, rolling and guard-canceling became your best friends."
                 r "Aleph couldn’t stand a chance to your impenetrable wall of defense!"
                 r "Or at least that was the case for about three seconds before you couldn’t keep up with overheads coming from both directions and surprise grabs from the puppet."
                 r "It seems like the immovable object had encountered the unstoppable force, and the results weren’t very pleasing."
                 jump boringmirrorshit


         label boringmirrorshit:
         $ renpy.movie_cutscene("2hoursl8tr.webm")
         r "As usual, you both play for a long time before the game gets stale and boring."
         r "But even then, you managed to win at least a few matches which is already more than enough to give you a sense of accomplishment and triumph."
         show image "alph"
         fightcadealeph "I’ve had enough of this."
         fightcadealeph "GGs."
         fightcadeplayer "What? What do you mean?"
         fightcadealeph  "You aren’t a complete waste of time, but you still have a long way to go before I can actually find some challenge in fighting you."
         fightcadealeph "You get me?"
         fightcadeplayer  "More or less…"
         fightcadealeph "My point is: You kinda suck, but you can get better."
         fightcadeplayer "Yeah, I’ve been told that before."
         fightcadealeph  "Good, so get to work."
         hide image "alph"
         fightcadeplayer "Alright! GGs!"
         stop music
         play music "fightcadedecideopponet.mp3"
         scene image "fightcade"
         with fade
         play music "fightcadedecideopponet.mp3"
         r "The game closes and once again you are left at the game’s Fightcade lobby."
         play sound "discordsound.ogg"
         r "With no mentally challenged people in the chat to make fun about, you recieve a ping from Discord and decide that it would be better to check that out."
         stop sound
         jump stinkotourneyannouncement











         label battleforramranch:

         if main_Hol:
                         fightcadeplayerchat "Yo tex"
                         show image "tex"
                         tx "Oh hey [povname]. Whats up?"
                         fightcadeplayerchat "Not much."
                         fightcadeplayerchat "I was just wondering if we could do some hol mirror matches."
                         tx "Mirror matches?"
                         tx "Sure sounds good."
                         r "And with those words spoken you send tex a challenge....."
                         r "And she accepts!"
                         jump holmainmirror



         else:
             fightcadeplayerchat "Hey tex"
             show image "tex"
             tx "Whats up?"
             fightcadeplayerchat "I was wondering if i could play you for a little bit"
             tx "Uh sure go ahead."
             hide image "tex"
             r "You send tex a challenege and she promptly accepts."
             jump texbattleshit


         label texbattleshit:
         scene image "black"
         with fade
         play music "Jock strap cowboys by grant mcdonald.mp3"
         r "As soon as the game begins Tex starts flinging all sorts of stuff at you."
         r "You feel like you constantly have to block high or the glass will hit you."
         r "She sees this and peppers you with low bullets."
         r "She sees your guard breaks and then immediately knocks you over with Hol’s slide."
         r "Then… you’re not even sure what happened but you died."
         fightcadeplayer "The fuck was that?"
         fightcadeplayer "I thought I blocked that!"
         show image "tex"
         fightcadetex "Yeah… that’s unblockable."
         fightcadeplayer "Unblockable? What the hell am I supposed to do then?"
         fightcadetex "Well, if you hit me it goes away."
         fightcadeplayer "But the bullet is between me and you."
         fightcadetex "Well a super will let you… Just forget it, you can always try roll around it, ok?"
         fightcadeplayer "Sweet!"
         r "Once again you play and soon you find yourself in a similar situation"
         r "But fortunately Tex messed up, giving you enough time to get up"
         r "But she still uses her Slow Bullet!"
         r "Remembering her advice, you roll past it."
         r "The bullet wiggles a bit before going past you, missing you by a hair’s width"
         r "You let out a sigh before sucking it back up again as Hol Horse grabs you. What do you do?"
         menu:
             "Tech Down":
                 $ tex_relationship +=2
                 r "With precision you didn’t know you had you decide to tech down and punished with a quick combo."
                 show image "tex"
                 fightcadetex "Nice! Surprising that you managed to pull that off, it’s pretty tricky!"
                 hide image "tex"
                 r "Then Tex knocks you over again and the cycle repeats....."
                 jump restinbenisholedition
             "Tech Back":
                 r "You tech backwards and a bullet just misses you as Tex tries to punish."
                 r "Fortunately for Tex there’s a lot more where that came from. as he then follows it up with even more bullets."
                 jump restinbenisholedition
             "Dont tech":
                 r "“Sometimes the best plan is to turn off your brain and pray for the best” you think smugly as your character thuds onto the ground"
                 r "Wait a minute, this seems familiar...."
                 r "Tex then laughs in chat as the slow bullet impacts you."
                 jump restinbenisholedition

         label restinbenisholedition:
         $ renpy.movie_cutscene("afewmomentslater.webm")
         fightcadeplayer "Everything is a learning experience, right?"
         show image "tex"
         fightcadetex "Oh, definitely."
         fightcadeplayer "And I learned a lot from this right?"
         fightcadetex "Well…"
         fightcadeplayer "20-0 is enough to learn some things, right?"
         fightcadetex "It should be…"
         fightcadeplayer "And you’re sure Hol Horse is mid-tier?"
         fightcadetex "Yes."
         fightcadeplayer "You know, maybe this isn’t the game for me."
         fightcadetex "Look maybe I shouldn’t be telling you this, but there is a tournament coming up for new players."
         fightcadetex "You could probably learn a lot from that."
         fightcadetex "So atleast stick around for it."
         fightcadeplayer "I guess… but when will it be?"
         fightcadetex "Soon enough."
         play sound "discordsound.ogg"
         fightcadeplayer "Alright then, GGs."
         stop sound
         fightcadetex "GGs."
         stop music
         play music "fightcadedecideopponet.mp3"
         scene image "fightcade"
         with fade
         r "You then decide to quickly visit the discord to check out what that ping was."
         jump stinkotourneyannouncement







         label holmainmirror:
         hide image "tex"
         scene image "black"
         with fade
         play music "Jock strap cowboys by grant mcdonald.mp3"
         r "The match starts and it doesn’t take long for you to realise this is going to be hell."
         r "With bullets and glass everywhere, it’s hard to even see whats going on."
         r "Tex just keeps rolling over and over again, dodging every single one of your projectiles."
         r "Once you attempt to grab her, she just recovers from the attack and punishes you with a super, taking away a huge amount of your health."
         r "Getting knocked down is almost a instant loss due to Hol’s wake-up game."
         r "That being said, due your panic mashing, you end up hitting Tex with a 2C, knocking her on the ground."
         r "This is your chance to deal huge amounts of damage! What do you do?"
         menu:
             "Use your slow bullets":
                 $ tex_relationship +=2
                 r "Time to get dirty"
                 r "You quickly input the command for the slow bullet special and you aim your shots at the fallen Hol Horse, managing to hit two bullets while Tex is getting up."
                 show image "tex"
                 fightcadetex "Good job! That’s how you do it."
                 fightcadetex "You should always use the slow bullets super when you knock down your opponent."
                 fightcadetex "I’m impressed you learned this just from watching me."
                 fightcadeplayer "Thanks! But this doesn’t change the fact that this tactic is cheap."
                 fightcadetex "Well, what can you do about it?"
                 fightcadeplayer "You can just not do it."
                 fightcadetex "Doubt you will win a lot of matches without this Oki. It’s Hol’s most damaging setup."
                 fightcadeplayer "Really? That sucks"
                 hide image "tex"
                 r "As you questioned the dirtiness of the oki, the next round starts."
                 jump holmainshitnig


             "Glass Shower and another 2C":
                 $ tex_relationship +=1
                 r "Hey if she’s already down it’s better to keep her that way, right?"
                 r "After inputting a 623B you use Hol’s slide so you can hit Tex with a high and a low attack that knocks down at the same time!"
                 r "For your surprise, this actually works! But only for a few times since Tex quickly catches up onto your strategy and counters it by simply jumping backwards."
                 show image "tex"
                 fightcadetex "You should only do that on knockdown if you don’t have any meter for slow bullets."
                 fightcadetex "And even then there are still better oki options than just knocking me down again."
                 fightcadeplayer "Wait, really?"
                 fightcadetex "Yeah."
                 fightcadeplayer "I mean, as long as you can’t get up, everything should be okay, right?"
                 fightcadetex "That’s not how this works."
                 hide image "tex"
                 fightcadeplayer "What do you mean?"
                 r "Before she could answer your question round 2 has begun"
                 jump holmainshitnig

             "Taunt.":
                 $ tex_relationship +=1
                 r "The ultimate texan strat."
                 r "Who cares about dealing damage? This is all about showing who’s the best."
                 r "You don’t need to take advantage of a fallen enemy to win the game. Instead, taunting is clearly the superior choice to be made."
                 show image "tex"
                 fightcadetex ". . ."
                 hide image "tex"
                 r "After that, Tex gets up and hits you with a 236AA and ends the round."
                 r "Round 2 begins shortly"
                 jump holmainshitnig

         label holmainshitnig:
         $ renpy.movie_cutscene("afewmomentslater.webm")
         if tex_fight == "quittex":
             r "After a string of unblockables you start to wonder about this mirror matchup."
             fightcadeplayer "Man, this Hol Horse matchup is so weird. . ."
             r "You have been playing the game for a while now."
             r "As expected, Tex won most of the matches, but you tried your best."
             fightcadeplayer "Jesus man its like i havent improved since out last match."
             show image "tex"
             fightcadetex "Don't say that"
             fightcadetex "Atleast you arent getting perfected anymore."
             fightcadeplayer "Yeah i guess...."
             fightcadetex "Anyways GGs."
             fightcadetex "Cool to see you stick with Hol. He’s a fun character."
             fightcadetex "Don’t be afraid to ping me for advice and i’m willing to fight you again when i’m free."
             fightcadetex "I don’t need to tryhard against you to win so it’s always fun."
             hide image "tex"
             fightcadeplayer "Uhh, sure."
             fightcadeplayer "Thanks for the matches."
             stop music
             play music "fightcadedecideopponet.mp3"
             scene image "fightcade"
             with fade
             r "And with that you close the game."
             play sound "discordsound.ogg"
             r "You also hear a ping from discord that you decide to check out."
             stop sound
             jump stinkotourneyannouncement




         else:
             r "More than 20 matches go by and you start to get tired from the game."
             r "Tex just keeps winning and every round feels like the same thing."
             fightcadeplayer "Damn, this matchup really is weird."
             show image "tex"
             fightcadetex "I warned you."
             fightcadeplayer "Anyway, GGs."
             fightcadetex "Yeah, GGs. I’m willing to help you anytime if i’m free. Just ping me on Discord for that."
             fightcadeplayer "I don’t know if i will ever want to fight another Hol Horse after this. . ."
             fightcadetex "You gotta learn how to deal with him one way or another."
             hide image "tex"
             fightcadeplayer "I suppose so. . ."
             stop music
             play music "fightcadedecideopponet.mp3"
             scene image "fightcade"
             with fade
             r "The game closes and once again you are left staring at the JoJo lobby."
             play sound "discordsound.ogg"
             r "You also hear a ping from discord that you decide to check out."
             stop sound
             jump stinkotourneyannouncement




         label geezerbattle:
         if bill_relationship >= 1:
                                      fightcadeplayerchat "Hey BiLL! Up for a challenge?"
                                      show image "BiLl.png"
                                      boomerusa "Huh? Yeah, sure."
                                      boomerusa "Time to punish you for that loss at the weekly."
                                      fightcadeplayerchat "Well, you see, I lost because, uhh..."
                                      boomerusa "No excuses [povname]."
                                      boomerusa "I’m handing you a spanking one way or another."
                                      jump decidethedestiny





         elif bill_relationship >= 0:
                                   fightcadeplayerchat "Hey BiLL, wanna play?"
                                   show image "BiLl.png"
                                   boomerusa "Who are you?"
                                   fightcadeplayerchat "I’m  [povname]! Don’t you remember me from the last weekly!?"
                                   hide image "BiLl.png"
                                   show image "potato"
                                   p "Don’t mind BiLL, that’s just old age."
                                   hide image "potato"
                                   show image "BiLl.png"
                                   boomerusa "Whatever, let’s just play."
                                   jump decidethedestiny


         label decidethedestiny:
         scene image "chooserubber"
         with fade
         play music "characterselect.wav"
         r "As you accept BiLL’s challenge and the game opens, you hear the familiar jingle of the HFTF main menu theme as the game opens."
         scene image "choosenrubber"
         r "After a short pause BiLL selects Rubber Soul."
         if bill_relationship >= 1:
                                 show image "BiLl.png"
                                 scene image "black"
                                 fightcadeplayer "Going for Rubber again?"
                                 fightcadeboomer "Well, he’s my main, after all."
                                 fightcadeboomer "Have you decided on a main?"
                                 fightcadeplayer "Yeah, [main]"
                                 if main_DIO:
                                     fightcadeboomer "Dio?"
                                     scene image "black"
                                     show image "BiLl.png"
                                     fightcadeboomer "I don't think he fits you"
                                     fightcadeplayer "What do you mean by that?"
                                     fightcadeboomer "His execution requirements are insane and i don't think your ready for it."
                                     fightcadeplayer "I know but i really want to learn him."
                                     fightcadeboomer "Well lets see how much of him you really know."
                                     jump retirementhomefight


                                 elif main_Devo:
                                     fightcadeboomer "Devo?"
                                     scene image "black"
                                     show image "BiLl.png"
                                     fightcadeboomer "You definetly arent ready to play him."
                                     fightcadeboomer "He's the hardest character in the game."
                                     fightcadeplayer "I know but his playstyle really appeals to me."
                                     fightcadeboomer "Well you better know what your doing."
                                     fightcadeboomer "Because i wont hold back."
                                     jump retirementhomefight
                                 elif main_Ice:
                                     fightcadeboomer "Ice?"
                                     scene image "black"
                                     show image "BiLl.png"
                                     fightcadeboomer "Not a bad choice>"
                                     fightcadeboomer "I play ice sometimes so i could show you some random tech for him."
                                     fightcadeplayer "That sounds great!"
                                     fightcadeboomer "Anyways for now just show me what you got."
                                     jump retirementhomefight


                                 elif main_Rubber:
                                      fightcadeboomer "Rubber mirror eh?"
                                      scene image "black"
                                      show image "BiLl.png"
                                      fightcadeboomer "Do you plan on following my footsteps?"
                                      fightcadeboomer "I could share some secret techniques if that's the case."
                                      fightcadeplayer "You've proven to me that even a weak character like him can be strong. so maybe I am."
                                      fightcadeboomer "He's not weak, he's B Tier."
                                      fightcadeplayer "Are you sure? Last time I checked he was C Tier."
                                      fightcadeboomer "Whatever, just pick him already."
                                      jump rubbermirror


                                 else:
                                     fightcadeboomer "I expected you to pick someone that's more fun, but you do you."
                                     scene image "black"
                                     show image "BiLl.png"
                                     fightcadeplayer "Don’t tell me you wanted me to main someone like Rubber."
                                     fightcadeboomer "Fine, then I won’t tell you that."
                                     jump retirementhomefight









         elif bill_relationship >= 0:
                                   fightcadeplayer "Yeah, I heard you were a rubber main!"
                                   show image "BiLl.png"
                                   fightcadeboomer "And who do you main kid?"
                                   fightcadeplayer "[main]!"
                                   if main_DIO:
                                       fightcadeboomer "Dio huh?"
                                       scene image "black"
                                       show image "BiLl.png"
                                       fightcadeboomer "Either you're going to be a dissapointment or a pleasent suprise."
                                       fightcadeplayer "What do you mean by that?"
                                       fightcadeboomer "Nothing."
                                       fightcadeboomer "Just show me what you got."
                                       jump retirementhomefight

                                   elif main_Devo:
                                       fightcadeboomer "Devo?"
                                       scene image "black"
                                       show image "BiLl.png"
                                       fightcadeboomer "Im suprised you even considerd picking him since no one knows how to play him well."
                                       fightcadeplayer "Well he just fitted my playstyle."
                                       fightcadeboomer "Don't think ill go easy on you though."
                                       fightcadeboomer "Show me what you got."
                                       jump retirementhomefight
                                   elif main_Ice:
                                       fightcadeboomer "Ice huh?"
                                       scene image "black"
                                       show image "BiLl.png"
                                       fightcadeboomer "I hope you learned how to confirm into his tandems."
                                       fightcadeboomer "Anyways i play ice sometimes so i'll be able to tell you when your being dumb."
                                       fightcadeplayer "For now show me what you got"
                                       jump retirementhomefight


                                   elif main_Rubber:
                                        fightcadeboomer "Rubber mirror eh?"
                                        scene image "black"
                                        show image "BiLl.png"
                                        fightcadeboomer "You know he's pretty good"
                                        fightcadeboomer "He's a b tier"
                                        fightcadeplayer "But on the wiki page it says he's c ti="
                                        fightcadeboomer "Shut up and just start the damn game."
                                        jump rubbermirror



                                   else:
                                       fightcadeboomer "Well, let’s see what you’ve got."
                                       scene image "black"
                                       show image "BiLl.png"
                                       jump retirementhomefight
         label retirementhomefight:
         scene image "black"
         with fade
         play music "fightingthegeezer.mp3"
         r "Your characters clash and the game begins."
         r "BiLL immediately arrests your options with his short hop and goop and"
         r "and"
         r "and…"
         r "There’s too much happening!"
         r "You feel totally powerless as BiLL keeps pushing forward with a hundred different tactics."
         r "This is even worse than that rubber you fought in the tournament!"
         r "Soon enough you get trapped in the corner with bill pressuring you."
         r "You are not going to win if you just stand still, you must do something about this!"
         menu:
             "Try to jump over her!":
                 r "BiLL seemed to be expecting this one as she jumped with you, bringing you into the ground and punching your face a few times before breaking your back and ending the match."
                 r "Soon enough round 2 starts"
                 jump endofgeezerfornow
             "Guard Cancel!":
                 $ bill_relationship +=1
                 r "You do a shoryuken to guard cancel right?"
                 r "If there’s ever a time to pull it of it's right now."
                 r "And it works!"
                 r "BiLL gets thrown a few paces back by your p̶a̶n̶i̶c̶k̶e̶d̶ ̶m̶a̶s̶h̶i̶n̶g̶ calculated attack but a seemingly stray arm of her stand clips you, ending the match."
                 r "Soon enough round 2 starts"
                 jump endofgeezerfornow
             "Pushblock him away! Get her out of your face!":
                 r "You desperately mash buttons in an attempt to get BiLL out of your face"
                 r "and it works!"
                 r "Using this space to plan your counterattack you rush at BiLL."
                 r "Sadly, she sees through this and hits you for your last sliver of health."
                 r "Soon enough round 2 starts"
                 jump endofgeezerfornow


         label endofgeezerfornow:
         $ renpy.movie_cutscene("11minuteslater.webm")
         hide image "BiLl.png"
         r "A few matches go by and you feel like you are slowly learning how to counter Rubber’s game."
         r "BiLL is still kicking your ass, but you are not getting perfected anymore and you even manage to win a whole match!"
         r "But before the matches go on any further, a message appears on the corner of your screen."
         show image "BiLl.png"
         fightcadeboomer "GG"
         fightcadeplayer "Oh, already?"
         fightcadeboomer "I’m kinda tired. Keep up the good pace and maybe one day you might become a good player."
         fightcadeplayer "Really!? You think so? Thanks!"
         fightcadeboomer "Yeah, whatever."
         fightcadeplayer "Well then, GGs!"
         hide image "BiLl.png"
         r "If BiLL was going to say more you’re not sure."
         r "And before you can even think about asking that, the game closes."
         stop music
         play music "fightcadedecideopponet.mp3"
         scene image "fightcade"
         with fade
         play sound "discordsound.ogg"
         r "While wondering what you should get for dinner, you suddenly get a ping from Discord."
         stop sound
         mn "Better check that out!"
         jump stinkotourneyannouncement






         label rubbermirror:
         scene image "black"
         with fade
         play music "fightingthegeezer.mp3"
         r "The match finally starts and you can already smell the stinkness of this matchup within a few seconds."
         r "The best way to describe Rubber’s dittos is by saying it’s a work of art, a battle so intense it brings out the best of both players, where the most skilled player reigns supreme..."
         r "......or at least the totally reversed scenario."
         r "Both of you can barely use S attacks and the fight is so boring that a Rock-Paper-Scissors game would be much more exciting and less…..stinky."
         r "Not that Rubber wasn’t annoying before, of course."
         fightcadeplayer "Maaaaaaan, what’s this game even called again?"
         show image "BiLl.png"
         fightcadeboomer "The One To Hit Goop First Wins - The Game."
         fightcadeplayer "This is so boring!"
         fightcadeplayer "We just keep doing the same thing, and you still manage to win!"
         fightcadeplayer "How?"
         fightcadeboomer "Pure mad skills."
         fightcadeplayer "Pure bullshit that is!"
         fightcadeboomer "Chill, I don’t really like Rubber mirror matches either."
         fightcadeplayer "Can’t imagine anyone would like this."
         fightcadeboomer "Well, what can you do about it?"
         fightcadeplayer "This sucks…"
         fightcadeboomer "I mean, you knew this was going to happen at one point when you picked Rubber."
         fightcadeplayer "I hadn’t given it much thought…"
         fightcadeboomer "Actually, why did you choose to main Rubber anyways?"
         menu:
             "I have poor execution":
                      $ bill_relationship += 1
                      jump garbitchplayer
             "His taunt":
                      $ bill_relationship += 1
                      jump ebicmaymays





             "Rubber is the only character I can truly connect with. I know he is not that good, but that doesn't matter. I’m not here to win, I’m here to have fun, and he is the perfect character for that!":
                      $ bill_relationship += 2
                      jump thankskanyeverycool

         label garbitchplayer:
         fightcadeplayer "Well, I’m not really that good at pressing buttons with a specific timing."
         fightcadeboomer "I see. Well, that’s 90% of Rubber’s players for you."
         fightcadeplayer "Aw, really?"
         fightcadeboomer "Still, you could have mained someone like Hol Horse."
         fightcadeplayer "Yeah. But there’s something so special about Rubber Soul…"
         fightcadeboomer "Man of great tastes you are…"
         jump endofgeezerfornow2

         label ebicmaymays:
         fightcadeplayer "Rubber has the best taunt in the game, why wouldn’t I main him?"
         fightcadeboomer "You can’t be serious…"
         fightcadeboomer "Is that all?"
         fightcadeplayer "Y-Yeah…"
         fightcadeboomer "Huh."
         fightcadeboomer "Well, I will give you some props for sticking with a character like him just because of that."
         fightcadeplayer "Thanks!"
         jump endofgeezerfornow2


         label thankskanyeverycool:
         fightcadeplayer "I don’t know."
         fightcadeboomer "Oh."
         fightcadeboomer "That’s a bit disappointing."
         fightcadeplayer "Yeah, sorry..."
         fightcadeboomer "But, I also don’t know why I like him so much."
         fightcadeplayer "Huh?"
         fightcadeboomer "He just kinda stuck with me."
         fightcadeplayer "That’s a cool story!"
         fightcadeboomer "Not really."
         fightcadeplayer "Well, it doesn’t matter, I like it!"
         jump endofgeezerfornow2

         label endofgeezerfornow2:
          $ renpy.movie_cutscene("11minuteslater.webm")
          hide image "BiLl.png"
          r "You spent a while chatting with BiLL about Rubber’s unlimited potential as a Top B Tier character with the game running on the background without you even realizing it."
          fightcadeplayer "Huh? Oh well it was cool chatting with ya Bill, but if we are not going to play there’s not any reason for me to be here!"
          show image "BiLl.png"
          fightcadeboomer "Welp, I’m not going to play anymore. GGs?"
          fightcadeplayer  "GGs! I think…"
          fightcadeboomer "I don’t get why you're a stinko."
          fightcadeboomer "You're not that terrible."
          fightcadeboomer "If the chance ever presents itself, try to get rid of that stench."
          fightcadeboomer "Anyways keep practicing and ill try to share some rubber tech with you"
          fightcadeplayer  "Alright, will do!"
          fightcadeboomer "Good. See you soon."
          fightcadeplayer  "See y--"
          stop music
          play music "fightcadedecideopponet.mp3"
          scene image "fightcade"
          with fade
          play sound "discordsound.ogg"
          r "Before you can finish typing your message the game has already closed itself and at the same time you get pinged on Discord."
          stop sound
          fightcadeplayer "Well that was a dick move"
          fightcadeplayer "I’ll just go check out the server then."
          jump stinkotourneyannouncement








         label stinkotourneyannouncement:
         play music "idleaskingtheme.mp3"
         scene image "annon"
         r "After getting back on you notice that the ping is from the announcements channel"
         r "Without any hesitation you scroll down and check what it is."
         show image "mahjong"
         m "Alright @stinkos, this is your chance to become normal human beings again."
         m "There will be a stinko tournament later today and as you all know, the winner gets their stink removed."
         m "This is your last chance to sign-up if you haven’t done that already."
         m "So hurry up retards."
         hide image "mahjong"
         r "The announcement is met with a flurry of reactions."
         r "You decide to check out stinko-containment to see what your ‘brothers in stench’ are doing after hearing this."
         scene image "general"
         Garrem "It’s time to show my skill."
         Gekc "Man I sure do love #nsfw."
         gripdip "This reminds me of a tournament arc."
         ns "Yeah me too"
         ns "it’s like when the protagonist proves their skill and becomes noteworthy in the eyes of their peers and elders."
         gripdip "Uh, that too."
         show image "lucas"
         boi "Haha, stinko tournaments are always so fun."
         ns "Really?"
         ns "You’ve won some of those, right?"
         boi "Yes and it was worth it."
         ns "But....aren’t you a permanent stinko though?"
         boi "Whatever."
         boi "Anyways stinko tournaments are usually hosted by either Majongles or SouI with ExFalchion casting with them."
         ns "ExFalchion?!"
         ns "The man!? The legend?!"
         ns "I’m his number one fan!"
         boi "Uh yeah"
         boi "anyways sometimes they get other people to come in and help cast like Zarythe, Peon2 or Skynaloz."
         ns "So will I see you there then?"
         boi "You going to play, huh?"
         boi "And, uh….."
         boi "My kakyoin is too good so I don’t think it’s a good idea for me to enter."
         boi "It’s just not fair."
         hide image "lucas"
         ns "Aw..."
         stinkoacure "Your kak is trash and mine is better Lucas, you know it."
         show image "lucas"
         boi "Shut up Acute"
         boi "You’ll never be regular before me."
         hide image "lucas"
         r "After lucas spoke those words, acute then posted a gif of a kakyoin combo."
         show image "tex"
         tx "Hey I saw that"
         tx "Pretty cool combo man."
         tx "Most people can’t do that around here"
         tx "Here, take a green."
         hide image "tex"
         r "Acute then dissapears from the stinko list that is to the right of that channel"
         r "And from the channel itself."
         pause 3.0
         show image "lucas"
         boi "What."
         hide image "lucas"
         Gekc "Niggas in the club doing aegis reflector!"
         r "You decide that’s enough #stinko-containment for today"
         r "and maybe for the rest of the week."
         scene image "black"
         stop music
         $ renpy.movie_cutscene("ashortwhilelater.webm")
         scene image "annon"
         play music "goingtrhoughthemotions.mp3"
         r "After signing up for the stinko tourney you hop onto guides and training to see if you can better prepare for the tournament."
         scene image "guide"
         r "As you enter the channel it seems you walk into a small arguement."
         sovietjoelbootleg "So I’m meant to learn the game with these kind of resources?"
         p2 "Sorry, this is all we got…"
         sovietjoelbootleg "Not even a proper training mode? Or wiki?"
         p2 "Well the wiki is being worked on"
         p2 "Training mode, not so much."
         sovietjoelbootleg "I'll have you know I’m a Grand Master Fang player in SFV."
         p2 "Alright bud I’m sure we’ll get a proper training mode for this 20 year old game sometime soon, ok?"
         p2 "So calm down."
         sovietjoelbootleg "Whatever."
         r "You hesitate slightly before typing."
         ns "Uh, what resources do we have for training?"
         p2 "Just uh, some cheats and standcrash."
         ns "How do I get the cheats?"
         p2 "Glad you asked."
         r "Peon then points you towards the pins where the instructions for the cheats are."
         ns "Ill make sure to check that out!"
         p2 "Its Nice to see a stinko taking interest in getting better at the game."
         ns "Yeah I kind of want to learn some tech for [main]."
         menu:
             "Is there anyone I could ping for help?":
                jump askforhelp

             "But im sure i can learn it on my own":
                p2 "Well if you say so."
                r "and so you head to the training mode build to pratice......something"
                scene image "black"
                with fade
                jump dumbasstraining



         label askforhelp:
              if main_Hol:
                  $ tex_relationship +=2
                  p2 "Hey Tex you’re pretty good with Hol right?"
                  p2 "Can you show this kid a few pointers?"
                  show image "tex"
                  tx "Oh hey [povname]."
                  tx "Sure i can tell him some stuff peon."
                  tx "Try doing stuff like 5a 5a 5b 236c 214b"
                  tx "really easy and puts them into blockstun whereever you want them."
                  tx "Then you can follow up with S or glass or…"
                  hide image "tex"
                  $ renpy.movie_cutscene("420minutesxd.webm")
                  r "Tex goes on and on and you realize that you have nothing to write all this important information down on."
                  r "You scramble for paper for a second before you remember discord saves it’s messages."
                  show image "tex"
                  tx "Did you get all that?"
                  hide image "tex"
                  ns "Yes! Thank You!"
                  r "And with all this info you head to the training mode build to test it all out."
                  jump trainingmodewithhelp

              if main_Mariah:
                 $ potatoboi_relationship +=2
                 p2 "Really?"
                 p2 "It goes without saying that you should be asking Potatoboih."
                 p2 "Potato help this guy out"
                 show image "potato"
                 p  "Are you really sure you want to learn Mariah?"
                 ns "Uh… yes?"
                 p "Excellent! Let me run you through her basics!"
                 ns "Wait… I…"
                 p "Mariah can basically only do things if her opponent is on the ground."
                 p "Her oki is actually decently strong with higher levels and to gain levels you need to avoid being grabbed"
                 p "and you can mix them up with 6b and knock them down with 2a 2a 2a and and…."
                 mn "This girl is going in circles!"
                 p "Really once you get enough levels, Mariah becomes nearly decent and then you can…"
                 ns "Ok, uh, thanks."
                 ns "I figured out a few things to practice."
                 p "Cool!"
                 p "Feel free to ping me if you need anymore info."
                 hide image "potato"
                 r "Potatoboih then jaunts off somewhere else to find more people to subject intense game knowledge to."
                 r "Meanwhile you head over to the training mode build to test it out."
                 jump trainingmodewithhelp

              if main_Devo:
                 $ aleph_relationship +=2
                 p2 "Hey Aleph, can you help this guy out?"
                 show image "alph"
                 a "Who dares ask the world-breaker for help!?"
                 ns "Uh… me."
                 ns "Do you have any Devo tips?"
                 a "Dave!? You should have just said so!"
                 ns "Well he looks really cool and I’ve had some success using him even though he’s really weird and…"
                 a "Yeah you have a lot of work ahead of you, Dave is the hardest character in the game!"
                 mn "Why does this guy keep calling Devo Dave?"
                 a "Yeah, he has one of the fastest rolls in the game and many oki options to choose from."
                 a "It’s pretty hard to always keep the doll where you want it."
                 a "Remember to oki loop with 2c and 214a as well!"
                 a "Here are a couple of of his combos to get you going."
                 a "5C xx 236+A, [6], 2A, 2A, S+5A > 5A xx s.22+C xx 214+S (TS), j.C, 5C xx 214+A, 2A, 66 DC, 2A, 2A, 2A, S+5A > 5A xx s.22+C/s.236+AA. s.22+C into 214+S is a 1F link.5C xx 236+A, [6], 2A, 2A, S+5A, d.5A, 6B > 214+S, j.C, 5C > 214+A, 2A, 5C, 214+AA, 2A, dash, 2A xN, 2A, 2A, 2A, S+5A > 5A > 22+C. 5C > 214+A, 2A, 5C > 236+A, walk, 2A, 2A, S+5A > d.5A > 6B > 214+S , j.C, 5C > 214+A, 2A, 5C, 214+AA, 2A, dash, 2A xN, 2A, 2A, 2A, S+5A > 5A > 22+C."
                 ns "Uh, what?"
                 a "Just watch this basic combo video and try to do these."
                 $ renpy.movie_cutscene("devocombos.webm")
                 r "Despite the video’s name, his combos don’t look basic at all."
                 ns "Uh thanks aleph"
                 ns "Ill try them out"
                 r "And so you head over to the training mode build to hopefully atleast do half of the bnb"
                 jump trainingmodewithhelp

              if main_Rubber:
                 $ bill_relationship +=2
                 p2 "You know who really likes Rubber?"
                 p2 "Bill."
                 ns "Bill?"
                 show image "BilL"
                 boomerusa "What do you want."
                 ns "Uh, i was wondering what I can actually do as Rubber to put on some pressure?"
                 ns "I think I’ve got 2a 2a 214a down and I’ve seen cool stuff like 214s 236aa but is that really enough to win games with?"
                 ns "Is j.a j.s the height of Rubber?!"
                 boomerusa "Come young grasshopper, you have much to learn."
                 ns "What?"
                 boomerusa "Just listen to me retard"
                 boomerusa "Rubber doesn't have too many tools at his disposal but can be great at zoning in the middle of the field with his goo or stand attacks"
                 boomerusa "What you gotta do is keep your distance and find the right moment for a jump in or approach with a low jab."
                 boomerusa "Then pressure them with 50/50 mixups"
                 boomerusa "Got that?"
                 ns "Uh yeah"
                 ns "Thanks bill!"
                 boomerusa "Feel free to ping me if you need any more help"
                 hide image "BilL"
                 r "And so you head over to the training mode to practice the mixups."
                 jump trainingmodewithhelp



              if main_Pol:
                 p2 "Really?"
                 p2 "Well there’s only one man to ask"
                 p2 "thelord-"
                 p2 "I mean SploogieMcNoodle."
                 p2 "Yo sploogie help this guy out"
                 show image "sploog"
                 Sp "Hey [povname] how are you?"
                 Sp "Have you come to the Sploogie Emporium™ to learn about Polnareff?"
                 ns "Uh yeah i guess."
                 Sp "Well you’ve come to the right place!"
                 Sp "Just check out my video on him and you'll be set."
                 ns "Sweet! Thanks sploogie!"
                 Sp "Thanks man I hope it helps you out with Polnareff."
                 Sp "He’s not really a hard character but you need to understand how charge characters work and…."
                 ns "But uh, where’s part two?"
                 Sp "Well, uh… so umm… well..."
                 hide image "sploog"
                 r "Suddenly the chat is filled with random people demanding for part two of Sploogies tutorial series."
                 r "You didn’t know there were this many Polnareff mains!"
                 show image "sploog"
                 Sp "It’s a little down the pipeline at the minute ok?"
                 Sp "How about I fill you in on all the other small bits you’re missing"
                 ns "I would love that"
                 hide image "sploog"
                 $ renpy.movie_cutscene("420minutesxd.webm")
                 r "After a while of listening to sploogie you decide to hit the lab"
                 ns "Thanks alot sploogie!"
                 show image "sploog"
                 Sp "No problem"
                 Sp "Feel free to ping me if you need any more advice."
                 hide image "sploog"
                 r "And so you head over to the training mode to practice the mixups."
                 jump trainingmodewithhelp



              if main_Ice:
                 p2 "Another Ice main!?"
                 p2 "Ok just go bother SouI."
                 p2 "Soui help this guy out"
                 show image "Soui.png"
                 So "Hey it’s me, the supreme Jojos player and owner of this server, SouI."
                 hide image "Soui.png"
                 ns "Soul? Like that thing I lost years ago?"
                 mino "Don’t steal my gig."
                 show image "Soui.png"
                 So "No, s-o-u-i, dumbass."
                 So "Now, why are you bothering me?"
                 ns "Peon said to bother you for learning ice"
                 So "Then you've come to the right place!"
                 So "Ok so let me break it down for you."
                 $ renpy.movie_cutscene("420minutesxd.webm")
                 r "SouI is… Surprisingly in-depth."
                 r "He seemed to be quite a haughty person but as soon as he noticed you were actually paying attention and trying to learn he immediately softened up and did his best to make sure you understand everything he said."
                 r "Most of what he tried to convey seemed to be neutral-based which, you seem to be grasping, is tough for Ice in certain matchups."
                 ns "Wow... thanks SouI! That gives me more than enough to practice with!"
                 show image "Soui.png"
                 So "Hmpf, you'll do fine kid."
                 So "Now I’m off to beat up some people on Fightcade"
                 So "If I see one more spammer I’m going to rape my router."
                 hide image "Soui.png"
                 r "And so you head over to the training mode to practice the tandem confirms."
                 jump trainingmodewithhelp






              if main_DIO:
                 p2 "Yo go hit up Zarythe, he can show you the Dio ropes."
                 p2 "Zar help this dude out."
                 show image "zar"
                 Z "You want to legit play Dio?"
                 Z "Here's some good advice"
                 Z "Don’t play Dio."
                 ns "What? But I want to seriouasly play Dio!"
                 Z "You don’t want to play Dio."
                 ns "Whatever, he’s cool and powerful. Teach me him."
                 Z "Trust me dumbass you do NOT want to play Dio."
                 Z "I can count on one hand how many Fightcade players can play him well."
                 ns "Is this about his combos?"
                 ns "I heard they were hard but I’ll practice lots so don’t worry!"
                 Z "…"
                 Z "Here is a video I made a little while back on the Dio bnb and how to learn it."
                 Z "Come back when you can do it."
                 ns "Thanks Zarythe!"
                 mn "Wait a second, what do all these things mean? Walk what?"
                 mn "Whatever! I’ll figure it out in training mode."
                 r "And so you head over to the training mode to try and atleast do the negative edge."
                 jump trainingmodewithhelp

         label dumbasstraining:
         $ renpy.movie_cutscene("18later.webm")
         scene image "black"
         with fade
         r "After a while of doing pretty much nothing you decide that its enough for one day."
         r "You also look at the clock"
         r "noticing its almost time for the stinko tourney!"
         jump herewego





         label trainingmodewithhelp:
         $ renpy.movie_cutscene("18later.webm")
         scene image "black"
         with fade
         r "After practing some bnbs and nuetral your hands start to hurt"
         r "You also look at the clock"
         r "noticing its almost time for the stinko tourney!"
         jump herewego


         label herewego:
         play sound "discordsound.ogg"
         r "Suddenly you get a ping from Majongles!"
         stop sound
         scene image "annon"
         with fade
         show image "mahjong"
         m "Tournament begins now idiots."
         m "Strap in because it’s going to be a wiiild ride."
         hide image "mahjong"
         ns "Hell yeah! This is going to be great!"
         play music "idlemusicforstinko.mp3"
         scene image "fightcade"
         with fade
         r "After doing some warmups for the tournament, you finally tune-in to the stream to listen, now with Fightcade open and keyboard keys configured."
         r "After 30 long minutes of the usual introduction, Majongles finally decides what matches will be streamed for the first round."
         r "ExFalchion is also a commentator but he doesn’t seem that talkative."
         m "Alright fags let’s get this started."
         Exfalch "Ye..."
         r "She starts to list a few names."
         r "Fortunately it seems like you are not going to be streamed this round."
         mn "Whew! That was close."
         mn "But I’m just delaying the inevitable."
         mn "If I plan to win I’m going to be streamed no matter what."
         mn "But now isn't the time to think about that!"
         mn "I have to check the challonge to see who is going to lose to my [main] next!"
         scene image "challenge"
         with fade
         r "Upon taking a quick look at the tournament brackets, you find out that your next opponent is called…"
         mn "The Giant Rat?"
         mn "Damn that’s an epic nickname…"
         mn "I guess i better get ready to challenege him"
         scene image "fightcade"
         with fade
         r "Despite such a creativity to pick names your foe doesn’t seem to have the best timing in the world"
         r "He is nowhere to be seen in the Fightcade lobby."
         mn "So I guess I’ll just have to wait for the man to show up huh?"
         mn "Hope it doesn’t take too long."
         pause 3.0
         mn "Any time now…"
         pause 3.0
         mn "Any ti--"
         $ renpy.movie_cutscene("20later.mpeg")
         mn "Alright, this is enough!"
         mn "If my opponent doesn’t show up…"
         mn "That means I get a free round, right!?"
         mn "Well it better"
         scene image "challenge"
         with fade
         r "As you set your match as a 69-0 in the Challonge page, you open the tab of the stream to check out how the tournament is going."
         scene image "black"
         with fade
         play music "majonglesqualitymusic.mp3"
         m "Man, these guys suck."
         r "Says Majongles as she's forced to commentate on a match that could only be compared to a monkey fight."
         r "However the chat seems pleased enough with the fight."
         r "You start to suspect that they also might be stinkos."
         mn "Man these guys look awful!"
         mn "This tourney will be a cakewalk!"
         m "Okay, glad that’s over."
         m "Let’s go to the round 2 matches now."
         mn "Crap! I better get ready!"
         m "Yeah so…..."
         m "let’s see here…"
         m "[povname] versus….."
         m "Isoito."
         Exfalch "This is going to be awful…"
         play music "stinkotourneytheme.mp3"
         mn "Okay! I got this!"
         mn "This is my second chance to show hundr-"
         mn "I mean dozens of people how good I really am!"
         r "Soon enough you go back to fightcade to fight iso"
         scene image "fightcade"
         with fade
         r "iso almost immediatly sends you a challenege"
         r "You click to accept and not long after the game opens"
         scene image "black"
         with fade
         fightcadeisotio "Good luck!"
         r "While the lag is not as bad as you expected it to be, it still occasionally pauses with a loud brr."
         $ renpy.movie_cutscene("2laggyroundslater.webm")
         scene image "fightcade"
         with fade
         r "And to your surprise you won without any trouble!"
         r "Guess you're just a step above the competition, huh?"
         r "You quickly checked the challonge and you next match is with..."
         mn "RedSodaPop?"
         mn "Who comes up with these names?"
         redpop "Are you prepared for a beating?"
         redpop "because you better be"
         r "Red sends a challenege that you promptly accept."
         scene image "black"
         with fade
         fightcadeplayer "glhf"
         $ renpy.movie_cutscene("Moments Later.webm")

         r "Red didn’t even take a round off."
         scene image "fightcade"
         with fade
         redpop "To be fair it’s been over a month since I last played."
         fightcadeplayerchat "What?"
         redpop "Well…."
         redpop "back to shitposting on discord...."
         mn "So this is how some stinkos never grow out of their stink."
         mn "They just give up!"
         r "This simple statement triggered an epiphany"
         r "a great realisation that would shape your perceptions of this game and it’s playerbase forever."
         mn "I can get good…"
         mn "if I just play and practice the game?"
         mn "I can get good if I try?"
         mn "I can be good?"
         mn "I can…"
         play sound "challengenosie.wav"
         r "While you were having a life defining moment"
         r "It seems someone challeneged you"
         mn "Phew! Another challenge!"
         mn "All that thinking was hurting my brain"
         Manolito "C’mon, I don’t have all day"
         Manolito "hurry up and accept"
         fightcadeplayerchat "Oh. Sorry."
         fightcadeplayerchat "Lets go!"
         $ renpy.movie_cutscene("Moments Later.webm")
         r "It doesnt take alot of effort to time to crush this guy's efforts"
         Manolito "Whoa you’re super strong!"
         Manolito "If I knew players like you were in this tournament I would never have joined!"
         fightcadeplayerchat "What?"
         Manolito "Let’s play again another time."
         r "You don't really know what to say."
         r "This is the first time someone actually complemented your skill."
         r "But before you could bask in pride, you decide to check majongle's stream"
         scene image "black"
         with fade
         play music "secondmajonglestheme.mp3"
         m "This fucking idiot LEARN A COMBO"
         Exfalch "I like him he’s an honest Hol Horse - like Mike Ross, ya know?"
         Exfalch "Not an impressively skilled player by any means but wins through experience, intuition, and fundamentals."
         m "What"
         r "Suddenly the Hol Horse pulls off a super on the Dio and gets him to 0 health."
         r "Ex then starts making hooting monkey noises."
         Exfalch "Whose gonna win?!"
         Exfalch "Look majongles LOOK his health is so low!"
         Exfalch "Ooh this is close."
         m "yeah, yeah, yeah"
         m "I think I can tell where this is going"
         m "my money is on the dio."
         Exfalch "What do you mean?!"
         Exfalch "That the dio is almost dead and the hol horse is shooting bullets like crazy!!!!"
         r "Hol Horse was indeed spamming those bullets."
         r "Just high ones for some reason."
         r "The Dio deciphers the pattern brilliantly and throws knives, allowing a bullet to pass through his i-frames."
         r "In a panic the hol horse simply keeps shooting bullets instead of blocking, eating the knives to the face and shredding his remaining health"
         r "Soon enough he ends up closing out the game."
         m "What did I tell you bud"
         m "the Dio had it covered."
         Exfalch "I’m kind of upset."
         m "Well at least those losers finals weren’t too bad."
         m "Let’s just see how the grand finals are."
         mn "Hold on, finals?!"
         mn "And since I haven’t lost yet that means I’m in the finals?!"
         mn "It’s already the finals?!!!"
         play music "final boss battle mahjong.mp3"
         r "This is it."
         r "You have really come this far"
         r "and the last opponet in your way to glory is just there, waiting for you."
         r "You quickly log onto fightcade to fight this bastard"
         scene image "fightcade"
         with fade
         r "While you don't know exactly who this player is, you feel chills going down your spine knowing how they had to climb their way out of the loser's brackets."
         r "Despite that, you put your fears aside to take on this foe."
         r "Whom sends you a challenege!"
         scene image "choosingdio"
         r "As soon as you accept the Fightcade challenge, you can already feel the tension in the air."
         r "Your opponent then chooses dio, while you choose [main]."
         scene image "black"
         r "You take a deep breath."
         mn "Heh this will be easy!"
         mn "I've faced stinkos, veterans and even the tournament hosts themselves!"
         mn "I can do this!"
         mn "I just have to believe and embrace the power of [main]!"
         r "No words are being typed as the match begins."
         r "Your opponent, going by the nickname of TotallyNotSkynaloz, rushes mercilessly towards your character with DIO."
         r "But this time you're going to fight with all of your will!"
         r "This is the final test of your skill."
         r "If you truly want to prove the world that you're not a stinko, you have to give it your all!"
         mn "I have endured the shit smell and lag of all my opponents until now!"
         fightcadeplayer "Come at me!"
         r "By putting to use everything you've learned so far, and with the power of plot armor, you manage to score a round against TotallyNotSkynaloz's rather bad DIO."
         mn "Hell yeah!"
         mn "One down and 5 more rounds to go!?"
         mn "Why the hell do I need to play more on the finals!?"
         mn "That's bullshit!"
         mn "Whatever, I need to focus on the game."
         mn "I can do this!"
         r "The second round starts and the fight proceeds the same way as before, but with a little more mashing of TotallyNotSkynaloz."
         r "Because of that, it's another easy win for you."
         mn "Sweet!"
         mn "I can already taste the feeling of being a normal human!"
         mn "I just have to keep winning."
         r "To your surprise, right after that, TotallyNotSkynaloz decided to switch characters"
         r "this time picking Polnareff."
         mn "Huh?"
         mn "Does this guy have multiple mains or something?"
         mn "That's odd."
         mn "But that's not stopping me anytime soon!"
         r "And indeed this does not stop you as it seems like your opponent doesn't even know what they're doing."
         r "You manage to win this match with even more ease than the last one. At this point, you are not even scared anymore and you start to wonder how this player even managed to get to the grand finals."
         mn "I was expecting a bit more out of this tournament."
         mn "Have I really gotten that good with just a few weeks?"
         mn "Maybe everyone here is just bad."
         mn "Not that I'm saying that's a bad thing, but..."
         r "Before you can conclude your line of thought you see TotallyNotSkynaloz picking New Kakyoin."
         mn "New Kak?"
         mn "Is this a joke?"
         r "Sadly that was not a joke as you lose the next round in the blink of an eye."
         mn "W-What?"
         mn "What the hell just happened?"
         mn "I couldn't see anything!"
         mn "Did I just lose?"
         r "Checking the round markers, it seems that you did lose a round in under a second."
         r "How that’s possible is beyond your comprehension."
         r "You slap yourself in the face to get back into focus."
         r "Soon the next round begins"
         r "This round seemed to go as fast as the last as TotallyNotSkynaloz somehow manages to keep getting you in the snake tie and reads all your button mashes."
         TotallyNotSkynaloz "You've awakened my final form kiddo"
         TotallyNotSkynaloz "prepare to die."
         fightcadeplayer "Fuck you!"
         r "TotallyNotSkynaloz says nothing and begins the game."
         mn "What the hell!?"
         mn "This stinko can tandem?"
         mn "Even if it’s a little unclean…"
         mn "Is this really the level of true stinkos?"
         r "Once again the game closes out in TotallyNotSkynaloz’s favour."
         mn "What the hell….."
         mn "she’s not going to make the full comeback is she?!"
         r "Game 5 begins and you do your best to pay close attention to all the things TotallyNotSkynaloz is doing in hopes of countering him."
         r "You’ve noticed a few of his patterns in the last few games."
         mn "There!"
         mn "I’ve seen him do that pressure strat before, so he’s going to try and follow it up with a forward dash here…"
         r "TotallyNotSkynaloz shows his skill as he adapts to your read and gets the knockdown easily."
         r "Which also then leads into another tandem."
         r "Which then leads into another round."
         r "Which then leads into you questioning your existence."
         mn "This round….."
         mn "This round I have to do something quick!"
         r "And something you did."
         r "You dumped all your meter in hopes of something landing and miraculously killing TotallyNotSkynaloz."
         r "But unfortunately, she knew how to hold backwards."
         r "And boom."
         r "Round for TotallyNotSkynaloz."
         r "Tournament over."
         play music "reallysadshithuh.mp3"
         r "You hang your head down."
         r "You were so close this time."
         r "After everything you did."
         r "All you practiced."
         r "All the passion you put in."
         r "It was stopped right here."
         r "Maybe you really and truly are a stinko."
         r "You hang your head and tune back into the stream."
         r "Just in time to catch what Majongles is announcing."
         play music "theendofmahjongarc.mp3"
         m "Yeah we know who you are retard."
         m "I’ve contacted the Discord police and they’re after you, get out of my tournament."
         mn "What the hell?"
         Exfalch "I’m so disappointed in you."
         sn "Hey, I was just trying to have some fun."
         Z "Have fun in the weeklies you faggot."
         Z "Don’t play in stinkos that you've already won retard."
         Z "Just for that you’re losing roles."
         sn "Nooooooo"
         m "Whatever."
         m "So uh"
         m "whoever was second place wins."
         m "Good job you."
         mn "Huh?"
         r "It seems like your opponent broke a major rule of the tournament, thus, giving the victory to you."
         play music "goodjobuwon.mp3"
         mn "So… I’m the winner!?"
         mn "Did I really win the tournament!?"
         mn "Am I going to be respected like a normal person now!?"
         mn "With this power i know what i can do for other stinkos!"
         mn "I’m going to be an example for them!"
         mn "I'll make them know that despite how bad you are, you can still become a great player if you try!"
         if tex_relationship >=6:
             play sound "discordsound.ogg"
             r "Suddenly you receive a direct message on Discord."
             show image "tex"
             tx "Hey, I heard you won the stinko tournament."
             ns "Yeah! That’s right."
             tx "Good job."
             tx "Keep up with the good work so you can win a real tourney next time."
             ns "You think I have a chance to do that?"
             tx "If you train hard enough."
             hide image "tex"
             ns "Okay! I will!"
             jump chap2_end










         elif potatoboi_relationship >=5:
             play sound "discordsound.ogg"
             r "Suddenly you receive a direct message on Discord."
             show image "potato"
             p "Yo, Pro Tagonist!"
             p "You did well at winning that stinky tournament."
             ns "Really? Thanks!"
             p "So, I’m busy right now and I just wanted to say that you did a good job."
             p "See you later!"
             hide image "potato"
             ns "See ya!"
             jump chap2_end






         elif aleph_relationship >=7:
             play sound "discordsound.ogg"
             r "Suddenly you receive a direct message on Discord."
             show image "alph"
             a "You sure showed those stinkos who’s the coolest kid in the town."
             ns "Huh? What do you mean?"
             a "The Majongles tourney you dumbass."
             a "Wasn’t expecting you to reach the finals."
             a "I lost a bet because of that."
             ns "What were you even betting?"
             a "Whatever."
             a "Good job."
             hide image "alph"
             ns "Oh, thanks!"
             jump chap2_end





         elif bill_relationship >=6:
             play sound "discordsound.ogg"
             r "Suddenly you receive a direct message on Discord."
             show image "BiLl"
             boomerusa "Nice work."
             r "She sends a monkey emoji."
             ns "Is this… the power of Rubber?"
             boomerusa "This is only a fraction of Rubber’s power."
             ns "Woah…"
             boomerusa "You still have a long way to go."
             boomerusa "Keep it up."
             hide image "BiLl"
             ns "Got it!"
             jump chap2_end





         elif sploogie_relationship >=5:
             play sound "discordsound.ogg"
             r "Suddenly you receive a direct message on Discord."
             show image "sploog"
             Sp "Hey [povname], pretty cool that you won this tourney."
             ns "I know right? It’s so cool!"
             Sp "I will admit that I didn’t really like you when you first joined the server, but you ain’t that bad."
             ns "Thanks… I guess?"
             Sp "But yeah, you now have the respect of the Linguini King."
             ns "Linguine what now?"
             Sp "Smell you later."
             hide image "sploog"
             jump chap2_end





         elif zarythe_relationship >=6:
             play sound "discordsound.ogg"
             r "Suddenly you receive a direct message on Discord."
             show image "zarythe.png"
             Z "Hey, good job. You made some good calls there."
             Z "I could see you being a proper {color=FFDF00}{u}{b}DIO{/b}{/u}{/color} main one day."
             ns "Gee thanks, your advice really helped me and..."
             Z "Don’t get full of yourself. You still have a lot to do."
             hide image "zarythe.png"
             ns "O-Ok Ma’am!"
             jump chap2_end



         elif soui_relationship >=6:
             play sound "discordsound.ogg"
             r "Suddenly you receive a direct message on Discord."
             show image "Soui.png"
             So "Hmpf."
             So "It seems like your skills have gotten better since we first met."
             ns "Yeah, I could totally kick your ass now!"
             So "Don’t get so cocky."
             So "All you did was win a stinko tourney."
             So "That means almost nothing."
             ns "Ouch."
             So "But it’s a step in the right direction."
             So "Train more and one day you will be able to face Doog properly."
             ns "Doog?"
             ns "Who’s that?"
             So "MargeSimps--"
             So "You know what?"
             So "Forget about it."
             So "Keep playing the game or I’ll eat you for dinner."
             ns "Uh… okay?"
             So "Cool. Bye."
             hide image "Soui.png"
             jump chap2_end




         elif majongles_relationship >=5:
             play sound "discordsound.ogg"
             r "Suddenly you receive a direct message on Discord."
             show image "mahjong"
             m "Thanks for providing a bit of entertainment to the stream."
             ns "Huh?"
             m "Most people just watch the stinko tourneys to have a laugh at them."
             m "But you at least showed a bit of skill there to keep things interesting."
             m "Even if you got fucked by Sky at the end there."
             ns "Hey!"
             ns"That fight was pure bullshit!"
             m "Whatever, you did well there."
             m "Keep training and maybe you wont be as ooga booga as you are now."
             hide image "mahjong"
             ns "Thanks?"
             jump chap2_end


         else:
             ns "Anyways"
             ns "It’s over now!"
             ns "Not only did I get rid of my stinko role but now I have a much cooler one showing my achievement!"
             ns "I’ve really gotten this far, huh?"
             ns "Man, this day was awesome!"
             ns "Now, I just need to get that regular role."
             r "However, after looking at the time, you think it’s a better idea to leave that task for another day."
             r "Hopefully, a day where your fingers aren’t hurting from your intense keyboard mashing."
             r "You drop into your bed, and seconds after, you fall asleep."
             return




         label chap2_end:
             ns "It’s over now!"
             ns "Not only did I get rid of my stinko role, but now I have a much cooler one showing my achievement!"
             ns "I’ve really gotten this far, huh?"
             ns "Man, this day was awesome!"
             ns "Now, I just need to get that regular role."
             r "However, after looking at the time, you think it’s a better idea to leave that task for another day."
             r "Hopefully, a day where your fingers aren’t hurting from your intense keyboard mashing."
             r "You drop into your bed, and seconds after, you fall asleep."
             return
