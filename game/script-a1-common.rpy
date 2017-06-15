label en_C0:

    scene black
    window hide
    with None 
    
    nvl show dissolve # MAYBE [str]
    
    n "I've always believed that there are many kinds of people."

    n "Those who calmly stroll through their uneventful lives, the ones who meander from this interest to another, they who walk in the shadow of others more notable than themselves, and so on."

    n "As for me... I was the type who ran. The people I wanted to be with, what I wanted to do with my life, where I wanted to be, I knew the answers to all those questions."

    n "I had my worries and concerns, of course, but those meant nothing when living with such purpose. My ambition was what set me free. For those fleeting years of my childhood, I was unstoppable."

    n "Three years ago, that world ended."
    
    nvl hide dissolve

    nvl clear
    
    return
    
label en_C1:

    scene bg school_gardens_ss #black
    with dissolve
    
    play music music_miki fadein 4.0 # start with Miki's theme
    
    window show

    play sound sfx_can_clatter
    
    "The rattle of a can hitting the vending machine rings out across the empty school grounds. With the orange of sunset settling over the campus, everyone's retreated to their dormitories and homes for an early start to their studying and various hobbies."

    "Without much else to do, I wander through the gardens while drinking to make the best of the unusually quiet surrounds."

    "Summer's biting particularly hard this year. At least, that's what everybody's been complaining about lately. I don't really see the problem, but I've always been more used to hot weather than others."

    "With little around me to think about, beyond the occasional sip from the can, my mind turns to something that has been bugging me."

    "Every day feels the same. The school week begins, I attend classes, school week ends. Laze around for the weekend, and then it all repeats once more. 'Stagnant' is probably the best word for it."

    "It's not that I hate such a life. Compared to how I've lived before now, it's something I feel I should probably treasure."

    "But my life is also finite. No matter how blissfully unaware I am of it, time still passes. Maybe it's summer holidays that've focused my thinking, or maybe the exams beforehand. Either way, this way of living will end."
 
    scene bg school_track_ss
    with locationchange
    
    play ambient sfx_park fadein 1.5
    $ renpy.music.set_volume(0.5, 1.5, channel="music")
    
    "Emerging through the line of trees separating the track from the main grounds, the movement of a lone person immediately catches my eye."

    "His figure casts a long shadow in the evening's light as he slowly runs along the far side of the track. Looks like it's hard going, with his arms swaying to and fro as he valiantly pushes himself onwards."

    "I idle up to the side of the track and take another swig. It's a welcome distraction from my troubling thoughts."

    "As he comes around the corner, it's possible to finally get a good look at him."

    "I'd recognise those dishevelled locks of Hisao's anywhere. While his natural habitat may be the classroom, I've seen him spluttering around the track alongside Emi a couple of times before."

    "Dressed, as always, in his shirt without the bothersome jacket, it's clear that he has a nice build. That said, despite his solid chest and broad shoulders, there's an unassuming air to him. Perhaps it's due to his rather plain face, or just his subdued nature from having recently changed schools."

    "Without anything in particular to say to the boy, I just take another sip of my drink as he continues up the track."

    "Maybe the normal thing to do here would be to cheer him on for throwing himself at the track with such gusto, but it really doesn't look like he's enjoying the ordeal."

    "His running form is becoming worse and worse, and his speed is noticably slowing. Even the bird that's swooped down to peck at something left in the grass doesn't bother moving as he runs by."

    "It reminds me of how I used to throw myself at the track, running however many laps I could before I broke from exhaustion."

    "I move to take another swig from my can as he comes back around, only to find it lacking. With my attention briefly diverted from Hisao to my sadly empty drink, I'm take mildly off guard as he stumbles off the track and comes to a haphazard stop just ahead of me."
 
    stop music fadeout 4.0
    
    $ renpy.music.set_volume(1.0, 4.0, channel="music") # restoring music volume
    
    hi "Can I... help you...?"

    "Not knowing if he'd even be able to hear me past his panting, I let him collect himself for a few seconds before answering."

    mk "Just watchin'."

    hi "Yeah... I can see that."

    "He clutches at his knees and tries his best to regulate his breathing, but it's in vain. It's when he clutches at his chest and his breathing noticably rises in pitch that I start to get a bit worried."

    mk "You okay? Looks like you kinda overdid it, there."

    hi "I'm fine. Totally fine."

    "If he's going to be like that, all that I can do is take a step back and let him recuperate."

    "Beyond his breathing and a slight breeze in the trees, there's nothing to be heard. It reminds me just how alone we are, likely being the only two people in the entire school grounds right now."

    "After who knows how much time, he finally manages to compose himself and stand upright, sweat still tricking down the side of his face. There's a sickly wheeze to his breathing, but I don't think he wants to be reminded of it."

    hi "Miura, right? I'm Hisao Nakai."

    mk "The mysterious transfer student himself. Pleased to meet ya."

    hi "What brings you out here, anyway?"

    mk "Just grabbin' a drink. You?"

    hi "Missed my morning run. E... I mean, Ibarazaki, said I should run in the evening to make up for it."

    mk "Don't worry, I know Emi. Damn near all the school does."

    "I nod towards the track, the bird still out there trying to drag a left over food packet away."

    mk "Just how long have you been out here?"

    hi "A while. I should probably just cut my losses and get dinner, but she'd kill me if I skipped out."

    mk "Man, just give up."

    "Come to think of it, this might be a good chance. Dinner alone is boring, and if I can twist him into paying for a meal, all the better."

    mk "If you're hungry, I know a good place if you're up for it."

    "He looks a little startled by the suggestion, running a hand through his hair as he tries to settle himself down and think things through. I can practically see the gears turning in his head as he selects his choice."

    mk "C'mon, a hot girl's asking you to eat with her. You're gonna refuse that?"

    hi "They say modesty is a virtue."

    mk "Never said I was a virtuous person."

    "May as well wait things out as he continues with his deliberation, as I'm pretty confident I know what the reply will be. Sure enough, he finally comes up with an answer."

    hi "Fine, I'll go along with you."
    
    stop ambient fadeout 2.0
    
    #centered "~ Timeskip ~" with dissolve
    scene bg suburb_shanghaiext_ss
    with shorttimeskip#locationchange
    
    "The Shanghai's location within the nearby town has always been convenient. I had thought even this might be too much for Hisao given his exhaustion, but he managed to drag himself here just fine."
    
    play sound sfx_storebell

    scene bg suburb_shanghaiint
    with locationchange
    
    play music music_daily fadein 1.0 
    
    $ renpy.music.set_volume(0.5, .5, channel="ambient")
    play ambient sfx_crowd_indoors fadein 1.0
    
    "I like the uniforms they have here, even if they do strike me as a little unconventional. Our meals placed before us, the waitress takes her leave to attend to a handful of other customers at the opposite end of the cafe."

    "Not being especially hungry, my meal's just a slice of pie and a drink. Hisao's pack of sandwhiches don't look like it'll last for long, one of them already having disappeared into his mouth."

    "He catches me staring, awkwardly holding the next midair while looking mildly embarassed."

    hi "Sorry, I just..."

    mk "It's normal to be hungry after exercise, man. Go ahead and stuff your face."

    "Hisao obediently does so, though with a touch more delicacy than before."

    mk "So what's the story with Emi, anyway?"

    hi "She just pushes me to exercise with her sometimes. Guess she enjoys the company. I mean, like you do now."

    mk "Doesn't seem like you enjoy the experience much."

    hi "Well, I do want to get back into shape. As much as I can, anyway."

    "He pulls his cuff up his arm a little, taking a loose flab of skin from his forearm and giving it a pinch as he frowns. He sure is pale under his shirt, though maybe I'm not the best judge of that."

    mk "You sure found the right person if you want to be whipped into shape. Just make sure she doesn't kill you first."

    hi "Believe me, she's come close."

    "His tone is way too serious for a throwaway joke. Surely she's not that much of a slavedriver."

    "Taking a bite into my own food, it turns out I'm surprisingly hungry myself. The two of us end up stuffing down our food in no time, crumbs littering the table in the aftermath."

    "With dinner finished, Hisao leans back in his seat and contentedly pats his stomach. I run my finger around the inside of my mouth to work out the remnants stuck to my teeth, savouring the taste of the last little bits I manage to find."

    "At first I take Hisao's staring out the window to be a sign of boredom, but one careless glance gives his game away. He's trying to distract himself from the bandaged stump resting on the table."

    "I'd hardly think worse of someone for looking at it; being distracted by something out of the ordinary is completely normal. I just give a smile, hoping to make him relax a bit."

    hi "Sorry."

    mk "Believe me, you're not the first to notice. It's not like a missing hand is exactly subtle."

    "Hoping, and succeeding, to defuse the situation a bit, I grin and waggle my stump in the air a little to emphasise the point. It's delightfully easy to read Hisao's emotions, even when he's trying his best to suppress them."

    hi "I still have no idea what to make of this place."

    mk "Town, or Yamaku?"

    "He just raises an eyebrow."

    mk "What's the problem with it?"

    hi "Hmm... I think 'confronting' would probably be the right word."

    hi "It's not every day you see someone with half their face heavily scarred, or have to try and communicate with someone who can't hear. Then there's the obvious example of Emi."

    mk "Well, I mean, you're not wrong. Being a transfer student would make that a lot worse, too."

    mk "Try coming at that from another angle, though - what're we doing now?"

    hi "Chatting at a cafe?"

    mk "And what'd you do today before that?"

    hi "Woke up, got dressed, went to classes, had lunch and tea in a club room, more classes, went to run on the track, and then started chatting with you."

    mk "Isn't that a pretty normal high school day?"

    "He moves to protest, but finds himself searching for words. However reluctantly it may be, he backs down once he realises that I have a point."

    mk "You'll get used to it soon enough. If everyone else at school seems cool with it, that's only because we all had a head start of years."

    hi "And if I accidentally offend someone? I almost did just then, remember?"

    mk "Then... so what? Just find someone else to talk to. There's hundreds of people here to pick from. Hell, you're talking to me easily enough."

    hi "A pretty normal high school, huh..."

    mk "Exactly. Just pick up some friends, find your groove, and ride the rest of the year out. You'll be fine."

    "He turns to look out the window, reflecting on the conversation. That expression of contemplation suits him well."

    "Evidently coming to a conclusion, he gives a nod before turning back to me."

    hi "Thanks. I'll keep that in mind."

    "The smile he gives me is kinda sweet. Weak, but terribly sincere. All I can do in response is give a satisfied grin back."

    "Such a chance meeting might not change much for me, but if I can help Hisao get on the right track, at least I'll have been useful to someone."

    "The weather really is nice today."
    
    stop music fadeout 2.5
    
    stop ambient fadeout 2.5
    $ renpy.music.set_volume(1.0, .5, channel="ambient")
    
    window hide
    
    scene black
    with dissolve
    
    return
    
