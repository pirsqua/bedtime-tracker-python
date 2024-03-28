class BedtimeDTO:
    def __init__(self, bedtime):
        self.bedtimeId = bedtime.bedtime_id
        # Convert the child model instance to a ChildDTO instance
        self.child = ChildDTO(bedtime.child)
        self.sleepStart = bedtime.sleep_start
        self.sleepEnd = bedtime.sleep_end
        self.success = bedtime.success
        self.isNap = bedtime.is_nap

class ChildDTO:
    def __init__(self, child):
        self.childId = child.child_id
        self.name = child.name

class PrizeDTO:
    def __init__(self, prize):
        self.prizeId = prize.prize_id
        self.name = prize.name
        self.description = prize.description
        self.imageUrl = prize.image_url
        self.priority = prize.priority
