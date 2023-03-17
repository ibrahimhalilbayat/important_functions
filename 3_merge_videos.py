from moviepy.editor import VideoFileClip, concatenate_videoclips


clip_1 = VideoFileClip("1.mp4")
clip_2 = VideoFileClip("2.mp4")
clip_3 = VideoFileClip("3.mp4")
clip_4 = VideoFileClip("4.mp4")
clip_5 = VideoFileClip("5.mp4")
clip_6 = VideoFileClip("8.mp4")
clip_7 = VideoFileClip("9.mp4")
clip_8 = VideoFileClip("9_2.mp4")
clip_9 = VideoFileClip("11.mp4")
clip_10 = VideoFileClip("12.mp4")

final_clip = concatenate_videoclips([clip_1,clip_2, clip_3, clip_4, clip_5, clip_6, clip_7, clip_8, clip_9, clip_10])
final_clip.write_videofile("final.mp4")
