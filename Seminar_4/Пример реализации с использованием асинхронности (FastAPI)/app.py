import os
import aiohttp
import asyncio

from fastapi import FastAPI

app = FastAPI()

async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = os.path.basename(url)
            with open(filename, 'wb') as file:
                file.write(await response.read())
            print(f"Image {filename} downloaded")

@app.get("/download-images")
async def download_images():
    start_time = time.time()

    urls = [
        "https://image.shutterstock.com/display_pic_with_logo/168215870/2623921/stock-photo-cargo-boat-by-the-beach-at-sunset-time-in-beautiful-colours-2623921.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/168215870/1320997/stock-photo-driftwood-and-rocks-on-sandy-beach-1320997.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/168215870/1031906905/stock-photo-formentor-beach-majorca-spain-1031906905.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/244516900/2250152377/stock-photo-invest-in-our-planet-earth-day-concept-background-ecology-concept-design-with-globe-map-2250152377.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/4368277/2289908109/stock-photo-white-clouds-collection-isolated-on-black-background-cloud-set-on-black-2289908109.jpg"
    ]

    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_image(url))
        tasks.append(task)

    await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time

    return {"message": "Images downloaded", "total_time": total_time}
