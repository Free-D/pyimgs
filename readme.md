# pyimgs

因为不想使用阿里/腾讯的桶，加上闲的没事，所以搞了一个小脚本

主要功能是为`typora`增加一个自定义图床

<br>
conf.ini参数解释：

```
base_url：server部署的地址，默认为本机32251端口
secret_key：server端与客户端定义的密钥
```

<br>

服务端启动示例：

``` shell
python server/main.py --port=端口 --secret_key=密钥
```