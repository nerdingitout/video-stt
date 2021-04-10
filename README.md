# video-stt
This GitHut repo is for a video transcriber demo
## Prerequisites
- Create a free IBM Cloud account: https://ibm.biz/ArabAISummit
- Create a CloudantDB service on IBM Cloud
- Create Watson Speech to Text service on IBM Cloud
- Create a <a href="https://developer.ibm.com/tutorials/how-to-create-a-node-red-starter-application/">Node-RED starter application on IBM Cloud</a>
## Explore Watson Speech to Text API
For this section, you will be exploring the Watson Speech to Text API from the <a href="https://cloud.ibm.com/apidocs/speech-to-text">API documentation</a>.
#### Audio Formats
audio/alaw, audio/basic, audio/flac, audio/g729, audio/l16, audio/mp3, audio/mpeg, audio/mulaw, audio/ogg, audio/ogg;codecs=opus, audio/ogg;codecs=vorbis, audio/wav, audio/webm, audio/webm;codecs=opus, audio/webm;codecs=vorbis

#### Get list of Models
```
curl -X GET -u "apikey:{apikey}" "{url}/v1/models/en-US_BroadbandModel"
```

#### Sample Request
(download sample file <a href="https://watson-developer-cloud.github.io/doc-tutorial-downloads/speech-to-text/reference/audio-file2.flac">audio-file2.flac</a> or replace the type and file name with your own files)
```
curl -X POST -u "apikey:{apikey}" --header "Content-Type: audio/flac" --data-binary @audio-file2.flac "{url}/v1/recognize?word_alternatives_threshold=0.9&keywords=colorado%2Ctornado%2Ctornadoes&keywords_threshold=0.5"
```
## Add environment variables
Create a ```config.py``` file and add the following lines of code, replace with your own credentials.
```
STT_API_KEY="<ADD YOUR STT API KEY HERE"
STT_URL="ADD STT ENDPOINT URL"
CLOUDANT_URL="ADD CLOUDANTDB URL"
CLOUDANT_USERNAME="ADD CLOUDANTDB USERNAME"
CLOUDANT_PASSWORD="ADD CLOUDANTDB PASSWORD"
CLOUDANT_API_KEY="ADD CLOUDANTDB API KEY"
```
## Using Node-RED with Watson Speech to Text
## Flask Application
For this section, you can check out the steps and resources in this <a href="https://github.com/Call-for-Code/cfc-covid-19-video-transcriber">GitHub repository</a>. This is another example of building video transcriber.
![image](https://user-images.githubusercontent.com/36239840/114268661-3ccc2500-9a13-11eb-8aa3-68363b136976.png)
