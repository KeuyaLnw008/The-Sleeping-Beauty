# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Narrator = Character(None)
define Prince = Character("Prince", color = "#cc0066",what_prefix='“', what_suffix='”',outlines = [ (absolute(1), "#000", absolute(0), absolute(0)) ])
define Princess = Character("Princess", color = "#cc0066",what_prefix='“', what_suffix='”',outlines = [ (absolute(1), "#000", absolute(0), absolute(0)) ])
define Servent = Character("Servant", color = "#cc0066",what_prefix='“', what_suffix='”',outlines = [ (absolute(1), "#000", absolute(0), absolute(0)) ])
define A = Character("")
define B = Character("Horseman", color = "#cc0066",what_prefix='“', what_suffix='”',outlines = [ (absolute(1), "#000", absolute(0), absolute(0)) ])
define Player =Character("[mcname]", color = "#cc0066",what_prefix='“', what_suffix='”',outlines = [ (absolute(1), "#000", absolute(0), absolute(0)) ])
define Player_proto =Character("คุณ", color = "#cc0066",what_prefix='“', what_suffix='”',outlines = [ (absolute(1), "#000", absolute(0), absolute(0)) ])

image loading_scene = Movie(size=(1920,1080), channel="movie",play="video/Untitled.ogv",)

$ End_Game = False

style test_style:
    color "#aa0000"
    size 35
style es_style:
    color "#aa0000"
    size 50

init -2:
    style say_thought:
        line_spacing 20
    style say_dialogue:
        line_spacing 20


init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#

screen door_open:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        idle "castledooridle.png"
        hover "castledoorhoverd.png"
        action Jump("theend")


init:
    $ sshake = Shake((0, 0, 0, 0), 2.0, dist=15)


# The game starts here.

