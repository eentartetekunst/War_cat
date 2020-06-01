
from moviepy.editor import *
from moviepy.video import *

audioclip = AudioFileClip("data/song.mp4").subclip(6, 26)
clip1 = VideoFileClip("data/котмарширует1.mp4", audio = False).subclip()
clip2 = VideoFileClip("data/котмарширует2.mp4", audio = False)
clip3 = VideoFileClip("data/MoHcat1.mp4", audio = False).subclip(20, 35)

w,h = moviesize = clip3.size

catmarch1 = (clip2.
         subclip().
         resize((w/3,h/3)).    
         margin( 6,color=(255,255,255)). 
         margin( bottom=20, right=20, opacity=0). 
         set_pos(('right','bottom')) )

catmarch2 = (clip1.
         subclip().
         resize((w/3,h/3)).
         margin( 6,color=(255,255,255)). 
         margin( bottom=20, right=20, opacity=0).
         set_pos(('left','bottom')) )

final = CompositeVideoClip([clip3,catmarch1,catmarch2]).set_audio(audioclip)

final.subclip(0.5).write_videofile(
        "/content/drive/My Drive/Cats/warcat.mp4",
        fps=24,
        codec='libx264')
