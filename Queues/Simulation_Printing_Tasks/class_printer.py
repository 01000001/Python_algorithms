class Printer:
    """
    The Printer class will need to track whether it has a current task.
    If it does, then it is busy and the amount of time needed can be
    computed from the number of pages in the task.
    The constructor will also allow the pages-per-minute setting to be
    initialized. The tick method decrements the internal timer and sets
    the printer to idle if the task is completed.
    """
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate
