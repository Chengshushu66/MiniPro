import utils,logging
from Api.apiFactory import ApiFactory


class TestProductApi:

    def test_product_classify_api(self):
        """商品分类"""
        # 请求返回数据
        res = ApiFactory.get_product_api().product_classify_api()
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言长度
        assert len(res.json()) > 0
        # 断言关键字段
        assert "id" in res.text and "name" in res.text and "topic_img_id" in res.text

    def test_classify_product_api(self):
        """分类下商品"""
        # 请求返回数据
        res = ApiFactory.get_product_api().classify_product_api()
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言长度
        assert len(res.json()) > 0
        # 断言关键字段
        assert False not in [i in res.text for i in ["id", "name", "price", "stock"]]

    def test_product_detail(self):
        """商品信息"""
        # 请求返回数据
        res = ApiFactory.get_product_api().product_detail_api(2)
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言id
        assert res.json().get("id") == 2
        # 断言price
        assert res.json().get("price") == "0.01"
        # 断言name
        assert res.json().get("name") == "梨花带雨 3个"