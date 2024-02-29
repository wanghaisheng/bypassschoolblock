from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
linky = []
namey = []
thumby = []

cat = 'new'
with open('create/links', 'r') as links:
  linky = links.read().splitlines()
with open('create/names', 'r') as names:
  namey = names.read().splitlines()
with open('create/thumbs', 'r') as thumbs:
  thumby = thumbs.read().splitlines()

for i, lid in enumerate(linky):
  name=namey[i]
  alls = open('directory.html', 'r')
  allss = alls.read()
  alls.close()
  if name not in allss:
    filedir = "play/" + name.lower().replace(' ', '-').replace(':', '').replace('?', '').replace('!', '').replace('*', '')+".html"
    url=lid
    thumburl = thumby[i]
    if not thumburl.startswith('../'):
      img = requests.get(thumburl)
      ext = urlopen(thumburl)
      thumbdir = 'images/' + filedir[5:-5] + "." + ext.info().get_content_type().split('/')[1]
      
      with open(thumbdir, 'wb') as newimg:
          newimg.write(img.content)
      thumb= '../' + thumbdir
    else:
      thumb = thumburl
    
    flash = ''
    
    
    
    with open('directory.html', 'r') as file:
        html_content= file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    div = soup.find('div', class_='grid-container')
    
    element_string=f'''
    <div class="col-lg-4 col-md-6 grid-2 game-frame">
                <a href="{filedir}">
                  <div class="game-item">
                    <div class="list-game">
                      <div class="list-thumbnail"><img
                          src="{thumb}"
                          data-src="{thumb}"
                          class="small-thumb img-rounded lazyload"></div>
                      <div class="list-info">
                        <div class="list-title">{name}</div>
                        <div class="list-category"></div>
    
                      </div>
                    </div>
                  </div>
                </a>
              </div>
    '''
    
    new_element = BeautifulSoup(element_string, 'html.parser')
    
    div.insert(0, new_element)
    
    with open('directory.html', 'w') as directory:
        directory.write(soup.prettify())
    
    with open('category/'+cat+".html", "r") as catfile:
        html_content=catfile.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    div = soup.find('div', class_='grid-container')
    
    element_string=f'''
    <div class="col-lg-2 col-md-4 col-6 grid-3">
      <a href="/{filedir}">
      <div class="game-item">
        <div class="list-game">
          <div class="list-thumbnail"><img src="{thumb}" data-src="{thumb}" class="lazyload" alt="{name}"></div>
        </div>
      </div>
      </a>
    </div>
    '''
    
    new_element = BeautifulSoup(element_string, 'html.parser')
    
    div.insert(0, new_element)
    
    with open('category/'+cat+".html", "w") as catfile:
        catfile.write(soup.prettify())
    
    with open(filedir, 'w') as game:
        game.write(f'''<!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
    
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <title>{name}  - rusk-games.pages.dev</title>
        <meta name="robots" content="noindex,nofollow" />
        <meta name="description" content="{name} - rusk-games.pages.dev: on Chromebook delivers seamless, lag-free gaming with an optimized interface, ensuring an enjoyable and safe experience for players of all ages">
        <link rel="icon" href="../images/favicon.ico" sizes="32x32">
    
    
          <meta property="og:image:width" content="200 px" />
          <meta property="og:image:height" content="200 px" />
          <meta property="og:title" content="{name}" />
          <meta property="og:site_name" content="{name}" />
          <meta property="og:description" content="{name} - rusk-games.pages.dev: on Chromebook delivers seamless, lag-free gaming with an optimized interface, ensuring an enjoyable and safe experience for players of all ages" />
          <meta property="og:type" content="website" />
          <meta property="og:image" content="{thumb}">
    
    
    
        <style type="text/css">
    .report-modal {{
      display: none;
      position: fixed;
      z-index: 20;
      padding-top: 100px;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      background-color: rgb(0,0,0);
      background-color: rgba(0,0,0,0.4);
    }}
    .report-modal-content {{
      background-color: #fefefe;
      color: #000;
      margin: auto;
      padding: 20px;
      border: 1px solid #888;
      max-width: 320px;
    }}
    .close {{
      color: #aaaaaa;
      float: right;
      font-size: 28px;
      font-weight: bold;
    }}
    .close:hover,.close:focus {{
      color: black;
      text-decoration: none;
      cursor: pointer;
    }}
    .report-label {{
      padding: 0 10px;
      margin-right: 5px;
      border-radius: 15px;
      display: inline-block;
      margin-bottom: 8px;
    }}
    </style>
        <link rel="stylesheet" type="text/css" href="../css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="../css/jquery-comments.css" />
        <link rel="stylesheet" type="text/css" href="../css/user.css" />
        <link rel="stylesheet" type="text/css" href="../css/style.css" />
        <link rel="stylesheet" type="text/css" href="../css/custom.css" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css" />
        <!-- Font Awesome icons (free version)-->
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
        <!-- Google fonts-->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    
    
    
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VZRYLR5KM1"></script>
    
    
    
    
    
    
    
    
    
    </head>
      <body id="page-top" style="background: url('../images/background1.png'); background-size: cover;">
    
    
    <!-- Navigation-->
           <div id="nav-placeholder"></div>
    <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.7.1.js"></script>
      <script type="text/javascript" src="../navbar.js"></script>
    
    
    
    
    
    
    
    
    
    
    <div class="container game-wrapper">
    <div style="padding-bottom: 20px">
         <!-- ads_ngang-->
    
    </div>
    
    
    
    
    
      <div class="row">
          <div class="col-md-9">
                <div class="game-container">
                  <div class="game-content" data-id="169">
                    <div id="allow_mobile_version"></div>			
                   <!-- 
                    <div id="mobile-play" style="display: none;">
                      <div class="mobile-thumb-play">
                        <img src="#">
                      </div>
                      <div id="mobile-play-btn">
                        <i class="bi bi-play-circle-fill"></i>
                      </div>
                    </div> -->
    
    
    
                    <div class="game-iframe-container" id="game-player">
                      <div id="mobile-back-button" draggable="true">
                        <i class="bi bi-x-circle-fill"></i>
                      </div>
                      <iframe class="game-iframe {flash}" id="game-area" src="{url}" width="480" height="800" scrolling="none" frameborder="0" allowfullscreen></iframe>
                    </div>
                  </div>
    
    
                  <div class="game-info">
                    <div class="header-left">
                      <h1 class="single-title">{name}</h1>
    
    
                    </div>
                    <div class="header-right">
    
    
                      <div class="b-action2">
    
                        <a href="#" onclick="open_fullscreen()" class="btn btn-capsule"><i class="bi bi-arrows-fullscreen b-icon"></i>Fullscreen</a>
                      </div>
                    </div>
                  </div>
                </div>
    
          </div><!-- end col-9 -->
    
    
          <div class="col-md-3">
            <div style="">
              <!-- ads_doc -->
    
            </div>
          </div>
    
    
      </div><!-- end row -->
    
    
    </div> <!-- end row container game-wrapper-->
    
    
    
    
    
    
    
    <div class="container">
    
                <div class="banner-ad-wrapper">
                  <div class="banner-ad-content" style="padding: 20px 0; text-align: center;">
    
    
    
    
                  </div>
                </div>
    
    
    
    
    
      <div class="content-wrapper">
        <div class="row">
    
    
          <div class="col-md-5">
            <div class="sidebar">
    
    
    
    
    
    
    
    
    
    
    
    
    </div>			
    
    
    
    </div>
    </div>
    </div>
    </div>
    
    
    
      <script type="text/javascript" src="../js/jquery-3.6.2.min.js"></script>
      <script type="text/javascript" src="../js/lazysizes.min.js"></script>
      <script type="text/javascript" src="../js/popper.min.js"></script>
      <script type="text/javascript" src="../js/bootstrap.min.js"></script>
    
    
      <script type="text/javascript" src="../js/script.js"></script>
      <script type="text/javascript" src="../js/custom.js"></script>
    
    
    
    
    
      </body>
    </html>
    ''')
    
    with open(f'embed/{filedir[5:]}', 'w') as game:
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
                                        <iframe src="{url}" frameborder="0" style="width: 100vw; height: 100vh" id="iframe"></iframe>
                                    </body>
                                    </html>
                                    ''')
    # soup = BeautifulSoup(html_content, 'html.parser')
    
    # divs = soup.find_all('div', class_='col-lg-4')
    
    # for i, div in enumerate(divs):
    #     a_tag = div.find_next('a')
    
    #     if a_tag and 'href' in a_tag.attrs:
    #         href_dict[a_tag['href']] = a_tag.sourceline
    
    # href_dict['hi']='hello'
    # sorted_dict = {k: href_dict[k] for k in sorted(href_dict)}
    
    # current_key = 'hi'
    # keys=list(sorted_dict.keys())
    
    # current_index = keys.index(current_key)
    # if current_index < len(keys) - 1:
    #     next_key = keys[current_index - 1]
    #     print(next_key)  
    
    
    
    
    