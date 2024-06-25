from pytube import YouTube
import os, time


def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=output_path)
        print(f"Video downloaded successfully and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    os.system("cls")
    url = input("Enter the URL of the video: ").strip()
    output_path = input("Enter the output path (directory) where the video will be saved: ").strip()

    if not os.path.exists(output_path):
        user = os.getlogin()
        output_path = f'c:/Users/{user}/Downloads'
    
    print('-'*10)
    download_youtube_video(url=url, output_path=output_path)
    time.sleep(3)
    