label start: #Prolouge Here.
    
    show loading_scene
    with fade
    pause

    show bg empty
    with fade

    play music "audio/Music/Dark Music - The Dream Weaver.mp3" fadein 2.0

    Narrator "สวัสดี คุณผู้เล่น"

    Narrator "ยินดีต้อนรับเข้าสู่โลกนิทานของข้านะ"

    Narrator "หน้าที่ของข้าคือพาเจ้าไปท่องโลกนิทานที่ข้าแต่งขึ้น"

    Narrator "โดยส่วนใหญ่ก็จะเป็นนิทานที่มีอยู่แล้วในโลกแห่งความเป็นจริงของเจ้า"

    Narrator "แต่ข้าไม่ได้ให้เจ้ามานั่งฟังเรื่องที่ข้าแต่งอย่างเดียวหรอกนะ"

    Narrator "ทำแบบนั้นคง.... น่าเบื่อแย่เลย"

    Narrator "ข้าเลยทำให้เจ้าสามารถเข้าไปมีส่วนร่วมกับเรื่องราวของข้าได้อย่างเต็มที่"

    Narrator "โดยในคราวนี้ข้าจะพาเจ้าไปใน เรื่อง \“เจ้าหญิงนิทรา\” ก่อนละกันนะ"

    Narrator "สิ่งที่เจ้าต้องทำก็คือ สวมบทบาทเป็นคนใช่ส่วนตัวของเจ้าชายในเรื่องนี้"

    Narrator "เจ้าจะต้องช่วยเจ้าชายตามหาเจ้าหญิงนิทราในตำนานให้เจอ"

    Narrator "เห็นไหม งานง่ายๆ"

    Narrator "เอาหละๆ ก่อนที่ข้าจะพาเจ้าไปตั้งชื่อตัวละครของเจ้า"

    Narrator "เจ้ามีคำถามอะไรจะถามข้าไหม?"

    menu:
        "ไม่มี":
            Narrator "เจ้าคงจะขี้เกียจถามสินะ"
            Narrator "สมกับบทบาทคนใช้ขี้เกียจจริงๆ"
            Narrator "งั้นก้มาเริ่มตั้งชื่อตัวละครของเจ้าเลยดีกว่านะ"
        "หาววว (หลับ)":
            Narrator "...."
            Narrator "เจ้าควรเรียนไปเรียนมารยาทในการเป็นผู้ฟังที่ดีมาเพิ่มนะ"
            Narrator "ข้าละเหนื่อยใจจริงๆ"
            Narrator "งั้นก็มาเริ่มตั้งชื่อตัวละครของเจ้าซะ ก่อนที่ข้าจะยัดชื่ออัปมงคลให้กับเจ้าแทน"
    scene bg entername
    with None

    $ mcname = renpy.input("ตั้งชื่อให้ตัวเองสิเจ้าคนใช้ขี้เกียจ")

    $ mcname = mcname.strip()
    if mcname == "":
        $ mcname = "Marcus"
        Narrator "เจ้าลืมใส่ชื่อรึไง? -_- งั้นเอาชื่อ Marcus ไปละกันนะ ง่ายดี"

    show bg empty
    with fade

    Narrator "[mcname]..."

    Narrator "ชื่อเห่ยดีข้าชอบนะ"

    Narrator "เอาละ ในเมื่อมีชื่อแล้ว เจ้าก็คงพร้อมที่จะออกไปช่วยเจ้าชายแล้วละ"

    Narrator "โอ้...แต่เกือบลืมไป ข้าขอเตือนอะไรไว้อย่างนึง"

    Narrator "อารมณ์ของเจ้ามีผลต่อ เรื่องราวนี้ เพราะฉะนั้นเวลาจะทำอะไรก็เลือกดีๆนะ"

    Narrator "เอาละเดียวข้าจะเริ่มเล่าเรื่องราวของตำนานนี้ให้เจ้าฟัง ตั้งใจฟังดีๆละ"

    Narrator "จากนี้ไปนิทานที่เคยเป็นจะเปลี่ยนไปจากตำนานเก่าที่เคยเป็นมา..."

    Narrator "และมันจะเป็นจุดเริ่มต้นของเรื่องราวทั้งหมด ที่ข้าจะเล่าตอนไปนี้"

    scene bg empty
    with fade

    stop music fadeout 2.0

    Narrator "ณ อาณาจักรแห่งหนึ่ง"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/Music/Dark Music - The Secret Garden.mp3" fadein 2.0

    scene bg prolouge1
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    Narrator "ซึ่งปกครองโดยพระราชาและราชินี ที่มีธิดาเป็นเจ้าหญิงผู้เลอโฉม"

    Narrator "อยู่มาวันหนึ่งก็เกิดเหตุการณ์ประหลาดขึ้น" 

    Narrator "ดินแดนที่เคยเต็มไปด้วยผู้คน ตอนนี้กลับกลายเป็นดินแดนร้างที่ไม่มีแม้แต่ฝูงสัตว์อาศัยอยู่"

    Narrator "พร้อมกับมีข่าวลือว่าในที่ตั้งของปราสาทที่เคยเป็นวังหลวงมีหญิงสาวผู้เลอโฉมนอนหลับไหลอยู่"

    scene bg prolouge2
    with fade

    Narrator "เหล่าผู้คนที่ได้ยินเรื่องราวที่ผ่านมาได้ทำการบอกต่อกันมา"

    Narrator " ว่าหญิงสาวคนนั้นเป็นธิดาของพระราชาและราชินีของดินแดนแห่งนั้น"

    Narrator "จากคำกล่าวของผู้คนก็ยังได้รู้อีกว่า..."

    Narrator "หากผู้ใดได้พบกับเจ้าหญิงและจุมพิตกับเธอจะทำให้ เจ้าหญิงผู้เลอโฉม ตื่นจากการหลับไหล"

    Narrator "คนคนนั้นก็จะได้ขึ้นเป็นพระราชาพร้อมกับได้เจ้าหญิงมาเป็นคู่ครอง และจะได้อยู่ด้วยกัน อย่างมีความสุข"

    scene bg prolouge3
    with fade

    Narrator "จากข่าวลือเหล่านี้ทำให้มีเหล่าสุภาพบุรุษจากทั่วทุกดินแดน"

    Narrator "ไม่ว่าจะเป็นเจ้าชายจากอาณาจักรใกล้เคียง พระราชา หรือแม้กระทั้งคนสามัญชน"

    Narrator " ก็ได้ออกเดินทางเพื่อไปยังดินแดนแห่งนี้ เพื่อต้องการที่จะได้จุมพิตกับเจ้าหญิง"

    Narrator "และได้มาซึ่ง ทั้งความรักและอำนาจที่จะได้รับมา"

    Narrator "แต่ไม่ว่าเวลาจะผ่านไปนานมากขนาดไหน"

    Narrator "ก็ยังไม่มีข่าวหรือข้อมูลที่จะเป็นสิ่งชี้นำได้ว่าเจ้าหญิง ได้จุมพิตและครองรักกับผู้ใดเลย...."

    scene bg empty
    stop music fadeout 1.0

    Narrator "มีเพียงอยู่สิ่งเดียวที่เป็นข้อเท็จจริงที่เกิดขึ้นก็คือ .."

    jump chapter1
    
    return



