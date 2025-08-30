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

    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>{data['title']}</title>
            <style>
                body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; }}
                video {{ width: 100%; height: 100%; object-fit: contain; }}
            </style>
        </head>
        <body>
            <video controls autoplay>
                <source src="{data['video_path']}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </body>
        </html>
    """

    return Response(html_content, mimetype='text/html')

if __name__ == '__main__':
    app.run()
