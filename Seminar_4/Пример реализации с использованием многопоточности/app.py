import requests
import threading
import time
import os

def download_image(url):
    filename = os.path.basename(url)
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Image {filename} downloaded")

def main():
    start_time = time.time()

    urls = [
        "https://image.shutterstock.com/display_pic_with_logo/3453398/2253107887/stock-photo-green-floating-leaves-flying-leaves-green-leaf-dancing-air-purifier-atmosphere-simple-main-picture-2253107887.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/244516900/2250152377/stock-photo-invest-in-our-planet-earth-day-concept-background-ecology-concept-design-with-globe-map-2250152377.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/3582656/2284848389/stock-photo-nice-city-park-by-the-lake-2284848389.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/168215870/260692694/stock-photo-businessman-watering-green-tree-on-city-background-concept-260692694.jpg"
    ]

    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Total time: {total_time}")

if __name__ == "__main__":
    main()
