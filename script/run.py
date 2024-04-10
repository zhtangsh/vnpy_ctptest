from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.object import  *

from vnpy_ctptest import CtptestGateway


def main():
    """主入口函数"""

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(CtptestGateway)
    gateway = main_engine.get_gateway('CTPTEST')
    default_setting: dict[str, str] = {
        "用户名": "224850",
        "密码": "CWNXV@ijbYb2Ape",
        "经纪商代码": "9999",
        "交易服务器": "180.168.146.187:10130",
        "行情服务器": "180.168.146.187:10131",
        "产品名称": "simnow_client_test",
        "授权编码": "0000000000000000"
    }
    gateway.connect(default_setting)
    # req = SubscribeRequest()


if __name__ == "__main__":
    main()
