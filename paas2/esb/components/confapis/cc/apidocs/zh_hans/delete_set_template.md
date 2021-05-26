### 功能描述

根据业务ID和集群模板ID列表删除指定业务下的集群模板

### 请求参数

{{ common_args_desc }}

#### 接口参数

| 字段                 | 类型   | 必选 | 描述           |
| -------------------- | ------ | ---- | ------------ |
| bk_biz_id            | int    | 是   | 业务ID        |
| set_template_ids     | array  | 是   | 集群模板ID列表 |


### 请求参数示例

```json
{
    "bk_supplier_account": "0",
    "bk_biz_id": 20,
    "set_template_ids": [59]
}
```

### 返回结果示例

```json
{
    "result": true,
    "code": 0,
    "message": "success",
    "permission": null,
    "data": null
}
```

### 返回结果参数说明

#### response

| 名称    | 类型   | 描述                                    |
| ------- | ------ | ------------------------------------- |
| result  | bool   | 请求成功与否。true:请求成功；false请求失败 |
| code    | int    | 错误编码。 0表示success，>0表示失败错误   |
| message | string | 请求失败返回的错误信息                   |
| data    | object | 请求返回的数据                          |