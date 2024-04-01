# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip1 = VideoFileClip("PredictVideo/fire1.mp4")
clip2 = VideoFileClip("PredictVideo/fire01.mp4")
clip3 = VideoFileClip("PredictVideo/fire11.mp4")
clip4 = VideoFileClip("PredictVideo/fire12.mp4")
clip5 = VideoFileClip("PredictVideo/fire13.mp4")
clip6 = VideoFileClip("PredictVideo/fire15.mp4")
clip7 = VideoFileClip("PredictVideo/fire16.mp4")
clip8 = VideoFileClip("PredictVideo/fire17.mp4")
clip9 = VideoFileClip("PredictVideo/fire18.mp4")
clip10 = VideoFileClip("PredictVideo/NewFire1.mp4")
clip12 = VideoFileClip("PredictVideo/NewFire4.mp4")
clip13 = VideoFileClip("PredictVideo/NewFire6.mp4")
clip25 = VideoFileClip("PredictVideo/NewFire4.mp4")
clip26 = VideoFileClip("PredictVideo/NewFire10.mp4")
clip14 = VideoFileClip("PredictVideo/NewFire11.mp4")
clip15 = VideoFileClip("PredictVideo/NewFire12.mp4")
clip16 = VideoFileClip("PredictVideo/NewFire13.mp4")
clip17 = VideoFileClip("PredictVideo/NewFire15.mp4")

clip18 = VideoFileClip("PredictVideo/merged2.mp4")
clip19= VideoFileClip("PredictVideo/merged3.mp4")
clip20 = VideoFileClip("PredictVideo/merged4.mp4")
clip21 = VideoFileClip("PredictVideo/merged5.mp4")
clip23 = VideoFileClip("PredictVideo/merged7.mp4")
clip24 = VideoFileClip("PredictVideo/merged8.mp4")



# # getting subclip as video is large
# clip1 = clip18.subclip(0, 20)
#
# # getting subclip as video is large
# clip2 = clip18.subclip(20, 30)

# concatenating both the clips
# final = concatenate_videoclips([clip1, clip2, clip3, clip4 ,clip5, clip6, clip7, clip8, clip9, clip10, clip12,  clip13, clip14, clip15, clip16, clip17 ,clip18, clip19, clip20,
#                                 clip21,clip23,clip24,clip25,clip26])

# final = concatenate_videoclips([clip23, clip24])
# final = concatenate_videoclips([clip18, clip19, clip20, clip21 ,clip23])

final = concatenate_videoclips([clip1, clip2, clip3, clip4 ,clip5, clip6, clip7, clip8, clip9])


# writing the video into a file / saving the combined video
final.write_videofile("PredictVideo/FireMixt2.mp4")