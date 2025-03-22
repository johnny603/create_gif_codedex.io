import imageio.v3 as iio

filenames = ['team-pic1.png', 'team-pic2.png']
images = [ ] # empty list that will be used to store the actual image data from these files

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0) #  turn the images into a GIF