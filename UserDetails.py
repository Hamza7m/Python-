# How To Get Other Instagram Users Details
from instagramy import InstagramUser
username = input("Enter your name ")
user = InstagramUser(username)
print("Follwing : ", user.number_of_followings)
print("Follwing :", user.number_of_followers)
print("post : ", user.number_of_posts)
print("Bio : ", user.biography)
print("website link : ", user.posts)
