# stock_helper


Json description of pipeline:

```
{
  "filter": {
      "conditions": [
        {
          "index_value": {
              "start": "2017-09-26", 
              "duration": 0, 
              "type": "CLOSE_INCREASE"
            }, 
          "const_value": 0.04, 
          "operator": "GREATER", 
          "type": "INDEX_TO_CONST", 
          "id": 0
        }, 
        {
          "value_2": {
            "start": "2017-09-01", 
            "duration": 10, 
            "type": "V_AVG"
          }, 
          "type": "INDEX_TO_INDEX", 
          "operator": "GREATER", 
          "id": 1, 
          "value_1": {
            "start": "2017-09-01", 
            "duration": 5, 
            "type": "V_AVG"
          }
        }
      ]
    }, 
    "stock_ids": ["600848"]
}

```

org str:

```
{"stock_ids": ["600848"], "filter": {"conditions": [{"operator": "GREATER", "index_value": {"duration": 0, "start": "2017-09-26", "type": "CLOSE_INCREASE"}, "id": 0, "const_value": 0.04, "type": "INDEX_TO_CONST"}, {"operator": "GREATER", "value_1": {"duration": 5, "start": "2017-09-01", "type": "V_AVG"}, "value_2": {"duration": 10, "start": "2017-09-01", "type": "V_AVG"}, "id": 1, "type": "INDEX_TO_INDEX"}]}}
```