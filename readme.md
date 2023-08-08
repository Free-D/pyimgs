# pyimgs

> 因为买了阿里/腾讯的云服务器，但是使用云存储还需要收费，又加上闲的没事，所以搞了一个小脚本
>
> 主要功能是为`typora`增加一个自定义图床


conf.ini参数解释：

```
base_url：server部署的地址，默认为本机32251端口
secret_key：server端与客户端定义的密钥
```



docker运行示例：

```shell
docker run --name pyimgs -e PORT=端口 -e SECRET_KEY=密钥 -v 本地路径:/pyimgs/upload -p 本地端口:容器端口 -d freenn/pyimgs:1.2
```

命令行启动服务端示例：

```shell
python server/main.py --port=端口 --secret_key=密钥
```

客户端启动示例：

首先运行一遍下面的命令，带不带参数都可以

```shell
python client/app.py <参数一>图片地址  <参数二>图片地址 ...
```

然后生成了`conf.ini`配置文件，修改配置文件中的`base_url`和`secret_key`与服务端一致

+ 备注1：conf.ini中的value不需要加引号

+ 备注2：也可以在<a href="https://github.com/Free-D/pyimgs/releases">这里</a>下载客户端exe

运行方式为，先双击exe文件，生成log文件夹和`conf.ini`默认配置，然后将图片拖动到exe文件上即可上传文件

与`typora`配合使用：

具体使用方法如下

+ 第一步：

  按`ctrl+逗号`打开偏好设置

+ 第二步：

  点击图像并且将配置改为图片相同的设置

  <p align="center">
    <br>
    <img decoding="auto" src="https://pyimgs.freepd.top/get-img/6dbbf04635b111ee84090242ac110009.png" width="70%"/>
    <br>
  </p>

+ 第三步

  将上传服务改为`Custom Command`，将命令改为`app.exe`所在位置

  <p align="center">
    <br>
    <img decoding="auto" src="https://pyimgs.freepd.top/get-img/e929ecce35b111ee84090242ac110009.png" width="70%"/>
    <br>
  </p>

  <p></p>
  
+ 第四步

  点击验证图片上传选项

  提示成功说明上传成功

  <p align="center">
    <br>
    <img decoding="auto" src="https://pyimgs.freepd.top/get-img/6743d61a35b211ee84090242ac110009.png" width="50%"/>
    <br>
  </p>

  如果失败则查看日志并且提交到`issues`

