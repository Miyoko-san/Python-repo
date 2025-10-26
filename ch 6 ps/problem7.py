# Write a program to find out whether a given post is talking about “Harry” or not.

article = input("Please enter the post here : ")

# if("Harry" in article):
#     print("Yes this article is about Harry.")
# else:
#     print("No this article is not about Harry.")

# this program is not very accurate as python is a case sensitive language 
# its better version is :

if("Harry".lower() in article.lower()):
    print("Yes this article is about Harry.")
else:
    print("No this article is not about Harry.")