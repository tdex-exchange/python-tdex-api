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
	currency: 币种(比如 1 - BTC) 必填
```

#### 提现

```
res = tdex.withdraw({currency:1, address: 'string', amount: float64})
```
```
params:
	currency uint32	 源币种。比如 1 - BTC 必填
	address	string	提现地址 必填
	amount	float64 数量 必填
```

#### 期货开仓
```
res = tdex.futuresOpen({cid:1, side: 0, scale: 10, volume: 1})
```
```
Params:

cid	int64 产品 必填

side	uint32	交易方向。0 - buy 1 - sell。参考 必填

scale	float64 杠杆 必填

volume	uint32	数量 必填

distance	bool 触发时使用价距或价格 选填

price	float64 限价 <=0:市价 singular 选填

timely	uint32	时效性(限价单用) singular。参考 选填

timelyParam	int32	时效性参数 选填

passive	bool 被动性 选填

visible	int32 显示数量 <0:全部可见 >=0隐藏 选填

strategy	uint32	策略。参考 选填

better	bool 以买一卖一价进入订单簿 选填

variable	uint32	策略使用的变量(条件订单用) singular。参考 选填

constant	float64 策略中常量(条件订单用) singular 选填

sl	Object	止损 singular 选填
 
	-distance	bool 价距|报价 市价单只用用价距

	-param float64 值

tp	Object	止盈 singular 选填

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

		  -cid	int64	产品 必填
		
		  -id	uint64	仓位 必填
		
		  -distance	bool	是否为相对价格 选填
		
		  -price	float64	限价 <=0: 市价 选填
		
		  -timely	uint32	时效性(限价单用) singular。参考 选填
		
		  -timelyParam	int32	时效性参数 选填
		
		  -strategy	uint32	策略。参考 选填
		 
		  -variable	uint32	策略使用的变量(条件订单用) singular。参考 选填
		
		  -constant	float64	策略中常量(条件订单用) singular 选填
		
		  -passive	bool	被动性 选填
		
		  -visible	int32	显示数量 <0:全部可见 >=0隐藏 选填
		
		  -better bool	 以买一卖一价进入订单簿 选填
```

#### 全部平仓

```
res = tdex.futuresCloseAll([])
```
```
params:
	list	uint64[]	产品列表 [CID(1),...] 必填
```

#### 设置止损
```
res = tdex.setsl({cid: int64, id: uint64,...})
```
```
parmas:

	cid	int64	产品 必填

	id	uint64	仓位 必填
	
	distance	bool	是否为相对价格 必填
	
	price	float64	限价 <=0: 市价 必填
	
	timely	uint32	时效性(限价单用) singular。参考 选填
	
	timelyParam	int32	时效性参数 选填
	
	strategy	uint32	策略。参考 选填
	
	variable	uint32	策略使用的变量(条件订单用) singular。参考 选填
	
	constant	float64 策略中常量(条件订单用) singular 选填
	
	passive	bool	被动性 选填
	
	visible	int32	显示数量 <0:全部可见 >=0隐藏 选填
	
	better	bool	以买一卖一价进入订单簿 选填
```
#### 设置止盈
```
res = tdex.settp({cid: int64, id: uint64,...})
```
```
params:

	cid	int64	产品 必填

	id	uint64	仓位 必填
	
	distance	bool	是否为相对价格 必填
	
	price	float64	限价 <=0: 市价 必填
	
	timely	uint32	时效性(限价单用) singular。参考 选填
	
	timelyParam	int32	时效性参数 选填
	
	strategy	uint32	策略。参考 选填
	
	variable	uint32	策略使用的变量(条件订单用) singular。参考 选填
	
	constant	float64 策略中常量(条件订单用) singular 选填
	
	passive	bool	被动性 选填
	
	visible	int32	显示数量 <0:全部可见 >=0隐藏 选填
	
	better	bool 以买一卖一价进入订单簿 选填
```
#### 合仓
```
res = tdex.merge({cid: int64, list: []})
```
```
params:

	cid	int64	产品 必填

	list	uint64[]	要合仓的仓位列表 必填
```
#### 分仓
```
res = tdex.split({cid: int64, id: uint64, volume: uint64})
```
```
params:

	cid	int64	产品 必填

	id	uint64	仓位 必填

	volume	uint64	数量 必填
```

#### 获取\设置 用户选项
```
res = tdex.scheme({cid: int64}, type)
```
```
params:

	cid	uint32	产品 必填
	type string 类型 get \ set	必填
	options map （type:set必填，type:get不填）
				- shared bool true:全仓; false:逐仓
				- merged bool true: 自动合仓; false: 独立仓位
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

	pageSize 可选	int32	页大小 选填
	page 可选	int32	当前页码 选填
```

#### 获取合约信息
```
res = tdex.getContract({symbol: string})
```
```
params:

	symbol	string	产品符号。目前只有 BTCUSD 必填
```

#### 现货买入
```
res = tdex.spotBuy({amount: float64, price: float64, symbol: string})
```
```
params:

	amount	float64	数量 必填

	price 可选	float64	价格。如果市价为 0，限价不为 0 选填
	
	symbol	string	交易对。如 TDUSDT 必填
```
#### 现货卖出
```
res = tdex.spotSell({amount: float64, price: float64, symbol: string})
```
```
params:

	amount	float64	数量 必填

	price 可选	float64	价格。如果市价为 0，限价不为 0 选填
	
	symbol	string	交易对。如 TDUSDT 必填
```
#### 现货订单历史
```
res = tdex.spotHistory({beginTime: string, endTime: string, pageSize: int32, page: int32})
```
```
params:

	beginTime	string	开始时间。2017-01-01 必填

	endTime	string	结束时间。2017-09-13 必填
	
	pageSize 可选	int32	页大小 选填
	
	page 可选	int32	当前页码 选填

```

#### 现货买卖统计
```
res = tdex.spotStat({beginTime: string, endTime: string, symbol: string})
```
```
params:

	symbol	string	产品 必填

	beginTime	int64	开始时间戳。秒 必填

	endTime	int64	结束时间戳。秒 必填
```



