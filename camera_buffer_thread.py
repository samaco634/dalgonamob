import threading
# Define the thread that will continuously pull frames from the camera
class CameraBufferCleanerThread(threading.Thread):
    def __init__(self, camera, name='camera-buffer-cleaner-thread'):
        self.camera = camera
        self.last_frame = None
        super(CameraBufferCleanerThread, self).__init__(name=name)
        self.running = True
        self.start()
        self.ret = False
        self.newFrame = False

    def run(self):
        while self.running:
            self.ret, self.last_frame = self.camera.read()
            
            if self.ret == True:
                self.newFrame = True
                
    def getFrame(self):
        if self.newFrame == True:
            self.newFrame = False
            return True, self.last_frame
        else :
            return False, self.last_frame
 
    def terminate(self):
        print('terminating thread')
        self.running = False
