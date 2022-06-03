dataset_info = dict(
    dataset_name="custom_windshield",
    paper_info=dict(
        author="Lin, Tsung-Yi and Maire, Michael and "
        "Belongie, Serge and Hays, James and "
        "Perona, Pietro and Ramanan, Deva and "
        r"Doll{\'a}r, Piotr and Zitnick, C Lawrence",
        title="Microsoft coco: Common objects in context",
        container="European conference on computer vision",
        year="2014",
        homepage="http://cocodataset.org/",
    ),
    keypoint_info={
        0: dict(
            name="lower_left", id=0, color=[0, 0, 255], type="lower", swap="lower_right"
        ),
        1: dict(
            name="top_left", id=1, color=[188, 255, 0], type="upper", swap="top_right"
        ),
        2: dict(
            name="top_right", id=2, color=[0, 255, 137], type="upper", swap="top_left"
        ),
        3: dict(
            name="lower_right", id=3, color=[255, 0, 0], type="lower", swap="lower_left"
        ),
    },
    skeleton_info={
        0: dict(link=("lower_left", "top_left"), id=0, color=[0, 255, 0]),
        1: dict(link=("top_left", "top_right"), id=1, color=[0, 255, 0]),
        2: dict(link=("top_right", "lower_right"), id=2, color=[0, 255, 0]),
        3: dict(link=("lower_right", "lower_left"), id=3, color=[0, 255, 0]),
    },
    joint_weights=[1.0, 1.0, 1.0, 1.0],
    sigmas=[],
)

