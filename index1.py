from instapy import InstaPy

session = InstaPy(username="anweshwebdev", password="ratedrsuperstar")
session.login()

session.like_by_tags(["webdevelopment","webdesign"], amount=10)

session.set_dont_like(["naked","nsfw","romance","bedroom"])

session.set_do_follow(True,percentage=90)

session.set_do_comment(True,percentage=100)

session.set_comments(["Follow me for latest news about web development","web development tutorials and news on my profile","Get updated with latest tech news around the world"])

session.set_do_reply_to_comments(True,percentage=60)

session.set_comment_replies(["Follow me for latest news about web development","web development tutorials and news on my profile","Get updated with latest tech news around the world"])

session.set_dont_unfollow_active_users(True)

session.end()

session.set_quota_supervisor(enabled=True, peak_comments_daily=250, peak_comments_hourly=20, peak_follows_daily=200)