label en_C2:

    scene bg school_gardens3
    with dissolve
    
    play music music_soothing fadein 0.25 # [str]
    
    window show
    
    "I find myself lazily sitting at the base of a particularly tree in the school gardens, making the most of its shade while watching the goings on ahead."

    "With the events over and medals dispensed, the people gathered for the track meet have now fanned out over the grounds. Runners excitedly talk with their friends and parents, with the handful who have romantic interests in the other participating school using the opportunity to catch up on more affectionate matters."

    "It's nice. In fact, I prefer this atmosphere to the competitive nature of the track meet itself. People just catching up with others, having a nice time as the importance of who won or lost whichever race fades away."

    "Without much else to do, I idly toy with the medal on my chest. First place was a lost cause; Emi's in another league when it comes to sprinting, after all. Silver still ain't bad, especially given that I'm hardly the competitive type to begin with."

    "I wonder what metal this thing is actually made of. Tin, maybe. I flick it a couple of times to try and guage the sound, but it's no use."

    "A shadow crossing my vision grabs my attention, but I needn't have bothered looking. The owner just keeps on walking towards the main building, her empty sleeves swaying in the breeze."

    "Looking back to where she came from, I see a familiar face slowly strolling around the grounds. Given that he isn't in gym uniform, he's probably only here because of Emi."

    "I feel a little bad for him. Sure, he's around the student council and Emi a lot, but that feels more like he's being bossed around than actually choosing to hang out with friends. Not that I'm innocent, I guess."

    "The thought of something some of the guys in the club had hastily arranged comes to mind as I mull over the situation."

    "I come to my feet after making my decision, striding past a gaggle of gossiping girls and calling out to him."

    hi "Oh, Miura. Hey."

    mk "Got dragged here by the shortie, eh?"

    "Hisao just hangs his head as I saunter up to him. He's pretty transparent."

    "It's always struck me how out of place Hisao seems around the track club and other sports stuff. He said he liked soccer when he introduced himself in class, but it's kinda hard to imagine such a passive and subdued lad running around a field and being boisterous."

    "It makes me wonder what he'd be doing with himself if Emi weren't dragging him around by the scruff of the neck."

    mk "Least she put on a show for you."

    hi "Has she always been that good at sprinting?"

    mk "Yep. She puts in the hours on the track, so it ain't surprise that it pays off. Fastest thing on no legs, and all that."

    hi "Still, it looks like you did fine yourself."

    mk "It's something. You hang around the club and look decently built; I'm surprised you didn't run in some race or another."

    hi "You saw me the other day on the track, didn't you?"

    "The face he pulls makes me feel bad for bringing it up. This being Yamaku, it isn't hard to think up reasons why he might have problems in that area."

    mk "Forget I asked. There is another reason I wanted to talk with you, actually."

    mk "Most of the track club's going to a karaoke place this evening to hang out. There's space for you, if you wanna come."

    "Hisao looks genuinely startled, but I think it's in a good way."

    hi "I was going to study..."

    mk "C'mon, it'll be fun. Some of the other guys want to know who you really are too, y'know."

    hi "I somehow doubt I'm that interesting."

    mk "Mysterious transfer student who keeps hanging around the track with Emi? What's there not to be curious about?"

    "He wavers a little, but eventually throws his arms up in surrender."

    hi "Alright, you got me. I'll come."
    
    stop music fadeout 1.5

    scene bg city_karaokeint
    with shorttimeskip

    "The moment we all entered the dimly-lit room, we started acting as if it were home. People laid on the couches, draped themselves over the arms and backs to talk to friends, threw snacks and drink bottles to each other, and generally made a din from all the arguing over the day's events."

    "Now that some time has passed, with the excitement and adrenaline of the track meet ebbing, things have finally settled down a little. The dozen people around make-do with gossiping while lounging around on the garishly coloured seats, occasionally cheer or jeer at whoever's up front belting out some crappy song or another, and busily chat the night away."

    "Not that I'm excluded, with Hisao seated to my right and speaking up to be heard over the atrocious number being sung to a chorus of laughs and teasing."

    hi "If you don't mind me asking, where are the girls from club? I'm sure I saw a couple besides Emi at the track meet, but only the guys are here."

    mk "What, you lookin' to pick up?"

    hi "I just transferred in, I don't move that quickly."

    mk "Come on, you could do worse than the girls in the track club. Fitness does wonders for you-know-what, after all..."

    "He gives me a flat face, but I detect a hint of embarrassment in it. Guess he's a bit of a prude."

    mk "They're just busy. Supposedly. Maybe it was too much of a sausage fest for them."

    "He moves to say something, but as the guy singing ends his round, the next beckons for Hisao to join him as he walks up to the mic. Yukio Hasegawa, nothing less than perhaps the most popular guy in track club. He's always cut graceful figure for a man, bearing slim, refined eyes, impeccably groomed hair, and a gentle face. Far from my type, but other girls seem to gush over him."

    "The others in the room, whether out of curiosity, friendliness, or teasing, quickly join in to try and make Hisao perform. The guy himself doesn't look enthused, but I suspect that's as much due to the pressure as the actual act."

    mk "You should do it. What've you got to lose?"

    hi "My dignity. I can't sing, you know."

    mk "What, you think any of us can? Stop being lame and just have some fun."

    "I put my hand on his back and give him a sharp push off his ass, jolting him into the center of the room. It's only momentary, but as he recovers, he throws an odd glance back to me afterwards. His anxious, almost scared, face leaves me speechless."

    "Everything returns to normality in a flash, the boy taking a breath before marching around the table and up to the mic with back hunched and feet dragging, waving down the cheers of those around him as he does. Whatever was going on in his head, it was far beyond just being shy."

    "With nobody else seemingly having noticed, all I can do is sit back puzzled in my seat and take a swig from the soft drink in front of me."

    "As the music starts up and the vocals kick in, it becomes obvious that the two are far from practiced at this. Their voices might not be bad, but they're horrendously out of key. Hisao's shyness is getting the better of him too, which only looks worse next to Yukio's confident demeanor."

    "From the corner of my eye, I notice the guy to my left leaning forward, his face turning to mine."

    "Named Haruhiko, though everyone calls him Haru, he's a follow classmate who also had the misfortune of being stuck on the first row of tables. While he may be quite gifted physically, being decently tall and strong, he's far from the sharpest tool in the shed. It matters little, though, as his endearing cheerful nature and eternal optimism cover for whatever shortcomings he may have."

    har "So, what's the over/under on the new guy?"

    "I set the drink back on the table, my hand rubbing my neck as I lean back. I don't know what answers he's expecting, but I doubt I'll be able to give him any."

    mk "You're asking me?"

    har "You're the one who invited him, you know."

    mk "He paid for my lunch, so I felt like I owed him. That's all there is to it."

    "The corner of his mouth tugs upwards. Just a little."

    har "You being honorable. There's a first."

    mk "Prick."

    mk "So do you know anything about him? All I know is that he's a nerd who gets bossed around by the shortie and the student council."

    har "Heard he used to play soccer. Not half bad at it, either."

    mk "Used to?"

    har "Somethin' wrong with this."

    "Haru glances to the two at the front of the room, both of them being far too distracted with their attempts to make something resembling a decent song to pay us much heed. Satisfied that we're communicating in private, he jabs at his chest with his thumb a couple of times."

    har "He had a heart attack. Real bad, too. Emi'd probably know more. Or the guy himself."

    "He adds the last suggestion as an afterthought, though understandably so. Plenty in Yamaku have their bugbears about what's happened to them in the past, though I'd be damn hypocritical to complain about it."

    mk "Come on, a heart attack? At that age?"

    har "It happens."

    "I expect him to admit that what he heard was some vague rumour or something, but he just shrugs and looks at me matter-of-factly."

    "What would Hisao be, 17? 18? That's the kind of thing you hear taking out frail old folks. Natural causes, and all that. Now that I think of it, maybe that explains why he got puffed so easily back when I saw him at the track."

    mk "Shit..."

    "It's kind of pathetic, but that's all the response I can muster as I lean back in my seat. Haru just lets out a dissatisfied sigh, equally put off by the idea."

    "Looking back at the duo finishing up their song at the front of the room, I can't help but see him in a new light."
    
    window hide
    
    scene black
    with dissolve
    
    return
    
label en_C3:
    
    scene bg school_library
    with dissolve
    
    window show
    
    "If I had to choose which room embodied the feeling of this school the most, it'd have to be the library."

    "It looks normal, at a glance. Large, sure, but otherwise normal. It's only when you start walking through the aisles that you realise the odd little allowances for the students. Audiobooks, braille books, wider passages, and the like. Then there's the cane or two propped against the desks of reading students."

    "There's also the old-fashioned stuffiness, too. Doesn't help that the literature club students are all quiet as mice, but it's something more than that. The furniture, staff, and general mustiness of the older books are all stifling."

    show suzu basic_concerned at centersit
    with charaenter
    
    "My eyes eventually fall on the girl across the table from me. 'Unremarkable' would perhaps be the best description of how she appears, save for the bags under her eyes and brace on her knee. For Yamaku, though, that's doing pretty well."

    "If I had to choose which pose embodied the personality of Suzu the most, it'd have to be her chin resting on her hand as her eyes lazily scan the manga magazine in front of her."

    "The girl looks up, her eyes meeting my own. Her reaction, or lack thereof, is about what I'd expect."

    show suzu basic_speak at centersit
    with charachange
    
    suz "Staring is rude."

    mk "I dunno how you put up with this place. Don't you have anything more exciting to do with yourself?"

    show suzu basic_concerned at centersit
    with charachange
    
    "She sighs as I start to rock back and forth on my chair to occupy myself. With nobody else willing to brave the heat, the track club's been largely abandoned for the day. I can think of better things to do than throw myself around an empty track."

    "Then again, the literature club sure makes a dull sight. The closest thing I can see to an actual club activity is half a dozen students sitting around a table quiet discussing some book or another."

    mk "Why don't you join them?"

    "Following my nod, she glances to her side and back with a minimum of effort, not even bothering to lift her head from her hand."
    
    show suzu basic_suprised at centersit
    with charachange
    
    suz "Because I'm busy reading this."

    mk "Isn't literature club for discussing literature?"
    
    show suzu basic_concerned at centersit
    with charachange
    
    suz "Most of us just read whatever. As long as we're quiet and in the library, nobody really cares."

    mk "So that's all you're gonna do? Read manga?"

    "I was sincerely hoping she'd suggest something for us to do, or maybe even socialise, but she simply shrugs and goes back to reading. It's hard to say whether it's out of apathy or being too tired to do much more than this."

    "Then again, I'd be more surprised if I could gauge her feelings. The kind way to describe her would be 'ambivalent', but after a year of being around her, I've settled on a diagnosis of 'possible lobotomy'. That air of quiet disapproval never seems to leave her."

    "As she slowly turns the page and continues her reading, a familiar voice draws my attention to the end of the library."

    "The tense voice of Ikezawa, hunched over on a beanbag in her usual little corner, isn't difficult to distinguish. Hisao sits on the floor beside her, a disarming smile on his face as he softly tries to chat."

    "I can't quite pick out their conversation, but the fact that they're having one at all is pretty impressive."

    "Suzu turns back around as I stop my gawking, her own interest apparently having been piqued."
    
    show suzu basic_suprised at centersit
    with charachange
    
    suz "She seems to like him."

    mk "Yeah, they get on well."

    "I might say that, but I have my misgivings. There's more than one story of when girls have tried getting close to her, only for things to go bad for all involved. How much of that is actually true or just gossip, I have no idea, but it's plainly obvious she has a lot of baggage."

    "It might be rather hypocritical, but I don't have much want to get involved. With the way I am, it could only go badly."

    #show hisao invis at rightedge
    #with None
    
    "Hisao comes to his feet as their conversation apparently ends, returning from their sanctuary at the end of the library. As he walks by us, a couple of thick novels held to his side, I give a short whistle and motion for him to come over."

    show suzu basic_concerned at twoleftsit
    with charamove
    
    #show hisao basic_suprised at tworight
    #with dissolvecharamove
    
    hi "Odd to see you here."

    mk "Well aren't you quick on the uptake?"

    mk "C'mon, take a seat. I need someone for company who has still some life left in them."

    "Hisao obediently does so, taking a seat and plopping his books down in front of him. A couple of sci-fi novels, by the looks of them. Not terrible taste. An improvement over Suzu's girly stuff, anyway."

    "Suzu briefly takes her head from her chin to see the new face. I decide to seize the chance."

    mk "Hisao, this is Suzu Suzuki."

    "He gives a warm greeting, to which Suzu simply gives a quiet nod, having reverted to her more shy self. He seems a little more sedate than the other friends from track club, so hopefully she'll open up to him a little more than them. Given time."

    hi "So you're into manga?"

    suz "Are you?"

    hi "A little. To be honest, I don't really follow any of the serialised stuff any more."

    suz "I see."

    "With Suzu leaving no opening for the conversation to continue, Hisao leans back from the table in disappointment and reaches for one of his books. It's a little sad to see things end this way, and I have told her not to be so antisocial."

    "Frustrated, I lean over the table, close my fist, and begin rubbing my knuckles into the top of her head."

    suz "Ow. Ow. Ow."

    hi "Uh, Miki..."

    mk "What have I told you about being like that?"

    "I'm not using much force at all, but her reaction's enough to make me back off rather quickly. The point's been made in any case."

    hi "So you're into shoujo, then?"

    suz "Is that bad?"

    hi "It's normal enough. Watch the shows?"

    suz "Yeah. This one's getting an adaptation soon which I'll have to catch."

    hi "Doesn't that stuff air pretty late?"

    suz "My sleep schedule's all over the place anyway."

    "He's clearly resisting snark given how tired she visibly looks, but wisely thinks better of it."

    mk "Didn't get much of that stuff on TV back where I came from."

    mk "So you used to read it, Hisao?"

    hi "It was good for killing time while wandering town. Didn't spend much time at home."

    suz "Your parents didn't mind?"

    hi "Both of them worked long hours, so not really."

    "There's a gulf between their concepts of what parents would allow, but it's understandable. For someone as pampered as Suzu, being let to wander so much must be a pretty strange idea. I suppose Hisao's a bit like me in that regard."

    mk "Well, at least someone's familiar with the scene. Had practically none of that stuff back home, so it's largely foreign to me."

    mk "Speaking of people's homes... I see you were visiting Hanako's little corner. Tryin' to make inroads with her?"

    hi "'Trying' is the key word, there."

    mk "Don't look so beaten. You can hold a conversation with her, right? That's more than anyone else in the class has managed so far."

    hi "That's more to her friend's credit than mine."

    mk "You really need to learn how to accept praise."

    "My reply is a bit crabby, and admittedly not only because it's a bad habit. 'Hanako's friend' could only be referring to one person; the pretty blonde that she often meets after class. I'm a little jealous of him for getting so close to her so easily."

    mk "You know, you say it's weird to see me here, but what about you?"

    hi "Reading's my main hobby."

    mk "And running?"

    hi "That's... more like a sentence."

    "It's only because we're in the library that I stifle a laugh. Suzu might try to hide it, but the flicker of a smirk flashes on her face as well. True bonding, though the misery of others."

    mk "I guess you're all set for exams, then."

    hi "Why do you say that?"

    mk "You're with Mutou all the time, you know. Guy's got high hopes. You get ridiculous marks for most of your subjects, too."

    hi "That's because I work for them."

    "This guy catches on way, way too quickly. I might not pay attention in class, but he doesn't have to burn me like that. Suzu's attention is finally wrested from her reading material, looking genuinely impressed. As much as her stony face can, anyway."

    mk "That's harsh, man."

    suz "You're strongest in math and science, correct?"

    hi "Yeah."

    suz "Could you look at something I couldn't get when we go back to class?"

    hi "Sure, no problem. Doesn't hurt to work it all out before exams come up."

    "Exams. I hate that word. The mood of the class has already begun to sour thanks to the anxiety and stress they cause, and it's only going to get worse in the weeks ahead."

    "At least they're useful for something. If studying's going to be how she expands her social circle, then all the better. Given how hard she works for her rather average marks, maybe he can help turn things around."
    
    #window hide
    
    return
    
