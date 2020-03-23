gps_modify_triangle_algorithms

# 說明
由於氣候, 地理環境等因素, APP紀錄User的路徑圖會有失準的現象.

為獲得較為正確的資料, 採用了兩種方式, 去掉一些奇異的定位點, 使路徑圖看起來可以更平滑, 計算的公里數可以更為準確.

1. 去掉前後距離較近的點, f.g: 30m

2. 依照時間順序, 每三的點形成的三角形, 若其中第二個頂點, 其 **角度過小**, 則忽略該點.

# 結果

原圖：

![Origin](/screenshot/origin_trajectory.png)

套用後：

![New](/screenshot/new_trajactory.png)


# Blog
[Android GPS 路徑優化](https://medium.com/@nacro711072/android-gps-路徑優化-4f30ad5da671)