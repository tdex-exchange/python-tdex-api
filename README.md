# python-tdex-api
This project is designed to help you make your own projects

# Python Tdex API

#### Installation
```
pip install tdexApi
pip install requests
```

#### Getting started

```
from tdexApi import Tdex
options = {
	'apiKey': 'your apiKey',
	'apiSecret': 'your apiSecret'
}
tdex = Tdex(options)

```

### OpenFunction

##### 用户详细信息
```
res = tdex.userInfo()
```
##### 查询有所余额
```
res = tdex.balances()
``` 

#### 查询单个余额

```
res = tdex.balance({currency:1})
```
```
params:
	currency: 币种(比如 1 - BTC)
```

#### 提现

```
res = tdex.withdraw({currency:1, address: 'string', amount: float64})
```
```
params:
	currency uint32	 源币种。比如 1 - BTC
	address	string	提现地址
	amount	float64 数量
```

#### 期货开仓
```
res = tdex.futuresOpen({cid:1, side: 0, scale: 10, volume: 1})
```
```
Params:

cid	int64 产品

side	uint32	交易方向。0 - buy 1 - sell。参考

scale	float64 杠杆

volume	uint32	数量

distance	bool 触发时使用价距或价格

price	float64 限价 <=0:市价 singular

timely	uint32	时效性(限价单用) singular。参考

timelyParam	int32	时效性参数

passive	bool 被动性

visible	int32 显示数量 <0:全部可见 >=0隐藏

strategy	uint32	策略。参考

better	bool 以买一卖一价进入订单簿

variable	uint32	策略使用的变量(条件订单用) singular。参考

constant	float64 策略中常量(条件订单用) singular

sl	Object	止损 singular

	-distance	bool 价距|报价 市价单只用用价距

	-param float64 值

tp	Object	止盈 singular

	-distance bool 价距|报价 市价单只用用价距

	-param	float64 值
```

#### 批量平仓
```
res = tdex.futuresClose([object])
```
```
params:
     
     list Object[]	持仓列表

		  -cid	int64	产品
		
		  -id	uint64	仓位
		
		  -distance	bool	是否为相对价格
		
		  -price	float64	限价 <=0: 市价
		
		  -timely	uint32	时效性(限价单用) singular。参考
		
		  -timelyParam	int32	时效性参数
		
		  -strategy	uint32	策略。参考
		
		  -variable	uint32	策略使用的变量(条件订单用) singular。参考
		
		  -constant	float64	策略中常量(条件订单用) singular
		
		  -passive	bool	被动性
		
		  -visible	int32	显示数量 <0:全部可见 >=0隐藏
		
		  -better bool	 以买一卖一价进入订单簿
```

#### 全部平仓

```
res = tdex.futuresCloseAll([])
```
```
params:
	list	uint64[]	产品列表 [CID,...]
```

#### 设置止损
```
res = tdex.setsl({cid: int64, id: uint64,...})
```
```
parmas:

	cid	int64	产品

	id	uint64	仓位
	
	distance	bool	是否为相对价格
	
	price	float64	限价 <=0: 市价
	
	timely	uint32	时效性(限价单用) singular。参考
	
	timelyParam	int32	时效性参数
	
	strategy	uint32	策略。参考
	
	variable	uint32	策略使用的变量(条件订单用) singular。参考
	
	constant	float64 策略中常量(条件订单用) singular
	
	passive	bool	被动性
	
	visible	int32	显示数量 <0:全部可见 >=0隐藏
	
	better	bool	以买一卖一价进入订单簿
```
#### 设置止盈
```
res = tdex.settp({cid: int64, id: uint64,...})
```
```
params:

	cid	int64	产品

	id	uint64	仓位
	
	distance	bool	是否为相对价格
	
	price	float64	限价 <=0: 市价
	
	timely	uint32	时效性(限价单用) singular。参考
	
	timelyParam	int32	时效性参数
	
	strategy	uint32	策略。参考
	
	variable	uint32	策略使用的变量(条件订单用) singular。参考
	
	constant	float64 策略中常量(条件订单用) singular
	
	passive	bool	被动性
	
	visible	int32	显示数量 <0:全部可见 >=0隐藏
	
	better	bool 以买一卖一价进入订单簿
```
#### 合仓
```
res = tdex.merge({cid: int64, list: []})
```
```
params:

	cid	int64	产品

	list	uint64[]	要合仓的仓位列表
```
#### 分仓
```
res = tdex.split({cid: int64, id: uint64, volume: uint64})
```
```
params:

	cid	int64	产品

	id	uint64	仓位

	volume	uint64	数量
```

#### 获取\设置 用户选项
```
res = tdex.scheme({cid: int64}, type)
```
```
params:

	cid	uint32	产品
	type string 类型 get \ set	
```
#### 获取订单
```
res = tdex.getOrders()
```

#### 获取持仓
```
res = tdex.getPosition()
```
#### 获取历史信息
```
res = tdex.getHistory({pageSize: int32, page: int32})
```
```
params:

	pageSize 可选	int32	页大小
	page 可选	int32	当前页码
```

#### 获取合约信息
```
res = tdex.getContract({symbol: string})
```
```
params:

	symbol	string	产品符号。目前只有 BTCUSD
```

#### 现货买入
```
res = tdex.spotBuy({amount: float64, price: float64, symbol: string})
```
```
params:

	amount	float64	数量

	price 可选	float64	价格。如果市价为 0，限价不为 0
	
	symbol	string	交易对。如 TDUSDT
```
#### 现货卖出
```
res = tdex.spotSell({amount: float64, price: float64, symbol: string})
```
```
params:

	amount	float64	数量

	price 可选	float64	价格。如果市价为 0，限价不为 0
	
	symbol	string	交易对。如 TDUSDT
```
#### 现货订单历史
```
res = tdex.spotHistory({beginTime: string, endTime: string, pageSize: int32, page: int32})
```
```
params:

	beginTime	string	开始时间。2017-01-01

	endTime	string	结束时间。2017-09-13
	
	pageSize 可选	int32	页大小
	
	page 可选	int32	当前页码

```

#### 现货买卖统计
```
res = tdex.spotStat({beginTime: string, endTime: string, symbol: string})
```
```
params:

	symbol	string	产品

	beginTime	int64	开始时间戳。秒

	endTime	int64	结束时间戳。秒
```



