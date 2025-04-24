
from pytube import YouTube
import subprocess

def vid_dwn(vidurl):
  vid = YouTube(vidurl)
  vidstm = vid.streams

  svid = vidstm.filter(res="1080p", mime_type="video/mp4", adaptive=True).first()
  saud = vidstm.get_audio_only(subtype='mp4')

  if svid:
    print('\nDownloading 1080p Video....')
    print(svid.download(output_path='tmp', filename='vid.mp4', skip_existing=False))
    print('\n1080p Video Downloaded')
  else:
    print('1080p Not found downloading 720p')
    print(vidstm.filter(res="720p", mime_type="video/mp4", adaptive=True).first().download(output_path='tmp',filename='vid.mp4', skip_existing=False))
    print('\n720p Downloaded')

  # print('skipping Video Download [NO NEED video]')

  print('Downloading audio...')
  print(saud.download(output_path='tmp', filename='aud.acc', skip_existing=False))
  print('\naudio downloaded') 


# def run_ffmpeg(num, vid = "final video"):
def run_ffmpeg(vid = "final video"):
  '''
  Name of video without extention
  '''
  print(f'Video Title\n {vid} \n')



  marge = f'ffmpeg -y -i ./tmp/vid.mp4 -i ./tmp/aud.acc -c copy -shortest ./tmp/out.mp4'
  # marge = f'ffmpeg -y -i ./tmp/vid.mp4 -i ./tmp/aud.acc -c copy -shortest "./out/{vid}.mp4"'


  cut = f'ffmpeg -y -ss 4 -i ./tmp/out.mp4 -ss 1.9 -c copy "./out/{vid}.mp4"'
  concat = f'ffmpeg -y -f concat -safe 0 -i ./tmp/concat.txt -c copy "./out/{vid}.mp4"'

  print('\nVideo & Audio Marging....')
  run_cmd(marge)
  print('\nVideo & Audio Marged')

# cut first, mearge later.
  # print('\nCliping Marged video....')
  # run_cmd(cut)
  # print('\nCliping Done!!')

  print('n\Concating video....')
  run_cmd(concat)
  print('\nConcat Done!!')



def run_cmd(cmd):
  '''
  cmd to run
  '''
  result = subprocess.run(cmd, 
                          shell = True, 
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, 
                          encoding='utf-8')

  if result.returncode == 0:
      print('DONE \n')
      ###########
      # print('ok \n', result.stdout)
      # print('err \n', result.stderr)
      ###########

  else:
      print('ERROR ERROR ERROR ERROR ERROR \n',result.stderr)




def main():
  txt = f''' #concat file with outro
  file 'out.mp4'
  file 'outro.mp4'
  '''
  with open("./tmp/concat.txt", "w") as f:
    f.write(txt)

  with open("file.txt", "r", encoding="utf8") as a_file:
    txt = [line.strip() for line in a_file]

  urls = [l.split(' === ') for l in txt]


  for url, name in urls[:15]:
    vid_dwn(url) 
    run_ffmpeg(name)
    print(f'\nDONE DONE DONE\n{name}\n')





if __name__ == '__main__':
  outro = "https://www.youtube.com/watch?v=gpopRCgGGBI"
  black = "https://www.youtube.com/watch?v=TpugbfK01Hs"

  print("Downloading Outro")
  print(YouTube(outro).streams.filter(res="1080p", mime_type="video/mp4", adaptive=True).first().download(output_path='tmp', filename='outro.mp4', skip_existing=False))
  print("Outro Downloaded\n")

  # print("Downloading Black Screen")
  # YouTube(black).streams.filter(res="1080p", mime_type="video/mp4", adaptive=True).first().download(output_path='tmp', filename='vid.mp4', skip_existing=False)
  # print("Black Screen for 10h Download")


  main()


