import os
import re
import textwrap
import random
import aiofiles
import aiohttp
import numpy as np

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch

import config
from AnonX import app

YOUTUBE_IMG_URL = [ 

"https://graph.org/file/d3b95355270a59a646d11.jpg",
"https://graph.org/file/80a815fc399268b7e7615.jpg",
"https://graph.org/file/e75b42d5e53a5b2b6a66a.jpg",
"https://graph.org/file/0612ac97ea873dac31b7f.jpg",
"https://graph.org/file/908526c5a94b90cff5435.jpg",
"https://graph.org/file/c448f32953dcd2d9507fb.jpg",
"https://graph.org/file/aa1eb8f0a9dbfe5d706d6.jpg",
"https://graph.org/file/7a9b84a1a1bf3fe4be404.jpg",
"https://graph.org/file/cbafe5ddb84d3fe7a4302.jpg",
"https://graph.org/file/5134cb427510f5f556c96.jpg",
"https://graph.org/file/07c71b50f0c785ba15195.jpg",
"https://graph.org/file/b666e6293722966959c07.jpg",
"https://graph.org/file/74111a460b32596edc1e5.jpg", 
"https://graph.org/file/d9a17c46674b8d5008bb7.jpg",
"https://graph.org/file/ea77c47229bab8e044b60.jpg", 
"https://graph.org/file/1ed7d90a7741ec545d59a.jpg",
"https://graph.org/file/c697a29f06c72b18cfb3c.jpg",
"https://graph.org/file/7e83a364e95a15a5f4690.jpg",
"https://graph.org/file/8e0ec6dafc455eee114c8.jpg",        
"https://graph.org/file/2a63d9650bab54e0139d7.jpg", 
"https://graph.org/file/0304b7b7406a5da6d4be7.jpg",
"https://graph.org/file/a2004a6ad5a92def5d406.jpg",
    
    
    ]

YOUTUBE_IMG_URLL = [ 

"https://graph.org/file/b410d7329decfa19108e0.jpg",
"https://graph.org/file/83a51633ce0ea305d17b3.jpg",
"https://graph.org/file/37f5f9406efcf06da7286.jpg",
"https://graph.org/file/7338c0db231db085f8775.jpg",
"https://graph.org/file/145f1e620ea6eb224ff0b.jpg",
"https://graph.org/file/f86d70519dde9c181f088.jpg",
"https://graph.org/file/027f66c1d3a8d9082c1a1.jpg",
"https://graph.org/file/d6e69a0ce858196e1eaef.jpg",
"https://graph.org/file/914637e9d5b00b1411d83.jpg",
"https://graph.org/file/c7ca1d6c76eb4b9fa793b.jpg",
"https://graph.org/file/42eecca572d131617f9dc.jpg",
"https://graph.org/file/2b0e6c70da848c0973da1.jpg", 
"https://graph.org/file/9f1845eb3fe4fdf68a272.jpg", 
"https://graph.org/file/2a16495badfc567bc118c.jpg",
"https://graph.org/file/60d4004d780fbc430838e.jpg",
"https://graph.org/file/5f436eb84f4f0fe4050a8.jpg",
"https://graph.org/file/16075770cf05225314c6c.jpg", 
"https://graph.org/file/316ac6887d0650939d25c.jpg", 
"https://graph.org/file/1f9a5edb8d1009a9f49ce.jpg",
"https://graph.org/file/95d7a9da66971edb44d49.jpg",
"https://graph.org/file/455cf3a85e2320127c93d.jpg",
"https://graph.org/file/801d721ff04732bc3fd43.jpg",        
    ]


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def add_corners(im):
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)


