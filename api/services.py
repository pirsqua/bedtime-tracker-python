from .models import Bedtime, Child, Prize
from .dtos import BedtimeDTO, ChildDTO, PrizeDTO


class BedtimeService:
    @staticmethod
    def get_all_bedtimes():
        bedtimes = Bedtime.objects.all()
        bedtime_dtos = [BedtimeDTO(bedtime) for bedtime in bedtimes]
        return bedtime_dtos
    
    @staticmethod
    def get_bedtime_by_id(bedtime_id):
        bedtime = Bedtime.objects.get(id=bedtime_id)
        return BedtimeDTO(bedtime)

    @staticmethod
    def create_bedtime(child_id, sleep_start, sleep_end, success, is_nap):
        bedtime = Bedtime.objects.create(childid=child_id, sleepstart=sleep_start, sleepend=sleep_end,
                                         success=success, isnap=is_nap)
        return BedtimeDTO(bedtime)


class ChildService:
    @staticmethod
    def get_all_children():
        children = Child.objects.all()
        child_dtos = [ChildDTO(child) for child in children]
        return child_dtos
    
    @staticmethod
    def get_child_by_id(child_id):
        child = Child.objects.get(id=child_id)
        return ChildDTO(child)

    @staticmethod
    def create_child(name):
        child = Child.objects.create(name=name)
        return ChildDTO(child)


class PrizeService:
    @staticmethod
    def get_all_prizes():
        prizes = Prize.objects.all()
        prize_dtos = [PrizeDTO(prize) for prize in prizes]
        return prize_dtos
    
    @staticmethod
    def get_prize_by_id(prize_id):
        prize = Prize.objects.get(id=prize_id)
        return PrizeDTO(prize)

    @staticmethod
    def create_prize(name, description, image_url, priority):
        prize = Prize.objects.create(name=name, description=description, imageurl=image_url, priority=priority)
        return PrizeDTO(prize)