label en_C4:
    
    scene bg school_cafeteria
    with shorttimeskip

    window show
    
    "I've always found the cafeteria to be a fun place to watch people."

    "Deftly manouvering through the rapidly filling room after being among the first to have their tray filled by the old ladies behind the counter, I can't help but glance around at the other students on my way to a free table."

    "By rights, the cafeteria should be a melting pot. Students from every club, class, condition, and year level are here, and with everyone in their uniforms, the differences between rich and poor, country and city, fashionable and unfashionable, fades to nothing."

    "But, people being people, they still find a way to stick to their cliques. The track club members form a clump as they playfully jostle one another, as do a bunch of the deaf students, huddling together in their impenetrable little social circle while signing in their silent second language."

    "There are the gaggles of popular girls with their posses, and the odd trio of less popular girls who stick to their few friends. The rowdy class clowns who loudly joke and act out, and the softly-spoke academics who keep to themselves while shuffling along. Everyone has their niche, even if that niche consists of only one."

    "Setting down my tray at an empty table, I separate the disposable chopsticks using the tips of my fingers as always. Strength comes in surprisingly useful when you largely rely on one hand for manipulation, with the two conjoined sticks easily splitting apart."

    "While I'd hesistate to say it's great, the food here is still pretty good. Filling, and by far satisfying enough to live on for quite a while. Can't complain about the price, either."

    "It doesn't take long for company to arrive after I've started eating, a familiar figure silently seating herself across the table from me."

    "Suzu simply begins to eat without a word. Such things aren't unusual with her, so I simply look down and continue with my own lunch."

    "As I shovel rice into my mouth, I find myself especially pleased with how they've cooked it today. Not too dry, not too sticky. Ditching the chopsticks and gulping down some soup, it turns out that they've done a good job on that too."

    "Whether Suzu's enjoying her lunch as much as I is, as always, a mystery."

    "Looking past her, two of the three stooges come into sight. With my hand taken, I end up waving my stump around in the air to get their attention. It does the job, with the duo changing course and heading our way."

    har "'Afternoon Miki, Suzuki."

    "Suzu pauses her eating to nod to the both of them, as do I. Hisao moves around to take a seat beside me with his juice and a packet of bread, while Haru manouvers himself to the end of the table holding a suspicous plain cardboard box with equally suspicious care."

    mk "What's with that?"

    "Hisao just shrugs as I lean over and ask him. Haru just gleams a smile in response, setting down the mystery box and lifting the top off with practiced ease."

    "As the sides fall away, a gorgeous looking red and white spongecake is revealed. A thick layer of cream separates the two layers of sponge, and another sits atop the cake. Big, succulent strawberries circle the outer rim, each sitting on its own further blob of cream. Finally, a light dusting of frosting covers the cake, like a thin shower of snow."

    "It's... beautiful. As expected of Haru."

    hi "You're drooling."

    mk "Don't care, gimme that thing."

    "He might be criticising me, but Suzu's attention is just as focused. Her sweet tooth is getting the better of her as the cafeteria food before her languishes."

    har "Right, right, just hold on a moment."

    "He takes the plastic knife cunningly carried inside the box, and sets about cutting a few slices. Look like the cake's already had a good third eaten."

    mk "So what's the story?"

    hi "Who's?"

    mk "Let's start with the cake."

    har "Made too much during home ec class. The teacher doesn't mind me baking my own stuff there as long as she gets some."

    hi "So you're into baking?"

    har "Sure am. Might not have many talents, but I'm good at the ones I have."

    "As he gets back to cutting it up, I look around for an answer to the second question on my mind; where the third stooge has gotten himself to."

    "As my eyes fall on him, I can't help but give a weak grin. Suzu notices my staring and twists her head around to see, but turns back to the cake in short measure."

    "Sure enough, he's standing around chatting up a couple of girls. I might not see the appeal in his appearance, but I can admit that he pulls off an air of confidence well, even without hearing what he's saying. Going by the bashful smile of the long-haired girl as she toys with her hair, and the other's excited chatting, he's making good progress with both."

    hi "Is he always like that? I swear he was with a couple of other girls last week."

    mk "Believe me, you have no idea."

    "Some people bake, some run, some study, and some pick up women."

    "As if he'd heard me, Yukio looks up from his companions to see Hisao and I staring. Sensing an escape, he nods to us and seemingly explains that he wants to come our way."

    "The girl with longer hair is about to follow him over before her friend stops her, gesturing at me while frowning. It's hard to be hurt by something you deserve, and as they both quickly decide to walk off, I can take solace in that at least my reputation's helped Yukio."

    yuk "And how are we today, ladies and gents?"

    hi "Good."

    har "Good."

    mk "Good."

    suz "Good."

    yuk "Don't be too enthusiastic, now."

    "He takes a seat beside Suzu, giving her a brief disarming smile as he does. She visibly wilts, despite doing her best to avoid doing so."

    "Haru looks back to the cake, but frowns as he begins to cut another slice."

    har "Hmm. We'll have one more slice than we have people. Should've worked that out first."

    mk "Dibs on the double portion."

    har "Piss off. Suzuki gets double."

    suz "Uh... thank you."

    mk "Hold on, what's the criteria here? Is it because she's a girl?"

    har "A polite young girl, yes."

    mk "What about me? I'm a girl too."

    yuk "Only when it suits you."

    "I get up out of my chair to get some height over him, which he responds to in kind."

    mk "Oh yeah? How about you try having periods?"

    yuk "Piss off, we have to-{w=.5}{nw}"

    mk "Look at me, I'm a man, oh no I have to shave my face, I have dreams that give me orgasms, how terrible~!"

    yuk "Well maybe you'd be treated like a girl if you actually acted like one!"

    mk "Huh? What's that? I can't hear you over bleeding from my genitals and feeling like I've been sucker-punched in the gut once a month!"

    yuk "You're making my point for me! If you didn't go on about your bloody periods while we're eating, we'd-!{w=.5}{nw}"

    mk "Maybe I'd act more like a girl once I got free crap for being one!"

    hi "Miki, Yukio, please..."

    "Hisao looks to Suzu for help as we snarl at each other, but all she's doing is burying her face in her palm and trying not to exist."

    "I want to thump Yukio for being an ass, but in contrast to the busy hum of students of before, the sudden silence around us that reminds me that we're in the cafeteria. Submitting to Hisao's begging, we both fall back into our seats, neither of us admitting that the argument is over."

    "As if the altercation had never happened, Haru passes the extra slice to Suzu, earning a shy nod of thanks. It only serves to make Yukio all the more pissed for some reason, but before I can step in to defuse the situation, Hisao does the job for me."

    hi "What brings you here anyway, Yukio?"

    yuk "Oh, it's a woeful tale. A terrible curse has struck me yet again. Day after day this happens, and only so rarely can I find refuge from its grip."

    "He's totally making an ordeal out of it, clutching at his chest and emoting as hard as he can. Even if it's for an audience of one, he still likes to play the orator. It's a shame he stopped acting, really."

    yuk "I'm just... too popular."

    hi "What."

    yuk "Girls just fall over themselves for me. It's been like this ever since high school started, and if anything it's only become worse."

    yuk "Oh, what I would do to get those women off me! I tell them I'm not interested, but it only makes them try all the harder."

    hi "You can't be serious."

    "Haru begins to come around each of our seats, setting down a slice before each of us before sitting beside Hisao. I quickly tuck into mine as soon as I can, the wonderful taste of cream and strawberries filling my mouth. Befriending this guy was one of the best decisions ever."

    "Mor" "It's true. He ended up quitting drama and switching to the track club just to lower his profile." # who? [str]

    "Hisao suddenly clicks his fingers in a flash of insight."

    hi "Ah, that explains it! I knew that face on the posters was yours. You must still work for them sometimes, right?"

    yuk "Yeah, though it's mostly organising new recruits and helping with behind the scenes stuff. They probably just use my face to draw in a bigger crowd..."

    "His smile fails him as he looks down at his dessert, a cloud of despair hanging overhead. I wonder how many girls he'd get if he let this side of himself show through more often."

    yuk "Man, it really is a pain. Those girls are so loud and obnoxious, I can't stand any of them."

    mk "I might not the best judge, but I don't really understand your appeal. Physically, at least."

    har "You don't?"

    mk "You do?"

    "I see an opportunity to both tease him and stroke my own ego, and so take it without hesitation."

    mk "Hmm... who do you think is hotter? Me, or Yukio?"

    "I lean around Hisao and stare intently at Haru, with Yukio reluctantly doing the same."

    "Haru's taking this surprisingly seriously, his head moving between our faces with a look of total concentration as he brings his fingers to his stubbled chin. Seconds pass, with Hisao and Suzu's interest obviously piqued as they stare and eat at the same time."

    "Everybody's on tenderhooks as we await his judgement, with Yukio's face slowly moving further and further back."

    har "I'd have to say Yukio."

    "I'm a little disappointed in the answer, but the look on Yukio's face more than makes up for it."

    yuk "That's a joke... right?"

    har "Not at all. I can definitely see why girls like you."

    yuk "You're the last person I wanted that kind of praise from."

    "Smiling at his discomfort, Hisao finishes his cake and gives due compliments to Haru, which I hurridly second."

    mk "Come to think of it, haven't you got lots of female friends, Hisao? Maybe you could give the stud here some tips on how to friendzone like a pro."

    hi "Thanks..."

    yuk "I'm not interested in keeping them as friends, I just want them to piss off."

    yuk "Here."

    "He plucks the strawberry off his dessert and plops it on top of Suzu's uneaten slice. She doesn't even notice, given her attention being focused on trying to get through the first without dropping crumbs everywhere."

    "He waits for a reaction to his act of kindness before giving up and hanging his head in defeat. I don't think Yukio is having a good day."

    mk "Well, there you have it, Hisao. These are the losers I hang out with."

    hi "They're not so bad."

    "Haru clamps onto Hisao's shoulder and gives him a playful shake. It's nice to see Hisao loosening up, even if it is just a little."
    
    window hide
    
    return
    
