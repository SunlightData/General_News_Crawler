import tarfile

import os

import datetime


def tar_dir(project, dir):
    date = datetime.date.today().strftime('%Y-%m-%d')
    tar = tarfile.open('{0}_{1}.tar.gz'.format(project, date), "w:gz")
    for root, dir, files in os.walk("attachment/" + dir):
        for file in files:
            print file
            fullpath = os.path.join(root, file)
            tar.add(fullpath)
    tar.close()


tar_dir('general_news', '1')
