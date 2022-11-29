"""
File: Haikyu!! Fly~~
Name: Yi Lin Yang
----------------------
TODO:
my drawing is a volleyball player in Haikyu!
Fly and dig the ball!!
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Haikyu!! Fly~~
    自由球員最帥氣了! 西谷最帥氣了!
    """
    # background and label
    background = GRect(800, 400)
    background.filled = True
    background.fill_color = 'darkgray'

    libero = GLabel('LIBERO', x=430, y=100)
    name = GLabel('西 谷  夕', x=560, y=150)
    haikyu = GLabel('ハイキュー!!', x=0, y=350)
    libero.font = '-80'
    name.font = '-45'
    haikyu.font = '-35'
    libero.color = 'orangered'
    name.color = 'orangered'
    haikyu.color = 'gold'

    # volleyball
    window = GWindow(width=800, height=400)
    volleyball = GOval(121, 121, x=20, y=30)
    volleyball.filled = True
    volleyball.fill_color = 'orange'

    blue_pc1 = GArc(180, 180, 120, 50, x=24, y=35)
    blue_pc1.filled = True
    blue_pc1.fill_color = 'royalblue'
    blue_pc1.color = 'royalblue'

    blue_pc2 = GArc(180, 180, 285, 50, x=57, y=56)
    blue_pc2.filled = True
    blue_pc2.fill_color = 'royalblue'
    blue_pc2.color = 'royalblue'

    blue_pc3 = GArc(140, 140, 10, 50, x=64, y=38)
    blue_pc3.filled = True
    blue_pc3.fill_color = 'royalblue'
    blue_pc3.color = 'royalblue'

    blue_pc4 = GArc(180, 180, 210, 55, x=28, y=60)
    blue_pc4.filled = True
    blue_pc4.fill_color = 'royalblue'
    blue_pc4.color = 'royalblue'

    tetragon1 = GPolygon()
    tetragon1.add_vertex((81, 86))
    tetragon1.add_vertex((60, 68))
    tetragon1.add_vertex((25, 66))
    tetragon1.add_vertex((40, 73))
    tetragon1.filled = True
    tetragon1.color = 'royalblue'
    tetragon1.fill_color = 'royalblue'

    tetragon2 = GPolygon()
    tetragon2.add_vertex((81, 86))
    tetragon2.add_vertex((90, 64))
    tetragon2.add_vertex((100, 53))
    tetragon2.add_vertex((115, 42))
    tetragon2.add_vertex((130, 63))
    tetragon2.add_vertex((100, 75))
    tetragon2.filled = True
    tetragon2.color = 'royalblue'
    tetragon2.fill_color = 'royalblue'

    tetragon3 = GPolygon()
    tetragon3.add_vertex((81, 86))
    tetragon3.add_vertex((110, 93))
    tetragon3.add_vertex((124, 103))
    tetragon3.add_vertex((134, 116))
    tetragon3.add_vertex((102, 117))
    tetragon3.filled = True
    tetragon3.color = 'royalblue'
    tetragon3.fill_color = 'royalblue'

    tetragon4 = GPolygon()
    tetragon4.add_vertex((81, 86))
    tetragon4.add_vertex((65, 106))
    tetragon4.add_vertex((65, 150))
    tetragon4.add_vertex((76, 120))
    tetragon4.filled = True
    tetragon4.color = 'royalblue'
    tetragon4.fill_color = 'royalblue'

# right hand
    hand1 = GPolygon()
    hand1.add_vertex((196, 155))
    hand1.add_vertex((151, 167))
    hand1.add_vertex((100, 196))
    hand1.add_vertex((43, 237))
    hand1.add_vertex((34, 273))
    hand1.add_vertex((58, 285))
    hand1.add_vertex((73, 279))
    hand1.add_vertex((89, 257))
    hand1.add_vertex((83, 250))
    hand1.add_vertex((100, 233))
    hand1.add_vertex((103, 224))
    hand1.add_vertex((126, 217))
    hand1.add_vertex((172, 208))
    hand1.add_vertex((202, 192))
    hand1.add_vertex((239, 187))
    hand1.add_vertex((249, 186))
    hand1.add_vertex((255, 177))
    hand1.add_vertex((257, 160))
    hand1.add_vertex((254, 145))
    hand1.add_vertex((249, 136))
    hand1.add_vertex((232, 146))
    hand1.filled = True
    hand1.fill_color = 'peachpuff'

    thumb1 = GLine(75, 239, 71, 247)
    thumb2 = GLine(71, 247, 57, 260)
    thumb3 = GLine(57, 260, 50, 269)
    thumb4 = GLine(50, 269, 50, 275)
    thumb5 = GLine(50, 275, 60, 272)
    thumb6 = GLine(60, 272, 73, 258)
    thumb7 = GLine(73, 258, 83, 250)

    finger1 = GLine(104, 225, 110, 212)
    finger2 = GLine(67, 240, 67, 250)
    finger3 = GLine(57, 244, 63, 253)
    finger4 = GLine(52, 257, 58, 257)

    # left hand
    hand2 = GPolygon()
    hand2.add_vertex((350, 278))
    hand2.add_vertex((332, 304))
    hand2.add_vertex((319, 309))
    hand2.add_vertex((305, 316))
    hand2.add_vertex((225, 371))
    hand2.add_vertex((194, 376))
    hand2.add_vertex((170, 375))
    hand2.add_vertex((157, 376))
    hand2.add_vertex((156, 381))
    hand2.add_vertex((162, 387))
    hand2.add_vertex((181, 387))
    hand2.add_vertex((192, 393))
    hand2.add_vertex((173, 405))
    hand2.add_vertex((164, 419))
    hand2.add_vertex((241, 400))
    hand2.add_vertex((336, 343))
    hand2.add_vertex((358, 330))
    hand2.add_vertex((397, 287))
    hand2.add_vertex((374, 279))
    hand2.add_vertex((351, 278))
    hand2.filled = True
    hand2.fill_color = 'peachpuff'
    fingerline = GLine(194, 376, 170, 375)

    # elbow pad
    elbow_pad = GPolygon()
    elbow_pad.add_vertex((195, 154))
    elbow_pad.add_vertex((204, 171))
    elbow_pad.add_vertex((201, 193))
    elbow_pad.add_vertex((221, 190))
    elbow_pad.add_vertex((240, 188))
    elbow_pad.add_vertex((244, 166))
    elbow_pad.add_vertex((243, 160))
    elbow_pad.add_vertex((239, 152))
    elbow_pad.add_vertex((227, 146))
    elbow_pad.filled = True

    # jersey, right-hand side
    jersey1 = GOval(40, 70, x=217, y=127)
    jersey1.filled = True
    jersey1.fill_color = 'sandybrown'

    # jersey, top
    jersey2 = GPolygon()
    jersey2.add_vertex((240, 126))
    jersey2.add_vertex((261, 126))
    jersey2.add_vertex((276, 119))
    jersey2.add_vertex((294, 113))
    jersey2.add_vertex((307, 114))
    jersey2.add_vertex((425, 167))
    jersey2.add_vertex((439, 206))
    jersey2.add_vertex((438, 236))
    jersey2.add_vertex((414, 267))
    jersey2.add_vertex((401, 297))
    jersey2.add_vertex((344, 283))
    jersey2.add_vertex((355, 266))
    jersey2.add_vertex((287, 189))
    jersey2.add_vertex((273, 183))
    jersey2.add_vertex((240, 198))
    jersey2.filled = True
    jersey2.fill_color = 'sandybrown'

    # jersey, bottom
    jersey3 = GPolygon()
    jersey3.add_vertex((429, 178))
    jersey3.add_vertex((451, 186))
    jersey3.add_vertex((473, 191))
    jersey3.add_vertex((491, 213))
    jersey3.add_vertex((512, 217))
    jersey3.add_vertex((530, 232))
    jersey3.add_vertex((544, 239))
    jersey3.add_vertex((555, 239))
    jersey3.add_vertex((562, 249))
    jersey3.add_vertex((566, 268))
    jersey3.add_vertex((549, 301))
    jersey3.add_vertex((518, 303))
    jersey3.add_vertex((508, 318))
    jersey3.add_vertex((484, 328))
    jersey3.add_vertex((466, 316))
    jersey3.add_vertex((406, 288))
    jersey3.filled = True
    jersey3.fill_color = 'sandybrown'

    # some lines on jersey
    j_line1 = GLine(355, 264, 360, 250)
    j_line2 = GLine(360, 250, 380, 227)
    j_line3 = GLine(373, 235, 373, 225)
    j_line4 = GLine(493, 215, 500, 236)
    j_line5 = GLine(502, 259, 497, 277)
    j_line6 = GLine(497, 277, 479, 290)
    j_line7 = GLine(479, 290, 460, 298)
    j_line8 = GLine(460, 298, 433, 300)

    # pattern on the front of jersey
    tie = GPolygon()
    tie.add_vertex((324, 194))
    tie.add_vertex((328, 217))
    tie.add_vertex((343, 211))
    tie.add_vertex((395, 175))
    tie.add_vertex((402, 183))
    tie.add_vertex((372, 203))
    tie.add_vertex((348, 218))
    tie.add_vertex((324, 224))
    tie.add_vertex((319, 194))
    tie.filled = True
    tie.fill_color = 'sienna'

    j_front = GPolygon()
    j_front.add_vertex((358, 212))
    j_front.add_vertex((365, 244))
    j_front.add_vertex((371, 238))
    j_front.add_vertex((363, 207))
    j_front.filled = True
    j_front.fill_color = 'white'

    j_front2 = GPolygon()
    j_front2.add_vertex((278, 183))
    j_front2.add_vertex((278, 186))
    j_front2.add_vertex((300, 176))
    j_front2.add_vertex((300, 170))
    j_front2.filled = True
    j_front2.fill_color = 'white'

    # jersey side
    j_side1 = GPolygon()
    j_side1.add_vertex((440, 225))
    j_side1.add_vertex((422, 257))
    j_side1.add_vertex((502, 262))
    j_side1.add_vertex((500, 235))
    j_side1.filled = True
    j_side1.fill_color = 'white'

    j_side2 = GPolygon()
    j_side2.add_vertex((439, 230))
    j_side2.add_vertex((427, 251))
    j_side2.add_vertex((501, 254))
    j_side2.add_vertex((501, 242))
    j_side2.filled = True
    j_side2.fill_color = 'sienna'

    j_side3 = GPolygon()
    j_side3.add_vertex((500, 235))
    j_side3.add_vertex((562, 249))
    j_side3.add_vertex((564, 269))
    j_side3.add_vertex((501, 257))
    j_side3.filled = True
    j_side3.fill_color = 'white'

    j_side4 = GPolygon()
    j_side4.add_vertex((501, 240))
    j_side4.add_vertex((563, 254))
    j_side4.add_vertex((565, 263))
    j_side4.add_vertex((502, 254))
    j_side4.filled = True
    j_side4.fill_color = 'sienna'

    # right leg
    leg1 = GPolygon()
    leg1.add_vertex((519, 302))
    leg1.add_vertex((544, 325))
    leg1.add_vertex((566, 351))
    leg1.add_vertex((562, 368))
    leg1.add_vertex((524, 342))
    leg1.add_vertex((487, 323))
    leg1.filled = True
    leg1.fill_color = 'peachpuff'

    # left leg
    leg2 = GPolygon()
    leg2.add_vertex((557, 245))
    leg2.add_vertex((598, 259))
    leg2.add_vertex((618, 240))
    leg2.add_vertex((632, 232))
    leg2.add_vertex((650, 227))
    leg2.add_vertex((668, 213))
    leg2.add_vertex((680, 230))
    leg2.add_vertex((609, 297))
    leg2.add_vertex((547, 295))
    leg2.filled = True
    leg2.fill_color = 'peachpuff'

    # right knee pad
    knee_pad1 = GPolygon()
    knee_pad1.add_vertex((522, 306))
    knee_pad1.add_vertex((520, 320))
    knee_pad1.add_vertex((511, 330))
    knee_pad1.add_vertex((502, 332))
    knee_pad1.add_vertex((512, 341))
    knee_pad1.add_vertex((525, 345))
    knee_pad1.add_vertex((533, 339))
    knee_pad1.add_vertex((537, 330))
    knee_pad1.add_vertex((538, 318))
    knee_pad1.filled = True

    # left knee pad
    knee_pad2 = GPolygon()
    knee_pad2.add_vertex((586, 257))
    knee_pad2.add_vertex((599, 257))
    knee_pad2.add_vertex((607, 251))
    knee_pad2.add_vertex((617, 252))
    knee_pad2.add_vertex((622, 264))
    knee_pad2.add_vertex((623, 276))
    knee_pad2.add_vertex((619, 289))
    knee_pad2.add_vertex((601, 300))
    knee_pad2.add_vertex((573, 297))
    knee_pad2.add_vertex((588, 290))
    knee_pad2.add_vertex((594, 280))
    knee_pad2.add_vertex((593, 265))
    knee_pad2.filled = True

    # right socks
    socks1 = GPolygon()
    socks1.add_vertex((556, 340))
    socks1.add_vertex((567, 352))
    socks1.add_vertex((562, 373))
    socks1.add_vertex((546, 357))
    socks1.add_vertex((553, 355))
    socks1.add_vertex((556, 352))
    socks1.filled = True
    socks1.fill_color = 'white'

    # right shoe
    shoe1 = GPolygon()
    shoe1.add_vertex((561, 346))
    shoe1.add_vertex((583, 339))
    shoe1.add_vertex((590, 390))
    shoe1.add_vertex((585, 394))
    shoe1.add_vertex((580, 392))
    shoe1.add_vertex((551, 365))
    shoe1.add_vertex((562, 360))
    shoe1.add_vertex((563, 348))
    shoe1.filled = True
    shoe1.fill_color = 'white'

    shoe_line1 = GLine(562, 360, 575, 380)
    shoe_line2 = GLine(563, 359, 555, 372)
    shoe_line3 = GLine(551, 365, 568, 367)
    shoe_line4 = GLine(569, 369, 567, 382)
    shoe_line5 = GLine(561, 375, 575, 377)
    shoe_line6 = GLine(580, 339, 587, 393)

    # left socks
    socks2 = GPolygon()
    socks2.add_vertex((677, 232))
    socks2.add_vertex((675, 222))
    socks2.add_vertex((667, 213))
    socks2.add_vertex((678, 203))
    socks2.add_vertex((699, 222))
    socks2.filled = True
    socks2.fill_color = 'white'

    # left shoe
    shoe2 = GPolygon()
    shoe2.add_vertex((673, 206))
    shoe2.add_vertex((678, 191))
    shoe2.add_vertex((686, 186))
    shoe2.add_vertex((694, 181))
    shoe2.add_vertex((702, 184))
    shoe2.add_vertex((749, 233))
    shoe2.add_vertex((752, 248))
    shoe2.add_vertex((728, 247))
    shoe2.add_vertex((708, 237))
    shoe2.add_vertex((699, 234))
    shoe2.add_vertex((690, 229))
    shoe2.add_vertex((690, 218))
    shoe2.add_vertex((683, 210))
    shoe2.filled = True
    shoe2.fill_color = 'white'

    shoe2_line1 = GLine(690, 217, 725, 238)
    shoe2_line2 = GLine(695, 182, 750, 240)
    shoe2_line3 = GLine(690, 217, 700, 235)
    shoe2_line4 = GLine(692, 231, 700, 222)
    shoe2_line5 = GLine(705, 226, 720, 243)
    shoe2_line6 = GLine(708, 237, 720, 234)

    # face
    face = GPolygon()
    face.add_vertex((333, 87))
    face.add_vertex((301, 130))
    face.add_vertex((297, 155))
    face.add_vertex((301, 185))
    face.add_vertex((303, 193))
    face.add_vertex((325, 196))
    face.add_vertex((352, 197))
    face.add_vertex((369, 187))
    face.add_vertex((396, 182))
    face.add_vertex((403, 173))
    face.add_vertex((406, 161))
    face.add_vertex((403, 154))
    face.add_vertex((390, 164))
    face.add_vertex((410, 148))
    face.add_vertex((381, 103))
    face.add_vertex((342, 81))
    face.filled = True
    face.fill_color = 'peachpuff'

    # eyebrow
    eyebrow1 = GPolygon()
    eyebrow1.add_vertex((326, 104))
    eyebrow1.add_vertex((331, 118))
    eyebrow1.add_vertex((328, 130))
    eyebrow1.add_vertex((328, 120))
    eyebrow1.filled = True
    eyebrow1.fill_color = "maroon"

    eyebrow2 = GPolygon()
    eyebrow2.add_vertex((345, 137))
    eyebrow2.add_vertex((354, 134))
    eyebrow2.add_vertex((372, 135))
    eyebrow2.add_vertex((355, 138))
    eyebrow2.filled = True
    eyebrow2.fill_color = "maroon"

    # eye
    eye1 = GPolygon()
    eye1.add_vertex((317, 115))
    eye1.add_vertex((323, 119))
    eye1.add_vertex((326, 124))
    eye1.add_vertex((327, 138))
    eye1.add_vertex((319, 139))
    eye1.add_vertex((313, 137))
    eye1.add_vertex((310, 128))
    eye1.add_vertex((312, 121))
    eye1.filled = True
    eye1.fill_color = "white"

    eye2 = GPolygon()
    eye2.add_vertex((343, 150))
    eye2.add_vertex((356, 146))
    eye2.add_vertex((366, 147))
    eye2.add_vertex((374, 153))
    eye2.add_vertex((368, 161))
    eye2.add_vertex((357, 165))
    eye2.add_vertex((346, 158))
    eye2.add_vertex((343, 157))
    eye2.filled = True
    eye2.fill_color = "white"

    # eyeball
    eyeball1 = GOval(10, 10, x=311, y=125)
    eyeball1.filled = True
    eyeball2 = GOval(10, 10, x=347, y=149)
    eyeball2.filled = True

    # nose
    nose_1 = GLine(320, 153, 315, 158)
    nose_2 = GLine(315, 158, 315, 163)

    # mouth
    mouth = GPolygon()
    mouth.add_vertex((307, 173))
    mouth.add_vertex((307, 179))
    mouth.add_vertex((316, 188))
    mouth.add_vertex((319, 185))
    mouth.add_vertex((318, 178))
    mouth.filled = True
    mouth.fill_color = "orangered"

    # neck
    neck = GPolygon()
    neck.add_vertex((324, 193))
    neck.add_vertex((384, 182))
    neck.add_vertex((367, 203))
    neck.add_vertex((325, 220))
    neck.filled = True
    neck.fill_color = 'peachpuff'

    # hair
    hair = GPolygon()
    hair.add_vertex((317, 107))
    hair.add_vertex((313, 89))
    hair.add_vertex((320, 96))
    hair.add_vertex((319, 80))
    hair.add_vertex((320, 73))
    hair.add_vertex((323, 83))
    hair.add_vertex((326, 62))
    hair.add_vertex((331, 66))
    hair.add_vertex((337, 50))
    hair.add_vertex((337, 71))
    hair.add_vertex((347, 57))
    hair.add_vertex((375, 39))
    hair.add_vertex((371, 49))
    hair.add_vertex((365, 56))
    hair.add_vertex((382, 51))
    hair.add_vertex((403, 50))
    hair.add_vertex((396, 57))
    hair.add_vertex((413, 59))
    hair.add_vertex((428, 55))
    hair.add_vertex((434, 51))
    hair.add_vertex((419, 65))
    hair.add_vertex((408, 69))
    hair.add_vertex((435, 73))
    hair.add_vertex((455, 75))
    hair.add_vertex((434, 82))
    hair.add_vertex((469, 90))
    hair.add_vertex((446, 94))
    hair.add_vertex((459, 99))
    hair.add_vertex((468, 97))
    hair.add_vertex((454, 112))
    hair.add_vertex((433, 125))
    hair.add_vertex((460, 120))
    hair.add_vertex((451, 136))
    hair.add_vertex((438, 145))
    hair.add_vertex((451, 148))
    hair.add_vertex((424, 163))
    hair.add_vertex((399, 179))
    hair.add_vertex((403, 173))
    hair.add_vertex((407, 160))
    hair.add_vertex((392, 164))
    hair.add_vertex((375, 178))
    hair.add_vertex((371, 176))
    hair.add_vertex((393, 153))
    hair.add_vertex((388, 152))
    hair.add_vertex((391, 149))
    hair.add_vertex((388, 136))
    hair.add_vertex((381, 130))
    hair.add_vertex((348, 91))
    hair.add_vertex((332, 88))
    hair.filled = True

    hair2 = GPolygon()
    hair2.add_vertex((356, 84))
    hair2.add_vertex((347, 97))
    hair2.add_vertex((347, 122))
    hair2.add_vertex((351, 97))
    hair2.filled = True
    hair2.fill_color = 'gold'

    hair3 = GPolygon()
    hair3.add_vertex((362, 85))
    hair3.add_vertex((356, 79))
    hair3.add_vertex((358, 71))
    hair3.add_vertex((366, 65))
    hair3.add_vertex((374, 61))
    hair3.add_vertex((366, 71))
    hair3.add_vertex((363, 77))
    hair3.filled = True
    hair3.fill_color = 'gold'

    hair4 = GPolygon()
    hair4.add_vertex((364, 85))
    hair4.add_vertex((374, 77))
    hair4.add_vertex((388, 75))
    hair4.add_vertex((403, 78))
    hair4.add_vertex((385, 79))
    hair4.add_vertex((371, 84))
    hair4.filled = True
    hair4.fill_color = 'gold'

    hair5 = GPolygon()
    hair5.add_vertex((364, 85))
    hair5.add_vertex((378, 84))
    hair5.add_vertex((408, 95))
    hair5.add_vertex((387, 91))
    hair5.add_vertex((364, 91))
    hair5.filled = True
    hair5.fill_color = 'gold'

    hair6 = GPolygon()
    hair6.add_vertex((367, 85))
    hair6.add_vertex((373, 109))
    hair6.add_vertex((381, 123))
    hair6.add_vertex((363, 96))
    hair6.add_vertex((363, 94))
    hair6.add_vertex((363, 125))
    hair6.add_vertex((358, 109))
    hair6.add_vertex((358, 91))
    hair6.add_vertex((358, 109))
    hair6.add_vertex((351, 129))
    hair6.add_vertex((353, 113))
    hair6.add_vertex((352, 86))
    hair6.add_vertex((358, 81))
    hair6.filled = True
    hair6.fill_color = 'gold'

    # add all objects to window
    window.add(background)

    window.add(volleyball)
    window.add(blue_pc1)
    window.add(blue_pc2)
    window.add(blue_pc3)
    window.add(blue_pc4)
    window.add(tetragon1)
    window.add(tetragon2)
    window.add(tetragon3)
    window.add(tetragon4)

    window.add(libero)
    window.add(name)
    window.add(haikyu)
    window.add(leg1)
    window.add(leg2)
    window.add(knee_pad1)
    window.add(knee_pad2)
    window.add(socks1)
    window.add(shoe1)
    window.add(shoe_line1)
    window.add(shoe_line2)
    window.add(shoe_line3)
    window.add(shoe_line4)
    window.add(shoe_line5)
    window.add(shoe_line6)
    window.add(socks2)
    window.add(shoe2)
    window.add(shoe2_line1)
    window.add(shoe2_line2)
    window.add(shoe2_line3)
    window.add(shoe2_line4)
    window.add(shoe2_line5)
    window.add(shoe2_line6)
    window.add(hand2)
    window.add(jersey3)
    window.add(j_side3)
    window.add(j_side4)
    window.add(j_side1)
    window.add(j_side2)

    window.add(jersey2)
    window.add(j_line1)
    window.add(j_line2)
    window.add(j_line3)
    window.add(j_line4)
    window.add(j_line5)
    window.add(j_line6)
    window.add(j_line7)
    window.add(j_line8)
    window.add(jersey1)

    window.add(neck)
    window.add(j_front)
    window.add(j_front2)
    window.add(tie)

    window.add(face)
    window.add(eyebrow1)
    window.add(eyebrow2)
    window.add(eye1)
    window.add(eye2)
    window.add(eyeball1)
    window.add(eyeball2)
    window.add(nose_1)
    window.add(nose_2)
    window.add(mouth)
    window.add(hair)
    window.add(hair2)
    window.add(hair3)
    window.add(hair4)
    window.add(hair5)
    window.add(hair6)

    window.add(hand1)
    window.add(elbow_pad)
    window.add(thumb1)
    window.add(thumb2)
    window.add(thumb3)
    window.add(thumb4)
    window.add(thumb5)
    window.add(thumb6)
    window.add(thumb7)
    window.add(finger1)
    window.add(finger2)
    window.add(finger3)
    window.add(finger4)
    window.add(fingerline)


if __name__ == '__main__':
    main()