label en_C5:

    scene bg school_scienceroom
    with shorttimeskip
    
    window show
    
    "Walking into class, my gaze immediately falls to Suzu's desk. Each and every morning she enters class long before I do, and though I might have hoped to catch her out, today is no different than any other."

    "It's one of life's small wonders; I never did understand how someone in a perpetual state of sleep deficiency manages to get here on time every day. Well, it's not that I don't understand how, so much as why."

    "I suppose it's a lie to say that nothing at all is different, though. Her head may be resting in her hand as it always is, but rather than looking out the window, her eyes are on the guy casually speaking with her in front of her desk."

    "Suzu and Hisao took to each other surprisingly quickly. She doesn't seem particularly interested in actually conversing, but just giving him the time of day is more than she gives the other guys in the track and field club. 'Boorish', she calls them."

    "Which isn't wrong, really."

    mk "Yo."

    #show hisao basic_suprised at twoleft
    show suzu basic_suprised at tworight
    with charaenter
    
    "The two of them react in unison to the sound of my voice, Hisao turning his body towards me as Suzu moves little more than her eyes. Their normal morning greetings come to a halt almost as soon as they begin."
    
    #show hisao basic_smile at twoleft
    show suzu basic_concerned at tworight # i should probably make more neutral and bored face for her [str]
    with charachange
    
    "Suzu just sighs as Hisao's face, as it so often does, turns to mild concern."

    hi "Are you... okay?"

    mk "Huh?"

    "He motions to his left cheek, my own fingers mirroring his out of reflex. It takes me a second to realise what he's referring to. I haven't looked in the mirror, but there'd no doubt be a nice big bruise there right about now."

    mk "Haha, this? I kinda got a bit rough with another club guy. We're cool, don't worry."
    
    show suzu basic_suprised at tworight 
    with charachange
    
    suz "Again?"

    hi "...This happens often?"
    
    #show suzu basic_speak at tworight 
    #with charachange
    
    suz "You have no idea."
    
    show suzu basic_concerned at tworight # i should probably make more neutral and bored face for her [str]
    with charachange
    
    "I disarm him with a stupid grin as I scratch the back on my neck."

    hi "Both of you seem rather accident-prone."

    hi "Then again, maybe accident isn't the right term to use for you."

    "The loud clapping of hands behind me would make me jump if it were less obvious who said hands belonged to. As Mutou clears his throat and tries to shepherd the gossiping class into their seats, Hisao obediently takes his leave of us and I turn to take my seat."

    #hide hisao
    hide suzu
    with charaexit
    
    "The fact he's addressing the class rather than me is cause for a mental sigh of relief. He wouldn't take kindly to casual talk of a scrap between students, and his classroom lectures are boring enough without being subjected to another on the subject."

    show muto irritated
    with charaenter
    
    mu "Oh, and Miura? I'll see you after class."

    "Damn it."

    scene bg school_gate
    with shorttimeskip
    
    "Jogging past the school gates, Suzu and Hisao can be seen patiently waiting for me. By now the main throng of leaving students has passed, reduced to to little more than the occasional person or two."

    suz "Have fun?"

    mk "Detention on Monday. What a pain in the ass."

    hi "At least it's Saturday, right? You've got a stay of execution for a couple of days."

    mk "Whatever. Let's just get lunch."

    suz "Shanghai?"

    mk "Yeah. You okay with that, Hisao?"

    hi "Sounds good."

    "The decision made, we set off down the hill for the local town."
    
    scene bg school_road
    with locationchange

    "I like this time of year. The weather, hot with decent but not overbearing humidity, reminds me of home. It also means being able to wear summer outfits, which are far more comfortable than winter clothing."

    "It's hard to tell if Suzu's fidgeting is because she's uncomfortable around Hisao, or just because she hates the heat. She's a winter kind of person after all, in every way."

    "Even Hisao, the rookie, looks more casual than she does. That said, he has the undeniable air of a tourist about him; eyes flitting about, pace just slightly slower than what looks natural, head turning this way and that."

    mk "Where you come from, anyway? You aren't a local, that's for sure."

    hi "The city. The quiet of places like this is a big difference."

    mk "Hah, a city boy. Should've known."

    hi "I take it you're from somewhere else, then?"

    suz "She's a hick from up North."

    mk "Hey."

    suz "Well, aren't you?"

    "I don't want to let her get away with it, but from the interested face Hisao's making, she's already won this."

    mk "We can't all be dainty spoiled princesses..."

    hi "You make it sound like you're from out in the sticks or something."

    mk "I am, dude. Tell you what, the first time wandering around the city near here was a big culture shock."

    "His reaction is kind of charming. He has no idea at all what a country life is like, no doubt desperately mining his brain for any images that he can muster."

    "Not that Suzu's any different. I don't really care to explain it to either of them; it's not something I take particular pride in, and bringing her there to visit would only cause problems."

    mk "Oh yeah, I noticed you chatting with the guys in the track club yesterday. You ever going to actually join, or what?"

    hi "Do I have to? I don't remember it being compulsory."

    mk "That's not what I'm asking! Urgh."

    hi "Maybe I should just join the literature club and wash my hands of the whole thing."

    suz "Yes, do that. The school hardly needs another jock running about."

    mk "Oi, doesn't that make me a jock?"

    hi "To be fair..."

    "I clap the boy over the head, drawing protests from him. The last thing I need is another Suzu on my case."

    suz "So violent."

    hi "Very violent."

    "I'm beginning to think I've created a monster by bringing these two together."
    
    scene bg suburb_shanghaiext
    with locationchange
    
    "By the time we reach the Shanghai, I feel like I've run the gauntlet with the two of them pecking away. Suzu throws the odd snark while alone, but she and Hisao egg each other on."

    "I don't really hate it, though. It's maybe even a little cute."
    
    play sound sfx_storebell

    scene bg suburb_shanghaiint
    with locationchange
    
    "The bell above the door gives its trademark rattle as we file in, the waitress's hurried shuffling towards us no less familiar. Look like the place is mostly empty, save for a handful of other patrons."

    "Maybe it's a good thing; if such a place can stay open for this many years and not shut down from the lack of customers, at least the staff aren't going to be too stressed. They keep their jobs, and the town keeps its little odd cafe."

    "When she reaches us, the waitress throws her upper body down in a sharp bow. Hisao flinches from how close she comes to headbutting him."

    yu "Welcome to the Shanghai! Please take a seat."

    "I give a weak smile as we go, picking an empty window-side table from amongst the many. Suzu shuffles into her seat and I slide in next to her, Hisao being relegated to the other side."

    mk "You've been here a few times now, right? You like it?"

    hi "The fact that Yuuko's here still weirds me out a bit..."

    mk "Haha, yeah. Lots of people say that. She's pretty at least, right?"

    hi "Guess so."

    mk "You gotta loosen up, man. You're a teenage guy, nobody's gonna believe that you don't have an eye for the ladies."

    hi "How should I answer, then?"

    mk "I dunno. 'I like her tits', 'she's got nice thighs'. Whatever."

    hi "...Is Yuuko looking at us?"

    suz "No, thank God."

    "I just smile at them. Looks like he's going to be just as easy to tease as Suzu is. Such prim and proper people, they are."

    "As they both recover from their fit of modesty, a more important matter comes to mind. I want to help him back on his feet, but if he'ss going to be around me for any length of time, he'll have to get used to Suzu as well. And vice-versa."

    "I stare to my companion beside me, making her tilt her head."

    mk "Wanna show him your party trick?"

    "She pauses for a moment to work out what I'm referring to. By her increasingly hesitant face, she's got the right idea."

    "After thinking on it for a good while, with Hisao's face curiously looking on, she comes to the conclusion I'd been hoping for."

    suz "If he's going to be hanging around, I guess we have to."

    hi "Show me what?"

    "I give him a disarming smile for a moment, before suddenly turning beside me."

    mk "BOO!"

    "All she does is raise an eyebrow. I have to admit I'm holding back a little; my mental block against possibly hurting her isn't that easy to get around."

    suz "That isn't going to work if-"

    hi "ARGH!"

    "Hisao leaping out of his seat and hitting his fists to the table as he shouts, albeit in a careful way given we're in public, has the intended effect. Suzu immediately jumps in fright, my own heart skipping a beat in sheer startlement."

    "With barely a second's delay, the life seemingly goes out of her. A sigh as the air from her lungs lazily passes her lips is all to be heard as her small body goes limp in her seat. Her head jerks downward as all control goes out of her neck, before her entire upper body falls forwards."

    "With an audible thud, her forehead lands on the table without the slightest resistance. Her arms follow soon after, flopping haphazardly onto the surface. With the show over, the girl beside me now lies seemingly dead, save for the movement of her breathing."

    "Hisao looks mortified, as if he himself had fired a bullet into her. Shock from the sudden nature of what happened, and extreme discomfort from a human moving and remaining limp in such an unnatural way, are written on his face."

    "I have to admit, for all I may be trying to play it cool, it still puts me off a little. I've never truly gotten used to this."

    hi "Is she... okay...?"

    mk "She's fine. Welcome to cataplexy."

    mk "Her muscles stop working when she gets shocked or has big emotions. It's like, bang, you end up a lifeless doll."

    hi "Part of her narcolepsy?"

    mk "Yep. It ain't always just sleeping, unfortunately."

    hi "Cataplexy..."

    "He says the word slowly and carefully, making sure he engraves it onto his mind. He gives the word a lot of weight in the way he says it, which is good to see."

    hi "Is it always like this?"

    mk "Well, Suzu's case is.... not light, to put it one way. Usually it's just like, weak knees, or not being able to keep your head up."

    "I feel bad for saying it so plainly, even if Suzu would've done just the same if she were able to right now. She got dealt a really shitty hand, and saying so just makes it feel all the more real."

    "He looks back to her for a moment, but doesn't last long before covering his face with his hands to try and recollect himself. I can't say I blame him."

    hi "Sorry, this is just..."

    mk "It's cool; I had the same reaction as you when I first saw it happen. Hell of a trick, eh?"

    hi "Does she need to be snapped out of it somehow?"

    mk "Give her a minute or two and she'll be right as rain."

    "No sooner do I say this, than Suzu begins to stir. Groaning slightly, she manages to move her arms to more comfortable positions before ever so slowly levering herself off the table."

    "With a bit of time to reorient herself and rub her eyes, she eventually comes back to the land of the living."

    suz "Don't be sorry about how you reacted. I'm used to it."

    hi "You heard everything?"

    suz "My muscles give out, not my senses. Which can be a pain all it's own."

    hi "How do you mean?"

    suz "When I get an attack, people often think I've had a seizure, fallen asleep, or fainted. It's not fun to be aware of what people are doing to your body while trying to wake you up, but unable to say anything."

    mk "And that's why it's handy to have someone around who knows all this when you get an attack."

    hi "Makes sense. To be honest, I had no idea narcolepsy included something like that."

    hi "How often does it happen, if you don't mind me asking?"

    "She just shrugs."

    suz "It varies."

    "Something's off about her answer. Whenever I've asked her questions about anything, but especially her narcolepsy, she always gives the most specific response she can. Partly because I pressured her into it so I could keep track."

    "Given she has no reason to be vague for his sake, it makes me concerned that her attacks are getting worse and she's trying not to tell me. It's the kind of terrible attempt at secrecy she'd try."

    hi "I'm guessing this is how you got the knee brace?"

    "A nod is her answer. Hisao's simpleminded curiosity is endearing, and Suzu dutifully doles out answers in her usual dull and encyclopedic manner. Talking about it in a generic way doesn't seem to bother her, at least as far as I can tell."

    "With this, Hisao's line of questioning appears to be at an end. His sits back and thinks for a little, the footsteps of Yuuko approaching our table eventually reaching our ears."

    yu "What would you like today?"

    hi "Coffee and a slice of pie, thanks."

    mk "Same as him."

    suz "Just tea, please."

    yu "No problem, coming right up!"

    "With her usual sharp bow, she scuttles off behind the counter. I still can't decide if the uniforms here are dorky or nice, but it suits her somehow. Not only because it shows off her nice legs, either. Her unusually chipper mood today makes her extra cute."

    "The three of us end up waiting in silence for our drinks. Suzu takes out her phone and begins tapping away at it, the screen held in front of her as she browses whatever site she's on now. Hisao just looks out the window, his expression showing him to be deep in thought."

    "I kind of want to bug him so I can have a conversation partner, but I decide to leave him be. The boy has a lot to think about right now, after all."

    "Looking around the cafe proves about as boring as expected. A few old people who came to this town to live out a quiet retirement sit at a few of the tables, and a handful students from Yamaku populate the others. I think I recognise the back of the class rep's head over the other side of the cafe, but I can't be sure."

    "After what feels like forever, Yuuko emerges with three drinks and two pie slices on a platter. Suzu may live in her own world sometimes, but at least she's polite, putting down her phone as they're set down on the table in order to thank her."

    play sound sfx_storebell

    "The bell above the door rings out, with Yuuko giving the briefest of nods before quickly scooting off to the entering customers."

    mk "The town's pretty nice, isn't it?"

    hi "Hmm? Oh, yeah, it is."

    "Hisao's absentminded reply annoys me a little, but the tinker of silverwear on her teacup draws the attention of both Hisao and I. Suzu ladles teaspoon after teaspoon of sugar into her tea, only stopping after it becomes more a sweet dessert than a drink."

    "After staring at his coffee for a bit afterwards, Hisao lets out a long breath before speaking up."

    hi "I wasn't going to mention this, but I probably should."

    "He already has the attention of Suzu and I after speaking, but the both of us become a lot more curious after he moves his tie to the side and begins unbuttoning the top of his shirt."

    "I briefly wonder how much of his chest I'm going to get to see, but he stops after undoing several of the topmost buttons. A shame; he looks like he'd have a nice chest on him."

    "Pulling his collar aside, what he intends to show us becomes clear. The top of a vertical line chasing up the very center of his chest, depressed just slightly into his flesh and shaded a little darker than the surrounding skin."

    suz "An operation?"

    hi "For my heart. A few months ago I had a heart attack caused by arrythmia. The scar's from when they cracked my chest open for surgery."

    "So what Haru said was true. I do my best to feign mild surprise, as the fact that I learned it before he was ready to do his show and tell makes me feel a little sheepish."

    "Then again, the fact that there's such a visual indication of what he's been through is a real surprise. I always thought of heart attacks as something you don't really see, but his large scar is impossible to miss. It's jarring."

    mk "That's... damn."

    "I feel a bit bad for opening my mouth but failing to find something to say. He gives a weak smile to excuse me for it, but I'd have honestly preferred him to be annoyed with me than make a face like that."

    hi "There you have it. The reason I transferred to Yamaku, that is."

    "Hisao buttons up his shirt and blows on his coffee before beginning to drink it, the fact that none of us really have anything more to say about his revelation becoming obvious. Suzu and I briefly look to each other before doing the same."

    "The more I think about it, the more it makes sense. His inability to keep up with Emi at all on the track, constant resting, weirdness around joining in sports... Given his build, he was no couch potato before it happened."

    "I have to admit that it was a smooth move to show us that right now; I can see the gears turning in Suzu's head. Opening himself up to us like that, especially just after Suzu showed her condition to him so vividly, will go a long way in earning her trust."

    "He probably doesn't know it yet, but it looks like he'll be able to handle her just fine. Not many people can."

    
    scene bg suburb_shanghaiint
    with shorttimeskip
    
    "As I chow down the last of my pie, I notice a subtle movement from the corner of my eye. Turning to where it came from, I see Suzu's head beginning to slowly nod, her eyelids also having trouble staying up. She might be working to hide it, but the harder she tries, the more obvious it is."

    "If she's already this bad, she's probably been fighting to stay lucid for a while. Silly girl."

    mk "It's fine."

    suz "Sorry."

    "She looks annoyed, but only in the most routine of ways. It's far from the first time this has happened, after all."

    "The world drops from her conciousness as she lowers herself down to the table, this time in a much more careful way than the last. I dutifully take her empty cup of tea and place it a few inches away as her arms come to rest around her head."

    "Hisao silently looks on, doing his best to appear nonplussed as he defers to my experience in dealing with her."

    "And just like that, Suzu's gone."

    mk "Whelp, she's out for the count."

    hi "This is just sleep, right?"

    mk "Yeah, just a nap. She's gonna be out for a while, most likely."

    hi "Do we wait for her, or...?"

    mk "Nah, I'll just carry her back."

    hi "You sure? I can do it if you want."

    mk "Your chivalry is cute, but it's fine. There is something else you can do, though."

    hi "Yeah?"

    mk "Spot me the meal? Pretty please?"

    hi "And why should I do that?"

    mk "'Cause I'm cute."

    "He just grimaces. I knew I should've gone with 'hot' or 'sexy'."

    hi "Alright, I'll do it. That will work exactly once, understand?"

    "Excellent. I wonder how many times I can get him to do that with various excuses."

    "Acting fast before he can retract his offer, I smile and call Yuuko over. With the bill paid over Suzu's peacefully sleeping body, our little outing comes to an end."

    scene bg school_road_ss
    with shorttimeskip

    "The trudge up the hill back up to Yamaku from town is a journey I've made countless times by now. I'm pretty sure I've lost count of the number of times I've made it while carrying a slumbering girl on my back, too."

    "It's not much of a bother, to be honest. She's a light little thing, worryingly so at times, and it's good exercise for my upper body in any case."

    "Hisao tries his best to look like this is a routine thing, but it's in vain. A one-handed girl walking up a hill with her sleeping friend on her back is just too odd a sight to ignore, at least in the beginning."

    hi "I've got no idea how you manage that."

    mk "It ain't so bad. I've been working out since forever anyway."

    "The thought of a girl being stronger than he is clearly dents his pride a little. That he's already breathing heavily while I'm not having much trouble at all just makes it worse."

    "At least he has a fair excuse, given what he said back there."

    hi "It's nice, though. You two must be really close."

    mk "Why do you say that?"

    hi "Suzu trusts you enough to be okay with you manhandling her, and you put yourself out to carry her around. You both seem to have a good handle on each other, too."

    "I think to myself a bit about his words. I suppose it's reasonable for an observer to think that, but I wouldn't really say we're close at all. I struggle for a bit to put our relationship into words, as much for me as for him."

    mk "It's... practical. Yeah, I think that's the best way to describe our relationship."

    hi "You fell into each other's orbit."

    mk "Yeah, exactly. You're good with those word things."

    "I'm happy with that description, and I think Suzu would be too, if she could hear it. Hisao, on the other hand, looks quite put off even if he did suggest it. He probably made the assumption just because we were both girls."

    "It's not worth getting too attached at this point, anyway. She's going to get into some good university, just like Hisao is given his constant praise from Mutou. That path is closed for me. Things got a lot better when I stopped caring about that fact."

    "But even now, as I carry her still body up the hill like this, I still feel the slightest bit comforted by her warmth."

    scene bg school_girlsdormhall
    with shorttimeskip

    "Having parted and gone our separate ways, Hisao to the male dormitory building - after telling me his room number, in case I decide to visit - and the two of us to the female one, I find myself shuffling up the hallway to Suzu's room. It's the floor below my own, unfortunately; if we were neighbors, it'd be a lot more convenient."

    "With my left arm holding up Suzu, I manage to retrieve the key to her room from my pocket after some fiddling. Her convincing the staff to let me get a copy of her dorm room key cut for situations like this was one of her better moves."

    "A quick flick of the hand, and the lock opens with a satisfying click. Manouvering around the door as I open it, the familiar smell of her room hits me before the view does."
 
    scene black
    with locationchange
    
    "It's 'girly', for lack of a better word. I don't know exactly what makes up the scent, beyond probably nail polish remover and light perfume, but it's unmistakable and foreign nevertheless."

    "Closing the door behind us and turning to the room ahead, I slowly navigate the way to her bed, taking care to manouver around the multitude of papers, books, clothes, manga, magazines, and toys scattered around the floor. She has a desk, but that's largely dedicated to her big laptop, plus a few other toys around it."

    "My room might be far from spotless, but at least you can see the floor. Then again, maybe that's just because I don't have the money to constantly buy things."

    "Grunting a little, I turn around at the side of her bed and bend down at the knees, slowly lowering Suzu onto her bed. With the weight lifted from my shoulders, I turn back and set about organising the disheveled heap, moving her legs and arms around to whatever looks reasonably comfortable."

    "My work done, I stand back up and admire my work. I can't help but smile at the absurdity of it all, even after all this time. A perfect little spoiled princess, neatly arranged with her plush toys all around her on the bed to keep her company."

    "I reach down and brush a stray hair away from her closed eyes, my gaze lingering a little on her motionless face. It's almost painful how delicate she looks, like a china doll that could crumble any second."

    "She really is a real life Sleeping Beauty."

    "I shouldn't get so sentimental about it. Maybe it's because I've only ever hung around with guys that a girl who actually acts like one feels so strange. It could just be yearning for a side of me I've never had a chance to explore. Who knows."

    "Well, whatever. I turn and scratch the back of my head as I make to leave, trying to brush the thoughts from my head. It doesn't really matter what Hisao thinks about our relationship; I'm not the kind of person a girl like her should be around."

    "I stop for a moment as I'm distracted by an actual doll on Suzu's shelf. An energetic-looking girl in bright clothes from some show she watched a while ago. She has a more at home, but only brought a handful to her dorm. She might call them figures rather than dolls, but I don't really get the difference."

    "I poke at its head for something to do as I mull things over."

    "We really are from two different worlds. For all I try, I can't think of a damn thing we have in common. I'm envious of so many things about her, from her innocence, to her family, to her wealth, but I've never bothered mentioning it."

    "Some people pop out of the right set of legs, and others don't. Some people mess everything up, and others don't. That's life."

    suz "Don't..."

    "Suzu's voice, little more than a faint and mumbled whisper, draws my attention to her as I obediently stop tweaking at her doll. It looks like she's awake, albeit only by the most generous definition."

    "She rubs her eyes, but does little beyond stare at the ceiling. I've always thought it must be hard to constantly be waking up in different places than where you went to sleep, but she's never once complained about it."

    mk "You okay?"

    suz "I'm fine."

    "No, she's not. Her voice has a slightly miffed edge to it, which she's too groggy to try and cover for."

    "She's never worried about being a bother to me before. Not that I mind; being useful to at least one other person in the world is something I need. She's a total idiot socially, but I think even she managed to work that out for herself."

    "That leaves the only other person that was with us."

    "It's kind of cute, really, getting all rattled about her narcolepsy in front of a boy. I shouldn't smile, but it's hard to supress. Having just transferred, it's unlikely Hisao would have a girlfriend right now, so she's in with a good chance."

    mk "Don't feel bad about it. Hisao's pretty understanding."

    suz "He's a total babe in the woods is what he is."

    mk "Haha, you got that right. He's totally helpless right now."

    mk "What do you think of the guy?"

    "She looks at me a moment trying to ascertain my intentions. That was an amazingly direct way to try and guage her feelings towards him, after all."

    suz "He's sensible. I don't mind him."

    "Well done, Hisao. That's one of the highest compliments someone could ever hope for from her."

    "She's not wrong, though. He might be a nerd, but he's comfortable dealing with the other club guys as friends. His sensitive side is enough to make Suzu lower her guard around him as well, which is someone none of those guys could ever do."

    "Looks like I'm stuck with him, then. There aren't many that can overcome Suzu's distrust of others, and as far as friends go, I could do a lot worse than Hisao. Having someone around who doesn't know about my past means a lot less baggage to deal with, too."

    suz "What are you smiling about?"

    mk "Nothin'. Just take it easy for today, alright? And eat a snack or something; don't think I missed you skipping lunch."

    suz "Only if you promise to do your homework for once."

    mk "Alright, alright, I will. See you tomorrow."

    suz "See you."

    "With that, I give her a parting wave before leaving the room and its girly smell."
    
    scene bg school_girlsdormhall
    with locationchange
    
    "Entering the hallway and carefully closing her door behind me, all I can do is rest my back against it as I close my eyes and sigh. Looks like the last few months of my time here won't be as simple as I expected."
    
    window hide
    
    scene black
    with dissolve
    
    return
    
