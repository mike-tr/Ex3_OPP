# Ex3_OPP

| Nodes       | Edges         | Python-Create  | Python-path                 | java-create | java-path                 |
|   :---:     |     :---:     |      :---:     |   :---:                     |    :---:    |:---:                      |
| 100k        | 100k          | 0.894sec       |                             | 0.286sec    |                           |
|             | 200k          | 1.3sec         | dist:  66.715               | 0.46sec     | dist:  66.715             |
|             |               |                | time : 1.174sec             |             | time : 0.1sec             |
|             | 1m            | 5.1sec         | dist:  13.798               | 1.6sec      | dist:  13.798             |
|             |               |                | time:  3.946sec             | 1.6sec      | time:  0.33sec            |
|             | 5m            | 25.5sec        |                             | 8.762sec    |                           |

| Nodes       | Edges         | Python-Create  | java-create | 
|   :---:     |     :---:     |      :---:     |    :---:    |
| 1m          | 1m            | 9.8sec         | 2.88sec     |
|             | 5m            | 29sec          | 13.4sec     | 
|             | 10m           | 58sec          | 31.2sec     | 

## Load From Json
| Nodes       | Edges      | Python-time | NetworkX-time  |
|   :---:     |   :---:    |   :---:     |   :---:        |
|1,000,000|10,000,000|39.455 sec|99.896 sec|

## Shortest Path
| File name      | Nodes       | Edges      | Python-time | NetworkX-time  |
|   :---:        |   :---:     |   :---:    |   :---:     |   :---:        |
|G_10_80_0.json|10|80|0.0 sec|0.0 sec|
|G_100_800_0.json|100|800|0.0 sec|0.0 sec|
|G_1000_8000_0.json|1000|8000|0.01 sec|0.0 sec|
|G_10000_80000_0.json|10000|80000|0.08 sec|0.05 sec|
|G_20000_160000_0.json|20000|160000|0.03 sec|0.03 sec|
|G_30000_240000_0.json|30000|240000|0.7 sec|0.36 sec|

## Strongly Connected Components
| File name      | Nodes       | Edges      | Python-time | NetworkX-time  |
|   :---:        |   :---:     |   :---:    |   :---:     |   :---:        |
|G_10_80_0.json|10|80|0.0 sec|0.0 sec|
|G_100_800_0.json|100|800|0.0 sec|0.0 sec|
|G_1000_8000_0.json|1000|8000|0.0 sec|0.0 sec|
|G_10000_80000_0.json|10000|80000|0.111 sec|0.092 sec|
|G_20000_160000_0.json|20000|160000|0.279 sec|0.203 sec|
|G_30000_240000_0.json|30000|240000|0.442 sec|0.332 sec|

![Python_vs_networkx_spd](https://user-images.githubusercontent.com/74137570/104298208-60430a80-54cc-11eb-84f5-ff0a290f0199.png)
![Python_vs_networkx_scc](https://user-images.githubusercontent.com/74137570/104298154-53261b80-54cc-11eb-9f8f-a481e95b33d1.png)
![paths](https://user-images.githubusercontent.com/48411662/104248823-ea5e8500-5472-11eb-8126-834eb18de1a3.jpg)
![scc](https://user-images.githubusercontent.com/48411662/104248826-eb8fb200-5472-11eb-9ae7-02ba8fc56a4d.jpg)
### java fails to load 1m - 10m Graph as it cannot read the json the "out of memory"
![scc_single](https://user-images.githubusercontent.com/48411662/104248828-eb8fb200-5472-11eb-9ffd-f4f2f5c9dcb4.jpg)

![Shortest_path](https://user-images.githubusercontent.com/74137570/104340787-ba11f780-5501-11eb-8678-ca6c6f430896.png)
![Sccs](https://user-images.githubusercontent.com/74137570/104340831-c302c900-5501-11eb-97f4-a702f404a71c.png)
![Scc](https://user-images.githubusercontent.com/74137570/104340851-cb5b0400-5501-11eb-8aaa-9950bf0c8106.png)

