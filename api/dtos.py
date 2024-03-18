class BedtimeDTO:
    def __init__(self, bedtime):
        self.bedtimeid = bedtime.bedtimeid
        self.childid = bedtime.childid
        self.sleepstart = bedtime.sleepstart
        self.sleepend = bedtime.sleepend
        self.success = bedtime.success
        self.isnap = bedtime.isnap

class ChildDTO:
    def __init__(self, child):
        self.childid = child.childid
        self.name = child.name

class PrizeDTO:
    def __init__(self, prize):
        self.prizeid = prize.prizeid
        self.name = prize.name
        self.description = prize.description
        self.imageurl = prize.imageurl
        self.priority = prize.priority
