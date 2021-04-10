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
