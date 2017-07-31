from cstock.request import Requester
from cstock.sina_engine import SinaEngine

engine = SinaEngine()
requester = Requester(engine)

stock_obj = requester.request('000626')
print(stock_obj[0].as_dict())