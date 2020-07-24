import cv2
import numpy as np

np.random.seed(0)


class GaussianBlur(object):
    # Implements Gaussian blur as described in the SimCLR paper
    def __init__(self, kernel_size, min=0.1, max=2.0):
        self.min = min
        self.max = max
        # kernel size is set to be 10% of the image height/width
        self.kernel_size = kernel_size
        
        # kernel should be odd
        if self.kernel_size % 2 == 0:
            self.kernel_size += 1

    def __call__(self, sample):
        sample = np.array(sample)

        sigma = (self.max - self.min) * np.random.random_sample() + self.min
        sample = cv2.GaussianBlur(sample, (self.kernel_size, self.kernel_size), sigma)

        return sample