label en_C6:

    scene bg city_street2
    with dissolve
    
    window show
    
    "Leaning back against the railing as the multitude of people ahead move to and fro, I do my best to pass the time by watching those who walk by."

    "I had arranged to meet Suzu and Hisao at noon, but it's getting perilously close and there's still no sign of either of them. I probably should have listened to Hisao and taken the same bus as he was going to use after all."

    "Not that I mind all that much. Just leaning back and watching others is entertaining, given the sheer variety in people you see. I suppose when you get enough people in one place, you'll eventually start seeing the odd ones."

    "Of course, badly hidden glances from the occasional person who notices my left arm ending in a stump reminds me that I'm one of the odd ones myself."

    "If I really cared, I could cross my arms, shove the stump in my jean pocket, or just pull down the sleeves of my shirt a little. It's not exactly hard to notice when my sleeves are rolled up, after all."

    "It hardly matters, though. I'm out of their conciousness a minute after they lose sight of me, so I may as well just wear whatever's comfortable. That's one of the advantages of a city over small town life; when you're surrounded by so many people, it's easy to be forgotten."

    "I look to my watch again to see the time, the dark grey digits reading out a time of five minutes to noon. At least I had an early lunch, so I'm hardly starving for food."

    "As soon as I begin to wonder if either of them will actually be here on time, I notice a familiar young man with brown hair manouvering through the crowd. It takes a moment to identify him, given that this is the first time I've seen him out of his school uniform."

    "Hisao doesn't look fussed by the crowd at all as he walks up, casually strolling through wherever he can see a gap in the people moving around him. Guess he's the punctual type, given how close he cut it."

    hi "Hey. Looks like I made it just in time."

    mk "Getting out of the retirement home took a while, then?"

    hi "Huh?"

    mk "The vest. It's not a cool look."

    hi "Don't knock the vest; it's smart."

    mk "Whatever you say, gramps."

    "He begins to protest, but turns to the side instead. My own gaze follows his out of curiosity, with the object of his attention becoming quickly obvious."

    "Suzu runs towards us as fast as her legs can take her, her white summer dress billowing out behind her as she tries to hold her bag to her side. It's kinda sad how slow she is despite the fact she's running."

    hi "Damn..."

    "I turn to see Hisao averting his eyes, holding his balled hand to his mouth to try and hide his expression."

    mk "Hmm?"

    hi "She's cute."

    "All I can do is give an amused snort."

    mk "Yup."

    "She pants heavily as she reaches us, barely managing to splutter out a greeting as she gasps for air. In the end we all got here on time, even if it was only just barely."

    suz "Sorry... I slept in... I didn't..."

    hi "Just calm down and take a breath. It's fine."

    "The two of us wait for Suzu to settle herself before either continues."

    hi "So do we actually have any plan about what we're doing, besides hanging out?"

    suz "I need to buy a couple of new notebooks. I've almost run out."

    mk "Stationery shopping? Really?"

    hi "To be honest, I could probably do with picking up a couple as well."

    mk "You two are the worst."

    "Further protests don't make any difference to either of them, so the three of us end up heading off towards a stationery shop to pick up school supplies. I guess I could buy a pen... or something. Beats waiting outside for them."

    scene bg city_street4
    with locationchange
    
    "As we walk on, the heat of the summer's day beating down, I find myself distracted by the sights alongside us. It's Hisao who eventually picks up on it."

    hi "What's up?"

    mk "You know, I can never get used to those huge displays. The ones they use for advertising and stuff."

    "I point upwards the massive screen mounted on the front of a tall store, the logo of some electronics company flashing up and moving about with wild and vivid color. Even in the summer's daylight, the screen is dazzlingly bright and impossible to ignore."

    "Hisao, for his part, looks rather unimpressed. I might as well have pointed to a pebble on the ground for all the interest he takes. The best he can do is tilt his head as he tries to think of something to say about it."

    hi "Yeah, it is pretty big."

    suz "He comes from the city. What do you expect?"

    "So Hisao's a city boy. Should've guessed."

    "Images of Tokyo and Osaka I've seen on television spring to mind; a teeming mass of people flowing through streets like gushing rivers of water, the bright blare of storeys-high screens beaming down on their heads."

    mk "Man, I gotta go to Tokyo sometime. It's like living in the future, there."

    hi "Hold on, you've never been to Tokyo? Not once?"

    "Even Suzu shares Hisao's disbelief, wheeling around to see me as the three of us grind to a halt. All I can do in response is shrug."

    mk "Never needed to."

    "The two of them share a knowing glance before continuing on. I think I just validated a whole bunch of ideas they had about me."

    "With a quick skip up to them, we continue on our way."

    scene black
    with locationchange
    
    "I just couldn't hack it. With the Suzu and Hisao dawdling around getting books, folders, and whatever else, I ended up bailing out and hitting the arcade next door."

    "Dancing games are rather pointless without friends, so the choice was largely already made as to what to play. Cheap plastic gun in hand, I plink away at the screen for minutes on end, sending zombies and other undead sprawling to the ground."

    "I wonder if I can get used to the quiet of home after being in a place like this. Fancy amusements like arcades, music stores, and concerts still feel like a novelty to me, but everyone else barely notices how amazing they are."

    "Even as I gun down more monsters in a violent pixellated rampage, a couple at the entrance can be heard deciding to go to the cinema instead of wasting time here. I did see movies before moving to Yamaku, but it was a rare treat back then. Here, it's just a spur of the moment decision."

    "That momentary lapse in concentration is all the excuse the game needs to destroy me, scratch marks suddenly littering the screen. I try to fight back, but my pace is completely gone."

    "As the continue screen comes up, hungry for more coins as always, a familiar voice comes from beside me."

    hi "You did pretty well. That game's pretty unforgiving."

    "Hisao and Suzu stand side by side, having patiently waited for me to finish. It's kinda funny to see them together like this; they look like they're cosplaying an elderly couple. No sense of fashion, not that I'm one to speak."

    "What he said piques my curiosity, though; I wonder is he's any better than me at this, given that he seems to have played before."

    mk "Fastest lightgun in the West. You any good at this stuff?"

    hi "Start up a 2-player game and I'll show you."

    "Something about the tone of his voice is different than usual. I only realise what it is after he's given Suzu his bag to hold and taken up position with the second lightgun, pulling it from its holster with practiced ease. He's excited. Just a little, but it's there."

    "I occasionally throw a glance at him as I set up a fresh round, throwing in my last few yen as he looks down the sights. Guess I'll be mooching off someone for dinner again, but my curiosity's demanding to be sated."

    "The two of us take up our positions as the co-op story mode starts up, going through the same lame intro sequence I've seen so many times before."

    "And then... it begins."

    "As undead spring up from the corridors we walk through, the two of us blast away as fast as the guns allow. We get past one level, then two, then three."

    "I'm starting to have problems as we reach the fourth, with more and more enemies requiring more and more shots start launching themselves at us. One life gets used, then another, and by the time the level's over, I'm sitting on just one left."

    "I hardly feel bad about it, though. It might only be by the skin of my teeth, but this is the first time I've managed to get to the fifth level. Hisao's quite the comrade, and peering over at his side of the screen, it looks like he's still got two lives left to my one."

    "He looks like like the other runners in the club when they get into the zone, with their eyes narrowed and mind focused. It's a cool look. Perhaps a little too cool, as his focused expression almost makes me miss the first enemies of the new level."

    "That said, it wouldn't have made of a much difference if it had. My last life disappears in the opening few moments, leaving the rest to Hisao. Not that he seems to mind, as he manages the challenge of two player's worth of enemies at once for some time."

    "But then it happens. One life is gone by the time the level's wrapped up, and by the time the sixth level has started, it's obvious he's overwhelmed. He puts up a heroic last stand, but in a few minutes, he's taken out by a veritable flood of enemies."

    "The continue screen returns once again, the both of us well and truly beaten. Hisao lets out a long breath as his shoulders slump, the adrenaline leaving him as he returns the lightgun to its holster."

    suz "That was pretty good."

    mk "Thanks. Had a good wingman, though."

    "Hisao just shrugs. He just looks at the screen for a while before turning to us with a cocky smile. I think it's the first time I've seen him genuinely proud of an accomplishment."

    hi "That's how you do it. We heading off?"
    
    scene bg city_street4
    with locationchange
    
    "Suzu nods and takes the lead, handing Hisao his bag before the three of us file out into the busy street outside. The difference between the air-conditioned arcade and sunbaked walkway is like night and day, with the afternoon's heat setting in."

    suz "You look pleased with yourself."

    hi "Just been a while since I hit the arcades. Kinda happy I can still pull that off."

    mk "You're the only guy I've seen manage to get that far. I thought they rigged those things so you had to keep buying lives to continue."

    hi "They pretty much do. Actually finishing is nearly impossible."

    mk "Well look at Mister Arcade Machine Expert talking big over here."

    "I turn to Suzu to back me up, only to find her no longer in sight. Both Hisao and I turn to check where she is in confusion."

    "Walking slower and slower behind us, Suzu's eyes remain pinned to the ground ahead of her. I might not be particularly bothered by the heat, but Suzu isn't as hardy as most."

    "My heart freezes as she suddenly begins to fall, legs crumpling underneath her and giving no resistance as her body drops downward. A movement from the corner of my vision darts forwards before I even have a chance to react."

    "It's all over in what must be less than a second. Hisao, hero of the day, stands with his legs bent as he holds Suzu's limp body to his front. Every time he lulls me into thinking he's just another boring studybug, he goes and pulls something like that."

    mk "That was some amazing stuff, dude."

    hi "Don't worry about that. Could you take her?"

    mk "Sure, hold on."

    "Back when he first entered Yamaku, everyday conversations tended up put him on guard, but now he's dealing with a public situation without panicking in the least. He might be sweating a little, but I'm still impressed."

    "I quickly jog up and turn around, Hisao helping manouver her onto my back. The heat alone wouldn't do this, but if she was tired before coming here, it might have finished her off. Whether it's cataplexy or a sudden sleep attack, she's not going to be in a condition to walk much more in either case."

    mk "See anywhere we could rest a bit?"

    "He scans around a little before pointing to a small cafe with some free outdoor tables."

    hi "Let's head over there. We can grab a coffee while she recuperates."

    "Sounds like a plan. I nod in assent as we move off, the slumbering girl on my back drawing more than a few badly hidden glances. I'm kind of glad she isn't awake for this, as she'd no doubt hate the attention."

    "Thankfully it isn't far to the place Hisao pointed out, with him going inside to order a couple of coffees while I deposit Suzu in a chair before taking a seat myself."

    scene bg city_cafe
    with locationchange
    
    "It's been a long time since she passed out in public. Now that I think about it, it must look incredibly suspicious to the people around us for two teenagers to be dragging around an unconscious girl. Maybe it's a good thing I'm a girl too, as two guys dragging her around would look even worse."
    
    "I idly rap my fingers on the table while occasionally glancing to her, arms and head arranged on the table in what's hopefully a comfortable position."

    "Thinking back to when she fell, I reach into the wallet in my back pocket and fish out some yen. I can't really ask Hisao to spot me the coffee after what he did for her; it's incidents like that which gave her that stupid knee brace in the first place."

    "Eventually he emerges from the glass door of the cafe, setting down a cup in front of me before sitting down. I put several notes on the table and slide them over in return, earning a nod of thanks before he slips them into his pocket."

    mk "Bit of excitement there, eh?"

    hi "I could do without more excitement in my life, to be honest."

    mk "Where'd you get reflexes like that, anyway?"

    hi "Dunno, probably partly from playing so much soccer. Before the heart attack, anyway."

    hi "I miss playing that..."

    "He gives a wistful sigh as he looks out to the street."

    "I feel terribly bad for asking. I know that sting all too well, and here I am inflicting it on someone else, albeit accidentally."

    mk "Wanted to go pro, or...?"

    hi "Nah, nothing like that. It's just... it was structure, I guess. Something to dedicate myself to."

    hi "I was good at it, you know. Nothing amazing, but I could keep up with the others easily enough. It was something I could do with friends, see myself improving at, and look forwards to each day."

    hi "I guess I didn't realise how much that meant to me, before I lost it."

    "Ah, I think I understand him a lot better now. The reason he studies so much isn't because he's some nerd, but because he wanted to fill that hole in his life."

    "That's admirable, I think. To deal with such a shock in that particular way is something I can respect."

    "Suzu begins to stir as we talk, mumbling something unintelligible as she tries to sit herself upright. The two of us just wait for her to fully wake, knowing that engaging her while she's so disoriented would be futile."

    "After shaking her head and pinching the bridge of her nose, she appears a little more lucid."

    suz "Where...?"

    hi "Just a cafe nearby, don't worry."

    mk "Superman here managed to catch you before you fell, so you're not hurt."

    "She just nods silently, still trying to regain her senses. Where she is and whether she ended up injured should cover just about everything."

    "As if to prove me wrong, she digs around in her bag a little and retrieves her trusty mobile phone, no doubt to check how long she's been out. It wouldn't have been all that much time, so it shouldn't come as a shock."

    "She pauses a little after doing so, looking to Hisao with a hint of shyness."

    suz "If you want my number..."

    hi "Ah, sure. May as well take it."

    "He quickly grabs his phone from his pocket and slides it across the table towards her. Her fingers make short work of the task, adding her number to his phone and vice-versa."

    "Feeling left out, I drag my old phone from my pocket as well. It might be noticably older than either of their whizz-bang things, but it does the job."

    mk "Yo, gimme."

    "Suzu glances to Hisao for confirmation, with a shrug being the answer as he busily sips his coffee."

    "With another slide his phone reaches me, and I quickly set about bringing up his contact list. It's difficult to just ignore what's right there, so I scroll a couple of times to see who he's deemed worthy before adding my own details."

    mk "Huh. You've got the student council goons in here?"

    hi "You make that sound like a bad thing."

    mk "Well... I mean, I'm fine with them, but..."

    "I glance to Suzu, who evades my staring."

    mk "They can be a bit intimidating."

    hi "I suppose I can see that, but they've been a lot of help. They do take their job seriously."

    suz "That's part of the problem."

    mk "You just gotta know how to deal with 'em. Straight back, stiff lip, and tell 'em what you mean."

    hi "You're the last person I expected to defend them."

    mk "Pfft, they're fine. I can appreciate people who take their work seriously, you know."

    hi "Maybe you should try doing that yourself."

    "Suzu's gaze shifts to me, waiting to see my comeback. I just settle for sticking my tongue out at him."

    "With the argument headed off and his phone returned, we content ourselves with drinking and talking for a good long time."
    window hide
    
    scene black
    with locationchange
    
    return
    