async def gen_thumb(videoid, user_id):
    if os.path.isfile(f"cache/{videoid}_{user_id}.png"):
        return f"cache/{videoid}_{user_id}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                result["viewCount"]["short"]
            except:
                pass
            try:
                result["channel"]["name"]
            except:
                pass

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        try:
            wxyz = await app.get_profile_photos(user_id)
            wxy = await app.download_media(wxyz[0]['file_id'], file_name=f'{user_id}.jpg')
        except:
            hehe = await app.get_profile_photos(app.id)
            wxy = await app.download_media(hehe[0]['file_id'], file_name=f'{app.id}.jpg')
        xy = Image.open(wxy)
        a = Image.new('L', [640, 640], 0)
        b = ImageDraw.Draw(a)
        b.pieslice([(0, 0), (640,640)], 0, 360, fill = 255, outline = "white")
        c = np.array(xy)
        d = np.array(a)
        e = np.dstack((c, d))
        f = Image.fromarray(e)
        x = f.resize((107, 107))

        youtube = Image.open(f"cache/thumb{videoid}.png")
        bg = Image.open(f"AloneX/assets/AloneX.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)

        image3 = changeImageSize(1280, 720, bg)
        image5 = image3.convert("RGBA")
        Image.alpha_composite(background, image5).save(f"cache/temp{videoid}.png")

        Xcenter = youtube.width / 2
        Ycenter = youtube.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = youtube.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.ANTIALIAS)
        logo.save(f"cache/chop{videoid}.png")
        if not os.path.isfile(f"cache/cropped{videoid}.png"):
            im = Image.open(f"cache/chop{videoid}.png").convert("RGBA")
            add_corners(im)
            im.save(f"cache/cropped{videoid}.png")

        crop_img = Image.open(f"cache/cropped{videoid}.png")
        logo = crop_img.convert("RGBA")
        logo.thumbnail((365, 365), Image.ANTIALIAS)
        width = int((1280 - 365) / 2)
        background = Image.open(f"cache/temp{videoid}.png")
        background.paste(logo, (width + 2, 138), mask=logo)
        background.paste(x, (710, 427), mask=x)
        background.paste(image3, (0, 0), mask=image3)

        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("AloneX/assets/font2.ttf", 45)
        ImageFont.truetype("AloneX/assets/font2.ttf", 70)
        arial = ImageFont.truetype("AloneX/assets/font2.ttf", 30)
        ImageFont.truetype("AloneX/assets/font.ttf", 30)
        para = textwrap.wrap(title, width=32)
        try:
            draw.text(
                (450, 25),
                f"STARTED PLAYING",
                fill="white",
                stroke_width=3,
                stroke_fill="grey",
                font=font,
            )
            if para[0]:
                text_w, text_h = draw.textsize(f"{para[0]}", font=font)
                draw.text(
                    ((1280 - text_w) / 2, 530),
                    f"{para[0]}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
            if para[1]:
                text_w, text_h = draw.textsize(f"{para[1]}", font=font)
                draw.text(
                    ((1280 - text_w) / 2, 580),
                    f"{para[1]}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
        except:
            pass
        text_w, text_h = draw.textsize(f"Duration: {duration} Mins", font=arial)
        draw.text(
            ((1280 - text_w) / 2, 660),
            f"Duration: {duration} Mins",
            fill="white",
            font=arial,
        )
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}_{user_id}.png")
        return f"cache/{videoid}_{user_id}.png"
    except Exception as e:
        print(e)
        return random.choice(YOUTUBE_IMG_URL)


async def gen_qthumb(videoid, user_id):
    if os.path.isfile(f"cache/que{videoid}_{user_id}.png"):
        return f"cache/que{videoid}_{user_id}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                result["viewCount"]["short"]
            except:
                pass
            try:
                result["channel"]["name"]
            except:
                pass

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        try:
            wxyz = await app.get_profile_photos(user_id)
            wxy = await app.download_media(wxyz[0]['file_id'], file_name=f'{user_id}.jpg')
        except:
            hehe = await app.get_profile_photos(app.id)
            wxy = await app.download_media(hehe[0]['file_id'], file_name=f'{app.id}.jpg')
        xy = Image.open(wxy)
        a = Image.new('L', [640, 640], 0)
        b = ImageDraw.Draw(a)
        b.pieslice([(0, 0), (640,640)], 0, 360, fill = 255, outline = "white")
        c = np.array(xy)
        d = np.array(a)
        e = np.dstack((c, d))
        f = Image.fromarray(e)
        x = f.resize((107, 107))

        youtube = Image.open(f"cache/thumb{videoid}.png")
        bg = Image.open(f"AloneX/assets/AloneX.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)

        image3 = changeImageSize(1280, 720, bg)
        image5 = image3.convert("RGBA")
        Image.alpha_composite(background, image5).save(f"cache/temp{videoid}.png")

        Xcenter = youtube.width / 2
        Ycenter = youtube.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = youtube.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.ANTIALIAS)
        logo.save(f"cache/chop{videoid}.png")
        if not os.path.isfile(f"cache/cropped{videoid}.png"):
            im = Image.open(f"cache/chop{videoid}.png").convert("RGBA")
            add_corners(im)
            im.save(f"cache/cropped{videoid}.png")

        crop_img = Image.open(f"cache/cropped{videoid}.png")
        logo = crop_img.convert("RGBA")
        logo.thumbnail((365, 365), Image.ANTIALIAS)
        width = int((1280 - 365) / 2)
        background = Image.open(f"cache/temp{videoid}.png")
        background.paste(logo, (width + 2, 138), mask=logo)
        background.paste(x, (710, 427), mask=x)
        background.paste(image3, (0, 0), mask=image3)

        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("AloneX/assets/font2.ttf", 45)
        ImageFont.truetype("AloneX/assets/font2.ttf", 70)
        arial = ImageFont.truetype("AloneX/assets/font2.ttf", 30)
        ImageFont.truetype("AloneX/assets/font.ttf", 30)
        para = textwrap.wrap(title, width=32)
        try:
            draw.text(
                (455, 25),
                "ADDED TO QUEUE",
                fill="white",
                stroke_width=5,
                stroke_fill="black",
                font=font,
            )
            if para[0]:
                text_w, text_h = draw.textsize(f"{para[0]}", font=font)
                draw.text(
                    ((1280 - text_w) / 2, 530),
                    f"{para[0]}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
            if para[1]:
                text_w, text_h = draw.textsize(f"{para[1]}", font=font)
                draw.text(
                    ((1280 - text_w) / 2, 580),
                    f"{para[1]}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
        except:
            pass
        text_w, text_h = draw.textsize(f"Duration: {duration} Mins", font=arial)
        draw.text(
            ((1280 - text_w) / 2, 660),
            f"Duration: {duration} Mins",
            fill="white",
            font=arial,
        )

        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        file = f"cache/que{videoid}_{user_id}.png"
        background.save(f"cache/que{videoid}_{user_id}.png")
        return f"cache/que{videoid}_{user_id}.png"
    except Exception as e:
        print(e)
        return random.choice(YOUTUBE_IMG_URLL)
