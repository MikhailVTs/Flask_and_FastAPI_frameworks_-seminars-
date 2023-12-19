import requests
import multiprocessing
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
        "https://image.shutterstock.com/display_pic_with_logo/168215870/530222/stock-photo-footbridge-in-prairie-530222.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/168215870/456980689/stock-photo-sheeps-on-the-dike-456980689.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/168215870/3462924/stock-photo-beautiful-outdoor-landscape-in-the-countryside-on-a-sunny-day-vertical-3462924.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/168215870/557229367/stock-photo-bardenas-reales-park-navarre-spain-557229367.jpg",
        "https://image.shutterstock.com/display_pic_with_logo/168215870/723839290/stock-photo-old-pier-at-trefor-caernarfon-wales-uk-723839290.jpg"
    ]

    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Total time: {total_time}")

if __name__ == "__main__":
    main()