label en_C7:

    scene bg school_track_running
    with locationchange
    
    window show
    
    "Sprinting has never been my thing. I've never managed to hype myself up for the competitive nature of the track meets, either."

    "But the act of running, of putting one foot in front of the other, that's what I've found pleasure in. I couldn't care less if other people are on the track with me or not. That isn't really the point of it."

    "As I jog around the track during lunch, I can feel my mind clearing. Some people do stuff like this to give themselves time to think, to mull things over. For me, it's the opposite. While running, I can just concentrate on the track itself, the breeze blowing past me, the sounds of the birds in the trees."

    "After everything that's happened, this is the one time I can forget it all. No more worries about school, home, or my past. Just me, and the track."

    "I give the others in the club a quick glance as I come around once more. As expected, the dozen that're here are just lazing around chatting between themselves. A few are drinking bottles of water and others are eating snacks, but all of them are on their asses. Too hot for them, probably."

    "Haru raises himself and gestures for me to join him, with Yukio nearby taking his feet also. No reason not to, so I break from the track and head over to the two."

    scene bg school_track
    with locationchange
    
    mk "Yo."

    "He gives a wave as I slow down and walk towards them. With a long breath and a bit of a stretch, I feel the exhaustion from the run ebb away."

    har "You seen Hisao today? He hasn't shown up to club yet."

    mk "Sorry, no idea where he's gotten to. Emi hasn't dragged his ass here?"

    "Thinking back to the end of last class... I think I saw Hisao leave with the main bunch of students, but I've no idea where he went to after that."

    "Yamagata snorts in amusement as Haru just crosses his arms and sighs."

    yuk "She's giving him the silent treatment. Think he balked at one too many of her morning runs."

    mk "That's harsh, man."

    "He just shrugs. Not much we can do about it, I suppose."

    mk "I guess one of us'll have to go on a hunt. She's gonna go nuts if she finds he's skipping club completely."

    har "He could just be studying. Exams are soon, you know."

    "He emphasises the last two words, as if Mutou busting my balls wasn't enough. He surrenders the point after the fed up glare I give him in response."

    "Each of us looks at each other, trying to come up with our best excuses to not bother. I just want to get back to running, and it's probably too hot for either of the others to be assed wandering around trying to find him."

    har "The usual?"

    "We all quickly nod; it's obviously going to be the only way to decide this. Huddling together, the four of us hold our fists out in preparation."

    har "Paper, scissors... rock!"

    "We each throw our choices out. One scissor, one rock, and then mine. For some strange reason, the others end up looking at me with flat faces."

    mk "It's rock."

    "I waggle my stump around in the air a little before giving up on the joke. Without further ado, we pump our fists up and down for another round. This time, I throw my choice out with my right hand."

    "...Two papers against my rock. Assholes."

    "I reluctantly slink off after a sympathetic pat on the shoulder, knowing full well that my goose is cooked. Guess I'll hit the library first; where better to find a nerd studying for exams, after all?"

    scene bg school_dormext_start
    with shorttimeskip
    
    "After failing to see him in the gardens leading back to the main building, poking my head into the largely empty classroom, and finding the library a bust, I make the trek back down the flights of stairs and across the school grounds to the dormitories."

    scene bg school_dormhallground
    with locationchange

    scene bg school_dormhallway
    with locationchange
    
    "Strolling through what should be the hallway to Hisao's dorm room, I casually glance around at the near-empty corkboards on either side. All that're there are a couple of old and tatty joke pictures, threatening to fall onto the floor."

    "It's odd to contrast with the sections of the male dorms I've seen, full of official notices, jokes, and messages to other guys in the nearby rooms. Teachers might try their best to keep the more crude ones torn down, but a few occasionally manage to stay up for an evening or two."

    "Eventually I reach my goal, pressing the door handle and gingerly pushing in to see if it'll open. It obediently opens at my touch, giving me a wave of relief. I'd probably have just given up if he wasn't here, but at least now this wasn't all for nothing."

    scene bg school_dormhisao
    with locationchange
    
    "Poking my head around the now half-open door, there doesn't seem to be any sign of life inside. Maybe he's in the toilet or something, though that doesn't explain why he retreated to his dorm room during club time. With no desire to wait around bored in the hallway, I decide to step in and indulge my curiosity about what his room is like."

    "Plain. There isn't any other word for it. He did transfer in recently, but it wouldn't kill him to put something on the walls, or some toy or whatever on his desk. All that's here are a bunch of books, his computer, and a few clothes strewn about. For a guy, he's very neat. Frustratingly so."

    "After pacing around a few times out of boredom, I take a quick moment to crouch down and peek under his bed, hoping to see if he's stuffed anything embarassing underneath."

    "Nothing, except for a couple of misplaced pieces of clothing. Disappointing. I guess he's the type to have that kind of thing on his computer, anyway."

    "It's only after getting back on my feet that I take more careful notice of his desk. Behind a couple of textbooks sits a bunch of bottles, drawing me towards them to see what they are."

    "Medications. I didn't think they could be, given how many there are; well over a dozen, by my count. I pick up one of the bottles to see the label more clearly, but can't divine anything from the lengthy name. '-ole', -'ine', '-ane', all the same to me. "

    "I gently put it down amongst the others as another item on his desk catches my eye. A single piece of paper, obviously a letter sitting atop its opened envelope, adorned with sunflower decorations and cute pink writing. It's obviously to Hisao, rather than from him."

    "By the time my conscience has said to step away, my eyes have already started scanning the letter's contents. I sure wish I had handwriting as neat as this."

    "'How are you? I hope you are well and happy at your new school. Everyone here misses you.' so it's from someone at his old school. I guess the mysterious transfer student does have a past after all."

    "Blah, blah, blah. Just a status update of what's been happening in the leadup to their set of exams. At least he still has contact with them, I suppose."

    "'The truth is, the times when I visited you at the hospital made me worried about you. I am not talking about your health. You seemed to become more and more distant and disheartened.' Well, yeah, being stuck in a hospital for a while would make you feel shitty."

    "As my eyes keep scanning the page, the penny finally drops."

    "'Now that the distance between us is also physical, it also feels more final, somehow. I wonder if we will meet again. Perhaps it's for the best if we don't?' She... wasn't just a friend, was she?"

    "Now I understand what this is. It's not some buddy writing to another about what's been happening lately. It's a break up, with a bunch of meaningless padding thrown in to distract from what she was really meaning to say."

    "I've made a mistake. I should never have seen this."

    "I step back to the center of the room and take a quick look towards the door, making sure I'm not being watched. My first thoughts are for my own self-preservation. Typical."
 
    scene bg school_dormhallway
    with locationchange
    
    "Deciding that I've had quite enough my prying, I quickly retreat to the hallway outside the room, taking care to quietly close the door just as it had been. There's nothing to be gained by confessing; it's better for everyone if this just never happened."

    "The faint sound of voices catches my ear, though thankfully it sounds more like general chatter than anything directed at me. Sounds like it's coming from one of the nearby dorm rooms."

    "Whether it's out of a desire to distract myself from what I've read, or simply trying to establish an alibi if Hisao comes by, I once again I quietly poke my head through an unlocked door. This time around, I do find somebody inside."

    "Hisao stands with his back to the door, busily chatting with someone else."

    "Everything about the other guy seems a little bit off. His height is a little too short. His hair is a little too scruffy. His glasses are a little too thick. His scarf... well, that's more than just a little off, and not just given that it's summer."

    "The scrawny guy notices me over Hisao's shoulder, their conversation abruptly ending as the two of them turn their visitor."

    mk "...'Sup?"

    hi "Haven't you heard of knocking?"

    "I obediently knock a few times on the door. The short guy just raises an eyebrow as Hisao sighs and motions in my direction."

    hi "Kenji, this is Miki Miura. Miki, this is Kenji Setou."

    mk "You don't have to make it sound like you're embarrassed to know me."

    "I'm not quite sure how to interpret the awkward face he pulls. Not much point in leaving now anyway, so I wander into the room regardless."

    scene bg school_dormkenji
    with locationchange
    
    "Unlike Hisao's, this is a room that feels lived in. Bits and bobs that Kenji's collected over the years and brought from home are littered around the room. It's what he has hanging on the walls that particularly catches my eye."

    "I nod to a poster of the local Pacific League baseball team, nestled in a corner next to some... professional bowling posters? I didn't even know they made posters for bowling teams."

    mk "Nice taste."

    ke "You know them?"

    mk "Kinda hard not to know the locals, even if they did flunk last season."

    ke "They're still the best team. It's just their coach."

    mk "Totally. I mean, just look at how well 2005 worked out."

    "All he does is frown a little, but I somehow get the feeling I'd have offended him less by insulting his mother."

    mk "Calm down, I follow them too. The sooner they find their groove, the better."

    "The quick save mends his attitude a little, but he still seems suspicious. Whether he knows it or not, Hisao steps in to save the day."

    hi "I had no idea you followed baseball."

    mk "Baseball is the best sport, you know."

    hi "Huh. Play?"

    mk "Used to."

    "Even after all these years, those two words still feel like a punch to the gut. I quickly move to hold my expression, but Hisao sees through it, going by his reaction."

    "An awkward silence follows. I shouldn't blame him, given that I was the one who brought it up. Better to just let it drop, as I feel like telling him one detail or another will make everything eventually unravel. I guess this is what they call 'baggage'."

    ke "Do you follow bowling?"

    "This dude has no idea how thankful I am for the change in topic. Even if it is a weird one."

    mk "Bowling... I think I played that once. Is there like, a professional scene or something?"

    "All hopes he might have had for engaging me visibly evaporate. I guess the dude puts a lot of stock in bowling."

    ke "Bowling is the best sport. Why does nobody understand this?"

    mk "Wasn't bowling more popular in the 80s or something? It's just something you do to kill time these days."

    ke "Exactly! The 80s were a golden era. All the best stuff comes from the 80s. Like bowling."

    hi "The economy was booming back then, so maybe you have a point."

    ke "It's not just sport and the economy, either. The 80s gave all the best action movies. The most important and educational media ever made."

    hi "I... don't think those movies were educational. At all."

    ke "They were documentaries on how to be a man, dude. They just don't make them like that any more."

    mk "You got a point there, actually. The newer action movies are all lacking something."

    ke "I know, right? We've lost control of Hollywood. There is no hope for them now. We have to retreat and guard the homeland."

    ke "We're alone in this world. Generations will grow up not knowing what true manliness looks like, cowed by their overlords. Soon popular culture will be all chick flicks and shoujo games. Even the action movies will be made for girls."

    "I don't really get what he's on about, but a future full of girly romance movies sounds bad. I saw one once out of curiosity, and nearly threw up from the sentimentality of it. How do people watch that stuff?"

    mk "That would be terrible."

    ke "Yes, terrible."

    ke "You keep good company, Hisao. I knew I was right to rely on you."

    "I sure said something right. He gives a thumbs-up, but Hisao looks like he'd rather be anywhere other than here right now. He hastily, and pretty blatantly, changes the subject."

    hi "What'd you want me for, anyway?"

    mk "That's... a very good question."

    mk "Oh, right. You didn't show up at club, so I came to drag your ass in."

    "He glances to his watch, its news apparently unpleasant for him."

    hi "She's gonna eat me alive. Sorry Kenji, I gotta go."

    ke "It's cool. We can we can cover the udentstay ouncilcay akeovertay sometime later. I have visual aids and everything."

    hi "Yeah... sometime later. I'll see you around."
    
    scene bg school_dormhallway
    with locationchange

    "The two of us take our leave, Hisao closing the door behind us before we start down the hallway."

    mk "Seems like a cool dude. Friend?"

    hi "He's... yeah. I guess he is."
    
    window hide
    
    return
    
