# -*- coding: utf-8 -*-
import json

from esb.bkcore.models import ESBChannel
from components.component import Component, SetupConfMixin
from common.forms import BaseComponentForm, DefaultBooleanField
from common.constants import API_TYPE_Q
from common.errors import CommonAPIError
from .toolkit import configs


class GetToken(Component, SetupConfMixin):
    """"""

    sys_name = configs.SYSTEM_NAME
    api_type = API_TYPE_Q

    class Form(BaseComponentForm):
        need_new_token = DefaultBooleanField(label="obtain a new token or not", default=False, required=False)

    def get_wx_config(self):
        try:
            send_weixin_channel = ESBChannel.objects.get(path="/cmsi/send_weixin/")
        except Exception:
            raise CommonAPIError(
                "Channel with path [/cmsi/send_weixin/] does not exist, can not get WeChat configuration"
            )
        return dict(json.loads(send_weixin_channel.comp_conf))

    def handle(self):
        wx_config = self.get_wx_config()
        wx_type = wx_config.get("wx_type")
        if wx_type in ["qy", "qywx"]:
            wx_qy_corpid = wx_config.get("wx_qy_corpid")
            wx_qy_corpsecret = wx_config.get("wx_qy_corpsecret")
            if not (wx_qy_corpid and wx_qy_corpsecret):
                raise CommonAPIError(
                    "Please improve the component configuration of component [/cmsi/send_weixin/] "
                    "in ESB channel management"
                )
            kwargs = {
                "corpid": wx_qy_corpid,
                "corpsecret": wx_qy_corpsecret,
            }
            self.response.payload = self.invoke_other("generic.weixin_qy.get_token", kwargs=kwargs)
        elif wx_type in ["mp"]:
            wx_app_id = wx_config.get("wx_app_id")
            wx_secret = wx_config.get("wx_secret")
            if not (wx_app_id and wx_secret):
                raise CommonAPIError(
                    "Please improve the component configuration of component [/cmsi/send_weixin/] "
                    "in ESB channel management"
                )
            kwargs = {
                "appid": wx_app_id,
                "secret": wx_secret,
                "need_new_token": self.form_data["need_new_token"],
            }
            self.response.payload = self.invoke_other("generic.weixin_mp.get_token", kwargs=kwargs)
        else:
            self.response.payload = {
                "result": False,
                "message": "In the component configuration for component [/cmsi/send_weixin/], "
                "the value of wx_type is not in the optional range",
            }