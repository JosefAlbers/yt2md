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

<details><summary>Click to expand output</summary><pre>
# Real men test in production… The truth about the CrowdStrike disaster

last Friday the world finally got the Y2K experience it deserved when millions of Windows machines went down thanks to a bad update from cyber security firm crowd strike 8.5 million to be exact but now the plot is thickened and multiple theories for why this actually happened have emerged a was it just a silly mistake B was it actually a Cyber attack being covered up or C was it a false flag planned centuries ago by our multi-dimensional lizard overlords in today's video we'll try to find out what really happened by taking a deep dive into the technical details but first here's a crazy detail you need to know on April 21st 2010 at approximately 1,400 hours a McAfee Antivirus update accidentally removed the windows service host file and knocked millions of computers running Windows XP off the internet causing many of them to go into an endless reboot loop the blue screen of death shut down critical services around the world that was 15 years ago when Justin Bieber was only 16 years old but it's nearly identical to the crowdstrike disaster going on right now here's the crazy part though the CTO of McAfee in 2010 was none other than George kurts the CEO of crowd strike today that's quite the example of failing upwards now he did just lose $300 million in paper wealth but most importantly we now know the embarrassing truth about how the crowd strike disaster actually happened almost it is July 22nd 2024 and you watching the code report the creator of C++ be straup once said C++ makes it harder to shoot yourself in the foot but when you do you blow your entire leg off and we should have listened to him crowd strike released an official statement explaining what happened come on you guys there it is right there in front of you the whole time you're dereferencing a m pointer open your eyes the crowd strike Falcon sensor is software that sits in the background on your machine looking for potential security anomalies it contains a driver which is the thing that actually executes code along with a bunch of Channel files which are basically just config files that contain rules about new potential attacks that the sensor can look for these files are not kernel drivers and can be updated on the Fly and when crowd strike pushed an update to channel file 291 a logic error caused the entire system to crash now normally when an application crashes it only breaks that application running in user land or ring three in the CPU protection ring no blue screen of death required but crowd strike is a unique piece of software that runs within ring zero or kernel mode the most privileged Zone around the CPU usually reserved for process scheduling and direct Hardware access ring zero is an area that normally only microsof is are allowed to touch and in order for any third party to run code here they must receive a whql certification from Microsoft to verify that your code won't Breck 8.5 million devices and shut down the global economy the crowd strike driver was whql certified so it sounds like it's Microsoft's fault well not so fast what's unique about crowd strike is that they can make updates to those config or Channel files dynamically in this case the driver had some kind of issue reading Channel file 291 causing the entire system to fail that's pretty much all the detail we have from official sources but luckily there's a guy on the internet who's a professional C++ programmer and provided a breakdown that went viral his hypothesis was that this was a skill issue where some engineer coded up a n pointer trying to access a memory address that doesn't exist a simple rookie coding mistake that could have been fixed with an if statement this tweet got a lot of traction but since then it's been Community noted and another security researcher explains that this code is reading pointers from a table in a loop and some are invalid perhaps an error parsing the configuration file left some entries uninitialized what's kind of crazy here is that it looks like the driver code has actually been broken for a long time and this one config file was the straw that broke the camel's back we may not know the full truth until there's a congressional hearing but it looks like some developer there wrote some bad code said works on my machine but then made the horrible mistake of deploying on a Friday but we can't blame this one person programmers write bad code all the time but a failure like this should never reach production the Falcon sensor is not just some crappy to-do list app when software operates in the critical path like this there should be multiple layers of protection quality assurance continuous integration this staggered rollouts and so on it's absolutely insane that this wasn't caught by some automated process before it killed 8.5 million computers heads need to roll for this but it's not the person who wrote the code it's an organizational failure and it's not the first time Colonel Curts has been connected to a worldwide outage he knows that real men test in production and is willing to die on that Hill the thing is this company sells a very expensive product that very few people understand and if you want to have an exotic car collection like this your Enterprise sales team is your highest priority not your software engineering team those nerds therefore the most likely root cause of This Disaster is just a lack of quality control at the company crowd strike but another theory floating around is that this wasn't an accident but actually the work of a foreign spy who infiltrated the company or perhaps a rogue employee who wanted to send a message a message that is time to switch to the Russ programming language for Windows driver development but the conspiracy theories go even deeper and some think this failure is so egregious that it was actually pre-planned in advance the world economic Forum has made predictions about a worldwide Cyber attack and crowd strike is a World economic Forum partner this was all just a test run for the real Cyber attack scheduled to happen on August 12th 2026 most of us will already be dead by then but if your goal is to write robust Colonel drivers on Windows you'll need to know how to problem solve like a programmer and you can start doing that for free thanks to this video sponsor brilliant problem solving is a skill that you keep forever brilliant's platform will introduce you to essential programming Concepts but most importantly the handson exercises will develop your brain to recognize and solve complex problems that developers need to over come on a daily basis best of all every lesson is concise and rewarding by investing just a few minutes each day you'll develop habits that can level up your programming skills for the rest of your life and you can do it anywhere even from your phone to try everything brilliant has to offer for free for 30 days visit brilliant.org fireship or scan this QR code for 20% off their premium annual subscription this has been the code report thanks for watching and I will see you in the next one
</pre></details>

## Notes

- If the script fails to retrieve the video title, it will use the video ID as the filename.
- The filename is sanitized to remove any characters that might cause issues with file systems.
- If you encounter any issues with transcript extraction, make sure the video has closed captions available.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](link-to-your-issues-page).

## License

This project is [MIT](link-to-your-license-file) licensed.