label en_C8:

    scene bg suburb_konbiniext_ni
    with shorttimeskip
    
    window show
    
    "With the sun well and truly having set, Haru, Hisao, and I pass the time lazing around in front of the convenience store. The light from the store illuminates the street around us as we sit on the ground, backs propped up against the window."

    "A couple of bags sit between us, holding a late dinner of onigiri, potato croquettes, and some canned drinks. Not exactly five-star cuisine, but it's edible and filling."

    "Aside from the sound of our munching away and occasional chatter, there's little else to be heard. The bulk of school's students have retired to their dorm rooms for the evening by now, leaving us to shoot the breeze in peace."

    hi "Still surprised Yukio's not here."

    mk "Don't believe him when he says he's studying?"

    hi "About as much as I'd believe you."

    mk "Dick."

    har "Leaving those two aside, I'm surprised you're not studying. You don't seem as careless as they are."

    hi "I needed the break, to be honest. There's only so much I can do before I'd burn out."

    har "Sounds like you've got a good head on your shoulders."

    "Hisao gives a grin and quick snort to pass off the praise, tucking into a drink afterwards. Praise seems to slide off him, which I've never quite understood. Why work so hard for no reward? I thought academic types lived for a pat on the head."

    "Haru cares much less than I about the matter, plucking out a familiar magazine from his bag with his free hand while chomping at the onigiri held in the other."

    mk "New issue out?"

    har "Yeah. Want to read after me?"

    mk "Sure."

    hi "A defence forces magazine? Didn't know you were interested in that stuff."

    har "Gotta have something to occupy myself with besides baking cakes."

    hi "You've really got your eye set on working in a bakery, don't you?"

    mk "You make that sounds like a bad thing. Having a purpose to your life is admirable, no matter what it is."

    hi "That sounds absolutely bizarre, coming from you."

    "I can't help but glare at him. For him to say that feels like an invalidation of everything that happened before my accident."

    "But on the other side of the coin, that's the front I've been presenting to him to begin with. My dream died. It's gone. What's the point in bringing it up?"

    "Without realising it, I've begun to rub my stump once more. Thankfully, Haru fills the air with more meaningless words to try and liven things back up."

    har "What about you, Hisao? You seem to have a good head on your shoulders, unlike her. Surely you have something to apply that brain to."

    hi "To be honest, I haven't really given it much thought. Suppose I'll have to, with graduation on the horizon."

    hi "I do agree with Miki, though. It's good to have something to work towards."

    hi "Come to think of it, what are you planning on doing with yourself?"

    "I should've known that would come up."

    mk "I plan on enjoying the springtime of youth."

    hi "In other words, nothing."

    mk "You say that like it's a bad thing. We're only young once, man."

    "He looks to the side, but finds no support from Haru. With a magazine in one hand and food in the other, he's made it clear he has no intention of getting involved." 

    "Hisao's eyes linger for a little too long, and as I follow his gaze, I see why. Even Haru looks up from his magazine after noticing the lull in the discussion."

    "A girl in the Yamaku uniform comes striding up the street in the direction of school, the three of us watching her as she strolls past. Quite a pretty thing, and carries herself well."

    "Whether she's noticed our glances is answered by the flirtatious flick she gives her hair, showing a brief flash of her cute earrings. I guess that's the way the game is played."

    "All too soon, she disappears into the night."

    "With the three of us thoroughly distracted, the previous discussion is hard to return to. Hisao and I take a few more gulps of our drinks, but Haru evidently has other ideas as he takes to his feet and passes me his reading material."

    "Standing bolt upright and looking up the street, he looks like a man on a mission. I think I know what's gotten into his head."

    hi "What's wrong?"

    har "Something came up. I have to go."

    mk "Go get 'em, tiger."

    "He gives us a nod before heading off, running a hand through his hair before putting them in his pockets to appear as casual as he can."

    hi "The springtime of youth, huh?"

    mk "Just as I said."

    "With the two of us left to our own devices, I pick up the can next to me and give it a swirl to check if it's empty, Hisao digging around in the bag between us for a croquette. As he pulls one out, he makes a disappointed face."

    hi "Aww, last one."

    mk "Mine!"

    hi "What? No."

    "Hisao fearfully twists to the side, clutching it with both hands as if it were a pearl or diamond. Without a second thought, I drop the magazine and can, jumping onto his back to try and snatch it from his grasp."

    hi "Miki!?"

    mk "I said mine! Give it!"

    "I throw my left arm around his neck to pin myself to him as I swipe at the food, Hisao frantically holding it out as far as he can with his right hand while jabbing me repeatedly with his left elbow."

    mk "I need sustenance!"

    hi "So what? I got it out! It's mine!"

    "We struggle some more as he tries in vain to throw me off, the two of us probably looking like utter idiots to any passerby. He suddenly changes tack and thrusts the croqette towards his mouth, but I manage to get an iron grip on his wrist."

    "He frantically tries to move his arm, but it's hopeless. I'm take off guard by how little effort it takes to manhandle him, as he looked quite well built at a glance. I push further into his back and squeeze my hand to make him drop it, drawing further protests as my grip gets tighter and tighter."

    "Our growling and grunting gets louder and louder, before eventually the pain becomes too much for him. Hisao's fingers snap open with the food promptly dropping to the pavement. I quickly reach out and grab it before he has the chance, before pulling back and returning to my seat as he rubs his sore wrist."

    "The both of us take a breather after the scuffle, the conquered casting a distinct frown towards the conqueror. I don't care; I got my food."

    hi "That's been on the ground, you know..."

    mk "Five second rule."

    "I give it a little dusting before jamming the item into my mouth in one go. It's a bit cold by now, but still worth the effort."

    "All Hisao's left to do as I munch away is heave a sigh and deposit our bags into the nearby bin, taking care to retrieve the can I threw away and dump that in too."

    "With dinner finished, I give my stomach a hearty pat and lean back against the window. It doesn't look like Hisao has any intentions of leaving as he retakes his seat beside me, making it obvious that he still has something he wants talk about."

    mk "So, what's eating you?"

    "He looks surprised that I picked up on it for a moment, but eventually acquiesces."

    hi "I'm not really sure. I guess with the summer holidays around the corner after exams, I'm just getting a bit reflective."

    hi "I've been here for a month, but still feel like the ground's moving under my feet. Stuff's just happening around me, sort of thing."

    mk "Isn't that normal? You didn't live alone before, right?"

    hi "Technically not, but both my parents worked. Spent most of my time either at practice or roaming around the city with friends, so I wasn't home much to begin with."

    "Spoke like a true urbanite."

    mk "Dude, living on your own for the first time is bloody hard. Handling laundry, feeding yourself for every meal, doing your chores out of need rather than being asked, being separated from your parents for months and sometimes years... it's a pretty huge change."

    hi "I had help, though. Shizune and Misha put themselves out for me more than once, and much as I hate to say it, you've been around too."

    mk "And what, that makes me wrong? You're living on your own, and got help when you needed it. Sounds to me like you're doing pretty well for yourself."

    mk "Even by Yamaku's standards you've been dealt a shit hand. I'm honestly pretty surprised you've managed so well, considering everything you've been through."

    "His expressions drops, and after a brief moment of thought, it becomes all too obvious why."

    hi "You were in my room, weren't you?"

    "I rapidly prepare to lie me ass off, but his dead serious expression leaves me speechless. I've never seen him so stony-faced. Awkwardly shrugging is all I can do."

    mk "A bit?"

    "What am I doing, I can lie better than that. What does that even mean, anyway?"

    "Well, there's no use denying it now."

    mk "Sorry."

    mk "How did you know?"

    hi "After I take a particular pill, I turn the bottle around. Helps keep track of whether I've had my daily medications that day or not."

    mk "And I didn't put one back the right way..."

    mk "I do mean what I said, though. You've done well for yourself."

    mk "To be honest, it makes me kinda jealous. I was a real piece of work when I first entered Yamaku, but here you are, skirting death and just rolling with the punches."

    "I leave an opening for him to ask about me, but he doesn't take it. Instead, he just looks... tired. Like an old man reflecting as his eyes slowly close."

    hi "I wonder about that."

    mk "What's wrong?"

    "He slowly shakes his dreary head, still looking at the ground."

    hi "You wouldn't understand."

    "Moments pass in silence, frustration at his sudden change in demeanor welling up."

    "He's right, of course, but that doesn't make it any easier. Hisao isn't just taking pills to suppress some medical issue or another. He's taking pills to not die. I think about how to do two things at once, or how to do up a button with one hand. He thinks about mortality and how his end might come."

    "We're eighteen. Kids. We can't even drink. That's too young to think about death. Of course I can't understand that crap, and neither can he, no matter how much he might pretend to."

    "I end up responding the only way I know how. By hitting him around the back of his head."

    hi "Ow! What was that for!?"

    mk "You're a real pain in the ass, you know that!?"

    mk "I thought Suzu was hard enough to deal with, and then you go and start getting all mopey. We're teenagers; we're allowed to not think about that crap."

    "Hisao's reaction to my frustrated appearance is both simple and unexpected. He laughs. At first a simpering chuckle, but in seconds he's escalated to a deep laugh right from the chest he appears to relish my pain. I should probably find it annoying for him to laugh at my expense, but it's more of a relief."

    mk "So you can laugh. I was beginning to wonder."

    hi "I was just thinking about how ridiculously blunt you are. You don't know the meaning of tact, do you?"

    hi "But that's fine. I like that about you."

    "All I can do is smile and give a halfhearted shrug at the compliment, and a bit out of relief that he didn't take too much offense. Hisao seems the type to appreciate honesty, after all, even if it is delivered in a frank way."

    hi "This is probably going to get me beaten, but... it's honestly hard to think of you as a girl. You certainly don't act like any I've been around."

    mk "Believe me, I've heard that more than once."

    hi "You don't mind?"

    mk "Couldn't care less. People can think what they like, doesn't harm me."

    hi "You're pretty weird, you know."

    mk "I don't want to hear that from you."

    "I hit him around the back of his head with my stump, drawing another chuckle from him. I can't help but get caught up in it, launching into laughter myself."

    "Maybe it's from how curious a person Hisao is, the both of us laughing off such morbid thoughts of mortality and death, or simply two overly tired people getting caught up in the stresses of exams and school life..."

    "But in any case, the both of us end up laughing together for a good, long while."
    
    window hide
    
    scene black
    with dissolve
    
    return
    
