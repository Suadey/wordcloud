"""
Image-colored wordcloud with boundary map
=========================================
A slightly more elaborate version of an image-colored wordcloud
that also takes edges in the image into account.
Recreating an image similar to the parrot example.

"""

import os
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude

from wordcloud import WordCloud, ImageColorGenerator

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# load wikipedia text on rainbow
text = open(os.path.join(d, '2020 topic.txt'), encoding="utf-8").read()

# load image. This has been modified in gimp to be brighter and have more saturation.
parrot_color = np.array(Image.open(os.path.join(d, "cc.jpg")))
# subsample by factor of 3. Very lossy but for a wordcloud we don't really care.
wc = WordCloud(max_words = 2000, background_color = 'white', max_font_size=40, random_state=42, relative_scaling=0)

# generate word cloud
wc.generate(text)

plt.figure(figsize=(20, 20))
plt.imshow(wc, interpolation="bilinear")
wc.to_file("parrot_new.png")