label chapter1:

    Narrator "{sc}{b}{i}{font=KC Nightmare.ttf}{=test_style}ยังไม่มีใครคนไหนที่ออกเดินทางไปหาเจ้าหญิงผู้เลอโฉม... {/b}{/font}{/i}{/=test_style}{/sc}"
    
    Narrator "{sc}{b}{i}{font=KC Nightmare.ttf}{=test_style}แล้วรอดออกมาจากดินแดนแห่งนั้น สักคนเดียว... {/b}{/font}{/i}{/=test_style}{/sc}"

    play sound "audio/Effect/Thunder   Sound effect.mp3"
    window hide
    pause 8
    
    play music "audio/Music/Professor Layton And the Unwound Future_Lost Future OST.mp3" fadein 2.0

    scene bg carriage
    with fade
    
    show prince
    with dissolve 

    Prince "เรื่องนั้นข้าได้ยินจนเบื่อแล้วล่ะนะ" 

    Player "ก็เห็นท่านทำหน้าตาเบื่อหน่ายมาตลอดทางที่นั่งรถม้ามานี่ขอรับ"

    Player "ข้าเลยอยากจะเล่าอะไรให้ฟังซักหน่อยเพื่อนายท่านจะหายเบื่อบ้าง"

    Prince "เฮ้อเจ้านี่จริงๆเลย... แล้วอีกนานไหมกว่าที่เราจะถึงหมู่บ้านที่เป็นจุดหมายปลายทางของเรา"

    Player "อีกไม่นานหรอกขอรับ ผ่านโค้งตรงนั้นไปก็น่าจะเห็นทางเข้าหมู่บ้านแล้วล่ะขอรับ"

    show prince happy
    with dissolve
    Prince "{=say_dialogue}งั้นก็ดี ตั้งแต่เรานั่งรถม้าออกมาจากวังจนมาถึงที่นี่ ทำเอาข้าปวดแข้งปวดขาไปหมดแล้ว แถมยังหิวจนไส้กิ่วอีกต่างหาก{/=say_dialogue}"

    Player "ก็นายท่านเป็นคนพูดเองนี่ขอรับว่าไม่ขอเสวยมื้อเช้าเพราะต้องการที่จะรีบออกไปตามหาเจ้าหญิงนิทรา"

    Player "ท่านจะมาบ่นทำไมล่ะขอรับ เป็นนายท่านที่เรื่องมากจริงๆนะขอรับ"
    
    show prince angry
    with dissolve
    
    Prince "ก็จริงนะแต่ นี่เจ้าแอบด่าข้าอยู่หรือเปล่า! เดี๋ยวก็สั่งประหารสะเลยนี่"

    Prince "อีกอย่างคนที่เล่าเรื่องนี้ให้ข้าฟังมันก็เจ้าไม่ใช่หรือไง!!!"

    show prince
    with dissolve

    Prince "เจ้าน่ะต้องช่วยข้าตามหาเจ้าหญิงนิทราให้จงได้"

    menu:
        "ไม่ล่ะขอรับ ข้าขอกลับไปที่วังดีกว่า":
            Prince "ข้าส่งเจ้ากลับไปได้นะ แต่มีแค่หัวที่ได้จะกลับไปที่บ้านของเจ้าล่ะนะ !"
            Player "ข้าไม่กลับแล้วขอรับ ข้าจะช่วยนายท่านอย่างสุดความสามารถเลยขอรับ !!"
        "แน่นอนขอรับ ข้าจะติดตามท่านไปเอง":
            Prince "ให้มันได้แบบนี้ สมกับเป็นข้ารับใช้ที่ข้าไว้ใจมากที่สุด"
            Player "ท่านพูดแบบนี้ข้าก็เขินแย่เลยสิขอรับ"    

    show prince happy
    with dissolve

    Prince "ฮึย ฮึ้ย"

    Prince "ข้าชักอยากจะเห็น เจ้าหญิงผู้เลอโฉม ว่าจะเหมาะมาเป็นมหาสีของข้าหรือเปล่า"

    Player "เอาละๆ พักเรื่องนี้ไว้ก่อนแล้วกัน"
    
    stop music

    play sound "audio/Effect/Horse screaming sound.mp3" 
    A "(เสียงม้าร้อง)"

    show prince shock
    with dissolve

    Prince "เกิดอะไรขึ้น!!!"

    B "ไม่ทราบขอรับ จู่ๆ ม้าก็มีอาการแปลกๆ ควบคุมรถม้าไม่อยู่แล้วขอรับ !!!"
    

    scene bg empty
    play sound "audio/Effect/Accident_crash_sound_effect.mp3"
    A "ทุกคน(อ๊ากกกกกก !!!!!)"

    A "โคร้มมมมม" with sshake
    pause 5

    jump chapter4entrance


