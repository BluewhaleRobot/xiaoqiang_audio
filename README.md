# xiaoqiang_audio
xiaoqiang audio package, play and record audio
小强声音处理程序，能够录制声音和播放声音(当前只有播放的功能)。通过消息发布声音，同时将录制的声音通过话题发布出来。
可以支持多种声音格式。

### 话题类型

|输入话题|话题类型|
|:--|:--|
|~audio|audio_common_msg/AudioData|

