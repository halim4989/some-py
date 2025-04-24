This uses `Pytube` module to download specific resolution video from YouTube.

Uses module `subprocess` to run commands from package `ffmpeg` to separate the audio, splits the video to the nearest **Keyframe* of the given time (seek time), and then meagres the video with another audio. saves them in a separate folder.



**splitting from keyframe does not requires re-rendering the video. makes video editing super fast.*



<br><br>
Why Use Two `-ss` in cut cmd??

This is a two-step seek technique:

* First -ss (before -i) = fast but possibly inaccurate (no decode)

* Second -ss (after -i) = accurate (decodes keyframes)


Combining both helps speed up processing and ensures accurate cutting.
