import argparse
import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import os

def get_video_id(url_or_id):
    if 'youtube.com' in url_or_id or 'youtu.be' in url_or_id:
        parsed_url = urlparse(url_or_id)
        if 'youtube.com' in url_or_id:
            return parse_qs(parsed_url.query).get('v', [None])[0]
        elif 'youtu.be' in url_or_id:
            return parsed_url.path[1:]
    else:
        return url_or_id

def get_video_title(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url)
    if response.status_code == 200:
        title = re.search(r'<title>(.*?)</title>', response.text)
        if title:
            return title.group(1).replace(' - YouTube', '').strip()
    return video_id

def sanitize_filename(title):
    return re.sub(r'[^\w\-_\. ]', '_', title)

def main():
    parser = argparse.ArgumentParser(description="Extract YouTube video transcript")
    parser.add_argument("video", help="YouTube video URL or ID")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("--oneline", action="store_true", help="Join transcript into one line")
    args = parser.parse_args()

    video_id = get_video_id(args.video)
    if not video_id:
        print("Invalid YouTube URL or video ID")
        return

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        print(f"Error retrieving transcript: {str(e)}")
        return

    video_title = get_video_title(video_id)
    output_file = args.output or f"{sanitize_filename(video_title)}.md"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {video_title}\n\n")
        if args.oneline:
            full_text = ' '.join(entry['text'] for entry in transcript)
            f.write(full_text)
        else:
            for entry in transcript:
                f.write(f"{entry['text']}\n")

    print(f"Transcript saved to {output_file}")

if __name__ == "__main__":
    main()