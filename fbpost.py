import requests
import json
 
#Get your own facebook token and insert here
access_token = ""
 
def comment_on_posts(posts, amount):
    counter = 0
    for post in posts:
        if counter >= amount:
            break
        else:
            counter = counter + 1
        url = "https://graph.facebook.com/{0}/comments".format(post['id'])
        message = "Hey..!"
        parameters = {'access_token' : access_token, 'message' : message}
        s = requests.post(url, data = parameters)
 
def get_posts():
    payload = {'access_token' : access_token}
    r = requests.get('https://graph.facebook.com/me/feed', params=payload)
    result = json.loads(r.text)
    return result['data']
 
if __name__ == "__main__":
    #number of posts in which you want to comment
    number = 2
    posts = get_posts()
    comment_on_posts(posts, number)
