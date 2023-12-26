import os
from bs4 import BeautifulSoup

folder_path = 'play'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.endswith('.html') or file_path.endswith('.htm'):
            with open(file_path, 'r') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
                iframes = soup.find_all('iframe')
                
                single_title = soup.find(class_='single-title')
                name = single_title.get_text()
                
                src = iframes[0].get('src')
                
                with open(f'embed/{file}', 'w') as game:
                    game.write(f'''
                               <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <title>{name}</title>
                                    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
                                </head>

                                <body style="padding: 0; margin: 0; background-color: white; overflow: hidden">
                                    <script src="embed.js"></script>
                                    <iframe src="{src}" frameborder="0" style="width: 100vw; height: 100vh" id="iframe"></iframe>
                                </body>
                                </html>
                                ''')
                print(src, name)
