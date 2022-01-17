from flask import Flask
obj=Flask(__name__)
@obj.rout("/")
def home():
    return "This is web page"
obj.run()