label en_C9:

    scene bg school_scienceroom
    with locationchange
    
    window show

    play sound sfx_normalbell
    
    "The ringing of the school bell heralds the end of yet another school day."

    "With the exams finally over and the wait until summer break down to days rather than weeks, the mood of the class has lifted immeasurably. Even for those that don't care particularly about their marks, the stress felt by everyone else is contagious."

    "Even Mutou looks a little more sedate, and he hasn't been quite as hard on me as he usually is. He wastes little time in declaring an end to the class and beginning to clean up his desk, knowing full well that trying to teach us any further would be futile."

    "I can't help but relish the sound of the class as people put away their things and begin to chat amongst themselves. Books, hobbies, movies, music, they talk about all the usual wastes of time students would be into, released from the Hell of algebra and physics."

    "As some hang around to gossip and others skip out into the hall to make phone calls and check their messages, I hop up onto my desk with practiced ease."

    "Looks like I might be here a while, so I might as well make myself comfortable. With her head on its side resting in her arms, Suzu silently sleeps away as people move around her table paying her little heed. I used to think it painfully cute, but it's become a wholly normal sight nowadays."

    "My vision of her is momentarily broke as Hanako skitters past me to the door, the blonde Amazon waiting for her outside as she so often is. Least she has someone to attach herself to, I suppose. There are worse lives than that of a limpet."

    "The main attraction finally makes his way towards me, having carefully gone over his notes and finally packed his stuff away."

    mk "Nerd."

    hi "Uh huh. So how well did you do in your exams?"

    mk "Fine."

    mk "...Probably."

    "Hisao just grimaces before briefly looking to the slumbering girl ahead of me."

    "It's been interesting to watch him slowly become more used to Yamaku's oddities, with the way he treats Suzu perhaps being the clearest sign of it. Her falling asleep or having cataplexy attacks is just a thing that happens, and all you can do is make sure she doesn't hurt herself."

    "But it isn't just her he treats that way. On the track he casually talks with the others from the club, and he occasionally helps out the student council without confusion over whether to address the impossibly busty taskmaster or her ever-bubbly accomplice."

    "He's standing on his own two feet as a member of the class, now. I take a small amount of satisfaction from that, even if my help might not have been much in the scheme of things."

    hi "How'd Suzu do, anyway? She seems to study hard enough."

    mk "Some people have to try harder than others, unfortunately."

    hi "She just finds it hard, or what?"

    mk "It's not that. She's got a pretty good brain up there, actually."

    mk "How would you do in school if you always felt as tired as she does, though? Plus there are the classes she accidentally naps through."

    hi "That's a good point."

    "As the conversation lulls, a glance aroud the classroom proves we're the last ones here. I wonder when Mutou managed to slip out so quietly."

    hi "So what're your plans for the holidays?"

    mk "Just messin' about at Suzu's place. Pretty nearby, and there's a beach and everything. You?"

    hi "Going home, I guess."

    mk "Catching up with friends and all that, yeah?"

    hi "I don't really have any left there. Beyond meeting my mother and father, I don't really know what I'll do."

    "Hisao has a habit of delivering difficult news with a terribly stilted smile. I can't help but feel a little bit of pity for him, despite how little he may want that. He might do well in class, but I'd know better than most how school isn't everything."

    "An idea forms in my head, which only seems better the more I think about it."

    mk "Hey, why don't you come with me to Suzu's!?"

    hi "You sure about that? I'm not even sure she likes me."

    mk "Believe me, she's cool with you. It'll be fun, don't worry about it so much!"

    hi "If she's okay with it..."

    mk "C'mon man, lighten up. You survived exams, now's your time to enjoy yourself."

    mk "Besides, shouldn't a man be pleased to spend a summer with two girls? We could do this, and we could do that..."

    "He tries his best not to look interested as I wildly grin and move my hand suggestively."

    yuk "You shouldn't talk like that, Miki; people might think you're serious. Especially with you being you."

    "Haru's eyes flit to the side for just a second. I just smirk before addressing Yukio."

    mk "Who says I'm joking?"

    yuk "You're not seriously thinking of hanging out with this loser, are you?"

    hi "I don't see anything wrong with the offer."

    har "I'll keep an eye on the obituaries."

    hi "Come on, she's not that rough is she?"

    "Yukio and Haru both snort, shaking his head and looking away respectively. All I do is give a flat face, but the possibility of them telling him is there. Hisao doesn't seem the type to hold a grudge, especially after his forgiving me for poking around his room, but he equally seems concerned for those weaker than he."

    "It's only now that Yukio notices Suzu in front of me, walking past my desk to get closer. He reaches out towards her, but I quickly intervene."

    mk "Oi, hands off."

    yuk "Since when were you in charge of her?"

    "I think Hisao's getting a sense of when Yukio and I are about to start going off at one another; he quickly steps in before things escalate once again, making making his friend - however reluctantly - back away from Suzu."

    hi "So uh, I'm guessing you guys came for a reason?"

    har "Just wanted to see if you lot wanted to come to the Shanghai with us."

    hi "Don't see why not. Miki?"

    mk "I'll stay here, go on and have your fun."

    hi "But..."

    mk "It's fine! See you guys tomorrow."

    "Hisao doesn't look pleased with the idea of leaving a comrade behind, but Yukio swings an arm around his neck and drags him out with he and Haru. I give an unseen wave as they leave the classroom, before turning back to my charge."

    "And so, the classroom goes quiet. All I'm left to do is idly gaze out the window."

    mk "Summer holidays..."

    "The words roll off my tongue with ease. I'm excited for them... I think. I know I've been looking forward to them, that's for sure. The topic's been on my mind for a good long time. Now that they're actually here, though, I can't quite pin down my feelings about them."

    "Maybe it's less the holidays themselves giving me cold feet, so much as what they signify. This is the last summer holiday before we graduate high school, after all."

    "I should be happy with how things are right now. My carefree days with Suzu, Haru, Hisao, Yukio, and the other guys in track club and class have been some of the best I've had since the accident, after all."

    "But those days will be over in a few months."

    "A movement from Suzu's desk catches my attention, the girl finally stirring from her long nap."

    "Blinking heavily and obviously still dazed, she picks herself up a little and groggily glances around while still half-asleep. It's only after scanning the room that she catches sight of my legs, following them up to my gently grinning face."

    "She simply turns to look out the window as I'd been before. Maybe she's still disoriented from her sleeping, apathetic towards my presence, or simply has nothing to say. In any case, she doesn't bother to say a word as she gazes at the bright summer scene outside, head resting in her hand as always."

    "I should be annoyed with her apathy for my sticking around here for her sake, but I can't even pretend to be. Maybe this is what it's like to be a doting parent, forgiving their daughter's impoliteness as lovable quirks. The more simple answer is that I'm just used to being treated like this by her."

    "I wonder what she'll do with her life. Suzu's terribly shy, but that isn't unheard of; it's not like she's anywhere near Ikezawa's level. She's never expressed any kind of ambition though, nor does she have any particular talents beyond a good work ethic."

    mk "You know how I'm coming over to your place for the holidays, right?"

    suz "Yes?"

    mk "I kinda invited Hisao."

    "Suzu just sighs. She briefly turns back to check my reaction, before going to looking outside. I can't even read her expression like this."

    suz "I guess it's fine."

    mk "Yay! It'll be great, I promise. He's a cool dude."

    suz "Is that really why you invited him?"

    mk "How do you mean?"

    suz "He doesn't like being pitied. Nobody does."

    "She really knows how to put me in my place, sometimes."

    "Is it really that bad to try and do the right thing by someone, though? I just want to make him happy, just like I want Suzu, Haru, and Yukio to be happy. That's normal for friends, right?"

    mk "Don't worry about it. Summer holidays are for relaxing, remember? We should make the most of them while they last."

    suz "'While they last'..."

    "Ah, I see now. She's been pondering the same things I have."

    "It pains me a little how I can't give her any advice on the matter. If I could find any answers, I'd give them."

    "All I can do is stay beside her as I've always done. Given that she's stayed at my side all this time, she must think the same."

    scene bg school_girlsdormhall
    with shorttimeskip
    
    "I give a quick nod to a passing first-year girl as I make my way back to my dormitory room, my hand occupied by a soft drink can. She returns the greeting as we pass, her eyes momentarily lingering on the arms bared by my tank top before we pass each other. At least that's one thing I can be proud of."

    "Another girl stands not far from my room, leaning against the wall and tapping away frantically on her phone. I might as well have not existed for all the attention she gives me as I pass by her and enter my dorm room, closing the door with a push from my foot."

    scene black
    with locationchange
    
    "The bed gives a soft thump as I fall onto it, sitting up and opening the can afterwards."

    "I try to focus on things I need to do, such as packing a bag for my outing to Suzu's, but I can't get my mind off what I was pondering earlier."

    "Nothing lasts forever. If I've learned anything in my life, that'd be it. That's not inherently a good or bad thing; it just is. Might as well ask why winters are cold and summers are hot."

    "I give the upturned cardboard box in the center of my room - a makeshift table that ended up just the right size for the job - a kick out of boredom. My aging phone falls off with a clunk, but I'm hardly worried; the thing's practically indestructible, which has been proven many times over."

    "Some of us will go on to great universities, others to menial jobs, and a few will go into family businesses. Most of the students here have long stories ahead of them, of which high school is but one small chapter. For me, graduation is as final as the period at the end of a sentence."

    "They might not say it, but I suspect the same thing has run through the minds of Suzu and Hisao. Yukio and Haru have their futures planned out, as a politician and baker respectively. The other two, not so much."

    "But I'm sure they'll both be fine. They're both good people, and know how to work hard once their hearts are set to a task. I had my shot, and I blew it."

    "Eventually, our carefree days will end. These summer holidays will be our last distraction from that looming future."

    "A sudden ringing breaks me from my thoughts. Setting the can on the corner of my desk, I hurridly got off the bed and scavenge the noisy phone from the floor as it skitters about vibrating away."

    "The number on the display is instantly recognisable."

    mk "Hi, dad."

    "I always feel like I'm on tenterhooks when I talk to him like this. Not at all when I'm talking to him face to face, but something about yakking away to a disembodied voice always put me off."

    "His deep voice is warm and boisterous as always, and entirely too loud for what's appropriate over the phone."

    jun "Miki! What'd I tell ya 'bout callin' me sometimes?"

    mk "I know, I know. It's just been busy."

    jun "Ah, exams, right? I hope you've done better than last year's effort."

    mk "So what's going on?"

    "Yeah, real smooth. I bet he didn't catch that diversion at all."

    "Thankfully, he just grumbles a bit before moving on. I'll get an earful once the results come in, no doubt."

    jun "Just wonderin' if you wanted to come up here. Finally got some of the rooms cleared, so we actually 'ave some space if you want to bring anyone."

    "Thinking back, a good half of the house has tended to be a complete mess. Since we never used the rooms, they ended up filled with this and that and rarely ever even dusted, let alone properly organised."

    "A summer at home. I've already made arrangements with Suzu, but I could probably twist her arm into coming with me. Same goes for Hisao."

    "It's been so long since I've been there. Simply no point, really; it's quite some way from here to travel, and beyond my father, there was nobody to meet or play with. If I had Hisao and Suzu for company, though, it might not be so boring."

    #"But I'd agreed to go to Suzu's, which has always been a fun experience. An opportunity to show Hisao the country, though..."

    # Choice point
    
    window hide
    
    return
    
label en_choiceC9:
menu:
    with menueffect
    
    "But I'd agreed to go to Suzu's, which has always been a fun experience. An opportunity to show Hisao the country, though..."
    
    "Follow existing plan.":
        return m1

    "Agree to go.":
        return m2
        
label en_C9a:
    # Follow existing plan

    window show
    "As much as the idea may tempt me, I told Suzu that I'd stay with her family."

    mk "I kinda already promised Suzuki I'd stay with her. Sorry."

    jun "Don't worry! Long as you're spendin' the time with someone, it's fine! Drop around at some point, though. It's been too long since I've seen you."

    mk "I will, don't worry. I'll give you a call later, okay?"

    jun "Just take it easy, Miki. I love you."

    mk "I know. I love you too."

    "I hate saying that over the phone."

    jun "And your exam result had better be better than you last ones, you hear me?"

    "All that can be heard afterwards is the phone's beeping."

    "Son of a bitch."

    # Continue onto Suzu branch
    window hide
    return
    
label en_C9b:
    # Agree to go

    window show
    "After thinking about it, I finally come to a decison."

    mk "Alright, I'll come. I'll be bringing two of my friends, though."

    jun "That's what I like to hear! Couple of your running friends, or what?"

    mk "Just Suzuki and Nakai, if they agree."

    jun "Nakai... Nakai..."

    "Oh, right. I haven't mentioned Hisao to him yet."

    mk "He's a friend from class. Pretty mild-mannered dude, shouldn't be trouble."

    jun "Bah! Your friends have always been trouble. Good thing I'm used to it by now."

    jun "It'll be good to see you again. Take care of yourself until you get here, alright?"

    mk "I will. Thanks."

    "With that, we say our goodbyes."

    "I guess I have some explaining to do with Suzu... but it should be an interesting holiday, provided they come."

    "After all these years, I'll finally be returning home."

    # Continue to Hisao branch
    window hide
    return
