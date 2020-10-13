import logging.handlers, os


def log_conf():
    """初始化日志配置"""

    # 日志文件的位置
    logPath = "./Log"

    # 日志器
    logger = logging.getLogger()
    # 日志器级别
    logger.setLevel(logging.INFO)

    # 处理器-控制台
    sh = logging.StreamHandler()

    # 处理器-文件
    file_path = logPath + os.sep + "mini.log"
    trfh = logging.handlers.TimedRotatingFileHandler(file_path,
                                                     when="midnight",
                                                     interval=1,
                                                     backupCount=15,
                                                     encoding="UTF-8")

    # 格式化字符串
    f = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    # 格式化器
    formatter = logging.Formatter(f)

    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)

    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(trfh)


# 请求通用接口地址
base_url = "http://e.cn/api/v1"

# 微信code
code = "013U240w3i6z7V2ufi0w3WrP6e1U240x"

# 请求头
headers = {
    "Content-Type": "application/json",
                    "token": "3b04f91db4456aab4b8a6b10f16de94f"
}
