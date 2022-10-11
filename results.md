# Thesis Experiments

## Experimental Setup 

### Pretrain
| param       | val            |
| ---         | ---            |
|n_epochs     |                | 
|initial lr   |                |
|lr scheduler |                |
|optimizer    |                | 

### Fine Tune
| param       | val           |
| ---         | ---           |
|n_epochs     | 150           | 
|initial lr   |               |
|lr scheduler |               |
|optimizer    |               | 

## Results

| pretrain dataset                              | fine-tune dataset | test set (evaluated on) | coco mAP | 
| ---                                           |    ---            | ---                     | ---      |
| None                                          | odor-trainval     | odor-test               |          |
| Obj-365                                       | odor-trainval     | odor-test               |          |
| Obj-365 (stylized)                            | odor-trainval     | odor-test               |          |
| Obj-365 (stylized w/ object consistency loss) | odor-trainval     | odor-test               |          |


