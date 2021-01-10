# Ex3_OPP

| Nodes       | Edges         | Python-Create  | Python-path                 | java-create | java-path                 |
|   :---:     |     :---:     |      :---:     |   :---:                     |    :---:    |:---:                      |
| 100k        | 100k          | 0.894sec       |                             | 0.286sec    |                           |
|             | 200k          | 1.3sec         | dist:  66.715               | 0.46sec     | dist:  66.715             |
|             |               |                | path : [0, 45085,...,1000]  |             | path : [0, 45085,...,1000]|
|             |               |                | time : 1.174sec             |             | time : 0.1sec             |
|             | 1m            | 5.1sec         | dist:  13.798               | 1.6sec      | dist:  13.798             |
|             |               |                | path : [0, 79317,...,1000]  | 8.762sec    | path : [0, 79317,...,1000]|
|             |               |                | path : [0, 79317,...,1000]  | 8.762sec    | path : [0, 79317,...,1000]|
|             | 5m            | 25.5sec        | path : [0, 79317,...,1000]  | 8.762sec    | path : [0, 79317,...,1000]|

| Nodes       | Edges         | Python-Create  | java-create | 
|   :---:     |     :---:     |      :---:     |    :---:    |
| 1m          | 1m            | 9.8sec         | 2.88sec     |
|             | 5m            | 29sec          | 13.4sec     | 
|             | 10m           | 58sec          | 31.2sec     | 

| File name      | Nodes       | Edges      | Python-time | NetworkX-time  |
|   :---:        |   :---:     |   :---:    |   :---:     |   :---:        |
|G_10_80_0.json|10|80|0.0 sec|0.0 sec|
|G_100_800_0.json|100|800|0.0 sec|0.0 sec|
|G_1000_8000_0.json|1000|8000|0.01 sec|0.0 sec|
|G_10000_80000_0.json|10000|80000|0.08 sec|0.05 sec|
|G_20000_160000_0.json|20000|160000|0.03 sec|0.03 sec|
|G_30000_240000_0.json|30000|240000|0.7 sec|0.36 sec|