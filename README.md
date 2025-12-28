# 农夫山泉瓶+充电宝目标检测项目
基于YOLOv8实现的自定义目标检测，支持图片/视频/摄像头实时检测。

## 环境配置
- Python 3.12
- PyTorch 2.5.1
- ultralytics 8.3.24
- 依赖安装：推荐使用ultralytics官网[快速配置](https://docs.ultralytics.com/zh/quickstart/)

## 数据集
- 类别：fs_bottle（农夫山泉瓶）、powerbank（充电宝）
- 规模：训练集70张，验证集30张
- 标注工具：LabelImg（Python3.8环境）

## 训练参数
- 模型：YOLOv8n
- epochs：100
- batch：32
- 最终精度：mAP50=0.995
