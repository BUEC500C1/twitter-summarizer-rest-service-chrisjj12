import keys
import tweepy
import wget
from PIL import Image, ImageDraw, ImageFont
import os
import io
import time
from flask import Flask, render_template, request, send_file


app = Flask(__name__,template_folder = "Templates")
file_name = "video.avi"
@app.route('/') #basic beginning of the app, the main page
def home():

    return render_template('main.html')
    
@app.route('/', methods=["POST"]) #getting info from the front end
def getvideo():
    username = request.form["userid"]
    choose_username(username)
    return send_file(file_name, mimetype = "avi", attachment_filename = file_name, as_attachment=True)

def choose_username(username):
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_secret)
    api = tweepy.API(auth)

    public_tweets = api.user_timeline(id = username)

    #def pull_tweets(public_tweets):
    media_files = set()
    texts = []
    j = 0
    for status in public_tweets:
        texts.append(status.text)
        media = status.entities.get('media', [])

        img = Image.new('RGB', (1000, 500), color = (73, 109, 137))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 15)
        d.text((10,10), status.text, fill=(255,255,0), font = font)
        tmp_name = 'tweet' + str(j) + '.png'
        img.save(tmp_name)
        j = j + 1
        
        if(len(media) > 0):
            temp = wget.download(media[0]['media_url'])
            tmp_name2 = 'tweet' + str(j) + '.png'
            im1 = Image.open(temp)
            im1.save(tmp_name2)
            j = j + 1
                
            #def make_video(username):
    pid = os.getpid()
    os.system('ffmpeg -framerate 0.5 -i '+'tweet'+'%d.png video.avi')
    


if __name__ == "__main__":
    os.system("rm *video.avi") #deletes existing videos
    os.system("rm *.png") #deletes existing png files
    app.run(host='0.0.0.0', port =8080)





