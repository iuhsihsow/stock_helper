# stock_helper


Json description of pipeline:

```
{
  "stock_ids": ["600848"], 
  "filter": {
    "conditions": [
      {
        "index_value": {
          "duration": 0, 
          "start": "2017-09-25", 
          "type": "CLOSE_INCREASE"}, 
        "const_value": 0.04, 
        "id": 0, 
        "operator": "GREATER", 
        "type": "INDEX_TO_CONST"
      }]
  }
}

```