return

label chapter4entrance:

    A "หลายชั่วโมงผ่านไป..."

    Prince "ตื่น………" with vpunch

    Prince "ตื่น…….. ตื่น…….! ตื่นได้แล้วจะนอนไปจนถึงเมื่อไหร่ !!!!!!" with vpunch

    play music "audio/Music/Mysterious Forest.mp3" fadein 2.0

    scene bg scaryforest
    with fade

    show prince
    with fade

    Player "อ่ะ นะ นายท่าน…. นี่มันเกิดอะไรขึ้นหรือขอรับ"

    Prince "ข้าก็ไม่รู้เหมือนกัน จู่ๆรถม้าที่พวกเรานั่งมาก็เกิดอุบัติเหตุขึ้นมา ข้าก็พึ่งได้สติก่อนเจ้าได้ไม่นาน"

    Player "อย่างงั้นหรือขอรับ"

    Prince "แล้วเจ้ารู้หรือเปล่าว่าเกิดอะไรขึ้น ? ดูเหมือนที่นี่มันจะคนละที่กับจุดที่รถม้าเกิดอุบัติเหตุนะ"

    Player "ข้าน้อยเองก็ไม่รู้เหมือนกันขอรับแต่ที่แน่ๆดูเหมือนจะไม่มีใครนอกจากพวกเราอยู่ที่นี่นะขอรับ"

    Prince "นั่นสินะ แล้วนี่เจ้าเดินได้หรือยังถ้าเดินออกจากป่านี่น่าจะรู้อะไรบ้าง"

    menu:
        "ไม่ไหวขอรับขอข้าพักก่อนได้ไหมขอรับ":
            Prince "งั้นข้าจะลากเจ้าไปเอง ข้าขี้เกียจที่จะรอให้เจ้าหายดี"
            Player "งะ งั้น ขะ ข้า ขอเดินเองดีกว่าขอรับนายท่าน"
        "ไหวแน่นอนขอรับ":
            Prince "งั้นก็ดี ไปกันเลย"
            Player "ขอรับ!"
     
    stop music fadeout 1.0
    
    play music "audio/Music/Tense Horror Music No Copyright Loop _Scary Forest_.mp3" fadein 2.0
    
    scene bg roseforest 
    with fade
    pause 3
    
    Narrator " ทั้งสองออกเดินทาง ผ่านป่าที่น่ากลัว และผิศวง"

    Narrator "เดินทางไปเรื่อยๆๆ มีหลายครั้งที่ทั้งสองจะหลงทาง"

    Narrator "แต่ก็ไม่หลง..."

    Narrator "สงสัยคนใช้ที่ข้าส่งไปคงจะเก่งเกินไปหน่อย"

    Narrator "น่าสนใจจริงๆ"

    scene bg rosemountain
    with fade
    pause 3

    Prince "เฮ้อ ดูเหมือนจะออกมาจากป่าแล้วล่ะนะ แต่เจ้ารู้ได้ยังไงว่าเดินมาทางนี้แล้วจะออกจากป่าได้"

    Player "......................."

    Prince "ยืนตัวแข็งอะไรของเจ้า ?"

    Player "นายท่านขอรับ นะ นะ นั่นมัน ปะ ปะ ปราสาท ขะ ขอรับ !!!!"

    Prince "อะไรนะ !!!"

    scene bg castle
    with fade

    Prince "ใช้แล้วต้องใช่แน่ๆ"

    Prince "ปราสาทของเจ้าหญิงนิทรา ดูเหมือนจะมาถึงแล้วสินะ"
    
    Prince "เราจะเข้ากันไปเลยดีหรือเปล่าเจ้าคิดว่าอย่างไร"

    menu:
        "แน่นอนขอรับเข้าไปกันเลย":
            Prince "ตอบได้ดี เข้าไปกันเลย"
            Player "ขอรับนายท่าน !"
        "ข้าว่าสำรวจรอบๆก่อนไหมขอรับ":
            Prince "ไม่ละ ขอเข้าไปเลยดีกว่า"
            Player "แล้วท่านจะถามข้าทำไมเนี่ย !?"

    scene bg castledoor
    with fade

    Prince "ช่างเป็นประตูที่งดงามเสียจริง"

    play music "audio/Music/Dark Music - The Dream Weaver.mp3" fadein 2.0

    Narrator "สวัสดีคุณผู้เล่นเป็นไงบ้างสนุกรึปล่าวละ"

    menu:
        "สนุกกับผีนะสิ":
            Narrator " ฮ่าๆๆๆ โอ้น่าสงสารจริงๆ"
        "ก็โอเคนะ ทำไมรึ?":
            Narrator "อื้มม เป็นคำตอบที่่น้อยคนจะตอบนะเนี่ย"

    Narrator "แต่ข้าก็ดีใจนะที่เจ้าตอบมาตรงๆ เพราะข้านะ..."

    Narrator "{sc}{b}{i}{font=KC Nightmare.ttf}{=test_style}เกลียดคนโกหกมากที่สุดเลยละ...{/b}{/font}{/i}{/=test_style}{/sc}"

    Narrator "เอาละเจ้าก็มาถึงหน้าประสาทของเจ้าหญิงในตำนาน"

    Narrator "คงจะดีใจละสินะ ที่หน้าที่ของนาย {bt}{b}ใกล้จะจบลงแล้ว{/b}{/bt}"

    Narrator "แต่นั้นแหละนะ ก็ทำหน้าทีของเจ้าให้ดีละกัน เพราะว่า...."

    Prince "เจ้าคุยกับใครนะ?"

    stop music

    show prince at left
    with dissolve

    menu:
        "ปล่าว...ข้าแค่คุยกับตัวเองนะ":
            jump goodend
        "ข้าคุยกับ...ประตูนะ":
            jump badend

