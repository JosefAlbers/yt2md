# `yt2md`: YouTube Transcript Extractor

This Python script allows you to easily extract transcripts from YouTube videos. It supports both video URLs and video IDs as input, and provides options for customizing the output.

## Features

- Extract transcripts from YouTube videos using either the video URL or video ID
- Automatically retrieve the video title and use it as the default output filename
- Option to save the transcript as a single line or with line breaks
- Custom output filename support
- Markdown formatting of the output file with the video title as a header

## Requirements

- Python 3.6+
- `youtube_transcript_api`
- `requests`

To install the required packages, run:

```
pip install youtube_transcript_api requests
```

## Usage

Basic usage:

```
python yt2md.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

or

```
python yt2md.py VIDEO_ID
```

### Options

- `-o`, `--output`: Specify a custom output file path
- `--oneline`: Join the entire transcript into a single line

### Examples

1. Extract transcript using video URL:
   ```
   python yt2md.py "https://www.youtube.com/watch?v=H9RSeDUdkCA"
   ```

2. Extract transcript using video ID:
   ```
   python yt2md.py H9RSeDUdkCA
   ```

3. Extract transcript and save to a custom file:
   ```
   python yt2md.py H9RSeDUdkCA -o my_transcript.md
   ```

4. Extract transcript and save as a single line:
   ```
   python yt2md.py H9RSeDUdkCA --oneline
   ```

## Output

The script will create a Markdown file containing the transcript. By default, the file will be named after the video title with a `.md` extension. The content will include:

1. The video title as a top-level header
2. The full transcript, either with line breaks (default) or as a single line (if `--oneline` is used)

## Notes

- If the script fails to retrieve the video title, it will use the video ID as the filename.
- The filename is sanitized to remove any characters that might cause issues with file systems.
- If you encounter any issues with transcript extraction, make sure the video has closed captions available.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](link-to-your-issues-page).

## License

This project is [MIT](link-to-your-license-file) licensed.