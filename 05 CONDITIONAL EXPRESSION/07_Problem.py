# Write a program to find out whether a given post is talking about “Harry” or not.

Post=input("Enter the post: ")

if("Harry".lower() in Post.lower()):
    print("This post is talking about ""Harry""")

else:
    print("This post is not talking about ""Harry""")