# Python Recorder for BitMEX Ticker Data

In short, I record the ticker data (orderbook, trades) directly using **logging module** of python. Then, **compress** the log files and delete the originals **periodically**. In detail, for each ticker/pair, 24 files which include the ticker data of 24 hours are recorded in the folder named with ticker name. Then, the corn jobs will start to collect data and compress the data every day.

## 1. Explination:

### 1.1 Why Adopt .gz files

**CSV file** is easy to read and analyze the date in it. However, the file size is too large to record market data for over 300 tickers/trading pairs.

**HDF5 data format** for pretty fast serialization to large datasets with small file size. HDF5 data is adopted by multiple high-frequency trading companies.

After consulting with employees in **Huobi.com**, I choose the same storage method with them in Huobi.com for storing ticker data as **.gz files** with well-organized file path. Also, according to the [discussion](https://www.zhihu.com/question/268114325) in the forum, saving ticker data within .gz files is widely adopted all over the world.

```
1. easy to code
2. the .gz file size is small
3. the file architecture is clear
4. widely adopted all over the world.
```

Notice: Currently, I recorded the data every minute instead of every hour for illustration. It can be easily changed from "Minute" to "Hour" by `logging.handlers.TimedRotatingFileHandler`. 

## 2. Collect Data

```sh
chmod a+x stop_get_data.sh
chmod a+x start_get_data.sh
./stop_get_data.sh    # kill all active python processes
./start_get_data.sh    # start to record data
```

### 2.1  Original Data Example

In order to **reduce the size of each file**, I only record the directory values of websocket responses instead of the overall directory. Clearly, the file size **can be further reduced** after each list is formatted as **a string**. 

In `/20190105/ETHXBT/log.2019-01-05_22-02` (before compressing):

```
orderBookL2_25: [['ETHXBT', 14599750000, 'Sell', 1, 2.5], ['ETHXBT', 14599950502, 'Sell', 53, 0.49498], ['ETHXBT', 14599992798, 'Sell', 1, 0.07202], ['ETHXBT', 14599994343, 'Sell', 1, 0.05657], ['ETHXBT', 14599995789, 'Sell', 100, 0.04211], ['ETHXBT', 14599995835, 'Sell', 5, 0.04165], ['ETHXBT', 14599995868, 'Sell', 1227, 0.04132], ['ETHXBT', 14599995887, 'Sell', 613, 0.04113], ['ETHXBT', 14599995920, 'Sell', 364, 0.0408], ['ETHXBT', 14599995927, 'Buy', 368, 0.04073], ['ETHXBT', 14599995932, 'Buy', 1204, 0.04068], ['ETHXBT', 14599995960, 'Buy', 613, 0.0404], ['ETHXBT', 14599995978, 'Buy', 1227, 0.04022], ['ETHXBT', 14599995999, 'Buy', 10, 0.04001], ['ETHXBT', 14599996070, 'Buy', 4, 0.0393], ['ETHXBT', 14599996100, 'Buy', 1, 0.039], ['ETHXBT', 14599996160, 'Buy', 5, 0.0384], ['ETHXBT', 14599996250, 'Buy', 105, 0.0375], ['ETHXBT', 14599996260, 'Buy', 100, 0.0374], ['ETHXBT', 14599996270, 'Buy', 100, 0.0373], ['ETHXBT', 14599996280, 'Buy', 100, 0.0372], ['ETHXBT', 14599996290, 'Buy', 100, 0.0371], ['ETHXBT', 14599996299, 'Buy', 100, 0.03701], ['ETHXBT', 14599996320, 'Buy', 100, 0.0368], ['ETHXBT', 14599996990, 'Buy', 100, 0.0301], ['ETHXBT', 14599996992, 'Buy', 3, 0.03008], ['ETHXBT', 14599996993, 'Buy', 100, 0.03007], ['ETHXBT', 14599997008, 'Buy', 100, 0.02992], ['ETHXBT', 14599997013, 'Buy', 100, 0.02987], ['ETHXBT', 14599997050, 'Buy', 2, 0.0295], ['ETHXBT', 14599997092, 'Buy', 2, 0.02908], ['ETHXBT', 14599997192, 'Buy', 10, 0.02808], ['ETHXBT', 14599997379, 'Buy', 200, 0.02621], ['ETHXBT', 14599997419, 'Buy', 3, 0.02581]]

recent_trades: [['2019-01-05T14:01:54.053Z', 'ETHXBT', 'Buy', 4, 0.0408, 'MinusTick', '662e4fda-91a4-2b0e-0e20-c97a93056f74', 16320000, 4, 0.1632]]
```


## 3. Compress Data
```sh
cd hft_data
chmod a+x compress_data.sh
./compress_data.sh
# compress every file in a directory separately and delete originals
```

### 3.1 before compressing
![](./util/orig.png)

### 3.2 after compressing
![](./util/after-compress.png)

## 4. TODO:

1. write a cronjob to run `./stop_get_data.sh` and `./start_get_data.sh` everyday
2. write a coonjob to run `./compress_data.sh` everyday


## 5. Reference:
1. https://github.com/BitMEX/api-connectors/tree/master/official-ws/python
2. https://quant.stackexchange.com/questions/29572/building-financial-data-time-series-database-from-scratch
3. https://www.zhihu.com/question/268114325
4. https://stackoverflow.com/questions/10363696/how-to-gzip-each-file-separately-inside-a-folder-and-then-if-successful-delete-t

