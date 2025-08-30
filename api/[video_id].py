from flask import Flask, request, Response

app = Flask(__name__)

video_data = {
    "10036": {
        "redirect_url": "https://otieu.com/4/9786651",
        "video_path": "https://finally-eta-seven.vercel.app/videos/10036.mp4",
        "title": "Backshot 10036",
        "description": "Get the 10036 backshot.",
        "thumbnail": "https://finally-eta-seven.vercel.app/images/thumbnail-10036.jpg"
    },
    # Add more entries
}

@app.route('/<video_id>')
def handler(video_id):
    if video_id not in video_data:
        return "Video not found.", 404

    data = video_data[video_id]
    host = request.headers.get('Host', 'finally-eta-seven.vercel.app')
    player_url = f"https://{host}/player/{video_id}"
    redirect_url = data['redirect_url']

    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="refresh" content="0; url={redirect_url}">
            <title>{data['title']}</title>
            <meta name="twitter:card" content="player">
            <meta name="twitter:site" content="@SharmaSumi35464">  # Replace!
            <meta name="twitter:title" content="{data['title']}">
            <meta name="twitter:description" content="{data['description']}">
            <meta name="twitter:player" content="{player_url}">
            <meta name="twitter:player:width" content="1280">
            <meta name="twitter:player:height" content="720">
            <meta name="twitter:image" content="{data['thumbnail']}">
            <meta name="twitter:image:alt" content="Thumbnail for {data['title']}">
        </head>
        <body>
            <p>If you are not redirected, please <a href="{redirect_url}">click here</a>.</p>
        </body>
        </html>
    """

    return Response(html_content, mimetype='text/html')

if __name__ == '__main__':
    app.run()
