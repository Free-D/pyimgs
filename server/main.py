# -*- coding: utf-8 -*-
# @ModuleName: main
# @Time: 2023/08/07 9:42
# @Author     : WangPengDa
# @Description:
# @Software   : PyCharm
import os
import uuid

from tornado import web, ioloop, gen, options


options.define("port", default=32251, help="监听端口", type=int)
options.define("secret_key", default="default", help="服务密钥", type=str)


class GetImgHandler(web.RequestHandler):

    @gen.coroutine
    def get(self, img):
        self.set_header("Content-Type", "image/jpg")
        if os.path.exists(img):
            file = open(img, "rb")
            while True:
                content = file.read(512)
                if not content:
                    file.close()
                    break
                self.write(content)
                gen.sleep(0.1)
                self.flush()
        else:
            self.finish({"status": 404, "message": "not found", "data": None, "success": False})


class UploadHandler(web.RequestHandler):

    @gen.coroutine
    def post(self):
        if self.request.headers.get("Secret-Key") != options.options.secret_key:
            self.finish({"code": 403, "message": "密钥错误", "data": None, "success": False})
            return
        files = self.request.files  # 获取上传的文件
        img = files.get('img', [])
        if img:
            filename = str(uuid.uuid1()).replace('-', '')
            ext = img[0].get('filename').split(".")[-1]
            data = img[0].get('body')
            path = f"upload/{filename}.{ext}"
            file = open(path, 'wb')  # 保存到upload文件夹中
            file.write(data)
            file.close()
            self.finish({"status": 200, "message": "提交成功", "data": path, "success": True})
        else:
            self.finish({"status": 400, "message": "没有获取到文件", "data": None, "success": False})


if __name__ == '__main__':
    options.parse_command_line()
    app = web.Application(
        [
            (r'/upload/?', UploadHandler),
            (r'/get-img/(?P<img>.*)/?', GetImgHandler),
        ]
    )
    app.listen(options.options.port)
    print(f"start server on http://127.0.0.1:{options.options.port}")
    ioloop.IOLoop.current().start()
