# 多算法支持架構

### 流程

1. 讀取聲音+json參數(檢索並分類訓練/非訓練資料)
2. 切割聲音為Unit資料 (可選項)
3. 計算Unit資料的特徵值
4. 為分析算法做準備
5. 執行算法
6. 分析結果

### 資料結構(請確保資料結構相符)

1. Data: 資料結構主目錄
2. DataSet:存放資料集

   > 資料集內每一組資料為一個資料夾，內有
   >
   > * 資料本體(聲音): 資料本體之一
   > * 採集用json: 資料本體之一
   > * 訓練用json(選): 沒有這筆無法執行訓練
   >
3. DataTemp: 訓練/分析的臨時資料儲存

   > 程式過程中目前已有的Temp資料夾：
   >
   > * Sliced:切割後的聲音存放位置
   >

### 特徵值


|     變數名稱     |    說明    | 備註 |
| :---------------: | :--------: | :--: |
|       Beta       | 剪切波參數 |      |
| Natural_frequency |  自然頻率  |      |

###### 未整理:

過零率、光譜質心、光譜衰減、梅爾頻率倒譜係數和色度頻率

### 參考資料

* 特徵值: https://zhuanlan.zhihu.com/p/54561504
* 音頻處理工具SOX: https://www.twblogs.net/a/5d0a815cbd9eee1e5c8158e5
* 算法大補包: https://zhuanlan.zhihu.com/p/114466283

### 追加參考資料

* 3.2.4. 振荡环节: https://zhuanlan.zhihu.com/p/465440879
* 分辨率選擇(): https://zhuanlan.zhihu.com/p/542572413