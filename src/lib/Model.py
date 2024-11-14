# -*- coding: utf-8 -*-
# @Time: 2024.11.14
# @Author: R
# @File: GetModel.py
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.metrics import mean_absolute_error
from src.lib.TrainDataProcess import ProcessData


# 训练并保存模型
def GetModel(city_idx,a="Model.pkl"):
    """
    :param a: 模型文件名
    :return:
        [socre: MAE评估结果,
        X_test: 预测数据集]
    """
    # 取到数据
    [X_train, X_valid, y_train, y_valid, X_test] = ProcessData(city_idx=city_idx)
    # 此处用XGB模型，不过有bug，弃用
    # 随机树森林模型
    model = RandomForestRegressor(random_state=0, n_estimators=300)
    # 训练模型
    model.fit(X_train, y_train)
    # 预测模型，用上个星期的数据
    preds = model.predict(X_valid)
    # 用MAE评估
    score = mean_absolute_error(y_valid, preds)
    # 保存模型到本地
    joblib.dump(model, filename="Model.pkl")
    # 返回MAE
    return [score, X_test]