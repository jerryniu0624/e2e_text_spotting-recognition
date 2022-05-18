import dataset


def build_data_loader(cfg):
    param = dict()
    for key in cfg:
        if (key == 'type' or key == 'debug'): #不导入type:哪种数据集
            continue
        param[key] = cfg[key]

    data_loader = dataset.__dict__[cfg.type](**param)

    return data_loader
