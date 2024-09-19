from flask import Flask

app = Flask(__name__)

@app.route('/')
def dog_gif():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Funny Dog GIF - Blue Theme</title>
        <style>
            body {
                background-color: #ADD8E6; /* Light Blue */
                background-image: url('https://www.publicdomainpictures.net/pictures/320000/velka/blue-abstract-background.jpg'); /* Tiled blue retro background */
                font-family: 'Comic Sans MS', cursive, sans-serif;
                color: #00008B; /* Dark Blue */
                text-align: center;
            }
            h1 {
                color: #1E90FF; /* Dodger Blue */
                font-size: 36px;
                text-shadow: 2px 2px #4682B4; /* Steel Blue shadow */
            }
            .gif-image {
                width: 400px;
                height: auto;
                border: 5px solid #1E90FF; /* Dodger Blue border */
            }
            .marquee-text {
                font-size: 24px;
                color: #4682B4; /* Steel Blue */
                border: 2px solid #1E90FF; /* Dodger Blue border */
                padding: 10px;
                margin: 20px;
                background-color: #B0E0E6; /* Powder Blue background */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1><marquee>Welcome to the Funny Dog GIF Page!</marquee></h1>

            <img src="https://i.imgur.com/abcd123.gif" alt="Funny Dog GIF" class="gif-image"> <!-- Replace this with the actual direct image URL -->

            <div class="marquee-text">
                <marquee behavior="alternate" direction="left">Enjoy the doggo!</marquee>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
