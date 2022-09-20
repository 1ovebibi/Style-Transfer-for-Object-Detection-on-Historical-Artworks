# dataset settings
dataset_type = 'CocoDataset'
data_root = 'data/ODOR/'
classes = ('anemone',
     'carnation',
     'columbine',
     'cornflower',
     'daffodil',
     'geranium',
     'heliotrope',
     'hyacinth',
     'iris',
     'jasmine',
     'lavender',
     'lilac',
     'lily',
     'lily of the valley',
     'neroli',
     'petunia',
     'poppy',
     'rose',
     'tulip',
     'violet',
     'other flower',
     'other fruit',
     'apple',
     'cherry',
     'peach',
     'currant',
     'fig',
     'grapes',
     'lemon',
     'melon',
     'pear',
     'plum',
     'strawberry',
     'other vegetable',
     'artichoke',
     'carrot',
     'garlic',
     'mushroom',
     'olive',
     'onion',
     'pumpkin',
     'other vessel',
     'glass with stem',
     'glass without stem',
     'jug',
     'cup',
     'chalice',
     'wine bottle',
     'carafe',
     'coffeepot',
     'teapot',
     'other vertebrate',
     'animal carcass',
     'bird',
     'cat',
     'cow',
     'dog',
     'donkey',
     'fish',
     'goat',
     'horse',
     'pig',
     'sheep',
     'whale',
     'other invertebrate',
     'bivalve',
     'butterfly',
     'caterpillar',
     'fly',
     'lobster',
     'prawn',
     'bug',
     'other jewellery',
     'bracelet',
     'pomander',
     'ring',
     'ashtray',
     'bread',
     'candle',
     'censer',
     'cheese',
     'fire',
     'gloves',
     'meat',
     'nut',
     'pipe',
     'smoke')
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'public/annotations_trainvalid.json',
        img_prefix=data_root + 'public/images/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'public/annotations_valid.json',
        img_prefix=data_root + 'public/images',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'private/annotations_test.json',
        img_prefix=data_root + 'private/images',
        pipeline=test_pipeline))
evaluation = dict(metric=['bbox'])