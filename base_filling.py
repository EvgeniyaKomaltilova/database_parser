from data_post.litters_post import litters_post
from data_post.locations_post import locations_post
from data_post.persons_post import persons_post
from data_post.prefix_post import prefix_post
from data_post.rats_post import rats_post
from data_post.rats_put import rats_put

url = 'http://***.ru/api/'

prefix_post(url)
locations_post(url)
persons_post(url)
rats_post(url)
litters_post(url)
rats_put(url)
