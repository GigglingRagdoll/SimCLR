import numpy as np

class ToRGB:
    def __call__(self, sample):
        return sample.convert('RGB')
