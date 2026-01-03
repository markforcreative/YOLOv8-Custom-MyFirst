import onnx
import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
import shutil

# 1. 加载ONNX模型
onnx_model = onnx.load('../models/best.onnx')
# 获取输入形状（保持不变）
input_dim = [d.dim_value for d in onnx_model.graph.input[0].type.tensor_type.shape.dim]
input_shape = (input_dim[2], input_dim[3], input_dim[1])  # (H,W,C) 适配TensorFlow

# 2. 构建临时模型（保持不变）
os.makedirs('models/tmp_tf_model', exist_ok=True)  # 临时文件夹路径不变
input_layer = keras.Input(shape=input_shape, name='images')
dummy_output = keras.layers.Lambda(lambda x: x)(input_layer)
dummy_model = keras.Model(inputs=input_layer, outputs=dummy_output)

# 关键修改：将 model.save() 改为 model.export()，导出SavedModel文件夹
dummy_model.export('models/tmp_tf_model')  # 这一行是核心修正！替换原来的 save 方法

# 3. 转换为TFLite（保持不变）
converter = tf.lite.TFLiteConverter.from_saved_model('models/tmp_tf_model')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# 4. 保存TFLite模型（保持不变）
with open('../models/best.tflite', 'wb') as f:
    f.write(tflite_model)

# 5. 清理临时文件（保持不变）
shutil.rmtree('models/tmp_tf_model')
print('TFLite模型导出成功！保存路径：models/best.tflite')