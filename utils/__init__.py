import os
import numpy as np
import random
import torch

from .metrics import quat_degree_error, rotation_angular_error, translation_angular_error, error_auc, compute_pose_errors
from .transform import rotation_matrix_from_ortho6d, rotation_matrix_from_quaternion
from .augment import Augmentor


def seed_torch(seed):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
