from dataclasses import dataclass
from enum import Enum


@dataclass
class User:
    username: str
    password: str


@dataclass
class TimeSlot(Enum):
    T_1730 = "17:30"
    T_1900 = "19:00"
    T_2030 = "20:30"
    T_1830 = "18:30"
    T_1930 = "19:30"


@dataclass
class PadelCourt:
    number: int
    booking_slots: dict[TimeSlot, str]


class PadelCourts:

    courts = [
        PadelCourt(
            number=1,
            booking_slots={
                TimeSlot.T_1830.value: "0104090111",
                TimeSlot.T_1930.value: "0104090112",
                TimeSlot.T_2030.value: "0104090113",
            },
        ),
        PadelCourt(
            number=2,
            booking_slots={
                TimeSlot.T_1830.value: "0104090211",
                TimeSlot.T_1930.value: "0104090212",
                TimeSlot.T_2030.value: "0104090213",
            },
        ),
        PadelCourt(
            number=3,
            booking_slots={
                TimeSlot.T_1730.value: "010409067",
                TimeSlot.T_1900.value: "010409068",
                TimeSlot.T_2030.value: "010409069",
            },
        ),
        PadelCourt(
            number=4,
            booking_slots={
                TimeSlot.T_1730.value: "010409077",
                TimeSlot.T_1900.value: "010409078",
                TimeSlot.T_2030.value: "010409079",
            },
        ),
    ]

    @staticmethod
    def get_long_session_court_ids():
        """Returns court slot IDs for courts 3 & 4"""
        ids_court_3 = list(PadelCourts.courts[2].booking_slots.values())
        ids_court_4 = list(PadelCourts.courts[3].booking_slots.values())
        return ids_court_3 + ids_court_4

    @staticmethod
    def get_short_session_court_ids():
        """Returns court slot IDs for courts 1 & 2"""
        ids_court_1 = list(PadelCourts.courts[0].booking_slots.values())
        ids_court_2 = list(PadelCourts.courts[1].booking_slots.values())
        return ids_court_1 + ids_court_2
