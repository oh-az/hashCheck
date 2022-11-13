# hashCheck 1.0v
A simple tool that reads hashes (md5 or sha-1) from a text file and outputs the results from VirusTotal.

# Features
Since VirusTotal has limitions on the free API, this tool will send 1 hash every 15 seconds to avoid the limitions. So a list of 100 hashes will take approximately 20 minutes.

# installation

1. Download the repo to your machine.
2. Move to the directory
```
cd hashCheck
```
3. Make sure colorma is installed. if not, you can run:
```
sudo pip3 install -r requierments.txt
```

# Usage
1. open KEY.txt and paste your API key inside.
2. run hashCheck and give it the text file as an argument:
```
python hashCheck.py <HASH_TEXT_FILE.txt>
```

![HashCheck](https://user-images.githubusercontent.com/74332587/201526918-9416689a-4615-4103-945f-1b9f915ceb7f.PNG)
