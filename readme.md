# 基于python的显著性目标检测和视频目标分割测评工具箱

A Python-based salient object detection and video object segmentation evaluation toolbox.

## 特性

* 提供`Fm Curve/PR Curves/MAE/(max/mean/weighted) Fmeasure/Smeasure/Emeasure`等八项显著性目标检测指标的评估
    * 纯python实现，基于numpy计算各项指标，速度有保障
    * 导出特定模型的结果到xlsx文件中（有待进一步优化）
    * 导出测试结果到txt文件中
    * 评估所有指定的方法，根据评估结果绘制PR曲线和F-measure曲线
* 针对**DAVIS 2016无监督视频目标分割**任务，提供`"J(M)", "J(O)", "J(D)", "F(M)", "F(O)", "F(D)"`等指标的评估（代码借鉴自davis官方的代码，建议使用前验证下）
    * 导出对指定的模型预测结果的评估结果
    * 表格化展示不同视频上模型预测的性能

三个主要的脚本：

1. `evaluate_sod_all_method.py`: 根据`config.py`中的配置，评估`config.py`中的`all_methods_info`指示的方法
2. `evaluate_sod_single_method.py`: 根据`config.py`中的配置，评估特定模型在特定数据模式（RGB、RGBD）下的结果
3. `evaluate_unvos_method.py`: 评估在davis2016数据集上，现有的模型预测结果对应的性能指标

## 使用方法

### 显著性目标检测任务

#### 评估单个模型

1. 修改`config.py`中的设置:
    * 模仿`OURS_1`指定模型对不同数据集预测结果的路径
    * 根据`user_setting`中的注释进行调整
2. `python evaluate_sod_single_method.py`

#### 评估多个模型

1. 修改`config.py`中的设置:
    * 模仿`all_methods_info`指定模型对不同数据集预测结果的路径和绘图的配置
    * 根据`user_setting`中的注释进行调整
2. `python evaluate_sod_all_method.py --mode [all, pr, fm]` 这里三项中的一个即可。具体含义可以通过`python evaluate_sod_all_method.py --help`了解


### DAVIS 2016无监督视频目标分割任务

1. `python evaluate_unvos_method.py --help`
2. 配置相关项后执行代码

## 最后

由于本工具箱是用来评估指标，所以计算过程的正确性十分重要，但是编写能力有限，可能存在一些小问题，希望大家可以及时指出。

## Thanks

```text
@inproceedings{Fmeasure,
    title={Frequency-tuned salient region detection},
    author={Achanta, Radhakrishna and Hemami, Sheila and Estrada, Francisco and S{\"u}sstrunk, Sabine},
    booktitle=CVPR,
    number={CONF},
    pages={1597--1604},
    year={2009}
}

@inproceedings{MAE,
    title={Saliency filters: Contrast based filtering for salient region detection},
    author={Perazzi, Federico and Kr{\"a}henb{\"u}hl, Philipp and Pritch, Yael and Hornung, Alexander},
    booktitle=CVPR,
    pages={733--740},
    year={2012}
}

@inproceedings{Smeasure,
    title={Structure-measure: A new way to evaluate foreground maps},
    author={Fan, Deng-Ping and Cheng, Ming-Ming and Liu, Yun and Li, Tao and Borji, Ali},
    booktitle=ICCV,
    pages={4548--4557},
    year={2017}
}

@inproceedings{Emeasure,
    title="Enhanced-alignment Measure for Binary Foreground Map Evaluation",
    author="Deng-Ping {Fan} and Cheng {Gong} and Yang {Cao} and Bo {Ren} and Ming-Ming {Cheng} and Ali {Borji}",
    booktitle=IJCAI,
    pages="698--704",
    year={2018}
}

@inproceedings{wFmeasure,
  title={How to evaluate foreground maps?},
  author={Margolin, Ran and Zelnik-Manor, Lihi and Tal, Ayellet},
  booktitle=CVPR,
  pages={248--255},
  year={2014}
}
```