return
label goodend:

    Prince "เจ้าคงจะเครียดมากเลยสินะ"
    Prince "เป็นเพราะข้าน่าจะพูดไม่ดีกับเจ้าหลายๆ อย่าง..."
    Prince "ข้านี้ช่างเป็นเจ้าชายที่แย่จริงๆ"
    Player "ไม่หรอกครับท่าน คนเราก็ผิดพลาดกันได้"
    Prince "งั้นหรอ"
    Player "เรารีบเข้าไปดีกว่าครับๆ"
    call screen door_open

return

label badend:

    show prince angry at left
    with dissolve

    Prince "เจ้าบ้าไปแล้วรึไงรีบเปิดประตูได้แล้ว"
    Player "ขอรับ...."

    call screen door_open

return

label theend:

    play sound "audio/Effect/Wood Gate Open (Fortnite Sound).mp3"

    scene bg insidecastle
    with fade
    pause 2

    play music "audio/Music/Dark Music - Queen of Thorns.mp3" fadein 2.0

    Prince "ว้าวววววว"

    Player "สะ สุดยอดไปเลยนะขอรับ"

    show prince happy
    with dissolve

    Prince "จริงๆด้วยสินะ ที่นี่เป็นปราสาทของเจ้าหญิงนิทราจริงๆ"

    Player "นายท่าน ดูห้องตรงนั้นสิขอรับ"

    hide prince happy
    scene bg princessdoor
    with pushleft

    show prince shock
    with dissolve
    pause(1.0)

    show prince shock at left
    with move
    pause(1.0)

    Prince "นั่นมัน ?"

    Player "ดูเหมือนจะเป็นห้องของเจ้าหญิงนิทรานะขอรับ"

    show prince
    with dissolve
    
    Prince "ข้าก็คิดแบบนั้น งั้นลองเข้าไปดูเลยดีกว่า"

    Player "ระวังตัวด้วยนะขอรับ อาจจะเป็นกับดักอะไรสักอย่างก็ได้นะขอรับ"

    play sound "audio/Effect/Wood Gate Open (Fortnite Sound).mp3"

    scene bg throneroom
    with fade
    pause 2
    
    show prince at left
    with dissolve

    Prince "นี่เจ้าดูตรงทางเข้าข้างหน้าสิ ข้าคิดว่าต้องเป็นทางเข้าไปที่ห้องของนางแน่ๆเลย!!"

    Prince "{size=+20}เจ้าหญิงนิทรา{/size}"

    Player "จริงๆด้วยขอรับ ! ในที่สุดเราก็เจอนางแล้วขอรับ !!"

    Player "วิธีปลุกเจ้าหญิงนิทราที่กำลังหลับใหลอยู่นายท่านคงจะรู้อยู่แล้วสินะขอรับ?"

    show prince happy at left
    with dissolve

    Prince "แน่นอนอยู่แล้ว"

    Prince " \“จุมพิต\” ยังไงล่ะ" 

    Prince "ข้าควรจะเข้าไปจุมพิตเลยใช้หรือไม่ เจ้าคิดว่ายังไงบ้าง?"

    menu:
        "ใช่แล้วขอรับ ต้องรีบเลยขอรับ":
            Prince "ดีล่ะงั้น...เจ้าก็รอข้าอยู่ข้างนอกห้องซะ เดียวข้าจัดการเอง"
            Player "ได้เลยขอรับ"
        "รอก่อนไหมขอรับ อาจจะเป็นกับดักก็ได้...":
            Prince "ไม่ล่ะข้ารอไม่ไหวแล้ว เจ้ารอข้าอยู่ข้างนอกห้องซะ"
            Player "ก็บอกแล้วว่าถ้าจะไม่ฟังข้าก็อย่าถามสิขอรับ !!"

    play sound "audio/Effect/FOOTSTEPS SOUND EFFECT.mp3"

    hide  prince happy
    with moveoutright
    pause 2.0

    Prince "ข้ามาหาเจ้าแล้วเจ้าหญิงผู้หลับใหล"

    Prince "ตอนนี้ข้าจะปลุกเจ้าให้ตื่นขึ้นมา และจงกลายเป็นคนรักของข้าเสียเถอะ"

    scene bg kiss
    with dissolve
    pause 3

    scene bg evil
    with dissolve
    pause 3

    Narrator "เป็นภาพที่สวยงามดีนะเจ้าว่างั้นไหม?"

    Player "โผล่มาสะตอนเกมจะจบเลยนะ"

    Narrator "ใช้........"

    Narrator "ใกล้จะถึงบทสรุปของเรื่องราวทั้งหมดแล้วสินะ"

    Player "มีอะไรรึปล่าว?"

    Narrator "เอาเป็นว่า...."

    Narrator "จำที่ข้าบอกเอาไว้ให้ดีๆก็แล้วกันนะ"

    scene bg throneroom
    with fade
    
    Narrator "หลังจากเจ้าที่ชายได้จุมพิตกับเจ้าหญิง..."

    Narrator "เจ้าหญิงก็ได้ตื่นขึ้นจากการหลับใหล"

    stop music

    play music "audio/Music/Professor Layton And the Unwound Future_Lost Future OST.mp3" fadein 2.0

    show prince at left
    with dissolve

    show princess at right
    with dissolve

    Princess "ท่าน...คือ...ใครหรอเพคะ?"

    Prince "ข้าคือเจ้าชาย อาเธอร์ แห่งเรเนเดียร์ ข้ามาเพื่อตามหาเจ้าหญิงผู้เลอเฉิมที่เขาเลื่องลือกัน"

    Prince "และเจ้าก็ชั่งงามสมคำร่ำลือจริงๆ"

    Princess "ขอบคุณที่ชมเพคะ...ท่านช่าง..."

    show prince happy at left
    with dissolve

    Prince "อะไรหรอๆ"

    Narrator "คุณที่กำลังมองเจ้าหญิงอย่างจดจ่อ"

    menu:
        "นางต้องเขินแน่ๆเลย >_<":
            Princess "น่ากิน..."
        "นางน่าจะพูดติดอ่างแน่ๆเลย":
            Princess "น่ากิน..."

    show prince shock at left
    with dissolve

    Prince "หะ!"

    Princess "ไม่ๆ...ข้าหมายถึงน่ารักจนน่ากินนะ เพคะ"

    show prince happy at left
    with dissolve

    Prince "อ่ออออ อย่างงี้นี้เองๆ"

    Princess "แต่ว่านะเพคะ...ตอนนี้ข้าหิวมากๆเลย..."

    Princess "ถ้าไม่เป็นการรบกวน..."

    Princess "พอจะมีอะไรให้หม่อมฉันทานไหม เพคะ"

    Prince "อ้า....แย่จังตอนนี้เราไม่มีอะไรติดมาเลยเดียวข้าให้คนใช้ไปหามาให้นะ"

    Prince "คนใช้!..."

    stop music

    Narrator "ทันใดนั้นเองเจ้าชายก็ได้ตะหนักถึงสิงที่เปลี่ยนไป"

    scene bg throneroom2
    with fade

    show prince shock at left
    with dissolve

    play music "audio/Music/Dark Music - Wilt Beauty.mp3" fadein 2.0

    Prince "อะไร เกิดอะไรขึ้นทำไมห้องถึงกลายเป็นแบบนี้" 

    Narrator "ห้องที่เคยเต็มไปด้วยกุหลายกลาย เป็นห้องที่เต็มไปด้วยหัวกะโหลกและโครงกระดูก..."

    Prince "คนรับใช้ คนรับใช้ !!! เกิดอะไรขึ้นกับห้องนี้" with vpunch

    Prince "{size=+10} %(mcname)s !{/size} " with vpunch

    Prince "{size=+20} %(mcname)s !{/size} " with vpunch

    Player "เจ้า......"

    Player "........"

    Player "........"

    Player "อะไรวะ ทำไมพูดไม่ได้"

    Narrator "ข้าว่า..."

    Narrator "เจ้ายืนดูเฉยๆดีกว่านะ ฮ่า ฮ่า ฮ่า"

    Player "ไอ้ Narrator!!!"

    play sound "audio/Effect/Undertale - Omega Flowey's Laugh.mp3"
    Narrator "{sc}{b}{i}{font=KC Nightmare.ttf}{=test_style}ฮ่ะ ฮ่ะ ฮ่า ฮ่า ฮะ ฮ่ะ ฮ่า ฮ่า ฮ่า ฮ่า ฮ่า ฮ่า{/b}{/font}{/i}{/=test_style}{/sc}" with sshake
    
    scene bg creepy1
    with dissolve

    Princess "{size=+10}ข้า...{/size}"   

    Prince "จะ...เจ้าหญิง เจ้าดูแปลกๆไปนะ"

    scene bg creepy2
    with None

    Princess "{size=+20}ข้า...{/size}"

    stop music

    play sound "audio/Effect/Bone Tear and Break Sound Effect 1.mp3"

    scene bg creepy3
    with None
    pause 4

    play sound "audio/Effect/718-scream.mp3"
    Princess "{sc}{b}{i}{font=KC Nightmare.ttf}{=es_style}หิว!!!!{/b}{/font}{/i}{/=es_style}{/sc}" with sshake

    Prince "อย่านะ! อย่าๆๆ!!!"

    Prince "{size=+20}อย่าาาาาาาา{/size}" with vpunch

    play sound "audio/Effect/Dinosaur blood sounds.mp3"

    scene bg creepy4
    with sshake
    pause 5

    play sound "audio/Effect/Dinosaur blood sounds.mp3"
    scene bg empty
    with None
    Prince "อ๊ากกก" with sshake

    play sound "audio/Effect/Dinosaur blood sounds.mp3"
    scene bg empty
    with None
    Prince "อ๊ากกกกกกกกกกก" with sshake

    scene bg empty
    with None
    pause 5
    
    Narrator "ฮืมม ดูแล้วสถานะการไม่ค่อยดีเลยนะ"
    Narrator "ดั่งกลอนที่ประพันธ์ไว้ว่า..."

    Narrator "กุหลาบแดงคือแสงแห่งรัก"
    Narrator "กุหลาบหักคือรักที่สลาย"
    Narrator "กุหลาบเขียวคือรักที่เดียวดาย"
    Narrator "กุหลาบตายคือคนที่ถูก...."

    Narrator "{b}{font=KC Nightmare.ttf}{color=#aa0000}{size=+30} กิน {/b}{/font}{/color}{/size}"

    play music "audio/Music/Dark Music - Wilt Beauty.mp3" fadein 2.0

    scene bg throneroom2
    with fade
    show princess evil

    Princess "เจ้า...."

    Princess "เจ้าคนใช้หน้าโง่ตรงนั้นนะ"

    Princess "ขอบใจนะที่พาอาหารอันโอชะมาถึงที่"

    Princess "ข้าละชอบพวกเจ้าชายวัยละอ่อนพวกนี้จริงๆ"

    window hide
    play sound "audio/Effect/Girl Laugh- Sound Effect.mp3"
    pause 3

    Princess "แต่ว่านะ..."

    Princess "ข้าจะทำยังไงกับเจ้าดี"

    Princess "อ้า ข้านึกออกแล้ว"

    Princess "เจ้ามาเป็นลูกสมุนของข้าดีไหมนะ"

    Princess "แลกกับที่ข้าจะไม่ {b}{font=KC Nightmare.ttf}{color=#aa0000}{size=+30} ฆ่า {/b}{/font}{/color}{/size} เจ้า"

    Princess "ดีไหม ฮึๆ"
    
    menu:
        "ข้ายอมแล้วอย่าฆ่า ข้าเลย":
            $End_Game = True
            jump credit
        "ข้าไม่ยอมแกหรอกอีนังปีศาจ!!!":
            $End_Game = True
            jump credit
return

label credit:

scene bg credit1
with fade
pause 3
scene bg credit2
with fade
pause 3
scene bg credit3
with fade
pause 3
scene bg credit4
with fade
pause 3
scene bg credit5
with fade
pause 3
scene bg credit6
with fade
pause 3
scene bg credit7
with fade
pause 3
scene bg credit8
with fade
pause 3
scene bg empty
with fade
pause 2

if End_Game == True:
    $config.name = _("The Creeping Beauty")



return
    
