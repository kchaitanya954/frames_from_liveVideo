#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:25:11 2021

@author: chaitanya
"""

import cv2
import pafy
import os
from datetime import datetime
import sys
directory = '/home/chaitanya/Documents/Bid data/project/test'

class frames:
    def __init__(self, source_url, quality = False):
        self.source_url = source_url
        self.vPafy = pafy.new(self.source_url)
        if quality:
            self.play = self.vPafy.getbest(preftype="mp4")
        else:
            self.play = self.vPafy.streams[0]

        self.url = self.play.url

    def saveFrames(self, n=5, channelName='channel'):
        vid = cv2.VideoCapture(self.url)
        fps = int(vid.get(cv2.CAP_PROP_FPS))
        frame_number = 0
        img_count = 1

        while True:
            frame_number += n * fps
            vid.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            check, frame = vid.read()
            if check:
                time = str(datetime.now())
                name = channelName + '_' + time + '_' + str(img_count) + '.jpg'
                print('Creating...' + name)
                os.chdir(directory)
                cv2.imwrite(name, frame)
                img_count += 1
        vid.release()
        cv2.destroyAllWindows()

    def saveVideo(self):
        vid = cv2.VideoCapture(self.url)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        os.chdir(directory)
        while (vid.isOpened()):
            check, frame = vid.read()
            if check:
                out.write(frame)

        vid.release()
        out.release()
        cv2.destroyAllWindows()

    
    
if __name__ == '__main__':
    try:
        url = 'https://www.youtube.com/watch?v=UUxkVYP36gA&ab_channel=AajTak'
        video = frames()
        video.saveFrames()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
