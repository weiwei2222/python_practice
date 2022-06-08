from flask import Flask, render_template, request
import requests
import smtplib

posts = [*requests.get("https://api.npoint.io/c790b4d5cab58020d391").json(),
         {"id": 0, "body": "this is some text", "title": "the title", "subtitle": "the subtitle",
          "image_url": "/static/assets/img/home-bg.jpg"},
         ]
my_email = "linweiwei2222@gmail.com"
password = "lin855146"


app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == post_id:
            requested_post = blog_post
            requested_post["image_url"] = requested_post.get("image_url", "/static/assets/img/home-bg11.jpg")
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data)
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        # send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, my_email, email_message)


if __name__ == "__main__":
    app.run(debug=True)