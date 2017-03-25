#!/usr/bin/python
import os

import praw
import time

reddit = praw.Reddit('bot1', user_agent='WhatsApp Brasil by /u/diisiqueira')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('brasil')
for submission in subreddit.new(limit=100):
    if submission.id not in posts_replied_to:
        if submission.link_flair_css_class == "humor":
            submission.reply("/r/whatsappbrasil")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

print("Finished!")