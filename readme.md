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

docker运行示例：

```shell
docker run --name pyimgs -e PORT=端口 -e SECRET_KEY=密钥 -v 本地路径:/pyimgs/upload -p 本地端口:容器端口 -d freenn/pyimgs:1.1
```

命令行启动服务端示例：

```shell
python server/main.py --port=端口 --secret_key=密钥
```

客户端启动示例：
<br>
首先运行一遍下面的命令，带不带参数都可以

```shell
python client/app.py <参数一>图片地址  <参数二>图片地址 ...
```

然后生成了`conf.ini`配置文件，修改配置文件中的`base_url`和`secret_key`与服务端一致
<br>
备注1：conf.ini中的value不需要加引号
<br>
备注2：也可以在<a href="https://github.com/Free-D/pyimgs/releases">这里</a>下载客户端exe，运行方式和上面一样

