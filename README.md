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
